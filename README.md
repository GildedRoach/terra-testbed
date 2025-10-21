# Terra Sources

Terra is a rolling-release Fedora repository for all the software you need.
With Terra, you can install the latest packages knowing that quality and security are assured.

See the introduction at [our website](https://terra.fyralabs.com).

This monorepo contains the package manifests for all packages in Terra.

## Installation

The latest detailed instructions are available in our Devdocs: https://developer.fyralabs.com/terra/installing

### Fedora

```bash
sudo dnf install --nogpgcheck --repofrompath 'terra,https://repos.fyralabs.com/terra$releasever' terra-release
```

If you are using immutable/atomic editions of Fedora, run the following commands instead:

```bash
curl -fsSL https://github.com/terrapkg/subatomic-repos/raw/main/terra.repo | pkexec tee /etc/yum.repos.d/terra.repo
sudo rpm-ostree install terra-release
```

Optionally, you can install `terra-release-extra` to use the Extras repository. This also installs the Nvidia, and Mesa streams but does not enable them.

### Enterprise Linux (EL)

Only EL10 is supported. Not all packages available in Terra are available in Terra EL at this time.

Terra EL requires the EPEL repos, which may be installed with:

```bash
sudo dnf install 'https://dl.fedoraproject.org/pub/epel/epel-release-latest-$releasever.noarch.rpm'
```

And Terra EL itself can be installed with:

```bash
sudo dnf install --nogpgcheck --repofrompath 'terra,https://repos.fyralabs.com/terrael$releasever' terra-release
```

## Documentation

Our documentation can be found on our [Devdocs](https://developer.fyralabs.com/terra/).

## pkgs.org

pkgs.org provides a list of the packages available in the main stream: https://fedora.pkgs.org/rawhide/terra/

## Questions?

Feel free to reach out by [joining our community](https://wiki.ultramarine-linux.org/en/community/community/). We're always happy to help!

- [Contribution Guide](https://developer.fyralabs.com/terra/contributing)
- [FAQ](https://developer.fyralabs.com/terra/faq)
- [Policy](https://developer.fyralabs.com/terra/policy)
