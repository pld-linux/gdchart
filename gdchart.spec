Summary:	GD-based chart library
Summary(pl):	Oparta na GD biblioteka do wykresów
Name:		gdchart
Version:	0.11.4
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.fred.net/brv/chart/%{name}%{version}dev.tar.gz
# Source0-md5:	eb3db4185f21185a89ae6f7cba49c404
Patch0:		%{name}-make.patch
Patch1:		%{name}-extern.patch
URL:		http://www.fred.net/brv/chart/
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gd-devel(gif) >= 1.8.4
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
Requires:	gd(gif)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD-based chart library.

%description -l pl
Oparta na GD biblioteka do wykresów.

%package devel
Summary:	Header files for gdchart library
Summary(pl):	Pliki nag³ówkowe biblioteki gdchart
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for gdchart library.

%description devel -l pl
Pliki nag³ówkowe biblioteki gdchart.

%package static
Summary:	Static gdchart library
Summary(pl):	Statyczna biblioteka gdchart
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

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
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
