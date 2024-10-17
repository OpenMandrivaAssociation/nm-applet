%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Gnome GUI for NetworkManager
Name:		nm-applet
Version:	0.9.8.2
Release:	1
Source0:	http://ftp.gnome.org/pub/GNOME/sources/network-manager-applet/%{url_ver}/network-manager-applet-%{version}.tar.xz
License:	GPLv2+
Group:		System/Configuration/Networking
Url:		https://www.gnome.org/projects/NetworkManager/
BuildRequires:	gettext
BuildRequires:	libtool
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	ppp-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-glib-vpn)
BuildRequires:	pkgconfig(libpng15)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libnotify)
Requires:	dbus
Requires:	gnome-keyring
Requires:	gtk+3
Requires:	NetworkManager
Requires:	pptp-linux
Requires:	shared-mime-info

%description
This package contains GNOME utilities and applications for use with
NetworkManager, including a panel applet for wireless networks.

%prep
%setup -q -n network-manager-applet-%{version}

%build
autoreconf -i --force
intltoolize --force
%configure2_5x	--localstatedir=%{_var} \
		--disable-static \
		--with-gcrypt=yes \
		--with-notify \
		--with-nss=yes \
		--with-gnutls=no
%make

%install
%makeinstall_std

%find_lang %{name}

find %{buildroot} -name \*.la|xargs rm -f

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%files -f nm-applet.lang
%doc ChangeLog NEWS AUTHORS README CONTRIBUTING
%{_bindir}/nm-applet
%{_bindir}/nm-connection-editor
%{_bindir}/nm-vpn-properties
%{_datadir}/nm-applet
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/gnome-vpn-properties
%{_sysconfdir}/dbus-1/system.d/nm-applet.conf
%{_sysconfdir}/xdg/autostart/nm-applet.desktop
# This should be in -devel package, but a new package for just this one file? bah
%{_includedir}/NetworkManager/nm-vpn-ui-interface.h
