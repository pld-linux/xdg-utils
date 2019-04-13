Summary:	Set of tools that assist applications with desktop integration
Summary(pl.UTF-8):	Zestaw narzędzi ułatwiających integrację aplikacji ze środowiskami graficznymi
Name:		xdg-utils
Version:	1.1.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://portland.freedesktop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	902042508b626027a3709d105f0b63ff
Source1:	get-source.sh
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
%doc ChangeLog LICENSE README RELEASE_NOTES TODO
%attr(755,root,root) %{_bindir}/xdg-desktop-icon
%attr(755,root,root) %{_bindir}/xdg-desktop-menu
%attr(755,root,root) %{_bindir}/xdg-email
%attr(755,root,root) %{_bindir}/xdg-icon-resource
%attr(755,root,root) %{_bindir}/xdg-mime
%attr(755,root,root) %{_bindir}/xdg-open
%attr(755,root,root) %{_bindir}/xdg-screensaver
%attr(755,root,root) %{_bindir}/xdg-settings
%{_mandir}/man1/xdg-desktop-icon.1*
%{_mandir}/man1/xdg-desktop-menu.1*
%{_mandir}/man1/xdg-email.1*
%{_mandir}/man1/xdg-icon-resource.1*
%{_mandir}/man1/xdg-mime.1*
%{_mandir}/man1/xdg-open.1*
%{_mandir}/man1/xdg-screensaver.1*
%{_mandir}/man1/xdg-settings.1*
