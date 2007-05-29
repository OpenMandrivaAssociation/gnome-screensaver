%define name gnome-screensaver
%define version 2.18.2
%define release %mkrel 1

Summary: GNOME Screensaver
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Source1: mandriva-slideshow.desktop
# (fc) 0.0.20-2mdk enable user switching
Patch1: gnome-screensaver-0.0.20-userswitching.patch
# (fc) 2.15.7-2mdv allow sort images list
Patch2: gnome-screensaver-2.17.4-sort.patch
# (fc) 2.15.7-2mdv allow solid background for images
Patch3: gnome-screensaver-2.17.5-solidbg.patch
# (fc) 2.15.7-2mdv change default settings
Patch4: gnome-screensaver-2.15.7-default.patch

License: GPL
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libgnome-menu-devel
BuildRequires: libgnomekbd-devel
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

%description
gnome-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.
It is designed to support:

        * the ability to lock down configuration settings
        * translation into other languages
        * user switching

%prep
%setup -q
%patch1 -p1 -b .userswitching
%patch2 -p1 -b .sort
%patch3 -p1 -b .solidbg
%patch4 -p1 -b .default

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

install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/screensavers

#menu
install -d -m 755 $RPM_BUILD_ROOT%{_menudir}
cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): \
	command="%{_bindir}/gnome-screensaver-preferences" \
	needs="gnome" \
	section="System/Configuration/GNOME" \
	icon="screensaver" \
	title="Screensaver" \
	longtitle="Set your screensaver preferences" \
	startup_notify="true" \
	xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Configuration-GNOME" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%find_lang %name

%define schemas %name

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
%doc README ChangeLog AUTHORS
%config(noreplace) %_sysconfdir/xdg/menus/gnome-screensavers.menu
%config(noreplace) %_sysconfdir/pam.d/gnome-screensaver
%_sysconfdir/gconf/schemas/%name.schemas
%_bindir/*
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
%_menudir/%name
