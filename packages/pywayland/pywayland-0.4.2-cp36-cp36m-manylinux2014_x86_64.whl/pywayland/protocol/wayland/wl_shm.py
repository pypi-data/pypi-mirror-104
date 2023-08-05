# This file has been autogenerated by the pywayland scanner

# Copyright © 2008-2011 Kristian Høgsberg
# Copyright © 2010-2011 Intel Corporation
# Copyright © 2012-2013 Collabora, Ltd.
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice (including the
# next paragraph) shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import enum

from pywayland.protocol_core import Argument, ArgumentType, Global, Interface, Proxy, Resource
from .wl_shm_pool import WlShmPool


class WlShm(Interface):
    """Shared memory support

    A singleton global object that provides support for shared memory.

    Clients can create :class:`~pywayland.protocol.wayland.WlShmPool` objects
    using the create_pool request.

    At connection setup time, the :class:`WlShm` object emits one or more
    format events to inform clients about the valid pixel formats that can be
    used for buffers.
    """

    name = "wl_shm"
    version = 1

    class error(enum.IntEnum):
        invalid_format = 0
        invalid_stride = 1
        invalid_fd = 2

    class format(enum.IntEnum):
        argb8888 = 0
        xrgb8888 = 1
        c8 = 0x20203843
        rgb332 = 0x38424752
        bgr233 = 0x38524742
        xrgb4444 = 0x32315258
        xbgr4444 = 0x32314258
        rgbx4444 = 0x32315852
        bgrx4444 = 0x32315842
        argb4444 = 0x32315241
        abgr4444 = 0x32314241
        rgba4444 = 0x32314152
        bgra4444 = 0x32314142
        xrgb1555 = 0x35315258
        xbgr1555 = 0x35314258
        rgbx5551 = 0x35315852
        bgrx5551 = 0x35315842
        argb1555 = 0x35315241
        abgr1555 = 0x35314241
        rgba5551 = 0x35314152
        bgra5551 = 0x35314142
        rgb565 = 0x36314752
        bgr565 = 0x36314742
        rgb888 = 0x34324752
        bgr888 = 0x34324742
        xbgr8888 = 0x34324258
        rgbx8888 = 0x34325852
        bgrx8888 = 0x34325842
        abgr8888 = 0x34324241
        rgba8888 = 0x34324152
        bgra8888 = 0x34324142
        xrgb2101010 = 0x30335258
        xbgr2101010 = 0x30334258
        rgbx1010102 = 0x30335852
        bgrx1010102 = 0x30335842
        argb2101010 = 0x30335241
        abgr2101010 = 0x30334241
        rgba1010102 = 0x30334152
        bgra1010102 = 0x30334142
        yuyv = 0x56595559
        yvyu = 0x55595659
        uyvy = 0x59565955
        vyuy = 0x59555956
        ayuv = 0x56555941
        nv12 = 0x3231564E
        nv21 = 0x3132564E
        nv16 = 0x3631564E
        nv61 = 0x3136564E
        yuv410 = 0x39565559
        yvu410 = 0x39555659
        yuv411 = 0x31315559
        yvu411 = 0x31315659
        yuv420 = 0x32315559
        yvu420 = 0x32315659
        yuv422 = 0x36315559
        yvu422 = 0x36315659
        yuv444 = 0x34325559
        yvu444 = 0x34325659
        r8 = 0x20203852
        r16 = 0x20363152
        rg88 = 0x38384752
        gr88 = 0x38385247
        rg1616 = 0x32334752
        gr1616 = 0x32335247
        xrgb16161616f = 0x48345258
        xbgr16161616f = 0x48344258
        argb16161616f = 0x48345241
        abgr16161616f = 0x48344241
        xyuv8888 = 0x56555958
        vuy888 = 0x34325556
        vuy101010 = 0x30335556
        y210 = 0x30313259
        y212 = 0x32313259
        y216 = 0x36313259
        y410 = 0x30313459
        y412 = 0x32313459
        y416 = 0x36313459
        xvyu2101010 = 0x30335658
        xvyu12_16161616 = 0x36335658
        xvyu16161616 = 0x38345658
        y0l0 = 0x304C3059
        x0l0 = 0x304C3058
        y0l2 = 0x324C3059
        x0l2 = 0x324C3058
        yuv420_8bit = 0x38305559
        yuv420_10bit = 0x30315559
        xrgb8888_a8 = 0x38415258
        xbgr8888_a8 = 0x38414258
        rgbx8888_a8 = 0x38415852
        bgrx8888_a8 = 0x38415842
        rgb888_a8 = 0x38413852
        bgr888_a8 = 0x38413842
        rgb565_a8 = 0x38413552
        bgr565_a8 = 0x38413542
        nv24 = 0x3432564E
        nv42 = 0x3234564E
        p210 = 0x30313250
        p010 = 0x30313050
        p012 = 0x32313050
        p016 = 0x36313050
        axbxgxrx106106106106 = 0x30314241
        nv15 = 0x3531564E
        q410 = 0x30313451
        q401 = 0x31303451


class WlShmProxy(Proxy):
    interface = WlShm

    @WlShm.request(
        Argument(ArgumentType.NewId, interface=WlShmPool),
        Argument(ArgumentType.FileDescriptor),
        Argument(ArgumentType.Int),
    )
    def create_pool(self, fd, size):
        """Create a shm pool

        Create a new :class:`~pywayland.protocol.wayland.WlShmPool` object.

        The pool can be used to create shared memory based buffer objects.  The
        server will mmap size bytes of the passed file descriptor, to use as
        backing memory for the pool.

        :param fd:
            file descriptor for the pool
        :type fd:
            `ArgumentType.FileDescriptor`
        :param size:
            pool size, in bytes
        :type size:
            `ArgumentType.Int`
        :returns:
            :class:`~pywayland.protocol.wayland.WlShmPool` -- pool to create
        """
        id = self._marshal_constructor(0, WlShmPool, fd, size)
        return id


class WlShmResource(Resource):
    interface = WlShm

    @WlShm.event(
        Argument(ArgumentType.Uint),
    )
    def format(self, format):
        """Pixel format description

        Informs the client about a valid pixel format that can be used for
        buffers. Known formats include argb8888 and xrgb8888.

        :param format:
            buffer pixel format
        :type format:
            `ArgumentType.Uint`
        """
        self._post_event(0, format)


class WlShmGlobal(Global):
    interface = WlShm


WlShm._gen_c()
WlShm.proxy_class = WlShmProxy
WlShm.resource_class = WlShmResource
WlShm.global_class = WlShmGlobal
