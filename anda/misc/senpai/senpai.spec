Name:			senpai
Version:		0.4.1
Release:		1%?dist
Summary:		Your everyday IRC student
License:		ISC
URL:			https://github.com/delthas/senpai
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildRequires:	golang scdoc gcc

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
senpai is an IRC client that works best with bouncers:

    - no logs are kept,
    - history is fetched from the server via CHATHISTORY,
    - networks are fetched from the server via bouncer-networks,
    - messages can be searched in logs via SEARCH,
    - files can be uploaded via FILEHOST (with drag & drop!)

%prep
%autosetup -n %{name}-%{version}

%build
%make_build

%install
install -Dm755 senpai                   %{buildroot}%{_bindir}/senpai
install -Dm644 doc/senpai.1             %{buildroot}%{_mandir}/man1/senpai.1
install -Dm644 doc/senpai.5             %{buildroot}%{_mandir}/man5/senpai.5
install -Dm644 contrib/senpai.desktop   %{buildroot}%{_datadir}/applications/senpai.desktop
install -Dm644 res/icon.48.png          %{buildroot}%{_iconsdir}/hicolor/48x48/apps/senpai.png
install -Dm644 res/icon.svg             %{buildroot}%{_iconsdir}/hicolor/scalable/apps/senpai.svg

%files
%doc README.md
%license LICENSE
%_bindir/senpai
%{_mandir}/man1/senpai.1.gz
%{_mandir}/man5/senpai.5.gz
%{_datadir}/applications/senpai.desktop
%{_iconsdir}/hicolor/48x48/apps/senpai.png
%{_iconsdir}/hicolor/scalable/apps/senpai.svg

%changelog
* Fri Oct 31 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
