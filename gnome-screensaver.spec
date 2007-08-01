%define name gnome-screensaver
%define version 2.19.6
%define release %mkrel 1

Summary: GNOME Screensaver
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Source1: ia-ora-free-slideshow.desktop
Source2: ia-ora-orange-slideshow.desktop
Source3: ia-ora-blue-slideshow.desktop
Source4: ia-ora-gray-slideshow.desktop
# (fc) 2.15.7-2mdv change default settings
Patch4: gnome-screensaver-2.15.7-default.patch
# (fc) 2.19.6-1mdv allow to disable image maximization
Patch5: gnome-screensaver-2.19-nomaximize.patch

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
%patch5 -p1 -b .nomaximize

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

install -m644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/applications/screensavers

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Configuration-GNOME" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%find_lang %name

%define schemas %name

%post
%update_menus
if [ ! -d %{_sysconfdir}/gconf/gconf.xml.local-defaults/apps/gnome-screensaver -a "x$META_CLASS" != "x" ]; then
 unset SCREENSAVER
 case "$META_CLASS" in
  *server) SCREENSAVER='[screensavers-ia-ora-gray-slideshow]' ;;
  *desktop) SCREENSAVER='[screensavers-ia-ora-orange-slideshow]' ;;
  *download) SCREENSAVER='[screensavers-ia-ora-free-slideshow]';;
 esac

  if [ "x$SCREENSAVER" != "x" ]; then 
  %{_bindir}/gconftool-2 --config-source=xml::/etc/gconf/gconf.xml.local-defaults/ --direct --type=list --list-type=string --set /apps/gnome-screensaver/themes "$SCREENSAVER" > /dev/null
  fi
fi
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
