
Name: libmodsecurity
Version: 3.0.12
Release: 1%{?dist}
Summary: A library that loads/interprets rules written in the ModSecurity SecRules
Group: System/Libraries

License: ASL 2.0
URL: https://www.modsecurity.org/

Source0: https://github.com/owasp-modsecurity/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: flex
BuildRequires: bison
BuildRequires: git-core
BuildRequires: ssdeep-devel
BuildRequires: libmaxminddb-devel
BuildRequires: lua-devel
BuildRequires: doxygen
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(yajl)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(lmdb)

%if 0%{?rhel} <= 8
BuildRequires: pkgconfig(geoip)
%endif

# libinjection is supposed to be bundled (same as with mod_security 2.x)
# See: https://github.com/client9/libinjection#embedding
Provides: bundled(libinjection) = 3.9.2

%description
Libmodsecurity is one component of the ModSecurity v3 project.
The library codebase serves as an interface to ModSecurity Connectors
taking in web traffic and applying traditional ModSecurity processing.
In general, it provides the capability to load/interpret rules written
in the ModSecurity SecRules format and apply them to HTTP content provided
by your application via Connectors.


%package devel
Summary: Development files for %{name}
Group: System/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package static
Summary: Development files for %{name}
Group: System/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains static libraries for developing
applications that use %{name}.



%prep
%autosetup -n modsecurity-v%{version}


%build
%configure --libdir=%{_libdir} --with-lmdb
%make_build


%install
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README.md AUTHORS
%{_libdir}/*.so.*
%{_bindir}/*
%license LICENSE

%files devel
%doc README.md AUTHORS
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig
%license LICENSE

%files static
%{_libdir}/*.a
%{_libdir}/*.la


%changelog
* Wed Jan 31 2024 Karl Johnson <karljohnson.it@gmail.com> 3.0.12-1
- Bump to 3.0.12

* Mon Aug 14 2023 Karl Johnson <karljohnson.it@gmail.com> 3.0.10-1
- Bump to 3.0.10

* Mon May 8 2023 Karl Johnson <karljohnson.it@gmail.com> 3.0.9-1
- Bump to 3.0.9

* Fri Jul 15 2022 Karl Johnson <karljohnson.it@gmail.com> 3.0.7-2
- Add EL9 support
- GeoIP support removed starting with el9, moving on to GeoIP2

* Wed Jun 15 2022 Karl Johnson <karljohnson.it@gmail.com> 3.0.7-1
- Bump to 3.0.7

* Thu May 19 2022 Karl Johnson <karljohnson.it@gmail.com> 3.0.6-1
- Bump to 3.0.6

* Mon Nov 15 2021 Karl Johnson <karljohnson.it@gmail.com> 3.0.5-1
- Bump to 3.0.5

* Fri Jan 10 2020 Karl Johnson <karljohnson.it@gmail.com> 3.0.3-3
- Add CentOS 8 support

* Thu Jan 2 2020 Karl Johnson <karljohnson.it@gmail.com> - 3.0.3-2
- Remove pkg-config bits since it's included in this release

* Tue Mar 26 2019 Karl Johnson <karljohnson.it@gmail.com> - 3.0.3-1
- Bump to 3.0.3
- Add MaxMind and Lua dependencies

* Fri Oct 19 2018 Dridi Boukelmoune <dridi@fedoraproject.org> - 3.0.2-3
- Back-port of modsecurity.pc

* Sun Apr 29 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.2-2
- Rebuild after PR#1

* Sat Apr 14 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2 (rhbz #1563219)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0 final release
- Drop upstreamed patch
- Add some new BRs

* Sun Oct 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-0.2.rc1
- Add a patch to fix the build on non-x86 arch

* Fri Sep 01 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-0.1.rc1
- Fix release tag

* Wed Aug 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-0.rc1
- Update to RC1
- Fix some spec issues

* Mon Feb 22 2016 Athmane Madjoudj <athmane@fedoraproject.org> 3.0-0.git
- Initial release
