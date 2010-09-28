Summary:	Set of tools that assist applications with desktop integration
Summary(pl.UTF-8):	Zestaw barzędzi ułatwiających integrację aplikacji ze środowiskami graficznymi
Name:		xdg-utils
Version:	1.0.2
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://portland.freedesktop.org/download/%{name}-%{version}.tgz
# Source0-md5:	348a5b91dc66426505022c74a64b2940
URL:		http://portland.freedesktop.org/wiki/XdgUtils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xmlto
Requires:	coreutils
Requires:	which
Requires:	xorg-app-xprop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xdg-utils is a set of command line tools that assist applications with
a variety of desktop integration tasks. About half of the tools focus
on tasks commonly required during the installation of a desktop
application and the other half focuses on integration with the desktop
environment while the application is running.

%description -l pl.UTF-8
Xdg-utils to zastaw konsolowych narzędzi ułatwiających integrację
aplikacji z różnymi środowiskami graficznymi. Mniej więcej połowa
z tych narzędzi przydatna jest w czasie instalacji danej
aplikacji, a druga polowa przydaje się już w czasie działania
aplikacji w danym środowisku graficznym.

%prep
%setup -q

%build
%configure

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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
