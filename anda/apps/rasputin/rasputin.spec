%global commit a445d545c8e1a3339acd53cadf4e9c08698a786d
%global commit_date 20251028
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rasputin
Version:        0~%commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Mouse and keyboard settings for Raspberry Pi Desktop
License:        BSD-3-Clause
URL:            https://github.com/raspberrypi-ui/rasputin
Source0:        %url/archive/%commit.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gtk3-devel
BuildRequires:  libxml2-devel
BuildRequires:  intltool
BuildRequires:  gcc

Requires:       libxml2

%description
%summary.

%prep
%autosetup -n rasputin-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%find_lang rpcc_rasputin

%files -f rpcc_rasputin.lang
%license debian/copyright
%{_datadir}/rpcc/ui/rasputin.ui
%{_libdir}/rpcc/librpcc_rasputin.so

%changelog
* Sun Oct 26 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
