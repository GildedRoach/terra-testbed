%global commit 8b9a9924cf2f7268337a9bad5e84b0083268f40d
%global commit_date 20250727
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           spotx-bash
Version:        %commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Adblock for the Spotify desktop client on Linux.
License:        MIT
URL:            https://github.com/SpotX-Official/SpotX-Bash
Source0:        %url/archive/%commit.tar.gz
Requires:       bash
BuildArch:      noarch
Provides:       spotx spotx-linux spot-x spotx.sh

%description
%summary

%prep
%autosetup -n SpotX-Bash-%commit

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm 755 spotx.sh %buildroot%{_bindir}/spotx

%post
%{__ln_s} -f %{_bindir}/spotx %{_bindir}/spotx.sh

%files
%doc README.md
%license LICENSE
%_bindir/spotx

%changelog
* Sat Dec 14 2024 Its-J
- Package SpotX-Bash