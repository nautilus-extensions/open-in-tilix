# Copyright (C) 2022 Nautilus Extensions 
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

import os, subprocess

from gi import require_version

try:
	require_version('Nautilus', '4.0')
	require_version('Gtk', '4.0')
	using_nautilus_43_onwards = True
	print('Using Nautilus 43 or newer')
except:
    require_version('Nautilus', '3.0')
    require_version('Gtk', '3.0')
    using_nautilus_43_onwards = False
    print('Using Nautilus 42 or older')

from gi.repository import Nautilus, GObject, Gio

try:
    from urllib import unquote
    from urlparse import urlparse
except ImportError:
    from urllib.parse import unquote, urlparse

TERMINAL = "tilix"
TILIX_KEYBINDINGS = "com.gexperts.Tilix.Keybindings"
GSETTINGS_OPEN_TERMINAL = "nautilus-open"
REMOTE_URI_SCHEME = ['ftp', 'sftp']

def _checkdecode(s):
    """Decode string assuming utf encoding if it's bytes, else return unmodified"""
    return s.decode('utf-8') if isinstance(s, bytes) else s

def open_terminal_in_file(filename):
    if filename:
        subprocess.call('{0} -w "{1}" &'.format(TERMINAL, filename), shell=True)
    else:
        subprocess.call("{0} &".format(TERMINAL), shell=True)

import locale

import gettext
ROOT_UID = 0

LOCALE_DIR = '@LOCALE_DIR@'

gettext.install('open-in-tilix', LOCALE_DIR)

locale.bindtextdomain('open-in-tilix', LOCALE_DIR)
locale.textdomain('open-in-tilix')

_ = gettext.gettext

class OpenInTilix(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        print("Nautilus In Tilix extension initialized")
        self.is_selected = False

    def get_file_items(self, files):
        if len(files) != 1:
            return
        items = []
        file_ = files[0]

        if file_.is_directory():

            if file_.get_uri_scheme() in REMOTE_URI_SCHEME:
                uri = _checkdecode(file_.get_uri())
                item = Nautilus.MenuItem(name='OpenInTilix::open_remote_item',
                                        label=_('Open Remote Tilix'),
                                        tip=_('Open Remote Tilix In {}').format(uri))
                item.connect('activate', self._menu_activate_cb, file_)
                items.append(item)

            filename = _checkdecode(file_.get_name())
            item = Nautilus.MenuItem(name='OpenInTilix::open_file_item',
                                    label=_('Open In Tilix'),
                                    tip=_('Open Tilix In {}').format(filename))
            item.connect('activate', self._menu_activate_cb, file_)
            items.append(item)

        return items
    
    def _menu_activate_cb(self, menu, file_):
        self._open_terminal(file_)

    def _menu_background_activate_cb(self, menu, file_):
        self._open_terminal(file_)

    def _open_terminal(self, file_):
        if file_.get_uri_scheme() in REMOTE_URI_SCHEME:
            result = urlparse(file_.get_uri())
            if result.username:
                value = 'ssh -t {0}@{1}'.format(result.username,
                                                result.hostname)
            else:
                value = 'ssh -t {0}'.format(result.hostname)
            if result.port:
                value = "{0} -p {1}".format(value, result.port)
            if file_.is_directory():
                value = '{0} cd "{1}" ; $SHELL'.format(value, result.path)

            subprocess.call('{0} -e "{1}" &'.format(TERMINAL, value), shell=True)
        else:
            filename = Gio.File.new_for_uri(file_.get_uri()).get_path()
            open_terminal_in_file(filename)
    def get_background_items(self, window, file_):
        items = []
        if file_.get_uri_scheme() in REMOTE_URI_SCHEME:
            item = Nautilus.MenuItem(name='OpenInTilix::open_bg_remote_item',
                                    label=_('Open Remote Tilix Here'),
                                    tip=_('Open Remote Tilix In This Directory'))
            item.connect('activate', self._menu_activate_cb, file_)
            items.append(item)

        item = Nautilus.MenuItem(name='OpenInTilix::open_bg_file_item',
                                label=_('Open Tilix Here'),
                                tip=_('Open Tilix In This Directory'))
        item.connect('activate', self._menu_background_activate_cb, file_)
        items.append(item)
        return items