# COPYRIGHT (C) 2020-2021 Nicotine+ Team
# COPYRIGHT (C) 2016-2017 Michael Labouebe <gfarmerfr@free.fr>
# COPYRIGHT (C) 2008-2010 Quinox <quinox@users.sf.net>
# COPYRIGHT (C) 2006-2009 Daelstorm <daelstorm@gmail.com>
# COPYRIGHT (C) 2003-2004 Hyriand <hyriand@thegraveyard.org>
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

import os
import time

from gi.repository import GdkPixbuf
from gi.repository import GLib
from gi.repository import Gtk

from pynicotine import slskmessages
from pynicotine.config import config
from pynicotine.gtkgui.utils import append_line
from pynicotine.gtkgui.utils import load_ui_elements
from pynicotine.gtkgui.utils import triggers_context_menu
from pynicotine.gtkgui.widgets.filechooser import save_file
from pynicotine.gtkgui.widgets.iconnotebook import IconNotebook
from pynicotine.gtkgui.widgets.infobar import InfoBar
from pynicotine.gtkgui.widgets.popupmenu import PopupMenu
from pynicotine.gtkgui.widgets.theme import update_widget_visuals
from pynicotine.gtkgui.widgets.treeview import initialise_columns
from pynicotine.gtkgui.widgets.treeview import set_treeview_selected_row
from pynicotine.logfacility import log
from pynicotine.utils import humanize
from pynicotine.utils import human_speed


# User Info and User Browse Notebooks
class UserTabs(IconNotebook):

    def __init__(self, frame, subwindow, notebookraw, tab_label, tab_name):

        self.frame = frame

        IconNotebook.__init__(
            self,
            self.frame.images,
            angle=config.sections["ui"]["labelinfo"],
            tabclosers=config.sections["ui"]["tabclosers"],
            show_hilite_image=config.sections["notifications"]["notification_tab_icons"],
            reorderable=config.sections["ui"]["tab_reorderable"],
            show_status_image=config.sections["ui"]["tab_status_icons"],
            notebookraw=notebookraw
        )

        self.popup_enable()

        self.subwindow = subwindow

        self.users = {}
        self.tab_label = tab_label
        self.tab_name = tab_name

    def init_window(self, user):

        try:
            status = self.frame.np.users[user].status
        except Exception:
            # Offline
            status = 0

        w = self.users[user] = self.subwindow(self, user)
        self.append_page(w.Main, user, w.on_close, status=status)

    def show_user(self, user, conn=None, msg=None, indeterminate_progress=False, change_page=True, folder=None, local_shares_type=None):

        self.save_columns()

        if user in self.users:
            self.users[user].conn = conn

        elif not change_page:
            # This tab was closed, but we received a response. Don't reopen it.
            return

        else:
            self.init_window(user)

        self.users[user].show_user(msg, folder, indeterminate_progress, local_shares_type)

        if change_page:
            self.set_current_page(self.page_num(self.users[user].Main))
            self.frame.change_main_page(self.tab_name)

    def show_connection_error(self, user):
        if user in self.users:
            self.users[user].show_connection_error()

    def save_columns(self):
        """ Save the treeview state of the currently selected tab """

        current_page = self.get_nth_page(self.get_current_page())

        for tab in self.users.values():
            if tab.Main == current_page:
                tab.save_columns()
                break

    def get_user_stats(self, msg):

        if msg.user in self.users:
            tab = self.users[msg.user]
            tab.speed.set_text(_("Speed: %s") % human_speed(msg.avgspeed))
            tab.filesshared.set_text(_("Files: %s") % humanize(msg.files))
            tab.dirsshared.set_text(_("Directories: %s") % humanize(msg.dirs))

    def get_user_status(self, msg):

        if msg.user in self.users:

            tab = self.users[msg.user]
            tab.status = msg.status

            self.set_user_status(tab.Main, msg.user, msg.status)

    def is_new_request(self, user):

        if user in self.users:
            return self.users[user].is_refreshing()

        return True

    def show_interests(self, msg):

        if msg.user in self.users:
            self.users[msg.user].show_interests(msg.likes, msg.hates)

    def update_gauge(self, msg):

        for i in self.users.values():
            if i.conn == msg.conn.conn:
                i.update_gauge(msg)

    def update_visuals(self):

        for i in self.users.values():
            i.update_visuals()

    def on_tab_popup(self, widget, page):

        username = self.get_page_owner(page, self.users)

        if username not in self.users:
            return False

        menu = self.users[username].user_popup
        menu.toggle_user_items()
        menu.popup()
        return True

    def login(self):

        for user in self.users:
            # Get notified of user status
            self.frame.np.watch_user(user)

    def conn_close(self):

        for user in self.users:
            tab = self.users[user]
            tab.status = 0

            self.set_user_status(tab.Main, user, tab.status)


