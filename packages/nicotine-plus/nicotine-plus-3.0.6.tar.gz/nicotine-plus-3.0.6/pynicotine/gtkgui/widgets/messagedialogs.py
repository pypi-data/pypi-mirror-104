# COPYRIGHT (C) 2020-2021 Nicotine+ Team
#
# GNU GENERAL PUBLIC LICENSE
#    Version 3, 29 June 2007
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gdk
from gi.repository import Gtk


""" Message Dialogs """


def combo_box_dialog(parent, title, message, callback, callback_data=None, default_text="",
                     option=False, optionmessage="", optionvalue=False, droplist=[]):

    self = Gtk.MessageDialog(
        transient_for=parent,
        message_type=Gtk.MessageType.OTHER,
        buttons=Gtk.ButtonsType.OK_CANCEL,
        text=title,
        secondary_text=message
    )
    self.connect("response", callback, callback_data)
    self.set_default_size(500, -1)
    self.set_destroy_with_parent(True)
    self.set_modal(True)

    label = self.get_message_area().get_children()[-1]
    label.set_selectable(True)

    self.gotoption = option

    self.combo = Gtk.ComboBoxText.new_with_entry()
    self.get_response_value = self.combo.get_child().get_text

    for i in droplist:
        self.combo.append_text(i)

    self.combo.get_child().connect("activate", lambda x: self.response(Gtk.ResponseType.OK))
    self.combo.get_child().set_text(default_text)

    self.get_message_area().add(self.combo)

    self.combo.show()
    self.combo.grab_focus()

    if self.gotoption:

        self.option = Gtk.CheckButton()
        self.option.set_active(optionvalue)
        self.option.set_label(optionmessage)
        self.option.show()

        self.get_message_area().add(self.option)
        self.get_second_response_value = self.option.get_active

    self.present_with_time(Gdk.CURRENT_TIME)


def entry_dialog(parent, title, message, callback, callback_data=None, default=""):

    self = Gtk.MessageDialog(
        transient_for=parent,
        message_type=Gtk.MessageType.OTHER,
        buttons=Gtk.ButtonsType.OK_CANCEL,
        text=title,
        secondary_text=message
    )
    self.connect("response", callback, callback_data)
    self.set_default_size(500, -1)
    self.set_destroy_with_parent(True)
    self.set_modal(True)

    label = self.get_message_area().get_children()[-1]
    label.set_selectable(True)

    entry = Gtk.Entry()
    entry.connect("activate", lambda x: self.response(Gtk.ResponseType.OK))
    entry.set_activates_default(True)
    entry.set_text(default)
    self.get_message_area().add(entry)
    entry.show()

    self.get_response_value = entry.get_text
    self.present_with_time(Gdk.CURRENT_TIME)


def message_dialog(parent, title, message, callback=None):

    self = Gtk.MessageDialog(
        transient_for=parent,
        message_type=Gtk.MessageType.INFO,
        buttons=Gtk.ButtonsType.OK,
        text=title,
        secondary_text=message
    )

    if not callback:
        def callback(x, y):
            x.destroy()

    self.connect("response", callback)
    self.set_destroy_with_parent(True)
    self.set_modal(True)

    label = self.get_message_area().get_children()[-1]
    label.set_selectable(True)

    self.present_with_time(Gdk.CURRENT_TIME)


def option_dialog(parent, title, message, callback, callback_data=None,
                  checkbox_label="", cancel=True, third=""):

    if cancel:
        buttons = Gtk.ButtonsType.OK_CANCEL
    else:
        buttons = Gtk.ButtonsType.OK

    self = Gtk.MessageDialog(
        transient_for=parent,
        message_type=Gtk.MessageType.QUESTION,
        buttons=buttons,
        text=title,
        secondary_text=message
    )
    self.connect("response", callback, callback_data)
    self.set_destroy_with_parent(True)
    self.set_modal(True)

    label = self.get_message_area().get_children()[-1]
    label.set_selectable(True)

    if checkbox_label:
        self.checkbox = Gtk.CheckButton()
        self.checkbox.set_label(checkbox_label)
        self.get_message_area().add(self.checkbox)
        self.checkbox.show()

    if third:
        self.add_button(third, Gtk.ResponseType.REJECT)

    self.present_with_time(Gdk.CURRENT_TIME)
