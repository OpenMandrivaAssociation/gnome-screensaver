%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	GNOME Screensaver
Name:		gnome-screensaver
Version:	3.6.1
Release:	17
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://www.gnome.org
Source0:	https://ftp.gnome.org/pub/GNOME/sources/gnome-screensaver/%{url_ver}/%{name}-%{version}.tar.xz
Patch101:	0001-Avoid-SEGV-in-gs_fade_reset.patch
Patch200:	gnome-desktop335.patch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libgnomekbdui)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xxf86misc)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xtst)

Requires:	xsltproc
Requires:	dbus-x11
Suggests:	mandriva-theme-screensaver

%description
gnome-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.
It is designed to support:

* the ability to lock down configuration settings
* translation into other languages
* user switching

%prep
%setup -q
%autopatch -p1

%build
%configure \
	--disable-more-warnings

%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS
%{_sysconfdir}/pam.d/gnome-screensaver
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/*
%{_libexecdir}/gnome-screensaver-dialog
%{_mandir}/man1/gnome-screensaver*

