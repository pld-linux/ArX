Summary:	ArX version control system
Summary(pl):	System kontroli wersji ArX
Name:		ArX
Version:	1.0pre8
Release:	1
License:	GPL
Group:		Development/Version Control
Source0:	http://superbeast.ucsd.edu/~landry/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e807b140d00882c57de8cfa322300e8c
URL:		http://savannah.nongnu.org/projects/arx/
PreReq:		fileutils gawk sed sh-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ArX is a source control management system with distributed
repositories, easy branching, and rich merge tools.

%description -l pl
ArX jest systemem zarz±dzania ¼ród³ami w rozproszonych repozytoriach.
Umo¿liwia ³atwe tworzenie rozga³êzieñ i zawiera narzêdzia uzgadniaj±ce
o bogatych mo¿liwo¶ciach.

%package devel
Summary:	ArX headers and static libs
Summary(pl):	Pliki nag³ówkowe i biblioteki statyczne ArX
Group:		Development/Libraries

%description devel
This package contains ArX headers and static libs.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i biblioteki statyczne ArX.

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
