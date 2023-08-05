# This file has been autogenerated by the pywayland scanner

# Copyright 2014 © Stephen "Lyude" Chandler Paul
# Copyright 2015-2016 © Red Hat, Inc.
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
from ..wayland import WlSurface
from .zwp_tablet_pad_group_v2 import ZwpTabletPadGroupV2
from .zwp_tablet_v2 import ZwpTabletV2


class ZwpTabletPadV2(Interface):
    """A set of buttons, rings and strips

    A pad device is a set of buttons, rings and strips usually physically
    present on the tablet device itself. Some exceptions exist where the pad
    device is physically detached, e.g. the Wacom ExpressKey Remote.

    Pad devices have no axes that control the cursor and are generally
    auxiliary devices to the tool devices used on the tablet surface.

    A pad device has a number of static characteristics, e.g. the number of
    rings. These capabilities are sent in an event sequence after the
    wp_tablet_seat.pad_added event before any actual events from this pad. This
    initial event sequence is terminated by a wp_tablet_pad.done event.

    All pad features (buttons, rings and strips) are logically divided into
    groups and all pads have at least one group. The available groups are
    notified through the wp_tablet_pad.group event; the compositor will emit
    one event per group before emitting wp_tablet_pad.done.

    Groups may have multiple modes. Modes allow clients to map multiple actions
    to a single pad feature. Only one mode can be active per group, although
    different groups may have different active modes.
    """

    name = "zwp_tablet_pad_v2"
    version = 1

    class button_state(enum.IntEnum):
        released = 0
        pressed = 1


class ZwpTabletPadV2Proxy(Proxy):
    interface = ZwpTabletPadV2

    @ZwpTabletPadV2.request(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.String),
        Argument(ArgumentType.Uint),
    )
    def set_feedback(self, button, description, serial):
        """Set compositor feedback

        Requests the compositor to use the provided feedback string associated
        with this button. This request should be issued immediately after a
        wp_tablet_pad_group.mode_switch event from the corresponding group is
        received, or whenever a button is mapped to a different action. See
        wp_tablet_pad_group.mode_switch for more details.

        Clients are encouraged to provide context-aware descriptions for the
        actions associated with each button, and compositors may use this
        information to offer visual feedback on the button layout (e.g. on-
        screen displays).

        Button indices start at 0. Setting the feedback string on a button that
        is reserved by the compositor (i.e. not belonging to any
        wp_tablet_pad_group) does not generate an error but the compositor is
        free to ignore the request.

        The provided string 'description' is a UTF-8 encoded string to be
        associated with this ring, and is considered user-visible; general
        internationalization rules apply.

        The serial argument will be that of the last
        wp_tablet_pad_group.mode_switch event received for the group of this
        button. Requests providing other serials than the most recent one will
        be ignored.

        :param button:
            button index
        :type button:
            `ArgumentType.Uint`
        :param description:
            button description
        :type description:
            `ArgumentType.String`
        :param serial:
            serial of the mode switch event
        :type serial:
            `ArgumentType.Uint`
        """
        self._marshal(0, button, description, serial)

    @ZwpTabletPadV2.request()
    def destroy(self):
        """Destroy the pad object

        Destroy the wp_tablet_pad object. Objects created from this object are
        unaffected and should be destroyed separately.
        """
        self._marshal(1)
        self._destroy()


class ZwpTabletPadV2Resource(Resource):
    interface = ZwpTabletPadV2

    @ZwpTabletPadV2.event(
        Argument(ArgumentType.NewId, interface=ZwpTabletPadGroupV2),
    )
    def group(self, pad_group):
        """Group announced

        Sent on wp_tablet_pad initialization to announce available groups. One
        event is sent for each pad group available.

        This event is sent in the initial burst of events before the
        wp_tablet_pad.done event. At least one group will be announced.

        :param pad_group:
        :type pad_group:
            :class:`~pywayland.protocol.tablet_unstable_v2.ZwpTabletPadGroupV2`
        """
        self._post_event(0, pad_group)

    @ZwpTabletPadV2.event(
        Argument(ArgumentType.String),
    )
    def path(self, path):
        """Path to the device

        A system-specific device path that indicates which device is behind
        this wp_tablet_pad. This information may be used to gather additional
        information about the device, e.g. through libwacom.

        The format of the path is unspecified, it may be a device node, a sysfs
        path, or some other identifier. It is up to the client to identify the
        string provided.

        This event is sent in the initial burst of events before the
        wp_tablet_pad.done event.

        :param path:
            path to local device
        :type path:
            `ArgumentType.String`
        """
        self._post_event(1, path)

    @ZwpTabletPadV2.event(
        Argument(ArgumentType.Uint),
    )
    def buttons(self, buttons):
        """Buttons announced

        Sent on wp_tablet_pad initialization to announce the available buttons.

        This event is sent in the initial burst of events before the
        wp_tablet_pad.done event. This event is only sent when at least one
        button is available.

        :param buttons:
            the number of buttons
        :type buttons:
            `ArgumentType.Uint`
        """
        self._post_event(2, buttons)

    @ZwpTabletPadV2.event()
    def done(self):
        """Pad description event sequence complete

        This event signals the end of the initial burst of descriptive events.
        A client may consider the static description of the pad to be complete
        and finalize initialization of the pad.
        """
        self._post_event(3)

    @ZwpTabletPadV2.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def button(self, time, button, state):
        """Physical button state

        Sent whenever the physical state of a button changes.

        :param time:
            the time of the event with millisecond granularity
        :type time:
            `ArgumentType.Uint`
        :param button:
            the index of the button that changed state
        :type button:
            `ArgumentType.Uint`
        :param state:
        :type state:
            `ArgumentType.Uint`
        """
        self._post_event(4, time, button, state)

    @ZwpTabletPadV2.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Object, interface=ZwpTabletV2),
        Argument(ArgumentType.Object, interface=WlSurface),
    )
    def enter(self, serial, tablet, surface):
        """Enter event

        Notification that this pad is focused on the specified surface.

        :param serial:
            serial number of the enter event
        :type serial:
            `ArgumentType.Uint`
        :param tablet:
            the tablet the pad is attached to
        :type tablet:
            :class:`~pywayland.protocol.tablet_unstable_v2.ZwpTabletV2`
        :param surface:
            surface the pad is focused on
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        """
        self._post_event(5, serial, tablet, surface)

    @ZwpTabletPadV2.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Object, interface=WlSurface),
    )
    def leave(self, serial, surface):
        """Enter event

        Notification that this pad is no longer focused on the specified
        surface.

        :param serial:
            serial number of the leave event
        :type serial:
            `ArgumentType.Uint`
        :param surface:
            surface the pad is no longer focused on
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        """
        self._post_event(6, serial, surface)

    @ZwpTabletPadV2.event()
    def removed(self):
        """Pad removed event

        Sent when the pad has been removed from the system. When a tablet is
        removed its pad(s) will be removed too.

        When this event is received, the client must destroy all rings, strips
        and groups that were offered by this pad, and issue
        wp_tablet_pad.destroy the pad itself.
        """
        self._post_event(7)


class ZwpTabletPadV2Global(Global):
    interface = ZwpTabletPadV2


ZwpTabletPadV2._gen_c()
ZwpTabletPadV2.proxy_class = ZwpTabletPadV2Proxy
ZwpTabletPadV2.resource_class = ZwpTabletPadV2Resource
ZwpTabletPadV2.global_class = ZwpTabletPadV2Global
