%define debug_package %nil
%global pypi_name qmk_cli
%global _desc The QMK CLI (command line interface) makes building and working with QMK keyboards easier. We have provided a number of commands to simplify and streamline tasks such as obtaining and compiling the QMK firmware, creating keymaps, and more.


Name:			python-%{pypi_name}
Version:		1.1.8
Release:		1%?dist
Summary:		A program to help users work with QMK
License:		MIT
URL:			https://github.com/qmk/qmk_cli
Source0:		%url/archive/refs/tags/%version.tar.gz
Patch0:         nonexistant-deps.patch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3dist(setuptools)
BuildRequires:  git
BuildRequires:  python3-devel

Requires:       python3
Requires:       python3-platformdirs
Requires:       python3-argcomplete
Requires:       python3-colorama
Requires:       python3-jsonschema
Requires:       git
Requires:       avr-gcc
Requires:       arm-none-eabi-gcc
Requires:       avr-libc
Requires:       arm-none-eabi-binutils
Requires:       arm-none-eabi-newlib
Requires:       avr-binutils
Requires:       dfu-programmer
Requires:       dfu-util
Requires:       avrdude
Requires:       python3-hjson
Requires:       python3-pygments
Requires:       python3-hid
Requires:       python3-pyusb
Requires:       python3-pyserial
Requires:       python3-pillow

Provides:       qmk
Provides:       qmk_cli
Provides:       qmk-cli
Provides:       python3-qmk_cli

Packager:	      Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -p1 -n qmk_cli-%version

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files qmk_cli

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md SECURITY.md
%license LICENSE
%{_bindir}/qmk
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/qmk-%version.dist-info/*

%changelog
* Thu Sep 04 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
