# Generated by rust2rpm 24
%bcond_without check
%global __brp_mangle_shebangs %{nil}

%global crate gitoxide

Name:           rust-gitoxide
Version:        0.45.0
Release:        1%?dist
Summary:        Command-line application for interacting with git repositories

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gitoxide
Source:         %{crates_source}

BuildRequires:  openssl-devel-engine cmake anda-srpm-macros rust-packaging >= 21 mold

%global _description %{expand:
A command-line application for interacting with git repositories.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-APACHE
%license LICENSE-MIT
%doc README.md
%{_bindir}/ein
%{_bindir}/gix

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cache-efficiency-debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cache-efficiency-debug-devel %{_description}

This package contains library source intended for building other packages which
use the "cache-efficiency-debug" feature of the "%{crate}" crate.

%files       -n %{name}+cache-efficiency-debug-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crosstermion-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crosstermion-devel %{_description}

This package contains library source intended for building other packages which
use the "crosstermion" feature of the "%{crate}" crate.

%files       -n %{name}+crosstermion-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+document-features-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+document-features-devel %{_description}

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%files       -n %{name}+document-features-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fast-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fast-devel %{_description}

This package contains library source intended for building other packages which
use the "fast" feature of the "%{crate}" crate.

%files       -n %{name}+fast-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fast-safe-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fast-safe-devel %{_description}

This package contains library source intended for building other packages which
use the "fast-safe" feature of the "%{crate}" crate.

%files       -n %{name}+fast-safe-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-lite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-lite-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-lite" feature of the "%{crate}" crate.

%files       -n %{name}+futures-lite-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gitoxide-core-async-client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gitoxide-core-async-client-devel %{_description}

This package contains library source intended for building other packages which
use the "gitoxide-core-async-client" feature of the "%{crate}" crate.

%files       -n %{name}+gitoxide-core-async-client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gitoxide-core-blocking-client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gitoxide-core-blocking-client-devel %{_description}

This package contains library source intended for building other packages which
use the "gitoxide-core-blocking-client" feature of the "%{crate}" crate.

%files       -n %{name}+gitoxide-core-blocking-client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gitoxide-core-tools-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gitoxide-core-tools-devel %{_description}

This package contains library source intended for building other packages which
use the "gitoxide-core-tools" feature of the "%{crate}" crate.

%files       -n %{name}+gitoxide-core-tools-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gitoxide-core-tools-query-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gitoxide-core-tools-query-devel %{_description}

This package contains library source intended for building other packages which
use the "gitoxide-core-tools-query" feature of the "%{crate}" crate.

%files       -n %{name}+gitoxide-core-tools-query-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http-client-curl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-client-curl-devel %{_description}

This package contains library source intended for building other packages which
use the "http-client-curl" feature of the "%{crate}" crate.

%files       -n %{name}+http-client-curl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http-client-reqwest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-client-reqwest-devel %{_description}

This package contains library source intended for building other packages which
use the "http-client-reqwest" feature of the "%{crate}" crate.

%files       -n %{name}+http-client-reqwest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+is-terminal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+is-terminal-devel %{_description}

This package contains library source intended for building other packages which
use the "is-terminal" feature of the "%{crate}" crate.

%files       -n %{name}+is-terminal-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+lean-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lean-devel %{_description}

This package contains library source intended for building other packages which
use the "lean" feature of the "%{crate}" crate.

%files       -n %{name}+lean-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+lean-async-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lean-async-devel %{_description}

This package contains library source intended for building other packages which
use the "lean-async" feature of the "%{crate}" crate.

%files       -n %{name}+lean-async-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+max-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max-devel %{_description}

This package contains library source intended for building other packages which
use the "max" feature of the "%{crate}" crate.

%files       -n %{name}+max-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+max-control-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max-control-devel %{_description}

This package contains library source intended for building other packages which
use the "max-control" feature of the "%{crate}" crate.

%files       -n %{name}+max-control-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+max-pure-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max-pure-devel %{_description}

This package contains library source intended for building other packages which
use the "max-pure" feature of the "%{crate}" crate.

%files       -n %{name}+max-pure-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pretty-cli-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pretty-cli-devel %{_description}

This package contains library source intended for building other packages which
use the "pretty-cli" feature of the "%{crate}" crate.

%files       -n %{name}+pretty-cli-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+prodash-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+prodash-devel %{_description}

This package contains library source intended for building other packages which
use the "prodash" feature of the "%{crate}" crate.

%files       -n %{name}+prodash-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+prodash-render-line-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+prodash-render-line-devel %{_description}

This package contains library source intended for building other packages which
use the "prodash-render-line" feature of the "%{crate}" crate.

%files       -n %{name}+prodash-render-line-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+prodash-render-line-crossterm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+prodash-render-line-crossterm-devel %{_description}

This package contains library source intended for building other packages which
use the "prodash-render-line-crossterm" feature of the "%{crate}" crate.

%files       -n %{name}+prodash-render-line-crossterm-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+prodash-render-tui-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+prodash-render-tui-devel %{_description}

This package contains library source intended for building other packages which
use the "prodash-render-tui" feature of the "%{crate}" crate.

%files       -n %{name}+prodash-render-tui-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+small-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+small-devel %{_description}

This package contains library source intended for building other packages which
use the "small" feature of the "%{crate}" crate.

%files       -n %{name}+small-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
