Name:		gnome-screensaver
Summary:	GNOME Screensaver
Version:	3.4.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

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
%apply_patches

%build
%configure2_5x \
	--disable-more-warnings

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS
%{_sysconfdir}/pam.d/gnome-screensaver
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/*
%{_libexecdir}/gnome-screensaver-dialog
%{_mandir}/man1/gnome-screensaver*