class UserInfo:

    def __init__(self, userinfos, user):

        self.userinfos = userinfos
        self.frame = userinfos.frame

        # Build the window
        load_ui_elements(self, os.path.join(self.frame.gui_dir, "ui", "userinfo.ui"))
        self.info_bar = InfoBar(self.InfoBar, Gtk.MessageType.INFO)

        # Request user status, speed and number of shared files
        self.frame.np.watch_user(user, force_update=True)

        # Request user interests
        self.frame.np.queue.append(slskmessages.UserInterests(user))

        self.user = user
        self.conn = None
        self._descr = ""
        self.image_pixbuf = None
        self.zoom_factor = 5
        self.actual_zoom = 0
        self.status = 0

        self.hates_store = Gtk.ListStore(str)
        self.Hates.set_model(self.hates_store)

        self.hate_column_numbers = list(range(self.hates_store.get_n_columns()))
        cols = initialise_columns(
            None,
            self.Hates,
            ["hates", _("Hates"), 0, "text", None]
        )
        cols["hates"].set_sort_column_id(0)

        self.hates_store.set_sort_column_id(0, Gtk.SortType.ASCENDING)

        self.likes_store = Gtk.ListStore(str)
        self.Likes.set_model(self.likes_store)

        self.like_column_numbers = list(range(self.likes_store.get_n_columns()))
        cols = initialise_columns(
            None,
            self.Likes,
            ["likes", _("Likes"), 0, "text", None]
        )
        cols["likes"].set_sort_column_id(0)

        self.likes_store.set_sort_column_id(0, Gtk.SortType.ASCENDING)

        self.tag_local = self.descr.get_buffer().create_tag()

        self.update_visuals()

        self.user_popup = popup = PopupMenu(self.frame)
        popup.setup_user_menu(user, page="userinfo")
        popup.setup(
            ("", None),
            ("#" + _("Close All Tabs"), self.on_close_all_tabs),
            ("#" + _("_Close Tab"), self.on_close)
        )

        self.interest_popup_menu = popup = PopupMenu(self.frame)
        popup.setup(
            ("$" + _("I _Like This"), self.on_like_recommendation),
            ("$" + _("I _Dislike This"), self.on_dislike_recommendation),
            ("", None),
            ("#" + _("_Search For Item"), self.on_interest_recommend_search)
        )

        self.image_menu = popup = PopupMenu(self.frame)
        popup.setup(
            ("#" + _("Zoom 1:1"), self.make_zoom_normal),
            ("#" + _("Zoom In"), self.make_zoom_in),
            ("#" + _("Zoom Out"), self.make_zoom_out),
            ("", None),
            ("#" + _("Save Picture"), self.on_save_picture)
        )

    def update_visuals(self):

        for widget in list(self.__dict__.values()):
            update_widget_visuals(widget)

    def show_interests(self, likes, hates):

        self.likes_store.clear()
        self.hates_store.clear()

        for like in likes:
            self.likes_store.insert_with_valuesv(-1, self.like_column_numbers, [like])

        for hate in hates:
            self.hates_store.insert_with_valuesv(-1, self.hate_column_numbers, [hate])

    def save_columns(self):
        # Unused
        pass

    def load_picture(self, data):

        try:
            import gc
            import tempfile

            with tempfile.NamedTemporaryFile() as f:
                f.write(data)
                del data

                self.image_pixbuf = GdkPixbuf.Pixbuf.new_from_file(f.name)
                self.image.set_from_pixbuf(self.image_pixbuf)

            gc.collect()

            self.actual_zoom = 0
            self.SavePicture.set_sensitive(True)

        except Exception as e:
            log.add(_("Failed to load picture for user %(user)s: %(error)s"), {
                "user": self.user,
                "error": str(e)
            })

    def show_user(self, msg, *args):

        if msg is None:
            return

        self._descr = msg.descr
        self.image_pixbuf = None
        self.descr.get_buffer().set_text("")

        append_line(self.descr, msg.descr, self.tag_local, showstamp=False, scroll=False)

        self.uploads.set_text(_("Upload slots: %i") % msg.totalupl)
        self.queuesize.set_text(_("Queued uploads: %i") % msg.queuesize)

        if msg.slotsavail:
            slots = _("Yes")
        else:
            slots = _("No")

        self.slotsavail.set_text(_("Free upload slots: %s") % slots)

        if msg.uploadallowed == 0:
            allowed = _("No one")
        elif msg.uploadallowed == 1:
            allowed = _("Everyone")
        elif msg.uploadallowed == 2:
            allowed = _("Buddies")
        elif msg.uploadallowed == 3:
            allowed = _("Trusted Users")
        else:
            allowed = _("unknown")

        self.AcceptUploads.set_text(_("%s") % allowed)

        if msg.has_pic and msg.pic is not None:
            self.load_picture(msg.pic)

        self.info_bar.set_visible(False)
        self.set_finished()

    def show_connection_error(self):

        self.info_bar.show_message(
            _("Unable to request information from user. Either you both have a closed listening port, the user is offline, or there's a temporary connectivity issue.")
        )

        self.set_finished()

    def set_finished(self):

        # Tab notification
        self.frame.request_tab_icon(self.frame.UserInfoTabLabel)
        self.userinfos.request_changed(self.Main)

        self.progressbar.set_fraction(1.0)

    def update_gauge(self, msg):

        if msg.total == 0 or msg.bytes == 0:
            fraction = 0.0
        elif msg.bytes >= msg.total:
            fraction = 1.0
        else:
            fraction = float(msg.bytes) / msg.total

        self.progressbar.set_fraction(fraction)

    """ Events """

    def on_popup_interest_menu(self, widget):

        model, iterator = widget.get_selection().get_selected()

        if iterator is None:
            return False

        item = model.get_value(iterator, 0)

        if item is None:
            return False

        self.interest_popup_menu.set_user(item)

        actions = self.interest_popup_menu.get_actions()
        actions[_("I _Like This")].set_state(
            GLib.Variant.new_boolean(item in config.sections["interests"]["likes"])
        )
        actions[_("I _Dislike This")].set_state(
            GLib.Variant.new_boolean(item in config.sections["interests"]["dislikes"])
        )

        self.interest_popup_menu.popup()
        return True

    def on_like_recommendation(self, action, state):
        self.frame.interests.on_like_recommendation(action, state, self.interest_popup_menu.get_user())

    def on_dislike_recommendation(self, action, state):
        self.frame.interests.on_dislike_recommendation(action, state, self.interest_popup_menu.get_user())

    def on_interest_recommend_search(self, *args):
        self.frame.interests.recommend_search(self.interest_popup_menu.get_user())

    def on_interest_list_clicked(self, widget, event):

        if triggers_context_menu(event):
            set_treeview_selected_row(widget, event)
            return self.on_popup_interest_menu(widget)

        return False

    def on_send_message(self, *args):
        self.frame.privatechats.send_message(self.user, show_user=True)
        self.frame.change_main_page("private")

    def on_show_ip_address(self, *args):
        self.frame.np.ip_requested.add(self.user)
        self.frame.np.queue.append(slskmessages.GetPeerAddress(self.user))

    def on_refresh(self, *args):
        self.info_bar.set_visible(False)
        self.progressbar.set_fraction(0.0)
        self.frame.local_user_info_request(self.user)

    def on_browse_user(self, *args):
        self.frame.browse_user(self.user)

    def on_add_to_list(self, *args):
        self.frame.np.userlist.add_to_list(self.user)

    def on_ban_user(self, *args):
        self.frame.np.network_filter.ban_user(self.user)

    def on_ignore_user(self, *args):
        self.frame.np.network_filter.ignore_user(self.user)

    def on_save_picture_response(self, selected, data):

        if not os.path.exists(selected):
            self.image_pixbuf.savev(selected, "jpeg", ["quality"], ["100"])
            log.add(_("Picture saved to %s"), selected)
        else:
            log.add(_("Picture not saved, %s already exists."), selected)

    def on_save_picture(self, *args):

        if self.image is None or self.image_pixbuf is None:
            return

        save_file(
            parent=self.frame.MainWindow,
            callback=self.on_save_picture_response,
            initialdir=config.sections["transfers"]["downloaddir"],
            initialfile="%s %s.jpg" % (self.user, time.strftime("%Y-%m-%d %H_%M_%S")),
            title="Save as..."
        )

    def on_image_click(self, widget, event):

        if triggers_context_menu(event):
            return self.on_image_popup_menu()

        return False

    def on_image_popup_menu(self, *args):

        act = True

        if self.image is None or self.image_pixbuf is None:
            act = False

        actions = self.image_menu.get_actions()
        for (action_id, action) in actions.items():
            action.set_enabled(act)

        self.image_menu.popup()
        return True

    def on_scroll_event(self, widget, event):

        if event.get_scroll_deltas().delta_y < 0:
            self.make_zoom_in()
        else:
            self.make_zoom_out()

        return True  # Don't scroll the Gtk.ScrolledWindow

    def make_zoom_normal(self, *args):
        self.make_zoom_in(zoom=True)

    def make_zoom_in(self, *args, zoom=None):

        def calc_zoom_in(a):
            return a + a * self.actual_zoom / 100 + a * self.zoom_factor / 100

        import gc

        if self.image is None or self.image_pixbuf is None or self.actual_zoom > 100:
            return

        x = self.image_pixbuf.get_width()
        y = self.image_pixbuf.get_height()

        if zoom:
            self.actual_zoom = 0
        else:
            self.actual_zoom += self.zoom_factor

        pixbuf_zoomed = self.image_pixbuf.scale_simple(calc_zoom_in(x), calc_zoom_in(y), GdkPixbuf.InterpType.TILES)
        self.image.set_from_pixbuf(pixbuf_zoomed)

        del pixbuf_zoomed

        gc.collect()

    def make_zoom_out(self, *args):

        def calc_zoom_out(a):
            return a + a * self.actual_zoom / 100 - a * self.zoom_factor / 100

        import gc

        if self.image is None or self.image_pixbuf is None:
            return

        x = self.image_pixbuf.get_width()
        y = self.image_pixbuf.get_height()

        self.actual_zoom -= self.zoom_factor

        if calc_zoom_out(x) < 10 or calc_zoom_out(y) < 10:
            self.actual_zoom += self.zoom_factor
            return

        pixbuf_zoomed = self.image_pixbuf.scale_simple(calc_zoom_out(x), calc_zoom_out(y), GdkPixbuf.InterpType.TILES)
        self.image.set_from_pixbuf(pixbuf_zoomed)

        del pixbuf_zoomed

        gc.collect()

    def on_close(self, *args):
        del self.userinfos.users[self.user]
        self.userinfos.remove_page(self.Main)

    def on_close_all_tabs(self, *args):
        self.userinfos.remove_all_pages()
