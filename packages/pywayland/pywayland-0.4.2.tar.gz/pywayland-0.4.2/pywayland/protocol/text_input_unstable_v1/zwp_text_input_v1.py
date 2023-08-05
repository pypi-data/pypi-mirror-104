# This file has been autogenerated by the pywayland scanner

# Copyright © 2012, 2013 Intel Corporation
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
from ..wayland import WlSeat
from ..wayland import WlSurface


class ZwpTextInputV1(Interface):
    """Text input

    An object used for text input. Adds support for text input and input
    methods to applications. A text_input object is created from a
    wl_text_input_manager and corresponds typically to a text entry in an
    application.

    Requests are used to activate/deactivate the text_input object and set
    state information like surrounding and selected text or the content type.
    The information about entered text is sent to the text_input object via the
    pre-edit and commit events. Using this interface removes the need for
    applications to directly process hardware key events and compose text out
    of them.

    Text is generally UTF-8 encoded, indices and lengths are in bytes.

    Serials are used to synchronize the state between the text input and an
    input method. New serials are sent by the text input in the commit_state
    request and are used by the input method to indicate the known text input
    state in events like preedit_string, commit_string, and keysym. The text
    input can then ignore events from the input method which are based on an
    outdated state (for example after a reset).

    Warning! The protocol described in this file is experimental and backward
    incompatible changes may be made. Backward compatible changes may be added
    together with the corresponding interface version bump. Backward
    incompatible changes are done by bumping the version number in the protocol
    and interface names and resetting the interface version. Once the protocol
    is to be declared stable, the 'z' prefix and the version number in the
    protocol and interface names are removed and the interface version number
    is reset.
    """

    name = "zwp_text_input_v1"
    version = 1

    class content_hint(enum.IntEnum):
        none = 0x0
        default = 0x7
        password = 0xC0
        auto_completion = 0x1
        auto_correction = 0x2
        auto_capitalization = 0x4
        lowercase = 0x8
        uppercase = 0x10
        titlecase = 0x20
        hidden_text = 0x40
        sensitive_data = 0x80
        latin = 0x100
        multiline = 0x200

    class content_purpose(enum.IntEnum):
        normal = 0
        alpha = 1
        digits = 2
        number = 3
        phone = 4
        url = 5
        email = 6
        name_ = 7
        password = 8
        date = 9
        time = 10
        datetime = 11
        terminal = 12

    class preedit_style(enum.IntEnum):
        default = 0
        none = 1
        active = 2
        inactive = 3
        highlight = 4
        underline = 5
        selection = 6
        incorrect = 7

    class text_direction(enum.IntEnum):
        auto = 0
        ltr = 1
        rtl = 2


