#? https://src.fedoraproject.org/rpms/hyprlang/blob/rawhide/f/hyprlang.spec

%global realname hyprlang
%global ver 0.6.3
%global commit 23f0debd2003f17bd65f851cd3f930cff8a8c809
%global commit_date 20250728
%global shortcommit %{sub %commit 1 7}

Name:           %realname.nightly
Version:        %ver^%{commit_date}git.%shortcommit
Release:        1%?dist
Summary:        The official implementation library for the hypr config language

License:        LGPL-3.0-only
URL:            https://github.com/hyprwm/hyprlang
Source0:        %url/archive/%commit.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  (pkgconfig(hyprutils) with hyprutils.nightly-devel)

Provides:		%realname = %evr
Conflicts:		%realname

%description
%{summary}.

%package        devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:		%realname-devel = %evr
Conflicts:		%realname-devel
%pkg_devel_files

%prep
%autosetup -p1 -n %realname-%commit

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libhyprlang.so.2
%{_libdir}/libhyprlang.so.%{ver}

%changelog
%autochangelog
