# https://ziglang.org/download/VERSION/release-notes.html#Support-Table
%global         zig_arches x86_64 aarch64 riscv64 %{mips64}
# Signing key from https://ziglang.org/download/
%global         public_key RWSGOq2NVecA2UPNdBUZykf1CCb147pkmdtYxgb3Ti+JO/wCYvhbAb/U

# note here at which Fedora or EL release we need to use compat LLVM packages
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 9
%define         llvm_compat 19
%endif
%global         llvm_version 19.0.0
%global         ver 0.15.0-dev.75+03123916e
%bcond bootstrap 1
%bcond docs      %{without bootstrap}
%bcond test      1
%if 0%{?fedora} <= 40
%global zig_cache_dir %{_builddir}/zig-cache
%else
%global zig_cache_dir %{builddir}/zig-cache
%endif
%global zig_build_options %{shrink: \
    --verbose \
    --release=fast \
    --summary all \
    \
    -Dtarget=native \
    -Dcpu=baseline \
    --zig-lib-dir lib \
    \
    --cache-dir "%{zig_cache_dir}" \
    --global-cache-dir "%{zig_cache_dir}" \
    \
    -Dversion-string="%{version}" \
    -Dstatic-llvm=false \
    -Denable-llvm=true \
    -Dno-langref=true \
    -Dstd-docs=false \
    -Dpie \
    -Dconfig_h="%{__cmake_builddir}/config.h" \
    -Dbuild-id="sha1" \
}
%global zig_install_options %zig_build_options %{shrink: \
    --prefix "%{_prefix}" \
}

Name:           zig-nightly
Version:        %(echo %{ver} | sed 's/-/~/g')
Release:        1%{?dist}
Summary:        Programming language for maintaining robust, optimal, and reusable software
License:        MIT AND NCSA AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-2.0-or-later AND GPL-2.0-or-later WITH GCC-exception-2.0 AND BSD-3-Clause AND Inner-Net-2.0 AND ISC AND LicenseRef-Fedora-Public-Domain AND GFDL-1.1-or-later AND ZPL-2.1
URL:            https://ziglang.org
Source0:        %{url}/builds/zig-%{ver}.tar.xz
Source1:        %{url}/builds/zig-%{ver}.tar.xz.minisig
# Remove native lib directories from rpath
# this is unlikely to be upstreamed in its current state because upstream
# wants to work around the shortcomings of NixOS
Patch0:         https://src.fedoraproject.org/fork/sentry/rpms/zig/raw/fork/0.14.0/f/0001-remove-native-lib-directories-from-rpath.patch
# Adds a build option for setting the build-id
# some projects are not programmed to handle a build-id's
# by having it as a flag we can make sure no developer runs into
# any trouble because of packaging demands
# https://github.com/ziglang/zig/pull/22516
Patch1:         https://src.fedoraproject.org/fork/sentry/rpms/zig/raw/fork/0.14.0/f/0002-std.Build-add-build-id-option.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libxml2-devel
BuildRequires:  llvm%{?llvm_compat}-devel
BuildRequires:  clang%{?llvm_compat}-devel
BuildRequires:  lld%{?llvm_compat}-devel
# for man page generation
BuildRequires:  help2man
# for signature verification
BuildRequires:  minisign
%if %{without bootstrap}
BuildRequires:  %{name} = %{version}
%endif
%if %{with test}
BuildRequires:  elfutils-libelf-devel
BuildRequires:  libstdc++-static
%endif
Requires:       %{name}-libs = %{version}
# Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
Provides: bundled(compiler-rt) = %{llvm_version}
# LGPL-2.1-or-later AND SunPro AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later WITH GNU-compiler-exception AND GPL-2.0-only AND ISC AND LicenseRef-Fedora-Public-Domain AND HPND AND CMU-Mach AND LGPL-2.0-or-later AND Unicode-3.0 AND GFDL-1.1-or-later AND GPL-1.0-or-later AND FSFUL AND MIT AND Inner-Net-2.0 AND X11 AND GPL-2.0-or-later WITH GCC-exception-2.0 AND GFDL-1.3-only AND GFDL-1.1-only
Provides: bundled(glibc) = 2.41
# Apache-2.0 WITH LLVM-exception OR MIT OR NCSA
Provides: bundled(libcxx) = %{llvm_version}
# Apache-2.0 WITH LLVM-exception OR MIT OR NCSA
Provides: bundled(libcxxabi) = %{llvm_version}
# NCSA
Provides: bundled(libunwind) = %{llvm_version}
# BSD, LGPG, ZPL
Provides: bundled(mingw) = 3839e21b08807479a31d5a9764666f82ae2f0356
# MIT
Provides: bundled(musl) = 1.2.5
# Apache-2.0 WITH LLVM-exception AND Apache-2.0 AND MIT AND BSD-2-Clause
Provides: bundled(wasi-libc) = d03829489904d38c624f6de9983190f1e5e7c9c5
ExclusiveArch: %{zig_arches}

