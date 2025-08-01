%global commit 3faca3a192a823e3f6183e4aee4ca827c6d973ba
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250725
%if 0%{?fedora} == 41
%ifarch %ix86
%global debug_package %{nil}
%endif
%endif

# While there's an upstream version at Supreeeme/extest, we're using
# the same fork as Bazzite so we can use the same patches.
# This fork has no tags so we're gonna use the commit hash as the version

# Don't mangle shebangs
%global __brp_mangle_shebangs %{nil}

# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           extest
Version:        %{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        X11 XTEST reimplementation primarily for Steam Controller on Wayland

License:        MIT
URL:            https://github.com/bazzite-org/extest

Source0:        %{url}/archive/%{commit}.tar.gz

# While the upstream project has the same script, it copies the Steam desktop shortcut to
# $HOME and modifies it there. The following inline script modifies the global Steam
# desktop shortcut to load Extest for all users.
Source1:        override_steam_desktop_file.sh

Packager:       Cappy Ishihara <cappy@fyralabs.com>

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  anda-srpm-macros
BuildRequires:  openssl-devel
BuildRequires:  gcc
BuildRequires:  perl
BuildRequires:  rust-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  clang
BuildRequires:  mold
Recommends:     %{name}-steam
%ifarch x86_64
Recommends:     %{name}(x86-32)
%endif

%description
Extest is a drop in replacement for the X11 XTEST extension. It creates a virtual device with the uinput kernel module. It's been primarily developed for allowing the desktop functionality on the Steam Controller to work while Steam is open on Wayland.


# Subpackage for dynamically patching Steam's scripts
%package steam
BuildArch:      noarch
Summary:        Extest subpackage that patches Steam's scripts to load Extest
Requires:       %{name}(x86-32)
Recommends:     %{name}

%description steam
This subpackage contains scripts that patch Steam's scripts to load Extest. This is necessary for Extest to work with Steam on Wayland.


%prep
%autosetup -n %{name}-%{commit}
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install
mkdir -p %{buildroot}%{_libdir}/extest/
install -D -p -m0755 target/rpm/libextest.so %{buildroot}%{_libdir}/extest/libextest.so

mkdir -p %{buildroot}%{_libexecdir}/extest/
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_libexecdir}/extest/override_steam_desktop_file.sh


# Trigger on Steam install for steam subpackage
%triggerin -n %{name}-steam -- steam
%{_libexecdir}/extest/override_steam_desktop_file.sh



%files
%license LICENSE
%doc README.md
%{_libdir}/extest/libextest.so

%files steam
%{_libexecdir}/extest/override_steam_desktop_file.sh


%changelog
%autochangelog
