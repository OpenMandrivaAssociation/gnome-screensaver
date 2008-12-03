%define name gnome-screensaver
%define version 2.25.1
%define release %mkrel 1

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
# (fc) add support for gnome-keyring (Fedora)
Patch8: gnome-screensaver-2.20-keyring.patch
# (vdanen) drops setgid calls to work with tcb auth
Patch9: gnome-screensaver-2.22.2-drop_setgid.patch

License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libgnome-menu-devel
BuildRequires: libgnomekbd-devel
BuildRequires: gnome-desktop-devel >= 2.23.2
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
%patch8 -p1 -b .keyring
#%patch9 -p0 -b .drop_setgid

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

sed -i -e 's@Exec=slideshow@Exec=%{_libdir}/gnome-screensaver/slideshow@g' $RPM_BUILD_ROOT%{_datadir}/applications/screensavers/ia-ora*.desktop

desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="GNOME" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%find_lang %name

%define schemas %name

# unset default screensaver
%triggerpostun -- gnome-screensaver < 2.20.0-2mdv
  %{_bindir}/gconftool-2 --config-source=xml::/etc/gconf/gconf.xml.local-defaults/ --direct --unset /apps/gnome-screensaver/themes > /dev/null


%if %mdkversion < 200900
%post
%update_menus
%post_install_gconf_schemas %{schemas}
%endif

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

%if %mdkversion < 200900
%postun
%clean_menus
%endif

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
