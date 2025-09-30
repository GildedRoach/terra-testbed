%define debug_package %nil

%global commit e33764c69179e35b60ad03931544a87357e1e81f
%global commit_date 20250413
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           stardust-xr-telescope
Version:        %commit_date.git~%shortcommit
Release:        2%?dist
Summary:        See the stars! Easy stardust setups to run on your computer
License:        MIT
URL:            https://github.com/StardustXR/telescope
Source0:        %url/archive/%commit.tar.gz

Requires:       bash
Requires:       xwayland-satellite
Requires:       stardust-xr-armillary
Requires:       stardust-xr-atmosphere
Requires:       stardust-xr-black-hole
Requires:       stardust-xr-comet
Requires:       stardust-xr-flatland
Requires:       stardust-xr-gravity
Requires:       stardust-xr-magnetar
Requires:       stardust-xr-non-spatial-input
Requires:       stardust-xr-protostar
Requires:       stardust-xr-server

BuildArch:      noarch
Provides:       telescope stardust-telescope

%description
See the stars! Easy stardust setups to run on your computer.

%prep
%autosetup -n telescope-%commit

%build

%install
install -Dm755 scripts/telescope          %buildroot%_bindir/telescope
install -Dm755 scripts/_telescope_startup %buildroot%_bindir/_telescope_startup

%files
%doc README.md
%license LICENSE
%_bindir/telescope
%_bindir/_telescope_startup
