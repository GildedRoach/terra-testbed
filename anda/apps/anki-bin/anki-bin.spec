%global xurl https://files.pythonhosted.org/packages/a3/86/c1c459a06466ffc3a205de9852875a922c378a7bfb9fb1310bea019dacd1/anki-25.7.5-cp39-abi3-manylinux_2_36_x86_64.whl
%global aurl https://files.pythonhosted.org/packages/29/75/81eb12d43381f5150a2fb1acc2757d25741af5bf0635f40faab61eefcb44/anki-25.7.5-cp39-abi3-manylinux_2_36_aarch64.whl
%global qurl https://files.pythonhosted.org/packages/5e/e6/4c36d3c1ed0e2a6e4bf95eb919d603078d935b5c75950c7627e79340f25a/aqt-25.7.5-py3-none-any.whl

Name:			anki-bin
Version:		25.7.5
Release:		1%?dist
Summary:		Flashcard program for using space repetition learning (Installed with wheel)
License:		AGPL-3.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-3.0 AND Apache-2.0 AND CC-BY-2.5
URL:			https://apps.ankiweb.net/
BuildRequires:          python3-pip rpm_macro(fdupes) cargo
Requires:               python3-sqlalchemy python3-simplejson python3-matplotlib python3-decorator python3-markdown python3-orjson
Requires:               python3-requests python3-pygame python3-beautifulsoup4 python3-httplib2 python3-pyaudio python3-jsonschema
Requires:               python3-flask-cors python3-protobuf python3-requests python3-waitress python3-pyqt6-webengine python3-send2trash
Requires:               python3-protobuf >= 4.21
Requires:               libxcrypt-compat hicolor-icon-theme sox
Requires:               (mpv or mpv-nightly)

ExclusiveArch:	        x86_64
Conflicts:		anki
%ifarch x86_64
Source0:		%xurl
%elifarch aarch64
Source0:                %aurl
%endif
Source1:		%qurl
Source2:		https://raw.githubusercontent.com/ankitects/anki/%{version}/qt/runanki.py
Source3:		https://raw.githubusercontent.com/ankitects/anki/%{version}/qt/bundle/lin/anki.desktop
Source4:                https://raw.githubusercontent.com/ankitects/anki/%{version}/qt/bundle/lin/anki.png
Source5:		https://raw.githubusercontent.com/ankitects/anki/%{version}/LICENSE
Source6:		https://raw.githubusercontent.com/ankitects/anki/%{version}/README.md

%description
Anki is a program designed to help you remember facts (such as words and
phrases in a foreign language) as easily, quickly and efficiently as possible.
Anki is based on a theory called spaced repetition.

%prep

%build

%install
pip3 install --root=%{buildroot} %SOURCE0 %SOURCE1
install -Dm755 %{SOURCE2} "%{buildroot}/usr/bin/anki"
install -Dm644 %{SOURCE3} "%{buildroot}/usr/share/applications/anki.desktop"
install -Dm644 %{SOURCE4} "%{buildroot}/usr/share/pixmaps/anki.png"
install -Dm644 %{SOURCE5} "%{buildroot}/%{_datadir}/licenses/%{name}/LICENSE"
install -Dm644 %{SOURCE6} "%{buildroot}/%{_datadir}/doc/%{name}/README.md"

cp -r %buildroot%_libdir/python3*/site-packages/{_aqt,anki*,aqt*} .
rm -rf %buildroot{%_libdir,/usr/lib}/python3*/site-packages/*
cp -r ./{_aqt,anki*,aqt*} %buildroot/usr/lib/python3*/site-packages/

rm -rf %buildroot%_bindir/{distro,flask,jsonschema,markdown_py,normalizer,send2trash,waitress-serve}

%fdupes %buildroot%_libdir/python*/site-packages/_aqt/data/


%files
%license LICENSE
%doc README.md
%_bindir/anki
%_bindir/pyuic6
%_bindir/pylupdate6
/usr/lib/python*/site-packages/_aqt/
/usr/lib/python*/site-packages/anki-%{version}.dist-info/
/usr/lib/python*/site-packages/anki/
/usr/lib/python*/site-packages/aqt-%{version}.dist-info/
/usr/lib/python*/site-packages/aqt/
%_datadir/applications/anki.desktop
%_datadir/pixmaps/anki.png

%changelog
* Fri Nov 10 2023 hazel-bunny <dabiswas112@gmail.com> - 23.10-2
- Add python3-orjson and mpv as dependencies

* Wed Jan 11 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.1.60
- Initial package
