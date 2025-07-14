Summary:	A mail notification program designed for blackbox
Summary(pl.UTF-8):	Powiadamiacz o poczcie zaprojektowany dla blackboksa
Name:		bbmail
Version:	0.8.3
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
# Source0-md5:	fc5dd75c3350402a3740a9982f206118
Patch0:		%{name}-sysconfdir.patch
Patch1:		%{name}-fmod.patch
URL:		http://bbtools.windsofstorm.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bbmail is a tool which notifies you about arriving mail. It works
great with blackbox window manager, because it use it's theme, but it
can also work with other. bbmail can use multiple mailboxes (in many
types) and is highly configurable.

%description -l pl.UTF-8
bbmail jest programem powiadamiającym o przychodzącej poczcie.
Współpracuje z zarządcą okien blackbox, używając jego ustawień
wyglądu, aczkolwiek może też działać z innym. Obsługuje wiele 
skrzynek pocztowych (w różnych formatach) i jest wysoce 
konfigurowalny.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/bb*
%dir %{_sysconfdir}/bbtools
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bbtools/%{name}.*
%{_mandir}/man1/*
