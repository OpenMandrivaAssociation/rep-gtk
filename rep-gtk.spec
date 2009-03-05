%define librepver 0.17.3

Name:		rep-gtk
Summary:	GTK+ binding for librep Lisp environment
Version:	0.18.4
Release: %mkrel 1
License:	GPLv2+
Group:		Development/GNOME and GTK+
BuildRequires:	libglade2.0-devel 
URL:		http://rep-gtk.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/rep-gtk/%{name}-%{version}.tar.bz2
Requires:	librep >= %{librepver}
BuildRequires:  librep-devel >= %{librepver}
BuildRequires:  libgcrypt-devel
BuildRequires:	libgnomeui2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot


%description
This is a binding of GTK+ for the librep Lisp interpreter.  It is based on 
Marius Vollmer's guile-gtk package (initially version 0.15, updated to 0.17), 
with a new glue-code generator.


%package libglade
#gw rpmlint wants %mklibname
Summary:	Librep binding for the libglade library for loading user interfaces
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}

%description libglade
This is a binding of libglade for the librep Lisp interpreter.  libglade allows
applications to dynamically load XML descriptions of GTK+ widget hierarchies. 
These hierarchies may be created by the GLADE GUI builder.


%package gnome
Summary:	GNOME binding for librep
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}

%description gnome
This is a binding of the various GNOME libraries for the librep Lisp 
interpreter. It include support for the basic GNOME functions, the GNOME user 
interface widgets, and the GNOME Canvas architecture, and the GNOME version
of libglade.


%prep
%setup -q

%build

%configure2_5x --with-libglade --with-gnome
make host_type=%{_target_platform}


%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std host_type=%{_target_platform}
rm -rf  %buildroot%_datadir/doc/rep-gtk-*

%if %_lib != lib
mv %buildroot%_prefix/lib/pkgconfig %buildroot%_libdir
%endif

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
%doc README README.guile-gtk ChangeLog gtk.defs gdk.defs BUGS examples
%dir  %{_libexecdir}/rep/%{_target_platform}/gui
%dir %{_libexecdir}/rep/%{_target_platform}/gui/gtk-2
%{_libexecdir}/rep/%{_target_platform}/gui/gtk-2/gtk.*
%{_libexecdir}/rep/%{_target_platform}/gui/gtk-2/types.*
%_libdir/pkgconfig/rep-gtk.pc

%files libglade
%defattr (-,root,root,0755)
%doc libglade.defs examples/test-libglade examples/simple.glade
%doc examples/rep-ui examples/rep-ui.glade
%{_libexecdir}/rep/%{_target_platform}/gui/gtk-2/libglade.*

%files gnome
%defattr (-,root,root,0755)
%doc gnome*.defs examples/gnome-test examples/canvas-test gdk-pixbuf.defs
%{_libexecdir}/rep/%{_target_platform}/gui/gtk-2/gnome*
