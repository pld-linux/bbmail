Summary:	A mail notification program designed for blackbox
Summary(pl):	Powiadamiacz o poczcie zaprojektowany dla blackboksa
Name:		bbmail
Version:	0.8.3
Release:	1
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
bbmail is a tool which notifies you about arriving mail. It works
great with blackbox window manager, because it use it's theme, but it
can also work with other. bbmail can use multiple mailboxes (in many
types) and is highly configurable.

%description -l pl
bbmail jest programem powiadamiaj±cym o przychodz±cej poczcie.
Wspólpracuje z zarz±dca okien blackbox, u¿ywaj±c jego ustawieñ
wygl±du, aczkolwiek mo¿e te¿ dzia³aæ z innym. Obs³uguje wiele skrzynek
pocztowych (w ró¿nych formatach) i jest wysoce konfigurowalny.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/bb*
%{_mandir}/*/*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bbtools/%{name}.*