class ZwpTextInputV1Proxy(Proxy):
    interface = ZwpTextInputV1

    @ZwpTextInputV1.request(
        Argument(ArgumentType.Object, interface=WlSeat),
        Argument(ArgumentType.Object, interface=WlSurface),
    )
    def activate(self, seat, surface):
        """Request activation

        Requests the text_input object to be activated (typically when the text
        entry gets focus).

        The seat argument is a :class:`~pywayland.protocol.wayland.WlSeat`
        which maintains the focus for this activation. The surface argument is
        a :class:`~pywayland.protocol.wayland.WlSurface` assigned to the
        text_input object and tracked for focus lost. The enter event is
        emitted on successful activation.

        :param seat:
        :type seat:
            :class:`~pywayland.protocol.wayland.WlSeat`
        :param surface:
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        """
        self._marshal(0, seat, surface)

    @ZwpTextInputV1.request(
        Argument(ArgumentType.Object, interface=WlSeat),
    )
    def deactivate(self, seat):
        """Request deactivation

        Requests the text_input object to be deactivated (typically when the
        text entry lost focus). The seat argument is a
        :class:`~pywayland.protocol.wayland.WlSeat` which was used for
        activation.

        :param seat:
        :type seat:
            :class:`~pywayland.protocol.wayland.WlSeat`
        """
        self._marshal(1, seat)

    @ZwpTextInputV1.request()
    def show_input_panel(self):
        """Show input panels

        Requests input panels (virtual keyboard) to show.
        """
        self._marshal(2)

    @ZwpTextInputV1.request()
    def hide_input_panel(self):
        """Hide input panels

        Requests input panels (virtual keyboard) to hide.
        """
        self._marshal(3)

    @ZwpTextInputV1.request()
    def reset(self):
        """Reset

        Should be called by an editor widget when the input state should be
        reset, for example after the text was changed outside of the normal
        input method flow.
        """
        self._marshal(4)

    @ZwpTextInputV1.request(
        Argument(ArgumentType.String),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def set_surrounding_text(self, text, cursor, anchor):
        """Sets the surrounding text

        Sets the plain surrounding text around the input position. Text is
        UTF-8 encoded. Cursor is the byte offset within the surrounding text.
        Anchor is the byte offset of the selection anchor within the
        surrounding text. If there is no selected text anchor, then it is the
        same as cursor.

        :param text:
        :type text:
            `ArgumentType.String`
        :param cursor:
        :type cursor:
            `ArgumentType.Uint`
        :param anchor:
        :type anchor:
            `ArgumentType.Uint`
        """
        self._marshal(5, text, cursor, anchor)

    @ZwpTextInputV1.request(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def set_content_type(self, hint, purpose):
        """Set content purpose and hint

        Sets the content purpose and content hint. While the purpose is the
        basic purpose of an input field, the hint flags allow to modify some of
        the behavior.

        When no content type is explicitly set, a normal content purpose with
        default hints (auto completion, auto correction, auto capitalization)
        should be assumed.

        :param hint:
        :type hint:
            `ArgumentType.Uint`
        :param purpose:
        :type purpose:
            `ArgumentType.Uint`
        """
        self._marshal(6, hint, purpose)

    @ZwpTextInputV1.request(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
    )
    def set_cursor_rectangle(self, x, y, width, height):
        """set_cursor_rectangle

        :param x:
        :type x:
            `ArgumentType.Int`
        :param y:
        :type y:
            `ArgumentType.Int`
        :param width:
        :type width:
            `ArgumentType.Int`
        :param height:
        :type height:
            `ArgumentType.Int`
        """
        self._marshal(7, x, y, width, height)

    @ZwpTextInputV1.request(
        Argument(ArgumentType.String),
    )
    def set_preferred_language(self, language):
        """Sets preferred language

        Sets a specific language. This allows for example a virtual keyboard to
        show a language specific layout. The "language" argument is an RFC-3066
        format language tag.

        It could be used for example in a word processor to indicate the
        language of the currently edited document or in an instant message
        application which tracks languages of contacts.

        :param language:
        :type language:
            `ArgumentType.String`
        """
        self._marshal(8, language)

    @ZwpTextInputV1.request(
        Argument(ArgumentType.Uint),
    )
    def commit_state(self, serial):
        """commit_state

        :param serial:
            used to identify the known state
        :type serial:
            `ArgumentType.Uint`
        """
        self._marshal(9, serial)

    @ZwpTextInputV1.request(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def invoke_action(self, button, index):
        """invoke_action

        :param button:
        :type button:
            `ArgumentType.Uint`
        :param index:
        :type index:
            `ArgumentType.Uint`
        """
        self._marshal(10, button, index)


class ZwpTextInputV1Resource(Resource):
    interface = ZwpTextInputV1

    @ZwpTextInputV1.event(
        Argument(ArgumentType.Object, interface=WlSurface),
    )
    def enter(self, surface):
        """Enter event

        Notify the text_input object when it received focus. Typically in
        response to an activate request.

        :param surface:
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        """
        self._post_event(0, surface)

    @ZwpTextInputV1.event()
    def leave(self):
        """Leave event

        Notify the text_input object when it lost focus. Either in response to
        a deactivate request or when the assigned surface lost focus or was
        destroyed.
        """
        self._post_event(1)

    @ZwpTextInputV1.event(
        Argument(ArgumentType.Array),
    )
    def modifiers_map(self, map):
        """Modifiers map

        Transfer an array of 0-terminated modifier names. The position in the
        array is the index of the modifier as used in the modifiers bitmask in
        the keysym event.

        :param map:
        :type map:
            `ArgumentType.Array`
        """
        self._post_event(2, map)

    @ZwpTextInputV1.event(
        Argument(ArgumentType.Uint),
    )
    def input_panel_state(self, state):
        """State of the input panel

        Notify when the visibility state of the input panel changed.

        :param state:
        :type state:
            `ArgumentType.Uint`
        """
        self._post_event(3, state)

    @ZwpTextInputV1.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.String),
        Argument(ArgumentType.String),
    )
    def preedit_string(self, serial, text, commit):
        """Pre-edit

        Notify when a new composing text (pre-edit) should be set around the
        current cursor position. Any previously set composing text should be
        removed.

        The commit text can be used to replace the preedit text on reset (for
        example on unfocus).

        The text input should also handle all preedit_style and preedit_cursor
        events occurring directly before preedit_string.

        :param serial:
            serial of the latest known text input state
        :type serial:
            `ArgumentType.Uint`
        :param text:
        :type text:
            `ArgumentType.String`
        :param commit:
        :type commit:
            `ArgumentType.String`
        """
        self._post_event(4, serial, text, commit)

    @ZwpTextInputV1.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def preedit_styling(self, index, length, style):
        """Pre-edit styling

        Sets styling information on composing text. The style is applied for
        length bytes from index relative to the beginning of the composing text
        (as byte offset). Multiple styles can be applied to a composing text by
        sending multiple preedit_styling events.

        This event is handled as part of a following preedit_string event.

        :param index:
        :type index:
            `ArgumentType.Uint`
        :param length:
        :type length:
            `ArgumentType.Uint`
        :param style:
        :type style:
            `ArgumentType.Uint`
        """
        self._post_event(5, index, length, style)

    @ZwpTextInputV1.event(
        Argument(ArgumentType.Int),
    )
    def preedit_cursor(self, index):
        """Pre-edit cursor

        Sets the cursor position inside the composing text (as byte offset)
        relative to the start of the composing text. When index is a negative
        number no cursor is shown.

        This event is handled as part of a following preedit_string event.

        :param index:
        :type index:
            `ArgumentType.Int`
        """
        self._post_event(6, index)

    @ZwpTextInputV1.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.String),
    )
    def commit_string(self, serial, text):
        """Commit

        Notify when text should be inserted into the editor widget. The text to
        commit could be either just a single character after a key press or the
        result of some composing (pre-edit). It could also be an empty text
        when some text should be removed (see delete_surrounding_text) or when
        the input cursor should be moved (see cursor_position).

        Any previously set composing text should be removed.

        :param serial:
            serial of the latest known text input state
        :type serial:
            `ArgumentType.Uint`
        :param text:
        :type text:
            `ArgumentType.String`
        """
        self._post_event(7, serial, text)

    @ZwpTextInputV1.event(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
    )
    def cursor_position(self, index, anchor):
        """Set cursor to new position

        Notify when the cursor or anchor position should be modified.

        This event should be handled as part of a following commit_string
        event.

        :param index:
        :type index:
            `ArgumentType.Int`
        :param anchor:
        :type anchor:
            `ArgumentType.Int`
        """
        self._post_event(8, index, anchor)

    @ZwpTextInputV1.event(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Uint),
    )
    def delete_surrounding_text(self, index, length):
        """Delete surrounding text

        Notify when the text around the current cursor position should be
        deleted.

        Index is relative to the current cursor (in bytes). Length is the
        length of deleted text (in bytes).

        This event should be handled as part of a following commit_string
        event.

        :param index:
        :type index:
            `ArgumentType.Int`
        :param length:
        :type length:
            `ArgumentType.Uint`
        """
        self._post_event(9, index, length)

    @ZwpTextInputV1.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def keysym(self, serial, time, sym, state, modifiers):
        """Keysym

        Notify when a key event was sent. Key events should not be used for
        normal text input operations, which should be done with commit_string,
        delete_surrounding_text, etc. The key event follows the
        :class:`~pywayland.protocol.wayland.WlKeyboard` key event convention.
        Sym is an XKB keysym, state a
        :class:`~pywayland.protocol.wayland.WlKeyboard` key_state. Modifiers
        are a mask for effective modifiers (where the modifier indices are set
        by the modifiers_map event)

        :param serial:
            serial of the latest known text input state
        :type serial:
            `ArgumentType.Uint`
        :param time:
        :type time:
            `ArgumentType.Uint`
        :param sym:
        :type sym:
            `ArgumentType.Uint`
        :param state:
        :type state:
            `ArgumentType.Uint`
        :param modifiers:
        :type modifiers:
            `ArgumentType.Uint`
        """
        self._post_event(10, serial, time, sym, state, modifiers)

    @ZwpTextInputV1.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.String),
    )
    def language(self, serial, language):
        """Language

        Sets the language of the input text. The "language" argument is an
        RFC-3066 format language tag.

        :param serial:
            serial of the latest known text input state
        :type serial:
            `ArgumentType.Uint`
        :param language:
        :type language:
            `ArgumentType.String`
        """
        self._post_event(11, serial, language)

    @ZwpTextInputV1.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def text_direction(self, serial, direction):
        """Text direction

        Sets the text direction of input text.

        It is mainly needed for showing an input cursor on the correct side of
        the editor when there is no input done yet and making sure neutral
        direction text is laid out properly.

        :param serial:
            serial of the latest known text input state
        :type serial:
            `ArgumentType.Uint`
        :param direction:
        :type direction:
            `ArgumentType.Uint`
        """
        self._post_event(12, serial, direction)


class ZwpTextInputV1Global(Global):
    interface = ZwpTextInputV1


ZwpTextInputV1._gen_c()
ZwpTextInputV1.proxy_class = ZwpTextInputV1Proxy
ZwpTextInputV1.resource_class = ZwpTextInputV1Resource
ZwpTextInputV1.global_class = ZwpTextInputV1Global
