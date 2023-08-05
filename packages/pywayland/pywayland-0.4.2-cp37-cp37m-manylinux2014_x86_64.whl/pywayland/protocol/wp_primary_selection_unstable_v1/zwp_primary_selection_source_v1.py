# This file has been autogenerated by the pywayland scanner

# Copyright © 2015, 2016 Red Hat
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

from pywayland.protocol_core import Argument, ArgumentType, Global, Interface, Proxy, Resource


class ZwpPrimarySelectionSourceV1(Interface):
    """Offer to replace the contents of the primary selection

    The source side of a wp_primary_selection_offer, it provides a way to
    describe the offered data and respond to requests to transfer the requested
    contents of the primary selection clipboard.
    """

    name = "zwp_primary_selection_source_v1"
    version = 1


class ZwpPrimarySelectionSourceV1Proxy(Proxy):
    interface = ZwpPrimarySelectionSourceV1

    @ZwpPrimarySelectionSourceV1.request(
        Argument(ArgumentType.String),
    )
    def offer(self, mime_type):
        """Add an offered mime type

        This request adds a mime type to the set of mime types advertised to
        targets. Can be called several times to offer multiple types.

        :param mime_type:
        :type mime_type:
            `ArgumentType.String`
        """
        self._marshal(0, mime_type)

    @ZwpPrimarySelectionSourceV1.request()
    def destroy(self):
        """Destroy the primary selection source

        Destroy the primary selection source.
        """
        self._marshal(1)
        self._destroy()


class ZwpPrimarySelectionSourceV1Resource(Resource):
    interface = ZwpPrimarySelectionSourceV1

    @ZwpPrimarySelectionSourceV1.event(
        Argument(ArgumentType.String),
        Argument(ArgumentType.FileDescriptor),
    )
    def send(self, mime_type, fd):
        """Send the primary selection contents

        Request for the current primary selection contents from the client.
        Send the specified mime type over the passed file descriptor, then
        close it.

        :param mime_type:
        :type mime_type:
            `ArgumentType.String`
        :param fd:
        :type fd:
            `ArgumentType.FileDescriptor`
        """
        self._post_event(0, mime_type, fd)

    @ZwpPrimarySelectionSourceV1.event()
    def cancelled(self):
        """Request for primary selection contents was canceled

        This primary selection source is no longer valid. The client should
        clean up and destroy this primary selection source.
        """
        self._post_event(1)


class ZwpPrimarySelectionSourceV1Global(Global):
    interface = ZwpPrimarySelectionSourceV1


ZwpPrimarySelectionSourceV1._gen_c()
ZwpPrimarySelectionSourceV1.proxy_class = ZwpPrimarySelectionSourceV1Proxy
ZwpPrimarySelectionSourceV1.resource_class = ZwpPrimarySelectionSourceV1Resource
ZwpPrimarySelectionSourceV1.global_class = ZwpPrimarySelectionSourceV1Global
