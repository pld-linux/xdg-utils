%define		subver	rc1
%define		rel		3
Summary:	Set of tools that assist applications with desktop integration
Summary(pl.UTF-8):	Zestaw narzędzi ułatwiających integrację aplikacji ze środowiskami graficznymi
Name:		xdg-utils
Version:	1.1.0
Release:	%{rel}.%{subver}
License:	MIT
Group:		X11/Applications
#Source0:	http://portland.freedesktop.org/download/%{name}-%{version}.tgz
Source0:	%{name}-v%{version}-%{subver}-71-g050333e.tar.gz
# Source0-md5:	7a83a4867afc6f5df896f0be0bace74a
Source1:	get-source.sh
Patch0:		0001-xdg-settings-add-MATE-support.patch
URL:		http://portland.freedesktop.org/wiki/XdgUtils
BuildRequires:	xmlto
Requires:	coreutils
Requires:	desktop-file-utils
Requires:	which
Requires:	xorg-app-xprop
Requires:	xorg-app-xset
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xdg-utils is a set of command line tools that assist applications with
a variety of desktop integration tasks. About half of the tools focus
on tasks commonly required during the installation of a desktop
application and the other half focuses on integration with the desktop
environment while the application is running.

%description -l pl.UTF-8
Xdg-utils to zestaw obsługiwanych z linii poleceń narzędzi
ułatwiających integrację aplikacji z różnymi środowiskami graficznymi.
Mniej więcej połowa z tych narzędzi przydatna jest w czasie instalacji
danej aplikacji, a druga połowa przydaje się już w czasie działania
aplikacji w danym środowisku graficznym.

%prep
%setup -qc
mv xdg-utils-v%{version}-*/* .
%patch0 -p1

%build
%configure

# for snapshot. need to regenerate scripts
%if 0%{?subver:1}
%{__make} scripts-clean -C scripts
%{__make} man scripts -C scripts
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/xdg-*
%{_mandir}/man1/xdg-*.1*
