#? https://src.fedoraproject.org/rpms/hyprgraphics/blob/rawhide/f/hyprgraphics.spec

%global realname hyprgraphics
%global ver 0.1.5
%global commit b86c4d9ed353073e764fef286423c5cc6fb9318b
%global commit_date 20250918
%global shortcommit %{sub %commit 1 7}

%bcond libjxl 1
Name:           %realname.nightly
Version:        %ver^%{commit_date}git.%shortcommit
Release:        1%?dist
Summary:        Graphics library for Hyprland

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprgraphics
Source0:		%url/archive/%commit.tar.gz
Packager:		madonuko <mado@fyralabs.com>

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  (pkgconfig(hyprlang) with hyprlang.nightly-devel)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  (pkgconfig(hyprutils) with hyprutils.nightly-devel)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(spng)

%if %{with libjxl}
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libjxl_cms)
BuildRequires:  pkgconfig(libjxl_threads)
%endif

%description
%{summary}.

%package        devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%pkg_devel_files


%prep
%autosetup -p1 -n %realname-%commit

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ifarch s390x
rm tests/resource/images/hyprland.jpg
%endif
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libhyprgraphics.so.0
%{_libdir}/libhyprgraphics.so.%{ver}
