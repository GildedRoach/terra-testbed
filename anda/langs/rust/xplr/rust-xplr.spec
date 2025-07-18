# Generated by rust2rpm 27
%undefine __brp_mangle_shebangs

%global crate xplr

Name:           rust-xplr
Version:        1.0.1
Release:        1%?dist
Summary:        Hackable, minimal, fast TUI file explorer

License:        MIT
URL:            https://crates.io/crates/xplr
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  mold
BuildRequires:  anda-srpm-macros

%global _description %{expand:
A hackable, minimal, fast TUI file explorer.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND GPL-3.0-only AND MIT AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/xplr

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/


%prep
%autosetup -n %{crate}-%{version}
%cargo_prep_online

%build
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install
