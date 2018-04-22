# Maintainer: john smith <hidden at mail dot com>
pkgname="gnome-livewallpaper"
pkgver=0.1
pkgrel=1
pkgdesc="Simple Gnome Livewallpaper Indicator by John Smith."
arch=('any')
url="https://github.com/john4smith/gnome-livewallpaper"
license=('GPL3')
depends=('gnome-shell' 'libappindicator-gtk3' 'python-gobject' 'dconf')
optdepends=('gnome-shell-extension-appindicator-git: gnome indicator support'
            'gnome-shell-extension-topicons-plus: gnome indicator support')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('SKIP')

prepare(){
 cd "${srcdir}"/${pkgname}-${pkgver}/
 sed -i "s/local\/src/share\/${pkgname}/g" ${pkgname}.desktop
}

package() {
 cd "${srcdir}"/${pkgname}-${pkgver}/
 install -dm755 "${pkgdir}"/usr/share/applications
 install -dm755 "${pkgdir}"/usr/share/${pkgname}
 install -m644 ${pkgname}.desktop "${pkgdir}"/usr/share/applications
 install -m755 ${pkgname}.py "${pkgdir}"/usr/share/${pkgname}
 install -m644 LICENSE "${pkgdir}"/usr/share/${pkgname}
}
