Summary:	ArX version control system
Summary(pl):	System kontroli wersji ArX
Name:		ArX
Version:	2.2.3
Release:	0.1
License:	GPL
Group:		Development/Version Control
Source0:	http://superbeast.ucsd.edu/~landry/ArX/%{name}-%{version}.tar.gz
# Source0-md5:	486a6f638e524854548694878b601211
URL:		http://savannah.nongnu.org/projects/arx/
Requires:	fileutils
Requires:	gawk
Requires:	sed
Requires:	sh-utils
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
%configure \
	--prefix=$RPM_BUILD_ROOT%{_prefix} \
	--bindir=$RPM_BUILD_ROOT%{_bindir} \
	--mandir=$RPM_BUILD_ROOT%{_mandir} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install
#bindir=$RPM_BUILD_ROOT%{_bindir} prefix=$RPM_BUILD_ROOT%{_prefix} mandir=$RPM_BUILD_ROOT%{_mandir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/arx
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/arx.1*
#%dir %{_prefix}/libexec/arch/
#%dir %{_prefix}/libexec/arch/*
#%attr(755,root,root) %{_prefix}/libexec/arch/*/*

%files devel
%defattr(644,root,root,755)
#%{_includedir}/*
#%{_libdir}/*.a
