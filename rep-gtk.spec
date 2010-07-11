%define librepver 0.90.5

Name:		rep-gtk
Summary:	GTK+ binding for librep Lisp environment
Version:	0.90.3
Release: %mkrel 1
License:	GPLv2+
Group:		Development/GNOME and GTK+
URL:		http://rep-gtk.sourceforge.net/
Source0:	http://download.tuxfamily.org/sawfish/rep-gtk/%{name}-%{version}.tar.xz
Requires:	librep >= %{librepver}
BuildRequires:  librep-devel >= %{librepver}
BuildRequires:  gtk+2-devel
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
%doc README README.guile-gtk gtk.defs gdk.defs BUGS examples
%dir  %{_libexecdir}/rep/%{_target_platform}/gui
%dir %{_libexecdir}/rep/%{_target_platform}/gui/gtk-2
%{_libexecdir}/rep/%{_target_platform}/gui/gtk-2/gtk.*
%{_libexecdir}/rep/%{_target_platform}/gui/gtk-2/types.*

%files devel
%defattr (-,root,root,0755)
%doc ChangeLog
%_includedir/rep-gtk
%_libdir/pkgconfig/rep-gtk.pc
