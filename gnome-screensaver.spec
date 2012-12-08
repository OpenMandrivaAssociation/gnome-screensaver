Name:		gnome-screensaver
Summary:	GNOME Screensaver
Version:	3.6.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz

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



%changelog
* Fri Oct  5 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Wed Jul 18 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.4-1
+ Revision: 810102
- update to new version 3.4.4

* Wed Jul 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.3-1
+ Revision: 808929
- update to new version 3.4.3

* Fri Jun 29 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.2-1
+ Revision: 807554
- new version 3.4.2

* Sun Apr 29 2012 Guilherme Moro <guilherme@mandriva.com> 3.4.1-1
+ Revision: 794387
- Updated to version 3.4.1

* Wed Mar 14 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.2-1
+ Revision: 784896
- new version 3.2.2
- cleaned up spec
- removed ia-ora stuff

* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 2.30.2-3
+ Revision: 677077
- rebuild to add gconf2 as req

* Thu Apr 07 2011 Funda Wang <fwang@mandriva.org> 2.30.2-2
+ Revision: 651739
- add gentoo patches (actually accepted by upstream)

* Wed Sep 29 2010 Götz Waschk <waschk@mandriva.org> 2.30.2-1mdv2011.0
+ Revision: 581967
- new version
- update file list

* Wed Sep 29 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-1mdv2011.0
+ Revision: 581965
- update to new version 2.30.1

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 529947
- update to new version 2.30.0

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 517052
- update to new version 2.29.92

* Fri Feb 12 2010 Götz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 505149
- update to new version 2.29.91

* Mon Feb 08 2010 Götz Waschk <waschk@mandriva.org> 2.29.90-1mdv2010.1
+ Revision: 502344
- update to new version 2.29.90

* Fri Jan 29 2010 Götz Waschk <waschk@mandriva.org> 2.29.1-1mdv2010.1
+ Revision: 497898
- update to new version 2.29.1

* Wed Jan 13 2010 Götz Waschk <waschk@mandriva.org> 2.28.0-3mdv2010.1
+ Revision: 490515
- rebuild for new libgnome-desktop

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 2.28.0-2mdv2010.1
+ Revision: 489641
- rebuild for new libxklavier

* Wed Sep 23 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 447693
- new version
- update file list

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 2.27.0-2mdv2010.0
+ Revision: 390582
- rebuild for new libgnomekbd

* Mon Jun 15 2009 Götz Waschk <waschk@mandriva.org> 2.27.0-1mdv2010.0
+ Revision: 386115
- new version
- update file list

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366920
- update to new version 2.26.1

* Thu Mar 19 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 357662
- new version
- drop patch 8

* Thu Jan 01 2009 Götz Waschk <waschk@mandriva.org> 2.25.2-2mdv2009.1
+ Revision: 323210
- rebuild for new gnome-desktop

* Thu Dec 18 2008 Götz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 315725
- update to new version 2.25.2

* Wed Dec 03 2008 Götz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 309630
- fix build deps
- new version
- drop patch 10

