#!/bin/sh
# Builds qte-popups_<version>_all.deb from ./src
set -e
VER=$(grep '^Version:' src/DEBIAN/control | cut -d' ' -f2)
chmod 755 src/usr/bin/qte-popups
dpkg-deb --build --root-owner-group src "qte-popups_${VER}_all.deb"
echo "Built qte-popups_${VER}_all.deb"
