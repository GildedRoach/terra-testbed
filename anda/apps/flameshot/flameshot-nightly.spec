#? https://github.com/flameshot-org/flameshot/blob/master/packaging/rpm/fedora/flameshot.spec

%global ver v12.1.0
%global commit 4574ddd9590f0c485d9fd445498363896735212e
%global shortcommit %{sub %{commit} 1 7}
%global commit_date 20250602
%global devel_name QtColorWidgets

Name:			flameshot.nightly
Version:		%ver^%{commit_date}git.%shortcommit
Release:		1%?dist
License:		GPL-3.0-or-later AND ASL-2.0 AND GPL-2.0-only AND LGPL-3.0-only AND FAL-1.3
Summary:		Powerful yet simple to use screenshot software
URL:			https://flameshot.org
Source0:		https://github.com/flameshot-org/flameshot/archive/%commit/flameshot-%commit.tar.gz
Packager:  madonuko <mado@fyralabs.com>

BuildRequires:	cmake >= 3.13.0
BuildRequires:	gcc-c++ >= 7
BuildRequires:	fdupes
BuildRequires:	libappstream-glib
BuildRequires:	ninja-build
BuildRequires:	desktop-file-utils

BuildRequires:	cmake(Qt5Core) >= 5.9.0
BuildRequires:	cmake(KF5GuiAddons) >= 5.89.0
BuildRequires:	cmake(Qt5DBus) >= 5.9.0
BuildRequires:	cmake(Qt5Gui) >= 5.9.0
BuildRequires:	cmake(Qt5LinguistTools) >= 5.9.0
BuildRequires:	cmake(Qt5Network) >= 5.9.0
BuildRequires:	cmake(Qt5Svg) >= 5.9.0
BuildRequires:	cmake(Qt5Widgets) >= 5.9.0

Requires:		hicolor-icon-theme
Requires:		qt5-qtbase >= 5.9.0
Requires:		qt5-qttools >= 5.9.0
Requires:		qt5-qtsvg%{?_isa} >= 5.9.0

%dnl Provides:		flameshot = %version-%release
Conflicts:		flameshot

Recommends:		xdg-desktop-portal%{?_isa}
Recommends:		(xdg-desktop-portal-gnome%{?_isa} if gnome-shell%{?_isa})
Recommends:		(xdg-desktop-portal-kde%{?_isa} if plasma-workspace-wayland%{?_isa})
Recommends:		(xdg-desktop-portal-wlr%{?_isa} if wlroots%{?_isa})

%description
Powerful and simple to use screenshot software with built-in
editor with advanced features.

Features:

 * Customizable appearance.
 * Easy to use.
 * In-app screenshot edition.
 * DBus interface.
 * Upload to Imgur


%package bash-completion
Summary:		Bash completion for %{name}
Requires:		%{name} = %{version}-%{release}
Requires: 		bash-completion
Supplements:	(%{name} and bash-completion)

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:		Fish completion for %{name}
Requires:		%{name} = %{version}-%{release}
Requires:		fish
Supplements:	(%{name} and fish)

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:		Zsh completion for %{name}
Requires:		%{name} = %{version}-%{release}
Requires:		zsh
Supplements:	(%{name} and zsh)

%description zsh-completion
Zsh command line completion support for %{name}.

%package devel
Summary:      Flameshot development files
Requires:     %{name} = %{version}

%description devel
Development files for Flameshot.

%prep
%autosetup -p1 -n flameshot-%commit

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_WAYLAND_CLIPBOARD:BOOL=ON \
%cmake_build

%install
%cmake_install
# https://fedoraproject.org/wiki/PackagingDrafts/find_lang
%find_lang Internationalization --with-qt
%fdupes %{buildroot}%{_datadir}/icons

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f Internationalization.lang
%{_datadir}/flameshot/translations/Internationalization_grc.qm
%doc README.md
%license LICENSE
%dir %{_datadir}/flameshot
%dir %{_datadir}/flameshot/translations
%{_bindir}/flameshot
%{_libdir}/lib%{devel_name}.so.*
%{_datadir}/applications/org.flameshot.Flameshot.desktop
%{_metainfodir}/org.flameshot.Flameshot.metainfo.xml
%{_datadir}/dbus-1/interfaces/org.flameshot.Flameshot.xml
%{_datadir}/dbus-1/services/org.flameshot.Flameshot.service
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_mandir}/man1/flameshot.1*

%files bash-completion
%{bash_completions_dir}/flameshot

%files fish-completion
%{fish_completions_dir}/flameshot.fish

%files zsh-completion
%{zsh_completions_dir}/_flameshot

%files devel
%{_libdir}/lib%{devel_name}.so
%{_libdir}/cmake/%{devel_name}/
%{_libdir}/pkgconfig/%{devel_name}.pc
%{_includedir}/%{devel_name}/
