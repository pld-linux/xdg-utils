#!/bin/sh
PACKAGE=xdg-utils

set -e
set -x

if [ ! -d $PACKAGE/ ]; then
	git clone git://anongit.freedesktop.org/git/xdg/xdg-utils $PACKAGE/
else
	cd $PACKAGE
	git pull --rebase
	cd ..
fi

export GIT_DIR=$PACKAGE/.git
VERSION=$(git describe --tags)
ARCHIVE=$PACKAGE-$VERSION.tar.gz

if [ -e $ARCHIVE ]; then
	echo >&2 "$ARCHIVE already exists"
	exit 0
fi
git archive master --prefix=$PACKAGE-$VERSION/ -o $ARCHIVE
