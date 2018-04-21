#!/usr/bin/python3
#
# LiveWallpaper Indicator
#
# Created by John Smith
#
### BEGIN LICENSE
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

import os,sys,gi,random,fcntl
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, Gio, GLib
from gi.repository import AppIndicator3 as appindicator

def quitApplication(widget):
    sys.exit(0)

def forceQuitText(message):
    dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.CLOSE, str(message))
    dialog.set_title('LiveWallpaper')
    dialog.set_default_size(400, 100)
    dialog.show_all()
    dialog.run()
    dialog.destroy()
    os._exit(0)

def findWallpapers():
    global IMAGES
    IMAGES = []
    try:
        SOURCE_FOLDER = sys.argv[1]
        if os.path.isdir(SOURCE_FOLDER):
            for root, dirs, files in os.walk(SOURCE_FOLDER):
                for file in files:
                    if (file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".jpeg") or file.endswith(".JPEG")):
                        IMAGES.append(os.path.join(root, file))
            random.shuffle(IMAGES)
            if not IMAGES:
                forceQuitText('No Images in the Source-Folder found!')
        else:
            forceQuitText('The given Value is not a Folder!')
    except:
        forceQuitText('No Value for the Source-Folder given!')

def randomWallpaper(widget):
    global IMAGE_NUMBER
    if os.path.isfile(IMAGES[IMAGE_NUMBER]):
        gsettings_screensaver.set_string("picture-uri", "file://" + IMAGES[IMAGE_NUMBER])
        gsettings_background.set_string("picture-uri", "file://" + IMAGES[IMAGE_NUMBER])
    if IMAGE_NUMBER < ( len(IMAGES) - 1 ):
        IMAGE_NUMBER += 1
    else:
        IMAGE_NUMBER = 0
    return True

def toggleSwitch(widget):
    global timerAsync
    isActive = widget.get_active()
    if isActive:
        timerAsync = GLib.timeout_add_seconds(NextWallpaperSec, randomWallpaper, '')
    else:
        if timerAsync > 0:
            GLib.source_remove(timerAsync)

def renderMenu():
    global menu_next
    global menu_switch
    global menu_quit

    # Menu Items
    menu_next = Gtk.MenuItem('Next Wallpaper...')
    menu_next.connect("activate", randomWallpaper)
    menu.append(menu_next)

    menu_switch = Gtk.CheckMenuItem('Random Wallpaper')
    menu_switch.connect("toggled", toggleSwitch)
    menu_switch.set_active(True)
    menu.append(menu_switch)

    menu.append(Gtk.SeparatorMenuItem.new())

    menu_quit = Gtk.MenuItem('Quit')
    menu_quit.connect("activate", quitApplication)
    menu.append(menu_quit)

    menu.show_all()
    ind.set_menu(menu)

##### Main Loop
if __name__ == "__main__":
  # Lock File
  try:
      lockFile = open('/tmp/livewallpaper.lock','w')
      # Try to aquire lock
      fcntl.flock(lockFile, fcntl.LOCK_EX|fcntl.LOCK_NB)
      # File has not been locked before
      fileIsLocked = False
  except:
      # File is already locked
      fileIsLocked = True
  if fileIsLocked:
      sys.exit('LiveWallpaper Indicator instance already running')
  lockFile.write('%d\n'%os.getpid())
  lockFile.flush()

  # Create Application Indicator
  icon_active = "preferences-desktop-wallpaper"
  ind = appindicator.Indicator.new ("LiveWallpaper", icon_active, appindicator.IndicatorCategory.APPLICATION_STATUS)
  ind.set_status(appindicator.IndicatorStatus.ACTIVE)

  # Main Env Vars
  IMAGE_NUMBER = 0
  NextWallpaperSec = 900 # 900 Sec or 15 Min

  # gsettings
  gsettings_background = Gio.Settings.new("org.gnome.desktop.background")
  gsettings_screensaver = Gio.Settings.new("org.gnome.desktop.screensaver")

  # Create Menu
  menu = Gtk.Menu()

  # Render menu items
  findWallpapers()
  renderMenu()

  # Start GTK Main
  Gtk.main()
