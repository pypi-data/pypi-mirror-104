# This file has been autogenerated by the pywayland scanner

# Copyright © 2016 Yong Bakos
# Copyright © 2015 Jason Ekstrand
# Copyright © 2015 Jonas Ådahl
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

from pywayland.protocol_core import Global, Interface, Proxy, Resource


class ZwpFullscreenShellModeFeedbackV1(Interface):
    name = "zwp_fullscreen_shell_mode_feedback_v1"
    version = 1


class ZwpFullscreenShellModeFeedbackV1Proxy(Proxy):
    interface = ZwpFullscreenShellModeFeedbackV1


class ZwpFullscreenShellModeFeedbackV1Resource(Resource):
    interface = ZwpFullscreenShellModeFeedbackV1

    @ZwpFullscreenShellModeFeedbackV1.event()
    def mode_successful(self):
        """Mode switch succeeded

        This event indicates that the attempted mode switch operation was
        successful.  A surface of the size requested in the mode switch will
        fill the output without scaling.

        Upon receiving this event, the client should destroy the
        wl_fullscreen_shell_mode_feedback object.
        """
        self._post_event(0)

    @ZwpFullscreenShellModeFeedbackV1.event()
    def mode_failed(self):
        """Mode switch failed

        This event indicates that the attempted mode switch operation failed.
        This may be because the requested output mode is not possible or it may
        mean that the compositor does not want to allow it.

        Upon receiving this event, the client should destroy the
        wl_fullscreen_shell_mode_feedback object.
        """
        self._post_event(1)

    @ZwpFullscreenShellModeFeedbackV1.event()
    def present_cancelled(self):
        """Mode switch cancelled

        This event indicates that the attempted mode switch operation was
        cancelled.  Most likely this is because the client requested a second
        mode switch before the first one completed.

        Upon receiving this event, the client should destroy the
        wl_fullscreen_shell_mode_feedback object.
        """
        self._post_event(2)


class ZwpFullscreenShellModeFeedbackV1Global(Global):
    interface = ZwpFullscreenShellModeFeedbackV1


ZwpFullscreenShellModeFeedbackV1._gen_c()
ZwpFullscreenShellModeFeedbackV1.proxy_class = ZwpFullscreenShellModeFeedbackV1Proxy
ZwpFullscreenShellModeFeedbackV1.resource_class = ZwpFullscreenShellModeFeedbackV1Resource
ZwpFullscreenShellModeFeedbackV1.global_class = ZwpFullscreenShellModeFeedbackV1Global
