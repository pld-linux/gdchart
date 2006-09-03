Summary:	GD-based chart library
Summary(pl):	Oparta na GD biblioteka do wykres�w
Name:		gdchart
Version:	0.11.5
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.fred.net/brv/chart/%{name}%{version}dev.tar.gz
# Source0-md5:	a4af7bc927d8b88934da56fce10a7a3c
Patch0:		%{name}-make.patch
Patch1:		%{name}-extern.patch
URL:		http://www.fred.net/brv/chart/
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gd-devel(gif) >= 2.0.28
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
Requires:	gd(gif)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD-based chart library.

%description -l pl
Oparta na GD biblioteka do wykres�w.

%package devel
Summary:	Header files for gdchart library
Summary(pl):	Pliki nag��wkowe biblioteki gdchart
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gdchart library.

%description devel -l pl
Pliki nag��wkowe biblioteki gdchart.

%package static
Summary:	Static gdchart library
Summary(pl):	Statyczna biblioteka gdchart
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gdchart library.

%description static -l pl
Statyczna biblioteka gdchart.

%prep
%setup -q -n %{name}%{version}dev
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	PREFIX_LIB="%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX_LIB="%{_libdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
