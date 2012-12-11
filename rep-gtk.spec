%define librepver 0.92.0

Name:		rep-gtk
Summary:	GTK+ binding for librep Lisp environment
Version:	0.90.8
Release: %mkrel 1
License:	GPLv2+
Group:		Development/GNOME and GTK+
URL:		http://rep-gtk.sourceforge.net/
Source0:	http://download.tuxfamily.org/librep/rep-gtk/%{name}-%{version}.tar.xz
Requires:	librep >= %{librepver}
BuildRequires:  librep-devel >= %{librepver}
BuildRequires:  gtk+2-devel
BuildRequires:  libgdk_pixbuf2.0-devel >= 2.24
BuildRequires:  libgcrypt-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot


%description
This is a binding of GTK+ for the librep Lisp interpreter.  It is based on 
Marius Vollmer's guile-gtk package (initially version 0.15, updated to 0.17), 
with a new glue-code generator.

%package devel
Summary: C headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This is a binding of GTK+ for the librep Lisp interpreter.  It is based on 
Marius Vollmer's guile-gtk package (initially version 0.15, updated to 0.17), 
with a new glue-code generator.



%prep
%setup -q
[ -x configure ] || ./autogen.sh

%build

%configure2_5x
make host_type=%{_target_platform}


%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std host_type=%{_target_platform}
rm -rf  %buildroot%_datadir/doc/rep-gtk-*

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}


%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files
%defattr (-,root,root,0755)
%doc README README.guile-gtk gtk.defs gdk.defs examples
%{_libexecdir}/rep/gui/

%files devel
%defattr (-,root,root,0755)
%doc ChangeLog
%_includedir/rep-gtk
%_libdir/pkgconfig/rep-gtk.pc


%changelog
* Wed Mar 28 2012 Götz Waschk <waschk@mandriva.org> 0.90.8-1mdv2012.0
+ Revision: 787941
- new version

* Mon Aug 29 2011 Götz Waschk <waschk@mandriva.org> 0.90.7-1
+ Revision: 697353
- new version
- bump gdk-pixbuf dep

* Sun May 01 2011 Götz Waschk <waschk@mandriva.org> 0.90.6-1
+ Revision: 661340
- new version
- bump librep dep
- update file list

* Sun Feb 27 2011 Götz Waschk <waschk@mandriva.org> 0.90.5-1
+ Revision: 640672
- new version
- fix source URL

* Thu Dec 16 2010 Götz Waschk <waschk@mandriva.org> 0.90.4-2mdv2011.0
+ Revision: 622276
- rebuild

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 0.90.4-1mdv2011.0
+ Revision: 581305
- new version
- update file list

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.90.3-1mdv2011.0
+ Revision: 550751
- new version
- new source URL

* Sat Jan 09 2010 Götz Waschk <waschk@mandriva.org> 0.90.2-1mdv2010.1
+ Revision: 488002
- new version
- drop librep dep
- add devel package

* Sat Dec 19 2009 Götz Waschk <waschk@mandriva.org> 0.90.1-1mdv2010.1
+ Revision: 480080
- update to new version 0.90.1

* Sat Aug 29 2009 Götz Waschk <waschk@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 422129
- update to new version 0.90.0

* Sun Jul 05 2009 Götz Waschk <waschk@mandriva.org> 0.18.6r2-1mdv2010.0
+ Revision: 392598
- update to new version 0.18.6r2

* Sat Jun 20 2009 Götz Waschk <waschk@mandriva.org> 0.18.6-1mdv2010.0
+ Revision: 387480
- new version
- call autogen

* Sun May 03 2009 Götz Waschk <waschk@mandriva.org> 0.18.5-1mdv2010.0
+ Revision: 371313
- new version
- fix installation

* Thu Mar 05 2009 Götz Waschk <waschk@mandriva.org> 0.18.4-1mdv2009.1
+ Revision: 348802
- fix installation
- drop libglade and gnome bindings
- new version
- bump librep dep

