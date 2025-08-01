%global commit 469001b7f623f780cfdcb50cc4842f7a4e6386ab
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global fulldate 2025-08-01
%global commit_date %(echo %{fulldate} | sed 's/-//g')
%global public_key RWQlAjJC23149WL2sEpT/l0QKy7hMIFhYdQOFy0Z7z7PbneUgvlsnYcV
%global ver 1.1.4
%global base_name ghostty
%global appid com.mitchellh.%{base_name}

Name:           %{base_name}-nightly
Version:        %{ver}~tip^%{commit_date}git%{shortcommit}
Release:        1%?dist
%if 0%{?fedora} <= 41
Epoch:          1
%endif
Summary:        A fast, native terminal emulator written in Zig; this is the Tip (nightly) build.
License:        MIT AND MPL-2.0 AND OFL-1.1 AND (WTFPL OR CC0-1.0) AND Apache-2.0
URL:            https://%{base_name}.org
Source0:        https://github.com/%{base_name}-org/%{base_name}/releases/download/tip/%{base_name}-source.tar.gz
Source1:        https://github.com/%{base_name}-org/%{base_name}/releases/download/tip/%{base_name}-source.tar.gz.minisig
BuildRequires:  anda-srpm-macros >= 0.2.15
BuildRequires:  gettext
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libX11-devel
BuildRequires:  minisign
BuildRequires:  ncurses
BuildRequires:  ncurses-devel
BuildRequires:  pandoc-cli
BuildRequires:  systemd-rpm-macros
BuildRequires:  zig >= 0.14.0
BuildRequires:  zig-rpm-macros
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(oniguruma)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-terminfo = %{evr}
Requires:       %{name}-shell-integration = %{evr}
Requires:       (%{name}-kio = %{evr} if kf6-kio)
Requires:       gtk4
Requires:       gtk4-layer-shell
Requires:       libadwaita
Conflicts:      %{base_name}
Provides:       %{base_name}-tip = %{ver}^%{commit_date}git%{shortcommit}
%if 0%{?fedora} <= 41
Provides:       %{name} = %{commit_date}.%{shortcommit}
%endif
Obsoletes:      %{name} = 20250130.04d3636
Packager:       Gilver E. <rockgrub@disroot.org>

%description
👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.

%package        bash-completion
Summary:        Ghostty Bash completion
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
%if 0%{?fedora} <= 41
Provides:       %{name}-bash-completion = %{commit_date}.%{shortcommit}
%endif
BuildArch:      noarch

%description    bash-completion
Bash shell completion for Ghostty.

%package        fish-completion
Summary:        Ghostty Fish completion
Requires:       %{name}
Requires:       fish
Supplements:    (%{name} and fish)
%if 0%{?fedora} <= 41
Provides:       %{name}-fish-completion = %{commit_date}.%{shortcommit}
%endif
BuildArch:      noarch

%description    fish-completion
Fish shell completion for Ghostty.

%package        zsh-completion
Summary:        Ghostty Zsh completion
Requires:       %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
%if 0%{?fedora} <= 41
Provides:       %{name}-zsh-completion = %{commit_date}.%{shortcommit}
%endif
BuildArch:      noarch

%description    zsh-completion
Zsh shell completion for Ghostty.

%package        kio
Summary:        KIO support for Ghostty
Requires:       %{name} = %{evr}
BuildArch:      noarch

%description    kio
This package allows Ghostty to interact with KIO.

%package        nautilus
Summary:        Nautilus menu support for Ghostty
Supplements:    (%{name} and nautilus)
Requires:       %{name} = %{evr}
BuildArch:      noarch

%description    nautilus
This package enables Nautilus integration for Ghostty.

%package        vim
Summary:        Vim plugins for Ghostty
Supplements:    (%{name} and vim-filesystem)
Requires:       %{name} = %{evr}
Requires:       vim-enhanced
Requires:       vim-filesystem
BuildArch:      noarch

%description    vim
This package provides the Ghostty Vim plugins.

%package        neovim
Summary:        Neovim plugins for Ghostty
Supplements:    (%{name} and neovim)
Requires:       %{name} = %{evr}
Requires:       neovim
BuildArch:      noarch

%description    neovim
This package provides the Neovim plugins for Ghostty.

%package        bat-syntax
Summary:        Bat syntax for Ghostty
Supplements:    (%{name} and bat)
Requires:       %{name} = %{evr}
Requires:       bat
BuildArch:      noarch

%description    bat-syntax
This package provides the Bat syntax files for Ghostty.

%package        shell-integration
Summary:        Ghostty shell integration
Supplements:    %{name}
%if 0%{?fedora} <= 41
Provides:       %{name}-shell-integration = %{commit_date}.%{shortcommit}
%endif
BuildArch:      noarch

%description    shell-integration
This package contains files allowing Ghostty to integrate with various shells.

%package        terminfo
Summary:        Ghostty terminfo
%if 0%{?fedora} >= 42
Requires:       ncurses-term >= 6.5-5.20250125
%endif
Supplements:    %{name}
%if 0%{?fedora} <= 41
Provides:       %{name}-terminfo = %{commit_date}.%{shortcommit}
%endif
Obsoletes:      %{name}-terminfo-source < %{evr}
BuildArch:      noarch

%description    terminfo
Ghostty's terminfo. Needed for basic terminal function.

%prep
/usr/bin/minisign -V -m %{SOURCE0} -x %{SOURCE1} -P %{public_key}
%autosetup -n %{base_name}-%{ver}-main+%{shortcommit}

