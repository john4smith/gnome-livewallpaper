# gnome-livewallpaper
Python3 Indicator for changes the Background every 15 min for the Gnome Desktop (Livewallpaper)
![Alt text](/screenshot.png?raw=true "Screenshot")
___
### Run
#### (install the necessary Python Packages for your Linux Distribution)
```
python3 gnome-livewallpaper.py ~/Pictures
```
___
### Create a Autostarter
Test it, befor you create a Autostarter and then copy the file to "/usr/local/src/".
Then create the file "~/.config/autostart/gnome-livewallpaper.desktop" with the content:
```
[Desktop Entry]
Type=Application
Name=Livewallpaper Indicator
Exec=/usr/local/src/gnome-livewallpaper.py ~/Pictures
Icon=preferences-desktop-wallpaper
Comment=Autochange your Desktop Wallpaper
```
