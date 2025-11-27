%global org_name Heroic-Games-Launcher
%global git_name %(echo %{org_name} | sed 's/-//g')
%global appid com.heroicgameslauncher.hgl
%global shortname heroic
%global legendary_version 0.20.37
%global gogdl_version 1.1.2
%global nile_version 1.1.2
%global comet_version 0.2.0

%electronmeta

Name:          %{shortname}-games-launcher
Version:       2.18.1
Release:       1%?dist
Summary:       A games launcher for GOG, Amazon, and Epic Games
License:       GPL-3.0-only AND MIT AND BSD-3-Clause
URL:           https://heroicgameslauncher.com
BuildRequires: anda-srpm-macros
BuildRequires: pnpm
BuildRequires: python3
Requires:      alsa-lib
Requires:      hicolor-icon-theme
Requires:      python3
Requires:      which
Recommends:    (falcond or gamemode)
Recommends:    mangohud
Recommends:    umu-launcher
Provides:      bundled(comet) = %{comet_version}
Provides:      bundled(gogdl) = %{gogdl_version}
Provides:      bundled(legendary) = %{legendary_version}
Provides:      bundled(nile) = %{nile_version}
Packager:      Gilver E. <rockgrub@disroot.org>

%description
Heroic is a Free and Open Source Epic, GOG, and Amazon Prime Games launcher for Linux, Windows, and macOS.

%prep
%git_clone https://github.com/%{org_name}/%{git_name} v%{version}

%build
%{__pnpm} install
%{__pnpm} run download-helper-binaries
%{__pnpm} electron-vite build
%{__pnpm} electron-builder --linux --%{_electron_cpu} --publish=never

%install
desktop-file-install --set-key=Exec --set-value="%{_libdir}/%{shortname}/%{shortname} %u" flatpak/%{appid}.desktop
%electron_install -b %{shortname} -S %{shortname} -d %{shortname} -i %{appid} -l

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop

%files
%doc     README.md
%doc     CODE_OF_CONDUCT.md
%license COPYING
%license bundled_licenses/*
%dir %{_libdir}/%{shortname}
%{_libdir}/%{shortname}/*
%{_bindir}/%{shortname}
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_iconsdir}/hicolor/16x16/apps/%{appid}.png
%{_iconsdir}/hicolor/32x32/apps/%{appid}.png
%{_iconsdir}/hicolor/48x48/apps/%{appid}.png
%{_iconsdir}/hicolor/64x64/apps/%{appid}.png
%{_iconsdir}/hicolor/128x128/apps/%{appid}.png
%{_iconsdir}/hicolor/256x256/apps/%{appid}.png
%{_iconsdir}/hicolor/512x512/apps/%{appid}.png
%{_iconsdir}/hicolor/1024x1024/apps/%{appid}.png

%changelog
* Sun Mar 02 2025 Gilver E. <rockgrub@disroot.org>
- Update to 2.16.0
- Fix incorrect RPM dependencies
* Thu Jan 30 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
