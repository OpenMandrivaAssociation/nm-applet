%define	svnrel	svn727
Summary:	Gnome GUI for NetworkManager
Name:		nm-applet
Version:	0.7.0
Release:	%mkrel 0.3.%{svnrel}
Source0:	%{name}-%{version}.%{svnrel}.tar.gz
License:	GPLv2+
Group:		System/Configuration/Networking
Url:		http://www.gnome.org/projects/NetworkManager/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libnm_util-devel libnm_glib-devel
BuildRequires:	dbus-devel dbus-glib-devel libGConf2-devel
BuildRequires:	gnome-keyring-devel gnome-panel-devel hal-devel
BuildRequires:	libglade2-devel libnotify-devel intltool nss-devel
BuildRequires:	libpolkit-devel libpolkit-gnome-devel libiw-devel
Requires:	networkmanager %{_lib}gail-gnome
Provides:	networmanager-gnome = %{version}-%{release}

%description
This package contains GNOME utilities and applications for use with
NetworkManager, including a panel applet for wireless networks.

%prep
%setup -q

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
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

find %{buildroot} -name \*.la|xargs rm -f

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f nm-applet.lang
%defattr(-,root,root)
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
