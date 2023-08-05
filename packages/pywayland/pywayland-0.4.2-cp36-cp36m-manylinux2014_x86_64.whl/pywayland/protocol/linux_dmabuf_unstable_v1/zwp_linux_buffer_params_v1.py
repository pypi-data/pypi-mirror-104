# This file has been autogenerated by the pywayland scanner

# Copyright © 2014, 2015 Collabora, Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import enum

from pywayland.protocol_core import Argument, ArgumentType, Global, Interface, Proxy, Resource
from ..wayland import WlBuffer


class ZwpLinuxBufferParamsV1(Interface):
    """Parameters for creating a dmabuf-based :class:`~pywayland.protocol.wayland.WlBuffer`

    This temporary object is a collection of dmabufs and other parameters that
    together form a single logical buffer. The temporary object may eventually
    create one :class:`~pywayland.protocol.wayland.WlBuffer` unless cancelled
    by destroying it before requesting 'create'.

    Single-planar formats only require one dmabuf, however multi-planar formats
    may require more than one dmabuf. For all formats, an 'add' request must be
    called once per plane (even if the underlying dmabuf fd is identical).

    You must use consecutive plane indices ('plane_idx' argument for 'add')
    from zero to the number of planes used by the drm_fourcc format code. All
    planes required by the format must be given exactly once, but can be given
    in any order. Each plane index can be set only once.
    """

    name = "zwp_linux_buffer_params_v1"
    version = 3

    class error(enum.IntEnum):
        already_used = 0
        plane_idx = 1
        plane_set = 2
        incomplete = 3
        invalid_format = 4
        invalid_dimensions = 5
        out_of_bounds = 6
        invalid_wl_buffer = 7

    class flags(enum.IntEnum):
        y_invert = 1
        interlaced = 2
        bottom_first = 4


