#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Test harnesses and mock classes for GLib
Summary(pl.UTF-8):	Osprzęt testowy i klasy atrap dla GLiba
Name:		libglib-testing
Version:	0.1.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://gitlab.gnome.org/pwithnall/libglib-testing/-/tags
Source0:	https://gitlab.gnome.org/pwithnall/libglib-testing/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	90fd671fc676464c5e67d31a41d70b26
URL:		https://gitlab.gnome.org/pwithnall/libglib-testing
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	gtk-doc
BuildRequires:	meson >= 0.45.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
Requires:	glib2 >= 1:2.44
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libglib-testing is a test library providing test harnesses and mock
classes which complement the classes provided by GLib. It is intended
to be used by any project which uses GLib and which wants to write
internal unit tests.

%description -l pl.UTF-8
libglib-testing to biblioteka do testów dostarczająca osprzęt testowy
oraz klasy atrap, uzupełniające klasy dostarczane przez GLiba. Celem
jest używanie w dowolnych projektach wykorzystujących GLiba, w których
mają być napisane wewnętrzne testy jednostkowe.

%package devel
Summary:	Header files for glib-testing library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki glib-testing
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.44

%description devel
Header files for glib-testing library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki glib-testing.

%package static
Summary:	Static glib-testing library
Summary(pl.UTF-8):	Statyczna biblioteka glib-testing
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static glib-testing library.

%description static -l pl.UTF-8
Statyczna biblioteka glib-testing.

%package apidocs
Summary:	API documentation for glib-testing library
Summary(pl.UTF-8):	Dokumentacja API biblioteki glib-testing
Group:		Documentation
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description apidocs
API documentation for glib-testing library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki glib-testing.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libglib-testing-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglib-testing-0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglib-testing-0.so
%{_includedir}/glib-testing-0
%{_pkgconfigdir}/glib-testing-0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libglib-testing-0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libglib-testing