%description
Zig is an open-source programming language designed for robustness, optimality,
and clarity. This package provides the zig compiler and the associated runtime.

# The Zig stdlib only contains uncompiled code
%package libs
Summary:        Zig Standard Library
BuildArch:      noarch

%description libs
Zig Standard Library

%if %{with docs}
%package doc
Summary:        Documentation for Zig
BuildArch:      noarch
Requires:       %{name} = %{version}

%description doc
Documentation for Zig. For more information, visit %{url}
%endif

%prep
/usr/bin/minisign -V -m %{SOURCE0} -x %{SOURCE1} -P %{public_key}
%autosetup -p1 -n zig-%{ver}

%build
export CFLAGS='-O2 -flto=auto -ffat-lto-objects -fexceptions -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -m64 -march=x86-64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -mtls-dialect=gnu2 -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer '
# zig doesn't know how to dynamically link llvm on its own so we need cmake to generate a header ahead of time
# if we provide the header we need to also build zigcpp

# C_FLAGS: wasm2c output generates a lot of noise with -Wunused.
# EXTRA_BUILD_ARGS: explicitly specify a build-id
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
    -DCMAKE_C_FLAGS_RELWITHDEBINFO:STRING="-DNDEBUG -Wno-unused" \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING="-DNDEBUG -Wno-unused" \
    \
    -DZIG_EXTRA_BUILD_ARGS:STRING="--verbose;--build-id=sha1" \
    -DZIG_SHARED_LLVM:BOOL=true \
    -DZIG_PIE:BOOL=true \
    \
    -DZIG_TARGET_MCPU:STRING=baseline \
    -DZIG_TARGET_TRIPLE:STRING=native \
    \
    -DZIG_VERSION:STRING="%{ver}"

%if %{with bootstrap}
%cmake_build --target stage3
%else
%cmake_build --target zigcpp
zig build %{zig_build_options}

# Zig has no official manpage
# https://github.com/ziglang/zig/issues/715
help2man --no-discard-stderr --no-info "./zig-out/bin/zig" --version-option=version --output=zig.1
%endif


%if %{with docs}
# Use the newly made stage 3 compiler to generate docs
./zig-out/bin/zig build docs \
    --verbose \
    --global-cache-dir "%{zig_cache_dir}" \
    -Dversion-string="%{version}"
%endif

%install
%if %{with bootstrap}
%cmake_install
%else
DESTDIR="%{buildroot}" zig build install %{zig_install_options}

install -D -pv -m 0644 -t %{buildroot}%{_mandir}/man1/zig.1
%endif


%if %{with macro}
install -D -pv -m 0644 %{SOURCE2} %{buildroot}%{_rpmmacrodir}/macros.%{name}
%endif

%if %{with test}
%check
# Run reduced set of tests, based on the Zig CI
"%{buildroot}%{_bindir}/zig" test test/behavior.zig -Itest
%endif

%files
%license LICENSE
%{_bindir}/zig
%if %{without bootstrap}
%{_mandir}/man1/zig.1.*
%endif

%files libs
%{_prefix}/lib/zig

%if %{with docs}
%files doc
%doc README.md
%doc zig-out/doc/langref.html
%doc zig-out/doc/std
%endif

%changelog
* Wed Jan 22 2025 ShinyGil <rockgrub@disroot.org>
- Initial package