* Mon Nov 24 2008 Götz Waschk <waschk@mandriva.org> 0.18.3-1mdv2009.1
+ Revision: 306174
- fix pkgconfig file location
- new version
- drop patch
- update license
- update file list

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.18-11mdv2009.0
+ Revision: 260213
- rebuild
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Feb 19 2008 Thierry Vignaud <tv@mandriva.org> 0.18-8mdv2008.1
+ Revision: 172432
- rebuild
- rebuild
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Jul 30 2007 Götz Waschk <waschk@mandriva.org> 0.18-6mdv2008.0
+ Revision: 56733
- fix buildrequires
- unpack patch
- Import rep-gtk



* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 0.18-1mdv2007.0
- Rebuild

* Tue Jan 10 2006 Götz Waschk <waschk@mandriva.org> 0.18-5mdk
- Rebuild
- use mkrel

* Mon Jan 24 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.18-4mdk
- from Anders Melchiorsen :
- changed gtk-2.4 fix to the one from 
  http://linuxfromscratch.org/pipermail/blfs-dev/2004-March/005502.html

* Fri Jun 25 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.18-3mdk
- replace patch with fix from cvs

* Wed Apr 21 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.18-2mdk
- fix source url
- fix buildrequires
- fix build with new gtk

* Sun Aug  3 2003 G�tz Waschk <waschk@linux-mandrake.com> 0.18-1mdk
- fix buildrequires
- new version

* Sun Jul 20 2003 G�tz Waschk <waschk@linux-mandrake.com> 0.17-3mdk
- rebuild against current orbit

* Thu Jan 16 2003 G�tz Waschk <waschk@linux-mandrake.com> 0.17-2mdk
- rebuild against latest ssl

* Fri Nov 15 2002 G�tz Waschk <waschk@linux-mandrake.com> 0.17-1mdk
- drop patch
- new version

* Fri Aug  9 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.16-2mdk
- Patch0: fix crash when selecting color (bug 87959)
- Recompiled against latest librep

* Mon Jun 24 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.16-1mdk
- Release 0.16

* Wed Jun 12 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.15-5.20020611.1mdk
- new snapshot

* Tue Jun  4 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.15-5.20020524.1mdk
- new snapshot

* Fri May 10 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.15-5.20020502.1mdk 
- GNOME 2 cvs snapshot

* Tue Oct 16 2001 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.15-4mdk
- rebuilt with libpng3

* Tue Jul  3 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.15-3mdk
- Recompiled against latest librep

* Mon Dec 18 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.15-2mdk
- Remove explicit dependency on libraries

* Fri Dec  8 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.15-1mdk
- 0.15

* Wed Nov 15 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.14-2mdk
- rebuild against (and require) librep-0.13.2

* Fri Sep 22 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.14-1mdk
- 0.14

* Wed Aug 30 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.13a-6mdk
- Add support for gdk-pixbuf 

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.13a-5mdk
- automatically added BuildRequires

* Thu Aug  3 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.13a-4mdk
- force version dependencies
- remove Packager

* Thu Jul 27 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.13a-3mdk
- rebuild to fix problems with previous build (macro problems)

* Wed Jul 19 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.13a-2mdk
- rebuild for directory changes

* Wed Jul 12 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.13a-1mdk
- 0.13a
- more macroization

* Tue Jul 11 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.13-1mdk
- 0.13

* Sun Jul  9 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.12-1mdk
- 0.12
- specfile cleanup
- macroization

* Thu May 11 2000 Vincent Danen <vdanen@linux-mandrake.com> 0.10-2mdk
- add --with-libglade so sawfish will build themer package

* Wed May 10 2000 Vincent Danen <vdanen@linux-mandrake.com> 0.10-1mdk
- 0.10

* Fri Apr 14 2000 Vincent Danen <vdanen@linux-mandrake.com>
- fix groups
- applied helixcode gnome patch

* Sat Mar 11 2000 Vincent Danen <vdanen@linux-mandrake.com>
- specfile cleanups
- 0.9.1

* Fri Feb 04 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- used srpm provided by Vincent Danen <vdanen@linux-mandrake.com>

* Sun Jan 30 2000 Vincent Danen <vdanen@linux-mandrake.com>
- initial specfile
- bzip sources
