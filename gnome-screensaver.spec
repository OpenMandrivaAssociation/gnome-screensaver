%define name gnome-screensaver
%define version 2.21.6
%define release %mkrel 2

Summary: GNOME Screensaver
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Source1: ia-ora-slideshow.desktop
Source2: ia-ora-blue-slideshow.desktop
Source3: ia-ora-orange-slideshow.desktop
Source4: ia-ora-gray-slideshow.desktop
Source5: ia-ora-free-slideshow.desktop
Source6: ia-ora-one-slideshow.desktop
# (fc) 2.15.7-2mdv change default settings
Patch4: gnome-screensaver-2.15.7-default.patch
# (fc) 2.20.0-4mdv save gamma ramp before modifying it (GNOME bug #342850) (John Bryant)
Patch7: gnome-screensaver-2.20-fixgammaramp.patch
# (fc) add support for gnome-keyring (Fedora)
Patch8: gnome-screensaver-2.20-keyring.patch

License: GPL
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libgnome-menu-devel
BuildRequires: libgnomekbd-devel
BuildRequires: libnotify-devel
BuildRequires: libxmu-devel
BuildRequires: libexif-devel
BuildRequires: libmesagl-devel
BuildRequires: libxscrnsaver-devel
BuildRequires: libxxf86misc-devel
BuildRequires: libxxf86vm-devel
BuildRequires: dbus-devel >= 0.30
BuildRequires: pam-devel
BuildRequires: gdm
BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: desktop-file-utils
Requires: libxslt-proc
Requires: dbus-x11
Suggests: mandriva-theme-screensaver

%description
gnome-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.
It is designed to support:

        * the ability to lock down configuration settings
        * translation into other languages
        * user switching

%prep
%setup -q
%patch4 -p1 -b .default
%patch7 -p1 -b .fixgammaramp
%patch8 -p1 -b .keyring

%build
%configure2_5x --disable-more-warnings --with-xscreensaverdir=%{_datadir}/xscreensaver/config --with-xscreensaverhackdir=%{_libdir}/xscreensaver
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

sed -ie 's@XSL=${DIST_BIN}/xscreensaver-config.xsl@XSL=%{_datadir}/gnome-screensaver/xscreensaver-config.xsl@' \
        data/migrate-xscreensaver-config.sh
sed -ie 's@b=`basename ${FILE} .xml`@b=xscreensaver-`basename ${FILE} .xml`@' \
        data/migrate-xscreensaver-config.sh

install -m755 data/migrate-xscreensaver-config.sh $RPM_BUILD_ROOT%{_datadir}/gnome-screensaver
install -m644 data/xscreensaver-config.xsl $RPM_BUILD_ROOT%{_datadir}/gnome-screensaver

install -m644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/applications/screensavers

desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="GNOME" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%find_lang %name

%define schemas %name

# unset default screensaver
%triggerpostun -- gnome-screensaver < 2.20.0-2mdv
  %{_bindir}/gconftool-2 --config-source=xml::/etc/gconf/gconf.xml.local-defaults/ --direct --unset /apps/gnome-screensaver/themes > /dev/null


%post
%update_menus
%post_install_gconf_schemas %{schemas}

%triggerin -- xscreensaver-base xscreensaver-gl xscreensaver-extrusion xscreensaver-matrix
(  cd %{_datadir}/applications/screensavers ; \
  for f in %{_datadir}/xscreensaver/config/*.xml; do
    %{_datadir}/gnome-screensaver/migrate-xscreensaver-config.sh $f > /dev/null 2>&1
  done)

%triggerun -- xscreensaver-base
[ "$2" = 0 ] || exit 0
(cd %{_datadir}/applications/screensavers; \
for f in $(rpm -ql xscreensaver-base | grep '%{_datadir}/xscreensaver/config/'); do
  rm -f xscreensaver-$(basename $f .xml).desktop
done)

%triggerun -- xscreensaver-gl
[ "$2" = 0 ] || exit 0
(cd %{_datadir}/applications/screensavers; \
for f in $(rpm -ql xscreensaver-gl | grep '%{_datadir}/xscreensaver/config/'); do
  rm -f xscreensaver-$(basename $f .xml).desktop
done)

%triggerun -- xscreensaver-extrusion
[ "$2" = 0 ] || exit 0
(cd %{_datadir}/applications/screensavers; \
for f in $(rpm -ql xscreensaver-extrusion | grep '%{_datadir}/xscreensaver/config/'); do
  rm -f xscreensaver-$(basename $f .xml).desktop
done)

%triggerun -- xscreensaver-matrix
[ "$2" = 0 ] || exit 0
(cd %{_datadir}/applications/screensavers; \
for f in $(rpm -ql xscreensaver-matrix | grep '%{_datadir}/xscreensaver/config/'); do
  rm -f xscreensaver-$(basename $f .xml).desktop
done)



%preun
%preun_uninstall_gconf_schemas %{schemas}

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS
%config(noreplace) %_sysconfdir/xdg/menus/gnome-screensavers.menu
%config(noreplace) %_sysconfdir/pam.d/gnome-screensaver
%_sysconfdir/gconf/schemas/%name.schemas
%_bindir/*
%_mandir/man1/gnome-screensaver*
%_libexecdir/gnome-screensaver-dialog
%_libexecdir/gnome-screensaver-gl-helper
%_libdir/%name
%_datadir/desktop-directories/gnome-screensaver.directory
%_datadir/applications/gnome-screensaver-preferences.desktop
%_datadir/applications/screensavers
%_datadir/pixmaps/backgrounds/cosmos
%_datadir/pixmaps/*.svg
%_datadir/%name/
%_libdir/pkgconfig/*.pc
