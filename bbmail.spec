Summary:	A mail notification program designed for blackbox
Summary(pl):	Powiadamiacz o poczcie zaprojektowany dla blackboksa
Name:		bbmail
Version:	0.8.2
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-sysconfdir.patch
URL:		http://bbtools.windsofstorm.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
bbmail is a tool which notifies you about arriving mail. It works great with
blackbox window manager, becouse it use it's theme, but it can also work
with other.
bbmail can use multiple mailboxes (in many types), it is highly configurable.

%description -l pl
bbmail jest programem powiadamiaj±cym o przychodz±cej poczcie. Wspólpracuje
z zarz±dca okien blackbox, u¿ywaj±c jego ustawieñ wygl±du, aczkolwiek mo¿e te¿
dzia³aæ z innym.
Obs³uguje wiele skrzynek pocztowych (w ró¿nych formatach), jest wysoce
konfigurowalny.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make} CXX="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS BUGS README TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/bb*
%{_mandir}/*/*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bbtools/%{name}.*
