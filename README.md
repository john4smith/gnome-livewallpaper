# gnome-livewallpaper
Python3 Indicator for changes the Background every 15 min for the Gnome Desktop (Livewallpaper)
![Alt text](/screenshot.png?raw=true "Screenshot")
___
### Run
- install the necessary Python Packages for your Linux Distribution (try and error)
- install one Extension for Gnome [appindicator](https://extensions.gnome.org/extension/615/appindicator-support/) or [topicons](https://extensions.gnome.org/extension/1031/topicons/)
```
python3 gnome-livewallpaper.py /usr/share/backgrounds
```
___
### Install
#### for Ubuntu 18.04, install the Release deb-File!
Copy the Script to "/usr/local/src/" with:
```
sudo install -dm755 /usr/local/src
sudo install -m755 gnome-livewallpaper.py /usr/local/src
```
___
### Create a Autostarter
##### Change the Backgroundfolder (full Path!)
Create a File "~/.config/autostart/gnome-livewallpaper.desktop" with the content:
```
[Desktop Entry]
Type=Application
Name=Livewallpaper Indicator
Exec=/usr/local/src/gnome-livewallpaper.py /usr/share/backgrounds
Icon=preferences-desktop-wallpaper
Comment=Autochange your Desktop Wallpaper
```
