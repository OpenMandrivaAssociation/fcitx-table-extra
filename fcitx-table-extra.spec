Summary:	Extra tables for Fcitx
Name:		fcitx-table-extra
Version:	0.3.7
Release:	1
Group:		System/Internationalization
License:	GPLv2+
URL:		http://fcitx-im.org/wiki/Fcitx
Source0:	http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	pkgconfig(fcitx)
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildArch:	noarch
Requires:	fcitx

%description
Fcitx-table-extra provides extra table for Fcitx, including Boshiamy, Zhengma,
and Cangjie 3/5.

Boshiamy table and its icon are released under their own license.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING
%{_datadir}/fcitx/table/*.mb
%{_datadir}/fcitx/table/*.conf
%{_datadir}/fcitx/imicon/*.png
%{_datadir}/icons/hicolor/64x64/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
