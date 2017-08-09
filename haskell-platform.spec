Name:   haskell-platform
Version:    8.0.2
Release:    2%{?dist}
Summary:    RHEL7 workaround
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  mesa-libGL 
BuildRequires:  mesa-libGLU

License:    BSD
URL:    https://haskell.org
Source:    https://haskell.org/platform/download/%{version}/%{name}-%{version}-unknown-posix--full-%{_arch}.tar.gz

%description
Package for RHEL7 - don't use it if you don't have to, this is just ugly workaround.
Probably one day I will die because of this spec file :(

%prep
%setup -q -c -n %{name}-%{version}

%install
tar -xvf hp-usr-local.tar.gz -C %{buildroot}

%post
/bin/sh /usr/local/haskell/ghc-8.0.2-x86_64/bin/activate-hs

%files
/usr

%changelog
* Wed Jul 26 2017 Marcin Franczyk <mfranczy@redhat.com> - 8.0.2-1
- haskell platform package for rhel7
