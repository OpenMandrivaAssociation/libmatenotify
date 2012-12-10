%define major	1
%define libname	%mklibname matenotify %{major}
%define devname %mklibname -d matenotify

Summary:	Desktop notifications library
Name:		libmatenotify
Version:	1.4.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

Buildrequires:	gtk-doc
Buildrequires:	mate-common
Buildrequires:	pkgconfig(dbus-glib-1)
Buildrequires:	pkgconfig(gtk+-2.0)

Requires:	virtual-notification-daemon

%description
A library that sends desktop notifications to a notification daemon, as
defined in the Desktop Notifications spec. These notifications can be
used to inform the user about an event or display some form of
information without getting in the user's way.

%package -n %{libname}
Group:		System/Libraries
Summary:	Desktop notifications library - shared library

%description -n %{libname}
This packages contains the shared library for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	Desktop notifications library - headers
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files
%{_bindir}/mate-notify-send

%files -n %{libname}
%{_libdir}/libmatenotify.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%doc %{_datadir}/gtk-doc/html/*



%changelog
* Thu Aug 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.0-1
+ Revision: 811550
- new version 1.4

* Wed Jun 13 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-2
+ Revision: 805472
- rebuild correcting lib & dev pkg names

* Thu May 31 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 801654
- imported package libmatenotify

