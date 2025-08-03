Name:       swaylock
Version:	1.8.3
Release:	1
Summary:    Screen locker for Wayland

License:    MIT
URL:        https://github.com/swaywm/swaylock
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Older versions were part of the sway package
Conflicts:      sway < 1.0

BuildRequires:  meson >= 0.48.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  scdoc

%description
swaylock is a screen locking utility for Wayland compositors.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
# Co-own completion directories
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