class ZwpLinuxBufferParamsV1Proxy(Proxy):
    interface = ZwpLinuxBufferParamsV1

    @ZwpLinuxBufferParamsV1.request()
    def destroy(self):
        """Delete this object, used or not

        Cleans up the temporary data sent to the server for dmabuf-based
        :class:`~pywayland.protocol.wayland.WlBuffer` creation.
        """
        self._marshal(0)
        self._destroy()

    @ZwpLinuxBufferParamsV1.request(
        Argument(ArgumentType.FileDescriptor),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def add(self, fd, plane_idx, offset, stride, modifier_hi, modifier_lo):
        """Add a dmabuf to the temporary set

        This request adds one dmabuf to the set in this
        :class:`ZwpLinuxBufferParamsV1`.

        The 64-bit unsigned value combined from modifier_hi and modifier_lo is
        the dmabuf layout modifier. DRM AddFB2 ioctl calls this the fb
        modifier, which is defined in drm_mode.h of Linux UAPI. This is an
        opaque token. Drivers use this token to express tiling, compression,
        etc. driver-specific modifications to the base format defined by the
        DRM fourcc code.

        Warning: It should be an error if the format/modifier pair was not
        advertised with the modifier event. This is not enforced yet because
        some implementations always accept DRM_FORMAT_MOD_INVALID. Also version
        2 of this protocol does not have the modifier event.

        This request raises the PLANE_IDX error if plane_idx is too large. The
        error PLANE_SET is raised if attempting to set a plane that was already
        set.

        :param fd:
            dmabuf fd
        :type fd:
            `ArgumentType.FileDescriptor`
        :param plane_idx:
            plane index
        :type plane_idx:
            `ArgumentType.Uint`
        :param offset:
            offset in bytes
        :type offset:
            `ArgumentType.Uint`
        :param stride:
            stride in bytes
        :type stride:
            `ArgumentType.Uint`
        :param modifier_hi:
            high 32 bits of layout modifier
        :type modifier_hi:
            `ArgumentType.Uint`
        :param modifier_lo:
            low 32 bits of layout modifier
        :type modifier_lo:
            `ArgumentType.Uint`
        """
        self._marshal(1, fd, plane_idx, offset, stride, modifier_hi, modifier_lo)

    @ZwpLinuxBufferParamsV1.request(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def create(self, width, height, format, flags):
        """Create a :class:`~pywayland.protocol.wayland.WlBuffer` from the given dmabufs

        This asks for creation of a
        :class:`~pywayland.protocol.wayland.WlBuffer` from the added dmabuf
        buffers. The :class:`~pywayland.protocol.wayland.WlBuffer` is not
        created immediately but returned via the 'created' event if the dmabuf
        sharing succeeds. The sharing may fail at runtime for reasons a client
        cannot predict, in which case the 'failed' event is triggered.

        The 'format' argument is a DRM_FORMAT code, as defined by the libdrm's
        drm_fourcc.h. The Linux kernel's DRM sub-system is the authoritative
        source on how the format codes should work.

        The 'flags' is a bitfield of the flags defined in enum "flags".
        'y_invert' means the that the image needs to be y-flipped.

        Flag 'interlaced' means that the frame in the buffer is not progressive
        as usual, but interlaced. An interlaced buffer as supported here must
        always contain both top and bottom fields. The top field always begins
        on the first pixel row. The temporal ordering between the two fields is
        top field first, unless 'bottom_first' is specified. It is undefined
        whether 'bottom_first' is ignored if 'interlaced' is not set.

        This protocol does not convey any information about field rate,
        duration, or timing, other than the relative ordering between the two
        fields in one buffer. A compositor may have to estimate the intended
        field rate from the incoming buffer rate. It is undefined whether the
        time of receiving :func:`WlSurface.commit()
        <pywayland.protocol.wayland.WlSurface.commit>` with a new buffer
        attached, applying the :class:`~pywayland.protocol.wayland.WlSurface`
        state, :func:`WlSurface.frame()
        <pywayland.protocol.wayland.WlSurface.frame>` callback trigger,
        presentation, or any other point in the compositor cycle is used to
        measure the frame or field times. There is no support for detecting
        missed or late frames/fields/buffers either, and there is no support
        whatsoever for cooperating with interlaced compositor output.

        The composited image quality resulting from the use of interlaced
        buffers is explicitly undefined. A compositor may use elaborate
        hardware features or software to deinterlace and create progressive
        output frames from a sequence of interlaced input buffers, or it may
        produce substandard image quality. However, compositors that cannot
        guarantee reasonable image quality in all cases are recommended to just
        reject all interlaced buffers.

        Any argument errors, including non-positive width or height, mismatch
        between the number of planes and the format, bad format, bad offset or
        stride, may be indicated by fatal protocol errors: INCOMPLETE,
        INVALID_FORMAT, INVALID_DIMENSIONS, OUT_OF_BOUNDS.

        Dmabuf import errors in the server that are not obvious client bugs are
        returned via the 'failed' event as non-fatal. This allows attempting
        dmabuf sharing and falling back in the client if it fails.

        This request can be sent only once in the object's lifetime, after
        which the only legal request is destroy. This object should be
        destroyed after issuing a 'create' request. Attempting to use this
        object after issuing 'create' raises ALREADY_USED protocol error.

        It is not mandatory to issue 'create'. If a client wants to cancel the
        buffer creation, it can just destroy this object.

        :param width:
            base plane width in pixels
        :type width:
            `ArgumentType.Int`
        :param height:
            base plane height in pixels
        :type height:
            `ArgumentType.Int`
        :param format:
            DRM_FORMAT code
        :type format:
            `ArgumentType.Uint`
        :param flags:
            see enum flags
        :type flags:
            `ArgumentType.Uint`
        """
        self._marshal(2, width, height, format, flags)

    @ZwpLinuxBufferParamsV1.request(
        Argument(ArgumentType.NewId, interface=WlBuffer),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        version=2,
    )
    def create_immed(self, width, height, format, flags):
        """Immediately create a :class:`~pywayland.protocol.wayland.WlBuffer` from the given                      dmabufs

        This asks for immediate creation of a
        :class:`~pywayland.protocol.wayland.WlBuffer` by importing the added
        dmabufs.

        In case of import success, no event is sent from the server, and the
        :class:`~pywayland.protocol.wayland.WlBuffer` is ready to be used by
        the client.

        Upon import failure, either of the following may happen, as seen fit by
        the implementation: - the client is terminated with one of the
        following fatal protocol   errors:   - INCOMPLETE, INVALID_FORMAT,
        INVALID_DIMENSIONS, OUT_OF_BOUNDS,     in case of argument errors such
        as mismatch between the number     of planes and the format, bad
        format, non-positive width or     height, or bad offset or stride.   -
        INVALID_WL_BUFFER, in case the cause for failure is unknown or
        plaform specific. - the server creates an invalid
        :class:`~pywayland.protocol.wayland.WlBuffer`, marks it as failed and
        sends a 'failed' event to the client. The result of using this
        invalid :class:`~pywayland.protocol.wayland.WlBuffer` as an argument in
        any request by the client is   defined by the compositor
        implementation.

        This takes the same arguments as a 'create' request, and obeys the same
        restrictions.

        :param width:
            base plane width in pixels
        :type width:
            `ArgumentType.Int`
        :param height:
            base plane height in pixels
        :type height:
            `ArgumentType.Int`
        :param format:
            DRM_FORMAT code
        :type format:
            `ArgumentType.Uint`
        :param flags:
            see enum flags
        :type flags:
            `ArgumentType.Uint`
        :returns:
            :class:`~pywayland.protocol.wayland.WlBuffer` -- id for the newly
            created :class:`~pywayland.protocol.wayland.WlBuffer`
        """
        buffer_id = self._marshal_constructor(3, WlBuffer, width, height, format, flags)
        return buffer_id


class ZwpLinuxBufferParamsV1Resource(Resource):
    interface = ZwpLinuxBufferParamsV1

    @ZwpLinuxBufferParamsV1.event(
        Argument(ArgumentType.NewId, interface=WlBuffer),
    )
    def created(self, buffer):
        """Buffer creation succeeded

        This event indicates that the attempted buffer creation was successful.
        It provides the new :class:`~pywayland.protocol.wayland.WlBuffer`
        referencing the dmabuf(s).

        Upon receiving this event, the client should destroy the
        zlinux_dmabuf_params object.

        :param buffer:
            the newly created :class:`~pywayland.protocol.wayland.WlBuffer`
        :type buffer:
            :class:`~pywayland.protocol.wayland.WlBuffer`
        """
        self._post_event(0, buffer)

    @ZwpLinuxBufferParamsV1.event()
    def failed(self):
        """Buffer creation failed

        This event indicates that the attempted buffer creation has failed. It
        usually means that one of the dmabuf constraints has not been
        fulfilled.

        Upon receiving this event, the client should destroy the
        zlinux_buffer_params object.
        """
        self._post_event(1)


class ZwpLinuxBufferParamsV1Global(Global):
    interface = ZwpLinuxBufferParamsV1


ZwpLinuxBufferParamsV1._gen_c()
ZwpLinuxBufferParamsV1.proxy_class = ZwpLinuxBufferParamsV1Proxy
ZwpLinuxBufferParamsV1.resource_class = ZwpLinuxBufferParamsV1Resource
ZwpLinuxBufferParamsV1.global_class = ZwpLinuxBufferParamsV1Global
