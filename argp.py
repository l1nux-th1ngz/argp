# PKGBUILD

pkgname=argp
pkgver=1.0
pkgrel=1
pkgdesc="GUI Chat App with GPT for Arch Linux"
arch=('any')
url="https://github.com/l1nux-th1ngz/argp"
license=('MIT')
depends=('python')

# Include the filename in the source array
source=("$pkgname-$pkgver.tar.gz::${url}/archive/v$pkgver.tar.gz")

build() {
    # No build actions are needed for a Python application
    :
}

package() {
    # Automatically download the source code from GitHub
    if [ ! -d "$srcdir/$pkgname-$pkgver" ]; then
        git clone --depth 1 --branch "v$pkgver" "$url" "$srcdir/$pkgname-$pkgver"
    fi

    # Install the application
    install -Dm755 "$srcdir/$pkgname-$pkgver/argp.py" "$pkgdir/usr/bin/argp"
}
