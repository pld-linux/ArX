Summary:	ArX version control system
Summary(pl.UTF-8):	System kontroli wersji ArX
Name:		ArX
Version:	2.2.4
Release:	0.1
License:	GPL
Group:		Development/Version Control
Source0:	http://savannah.nongnu.org/download/arx/%{name}-%{version}.tar.gz
# Source0-md5:	75ef7a4b16e7cd3ebb9724298f2751f6
URL:		http://savannah.nongnu.org/projects/arx/
Requires:	fileutils
Requires:	gawk
Requires:	sed
Requires:	sh-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ArX is a source control management system with distributed
repositories, easy branching, and rich merge tools.

%description -l pl.UTF-8
ArX jest systemem zarządzania źródłami w rozproszonych repozytoriach.
Umożliwia łatwe tworzenie rozgałęzień i zawiera narzędzia uzgadniające
o bogatych możliwościach.

%package devel
Summary:	ArX headers and static libs
Summary(pl.UTF-8):	Pliki nagłówkowe i biblioteki statyczne ArX
Group:		Development/Libraries

%description devel
This package contains ArX headers and static libs.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe i biblioteki statyczne ArX.

%prep
%setup -q

%build
%configure \
	--prefix=$RPM_BUILD_ROOT%{_prefix} \
	--bindir=$RPM_BUILD_ROOT%{_bindir} \
	--mandir=$RPM_BUILD_ROOT%{_mandir}

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
