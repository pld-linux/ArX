Summary:	ArX version control system
Name:		ArX
Version:	1.0pre8
Release:	1
URL:		http://arx.fifthvision.net/
Source0:	http://superbeast.ucsd.edu/~landry/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e807b140d00882c57de8cfa322300e8c
License:	GPL
Group:		Development/Tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		fileutils gawk sed sh-utils

%description
ArX is a source control management system with distributed
repositories, easy branching, and rich merge tools.

%package devel
Summary: ArX headers and static libs
Group: Development/Libraries

%description devel
ArX headers and static libs

%prep
%setup -q

%build
mkdir =build
cd =build
../src/configure --prefix=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd =build
install -d $RPM_BUILD_ROOT%{_prefix}
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} real-prefix=%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir /usr/libexec/arch/
%dir /usr/libexec/arch/*
%attr(755,root,root) /usr/libexec/arch/*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.a
