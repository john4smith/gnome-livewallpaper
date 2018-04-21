# Make a Debian/Ubuntu Package
#### Download the Source Package from GitHub, extract it and then run this in your Terminal
```
cd gnome-caffeine-*/
pkgname="gnome-caffeine"
pkgdir="/tmp/gnome-caffeine-$$"
mkdir -p "${pkgdir}"/DEBIAN
install -dm755 "${pkgdir}"/usr/share/applications
install -dm755 "${pkgdir}"/usr/share/${pkgname}
install -m644 gnome-caffeine.desktop "${pkgdir}"/usr/share/applications
install -m755 gnome-caffeine.py "${pkgdir}"/usr/share/${pkgname}
install -m644 LICENSE "${pkgdir}"/usr/share/${pkgname}
install -m644 debian/control "${pkgdir}"/DEBIAN
sed -i "s/\/usr\/local\/src/\/usr\/share\/${pkgname}/g" "${pkgdir}"/usr/share/applications/*
pkgsize=$(du -s "${pkgdir}"/usr | cut -f1)
pkgver=$(grep ^Version: "${pkgdir}"/DEBIAN/control | cut -d" " -f2)
sed -i "s/^Installed-Size:.*/Installed-Size: ${pkgsize}/" "${pkgdir}"/DEBIAN/control
bash -c "cd \"${pkgdir}\"; find usr/ -type f -exec md5sum '{}' \; > DEBIAN/md5sums"
dpkg-deb --build "${pkgdir}" ../${pkgname}-${pkgver}_all.deb
```
