#!/bin/sh

autoreconf --force --install

echo "now, execute ./configure"
echo "after that, you could build an ipkg with 'make ipkg' in any of the"
echo "directories which support the ipkg target."