* Thu Nov 27 2008 Frederic Crozat <fcrozat@mandriva.com> 2.24.1-2mdv2009.1
+ Revision: 307261
- Patch10: hardcode path for screensaver helpers (Mdv bug #44321)

* Thu Nov 13 2008 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 302892
- update to new version 2.24.1

* Thu Nov 06 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-2mdv2009.1
+ Revision: 300178
- rebuild for new  gnome-desktop

* Wed Sep 24 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287704
- new version

* Fri Aug 29 2008 Götz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 277244
- new version
- drop patch 0

* Mon Aug 25 2008 Vincent Danen <vdanen@mandriva.com> 2.23.3-2mdv2009.0
+ Revision: 275967
- disable the drop_setgid patch for now

* Wed Jul 23 2008 Götz Waschk <waschk@mandriva.org> 2.23.3-1mdv2009.0
+ Revision: 242689
- new version

* Fri Jul 04 2008 Götz Waschk <waschk@mandriva.org> 2.23.2-2mdv2009.0
+ Revision: 231568
- new version
- patch to make it build
- drop patch 7
- update license
- bump deps

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri May 30 2008 Vincent Danen <vdanen@mandriva.com> 2.22.2-2mdv2009.0
+ Revision: 213355
- add patch to drop the setgid() call in order to make it work with pam_tcb

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 192485
- new version

* Wed Apr 02 2008 Frederic Crozat <fcrozat@mandriva.com> 2.22.1-1mdv2008.1
+ Revision: 191694
- Release 2.22.1 (security fix, for CVE-2008-0887)

* Tue Mar 11 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 185025
- new version

* Thu Jan 31 2008 Götz Waschk <waschk@mandriva.org> 2.21.6-2mdv2008.1
+ Revision: 160712
- rebuild for new libxklavier

* Thu Jan 31 2008 Götz Waschk <waschk@mandriva.org> 2.21.6-1mdv2008.1
+ Revision: 160632
- new version
- drop patches 5,6
- update file list

* Tue Jan 22 2008 Frederic Crozat <fcrozat@mandriva.com> 2.20.0-5mdv2008.1
+ Revision: 156529
- Patch8 (Fedora): add support for gnome-keyring PAM integration

* Sat Jan 12 2008 Frederic Crozat <fcrozat@mandriva.com> 2.20.0-4mdv2008.1
+ Revision: 149810
- Patch7 (John Bryant): save gamma ramp before modifying it (GNOME bug #342850)

  + Thierry Vignaud <tv@mandriva.org>
    - do not package big ChangeLog
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Sep 20 2007 Frederic Crozat <fcrozat@mandriva.com> 2.20.0-2mdv2008.0
+ Revision: 91446
- Patch5: disable profiling
- Patch6: really order slideshow when requested
- Merge all ia ora screensaver into one, with black blackground
- No longer configure screensaver according to META_CLASS

* Tue Sep 18 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89452
- new version

* Fri Sep 07 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.7-3mdv2008.0
+ Revision: 81774
- Fix .desktop to not appear in main menu
- Add new slideshow parameter for Ia Ora One
- Add trigger to handle default settings when upgrading distribution

* Tue Aug 28 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.7-2mdv2008.0
+ Revision: 72567
- Fix Ia Ora screensavers to use the new upstream no-strech slideshow feature

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 2.19.7-1mdv2008.0
+ Revision: 72477
- new version
- drop patch 5

* Wed Aug 01 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.6-1mdv2008.0
+ Revision: 57747
- Release 2.19.6
- Remove patches 1 (no needed), 2, 3 (merged upstream)
- Patch5: allow to disable image maximisation on slideshow
- Add source1, 2, 3, 4 : split Ia Ora screensavers according to colors
- Remove old menu file

* Fri Jun 08 2007 Götz Waschk <waschk@mandriva.org> 2.19.1.1-3mdv2008.0
+ Revision: 37256
- fix buildrequires

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 2.19.1.1-2mdv2008.0
+ Revision: 36168
- rebuild with correct optflags

  + Götz Waschk <waschk@mandriva.org>
    - new version

* Tue May 29 2007 Götz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 32373
- new version

* Wed Apr 18 2007 Götz Waschk <waschk@mandriva.org> 2.18.1-1mdv2008.0
+ Revision: 14377
- new version


* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 142051
- new version

* Mon Feb 26 2007 Götz Waschk <waschk@mandriva.org> 2.17.8-1mdv2007.1
+ Revision: 126158
- new version
- drop patch 5

* Fri Feb 16 2007 Frederic Crozat <fcrozat@mandriva.com> 2.17.7-2mdv2007.1
+ Revision: 121728
-Patch5 (SVN): fix locking

* Mon Feb 12 2007 Götz Waschk <waschk@mandriva.org> 2.17.7-1mdv2007.1
+ Revision: 120224
- new version

* Mon Jan 22 2007 Götz Waschk <waschk@mandriva.org> 2.17.6-1mdv2007.1
+ Revision: 111993
- new version

* Tue Jan 09 2007 Götz Waschk <waschk@mandriva.org> 2.17.5-1mdv2007.1
+ Revision: 106280
- new version
- rediff patch 3

* Wed Dec 20 2006 Götz Waschk <waschk@mandriva.org> 2.17.4-1mdv2007.1
+ Revision: 100781
- new version
- rediff patch 2

* Tue Dec 05 2006 Götz Waschk <waschk@mandriva.org> 2.17.3-2mdv2007.1
+ Revision: 90932
- bump release
- fix buildrequires
- new version

* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 2.17.2-4mdv2007.1
+ Revision: 88297
- buildrequires
- bot rebuild
- bot rebuild
- new version
- depend on libgnomekbd

* Wed Nov 22 2006 Götz Waschk <waschk@mandriva.org> 2.16.2-2mdv2007.1
+ Revision: 86432
- bot rebuild
- new version
- unpack patches
- Import gnome-screensaver

* Tue Oct 10 2006 G�tz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.1
- fix buildrequires
- New version 2.16.1

* Thu Sep 14 2006 Frederic Crozat <fcrozat@mandriva.com> 2.16.0-2mdv2007.0
- Fix xdg menu
- run remove trigger only when uninstalling xscreensaver packages

* Wed Sep 06 2006 G�tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- drop patch 5
- New release 2.16.0

* Tue Sep 05 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.7-3mdv2007.0
- Patch5: various cvs fixes
- Move back xdg file to /etc/xdg, fix Mdv bug #25172

* Tue Aug 29 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.7-2mdv2007.0
- Patch2: allow to disable image randomization
- Patch3: allow solid background for images
- add mandriva screensaver
- Patch4: change default settings (don't lock, mandriva default screensaver)

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.15.7-1mdv2007.0
- New release 2.15.7

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 2.15.6-1mdv2007.0
- New release 2.15.6

* Fri Aug 04 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.5-2mdv2007.0
- Rebuild with latest dbus

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 2.15.5-1mdv2007.0
- New release 2.15.5

* Wed Jul 12 2006 G�tz Waschk <waschk@mandriva.org> 2.15.4-1mdv2007.0
- update file list
- New release 2.15.4

* Thu Jul 06 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.3-4mdv2007.0
- Add dependency on dbus-x11 (Mdv bug #23527)

* Sat Jun 24 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.3-3mdv2007.0
- Switch to XDG menu
- use new macros
- add support for xscreensaver hacks (Fedora)
- Patch2: add xscreensaver .desktop location

* Wed Jun 14 2006 G�tz Waschk <waschk@mandriva.org> 2.15.3-2mdv2007.0
- fix buildrequires

* Wed Jun 14 2006 Götz Waschk <waschk@mandriva.org> 2.15.3-1
- New release 2.15.3

* Wed Jun 07 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.2-1mdv2007.0
- Release 2.15.2

* Wed May 31 2006 Götz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- New release 2.14.2

* Tue Apr 11 2006 Götz Waschk <waschk@mandriva.org> 2.14.1-1mdk
- New release 2.14.1

* Mon Mar 13 2006 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdk
- New release 2.14.0

* Tue Feb 28 2006 G�tz Waschk <waschk@mandriva.org> 2.13.92-1mdk
- update file list
- New release 2.13.92

* Wed Feb 15 2006 Götz Waschk <waschk@mandriva.org> 2.13.91-1mdk
- New release 2.13.91

* Tue Jan 31 2006 Götz Waschk <waschk@mandriva.org> 2.13.90-1mdk
- New release 2.13.90

* Mon Jan 30 2006 Olivier Blin <oblin@mandriva.com> 2.13.5-3mdk
- drop Patch0 (pam_stack), we don't have an obsolete pam anymore

* Thu Jan 26 2006 G�tz Waschk <waschk@mandriva.org> 2.13.5-2mdk
- rebuild for new dbus

* Mon Jan 16 2006 Götz Waschk <waschk@mandriva.org> 2.13.5-1mdk
- New release 2.13.5

* Thu Jan 05 2006 Götz Waschk <waschk@mandriva.org> 0.0.24-1mdk
- New release 0.0.24

* Thu Dec 29 2005 G�tz Waschk <waschk@mandriva.org> 0.0.23-2mdk
- fix buildrequires

* Mon Dec 19 2005 G�tz Waschk <waschk@mandriva.org> 0.0.23-1mdk
- update file list
- New release 0.0.23

* Wed Dec 14 2005 Götz Waschk <waschk@mandriva.org> 0.0.22-1mdk
- New release 0.0.22

* Wed Dec 07 2005 Götz Waschk <waschk@mandriva.org> 0.0.21-1mdk
- New release 0.0.21
- use mkrel

* Tue Nov 22 2005 Frederic Crozat <fcrozat@mandriva.com> 0.0.20-2mdk
- Patch1: enable user switching by default
- remove gdm dependency
- move menu file to the right location

* Wed Nov 16 2005 Götz Waschk <waschk@mandriva.org> 0.0.20-1mdk
- New release 0.0.20

* Tue Nov 15 2005 Götz Waschk <waschk@mandriva.org> 0.0.19-1mdk
- New release 0.0.19

* Thu Nov 03 2005 Götz Waschk <waschk@mandriva.org> 0.0.18-1mdk
- New release 0.0.18

* Thu Oct 27 2005 G�tz Waschk <waschk@mandriva.org> 0.0.17-3mdk
- fix pam configuration (bug #19456)

* Wed Oct 26 2005 G�tz Waschk <waschk@mandriva.org> 0.0.17-2mdk
- fix buildrequires

* Wed Oct 26 2005 G�tz Waschk <waschk@mandriva.org> 0.0.17-1mdk
- New release 0.0.17
- update file list
- bump deps

* Thu Jun 09 2005 Götz Waschk <waschk@mandriva.org> 0.0.6-0.20050608.1mdk
- initial package