ZIG_GLOBAL_CACHE_DIR="%{_zig_cache_dir}" ./nix/build-support/fetch-zig-cache.sh

%build

%install
DESTDIR="%{buildroot}" \
%{zig_build_target -r fast} \
    --prefix "%{_prefix}" --prefix-lib-dir "%{_libdir}" \
    --prefix-exe-dir "%{_bindir}" --prefix-include-dir "%{_includedir}" \
    -Dversion-string="%{ver}-dev+%{shortcommit}" \
    -Dstrip=false \
    -Dpie=true \
    -Demit-docs 

# Don't conflict with ncurses-term on F42 and up
%if 0%{?fedora} >= 42
rm -rf %{buildroot}%{_datadir}/terminfo/g/%{base_name}
%endif

%find_lang %{appid}

%files -f %{appid}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{base_name}
%{_datadir}/applications/%{appid}.desktop
%dir %{_datadir}/%{base_name}
%{_datadir}/%{base_name}/doc
%{_datadir}/%{base_name}/themes
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/dbus-1/services/%{appid}.service
%{_iconsdir}/hicolor/16x16/apps/%{appid}.png
%{_iconsdir}/hicolor/16x16@2/apps/%{appid}.png
%{_iconsdir}/hicolor/32x32/apps/%{appid}.png
%{_iconsdir}/hicolor/32x32@2/apps/%{appid}.png
%{_iconsdir}/hicolor/128x128/apps/%{appid}.png
%{_iconsdir}/hicolor/128x128@2/apps/%{appid}.png
%{_iconsdir}/hicolor/256x256/apps/%{appid}.png
%{_iconsdir}/hicolor/256x256@2/apps/%{appid}.png
%{_iconsdir}/hicolor/512x512/apps/%{appid}.png
%{_iconsdir}/hicolor/1024x1024/apps/%{appid}.png
%{_mandir}/man1/%{base_name}.1.gz
%{_mandir}/man5/%{base_name}.5.gz
%{_userunitdir}/app-%{appid}.service

%files bash-completion
%{bash_completions_dir}/%{base_name}.bash

%files fish-completion
%{fish_completions_dir}/%{base_name}.fish

%files zsh-completion
%{zsh_completions_dir}/_%{base_name}

%files kio
%{_datadir}/kio/servicemenus/%{appid}.desktop

%files nautilus
%{_datadir}/nautilus-python/extensions/%{base_name}.py

%files vim
%{_datadir}/vim/vimfiles/compiler/%{base_name}.vim
%{_datadir}/vim/vimfiles/ftdetect/%{base_name}.vim
%{_datadir}/vim/vimfiles/ftplugin/%{base_name}.vim
%{_datadir}/vim/vimfiles/syntax/%{base_name}.vim

%files neovim
%{_datadir}/nvim/site/compiler/%{base_name}.vim
%{_datadir}/nvim/site/ftdetect/%{base_name}.vim
%{_datadir}/nvim/site/ftplugin/%{base_name}.vim
%{_datadir}/nvim/site/syntax/%{base_name}.vim

%files bat-syntax
%{_datadir}/bat/syntaxes/%{base_name}.sublime-syntax

%files shell-integration
%dir %{_datadir}/%{base_name}/shell-integration
%{_datadir}/%{base_name}/shell-integration/bash/bash-preexec.sh
%{_datadir}/%{base_name}/shell-integration/bash/%{base_name}.bash
%{_datadir}/%{base_name}/shell-integration/elvish/lib/%{base_name}-integration.elv
%{_datadir}/%{base_name}/shell-integration/fish/vendor_conf.d/%{base_name}-shell-integration.fish
%{_datadir}/%{base_name}/shell-integration/zsh/.zshenv
%{_datadir}/%{base_name}/shell-integration/zsh/%{base_name}-integration

%files terminfo
%if 0%{?fedora} < 42
%{_datadir}/terminfo/g/%{base_name}
%endif
%{_datadir}/terminfo/x/xterm-%{base_name}

%post
%systemd_user_post app-%{appid}.service

%preun
%systemd_user_preun app-%{appid}.service

%postun
%systemd_user_postun app-%{appid}.service

%changelog
* Sat May 31 2025 Gilver E. <rockgrub@disroot.org> - 1.1.4~tip^20250531git1ff9162
- Updated for Zig 0.14.0
- Updated for ncurses-term compatibility in Fedora 42 and Rawhide
* Wed Mar 05 2025 Gilver E. <rockgrub@disroot.org>
- Update to 1.1.3~tip^20250305git66e8d91-2%{?dist}
 * Ghostty now has localization support via gettext as well as corresponding localization files
* Fri Jan 31 2025 Gilver E. <rockgrub@disroot.org>
- Update to 1.1.1~tip^20250131git5508e7-1%{?dist}
 * Low GHSA-98wc-794w-gjx3: Ghostty leaked file descriptors allowing the shell and any of its child processes to impact other Ghostty terminal instances
 * Better Git versioning scheme
 * Ghostty terminfo source files are now a subpackage
 * Shell integration and completion and terminfo subpackages are now properly noarch
* Tue Dec 31 2024 Gilver E. <rockgrub@disroot.org>
- Update to 20241231.3f7c3af
 * High CVE-2003-0063: Allows execution of arbitrary commands
 * Medium CVE-2003-0070: Allows execution of arbitrary commands
* Thu Dec 26 2024 Gilver E. <rockgrub@disroot.org>
- Initial package
