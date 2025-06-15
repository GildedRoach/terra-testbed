Name:           nimble
Version:        0.18.2
Release:        1%?dist
Summary:        Package manager for the Nim programming language
License:        BSD
URL:            https://github.com/nim-lang/nimble
Source0:        %url/archive/refs/tags/v%version.tar.gz
Source1:        nimble.1
# We use `nim` to get `nimble`… to build `nimble`
BuildRequires:  nim anda-srpm-macros git-core rpm_macro(bash_completions_dir)
Conflicts:      nim

%description
%summary.

%prep
%autosetup
%nim_prep

%build
%nim_build src/nimble

%install
install -Dpm755 src/nimble %buildroot%_bindir/nimble
install -Dpm644 -t%buildroot%_mandir/man1 %SOURCE1
install -Dpm644 nimble.bash-completion %buildroot%bash_completions_dir/nimble
install -Dpm644 nimble.zsh-completion %buildroot%zsh_completions_dir/_nimble.zsh

%files
%doc readme.markdown
%license license.txt
%_bindir/nimble
%_mandir/man1/nimble.1.gz
%bash_completions_dir/nimble
%zsh_completions_dir/_nimble.zsh
