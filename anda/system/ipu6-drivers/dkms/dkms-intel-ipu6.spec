%global debug_package %{nil}
%global ipu6_commit c09e2198d801e1eb701984d2948373123ba92a56
%global ipu6_commitdate 20250424
%global ipu6_shortcommit %(c=%{ipu6_commit}; echo ${c:0:7})
%global usbio_commit 450939ff5f8af733bc89c564603222a4d420acf3
%global usbio_commitdate 20241210
%global usbio_shortcommit %(c=%{usbio_commit}; echo ${c:0:7})
%global commit_date 20250224
%global modulename intel-ipu6
# Actual "release" version, currently unused as the release versions are back and forth on if on if they use 1.0.0 or 1.0.1
%global ver 1.0.1

Name:           dkms-%{modulename}
Summary:        DKMS module for %{modulename}
Version:        0^%{ipu6_commitdate}git.%{ipu6_shortcommit}
Release:        1%?dist
License:        GPL-2.0-or-later
URL:            https://github.com/intel/ipu6-drivers
Source0:        https://github.com/intel/ipu6-drivers/archive/%{ipu6_commit}/ipu6-drivers-%{ipu6_shortcommit}.tar.gz
Source1:        https://github.com/intel/usbio-drivers/archive/%{usbio_commit}/usbio-drivers-%{usbio_shortcommit}.tar.gz
Source2:        no-weak-modules.conf
# Patches
# https://github.com/intel/ipu6-drivers/pull/322
Patch1:         0001-Makefile-Switch-sensor-driver-symbols-from-CONFIG_VI.patch
Patch2:         0002-Makefile-Re-enable-gc5035-compilation-with-kernels-6.patch
Patch3:         0003-Makefile-Do-not-build-hi556-driver-with-kernels-6.10.patch
Patch4:         0004-Makefile-Do-not-build-ov01a10-driver-with-kernels-6..patch
# https://github.com/intel/ipu6-drivers/pull/321
Patch5:         0005-media-ipu6-Fix-out-of-tree-builds.patch
Patch6:         0006-media-ipu6-Fix-building-with-kernel-6.13.patch
Patch7:         0007-Modify-0001-v6.10-IPU6-headers-used-by-PSYS.patch-fo.patch
# https://github.com/intel/ipu6-drivers/pull/324
Patch8:         0008-ipu6-psys-Adjust-DMA-code-for-ipu6-bus-DMA-changes-i.patch
Patch9:         0009-Add-ipu6-dma.h-to-0001-v6.10-IPU6-headers-used-by-PS.patch
# https://github.com/intel/ipu6-drivers/pull/327
Patch10:        0010-psys-Do-not-skipping-registering-ipu_psys_bus-for-ke.patch
Patch11:        0011-psys-Use-cdev_device_add-for-dev-ipu-psys0.patch
# https://github.com/intel/usbio-drivers/pull/33
Patch20:        0010-usbio-Fix-GPIO-and-I2C-driver-modaliases.patch
# https://github.com/intel/usbio-drivers/pull/34
Patch21:        0011-usbio-Fix-I2C-max-transfer-size.patch
Patch22:        0012-usbio-Use-MAX_PAYLOAD_BSIZE-in-usbio_bulk_write.patch
# Downstream/Fedora specific patches
Patch101:       0101-Fedora-local-mod-integrate-usbio-drivers-within-ipu6.patch
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros
Requires:       %{modulename}-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

%description
This package enables the Intel IPU6 image processor.

%prep
%setup -q -c -a 1
(cd ipu6-drivers-%{ipu6_commit}
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1
%patch 6 -p1
%patch 7 -p1
%patch 8 -p1
%patch 9 -p1
%patch 10 -p1
%patch 11 -p1
%patch 101 -p1
patch -p1 < patches/0001-v6.10-IPU6-headers-used-by-PSYS.patch
sed -i "s/^PACKAGE_VERSION=\".*\"$/PACKAGE_VERSION=\"%{version}\"/g" ./dkms.conf
)
(cd usbio-drivers-%{usbio_commit}
%patch 20 -p1
%patch 21 -p1
%patch 22 -p1
)

cp -Rp usbio-drivers-%{usbio_commit}/drivers ipu6-drivers-%{ipu6_commit}/
cp -Rp usbio-drivers-%{usbio_commit}/include ipu6-drivers-%{ipu6_commit}/

%build

%install
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}
cp -fr ipu6-drivers-%{ipu6_commit}/{drivers,include,patch,patches,Makefile,dkms.conf} %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

%if 0%{?fedora}
# Do not enable weak modules support in Fedora (no kABI):
install -Dpm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%post
dkms add -m %{modulename} -v %{version} -q --rpm_safe_upgrade || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{modulename} -v %{version} -q || :
dkms install -m %{modulename} -v %{version} -q --force || :

%preun
# Remove all versions from DKMS registry:
dkms remove -m %{modulename} -v %{version} -q --all --rpm_safe_upgrade || :

%files
%{_usrsrc}/%{modulename}-%{version}
%if 0%{?fedora}
%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%changelog
* Thu Apr 24 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
