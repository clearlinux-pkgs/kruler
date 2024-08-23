#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kruler
Version  : 24.08.0
Release  : 71
URL      : https://download.kde.org/stable/release-service/24.08.0/src/kruler-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/kruler-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/kruler-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: kruler-bin = %{version}-%{release}
Requires: kruler-data = %{version}-%{release}
Requires: kruler-license = %{version}-%{release}
Requires: kruler-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : knotifications-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the kruler package.
Group: Binaries
Requires: kruler-data = %{version}-%{release}
Requires: kruler-license = %{version}-%{release}

%description bin
bin components for the kruler package.


%package data
Summary: data components for the kruler package.
Group: Data

%description data
data components for the kruler package.


%package doc
Summary: doc components for the kruler package.
Group: Documentation

%description doc
doc components for the kruler package.


%package license
Summary: license components for the kruler package.
Group: Default

%description license
license components for the kruler package.


%package locales
Summary: locales components for the kruler package.
Group: Default

%description locales
locales components for the kruler package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kruler-24.08.0
cd %{_builddir}/kruler-24.08.0
pushd ..
cp -a kruler-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724444448
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724444448
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kruler
cp %{_builddir}/kruler-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kruler/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kruler-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kruler/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kruler-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kruler/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kruler
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kruler
/usr/bin/kruler

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kruler.desktop
/usr/share/icons/hicolor/128x128/apps/kruler.png
/usr/share/icons/hicolor/16x16/actions/kruler-east.png
/usr/share/icons/hicolor/16x16/actions/kruler-north.png
/usr/share/icons/hicolor/16x16/actions/kruler-south.png
/usr/share/icons/hicolor/16x16/actions/kruler-west.png
/usr/share/icons/hicolor/16x16/apps/kruler.png
/usr/share/icons/hicolor/22x22/actions/kruler-east.png
/usr/share/icons/hicolor/22x22/actions/kruler-north.png
/usr/share/icons/hicolor/22x22/actions/kruler-south.png
/usr/share/icons/hicolor/22x22/actions/kruler-west.png
/usr/share/icons/hicolor/22x22/apps/kruler.png
/usr/share/icons/hicolor/32x32/apps/kruler.png
/usr/share/icons/hicolor/48x48/apps/kruler.png
/usr/share/icons/hicolor/64x64/apps/kruler.png
/usr/share/knotifications6/kruler.notifyrc
/usr/share/kruler/sounds/move.wav
/usr/share/metainfo/org.kde.kruler.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kruler/index.cache.bz2
/usr/share/doc/HTML/ca/kruler/index.docbook
/usr/share/doc/HTML/ca/kruler/kruler-settings.png
/usr/share/doc/HTML/de/kruler/index.cache.bz2
/usr/share/doc/HTML/de/kruler/index.docbook
/usr/share/doc/HTML/en/kruler/index.cache.bz2
/usr/share/doc/HTML/en/kruler/index.docbook
/usr/share/doc/HTML/en/kruler/kruler-settings.png
/usr/share/doc/HTML/en/kruler/kruler.png
/usr/share/doc/HTML/es/kruler/index.cache.bz2
/usr/share/doc/HTML/es/kruler/index.docbook
/usr/share/doc/HTML/fr/kruler/index.cache.bz2
/usr/share/doc/HTML/fr/kruler/index.docbook
/usr/share/doc/HTML/id/kruler/index.cache.bz2
/usr/share/doc/HTML/id/kruler/index.docbook
/usr/share/doc/HTML/it/kruler/index.cache.bz2
/usr/share/doc/HTML/it/kruler/index.docbook
/usr/share/doc/HTML/it/kruler/kruler-settings.png
/usr/share/doc/HTML/nl/kruler/index.cache.bz2
/usr/share/doc/HTML/nl/kruler/index.docbook
/usr/share/doc/HTML/pt/kruler/index.cache.bz2
/usr/share/doc/HTML/pt/kruler/index.docbook
/usr/share/doc/HTML/pt_BR/kruler/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kruler/index.docbook
/usr/share/doc/HTML/pt_BR/kruler/kruler-settings.png
/usr/share/doc/HTML/pt_BR/kruler/kruler.png
/usr/share/doc/HTML/ru/kruler/index.cache.bz2
/usr/share/doc/HTML/ru/kruler/index.docbook
/usr/share/doc/HTML/sv/kruler/index.cache.bz2
/usr/share/doc/HTML/sv/kruler/index.docbook
/usr/share/doc/HTML/tr/kruler/index.cache.bz2
/usr/share/doc/HTML/tr/kruler/index.docbook
/usr/share/doc/HTML/uk/kruler/index.cache.bz2
/usr/share/doc/HTML/uk/kruler/index.docbook
/usr/share/doc/HTML/uk/kruler/kruler-settings.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kruler/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kruler/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kruler/7697008f58568e61e7598e796eafc2a997503fde

%files locales -f kruler.lang
%defattr(-,root,root,-)

