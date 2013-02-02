Summary:	GNOME core client for GGZ
Summary(pl.UTF-8):	Klient GGZ dla środowiska GNOME
Name:		ggz-gtk-games
Version:	0.0.14.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://mirrors.dotsrc.org/ggzgamingzone/ggz/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	72049279f3f2d1a0a0b5196331867754
Patch0:		%{name}-nls-domains.patch
URL:		http://www.ggzgamingzone.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ggz-client-libs-devel >= 0.0.14
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libggz-devel >= 0.0.14
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires(post,preun):	ggz-client-libs >= 0.0.14
Requires:	ggz-client-libs >= 0.0.14
Requires:	libggz-devel >= 0.0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GNOME core client for GGZ.

%description -l pl.UTF-8
Ten pakiet to klient GGZ dla środowiska GNOME.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4 -I m4/ggz
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# collect modules.ggz pieces
install -d $RPM_BUILD_ROOT%{_datadir}/ggz/ggz-config
for d in chess chinese-checkers combat dots ggzcards hastings reversi spades tictactoe ; do
	cp -p ${d}/module.dsc $RPM_BUILD_ROOT%{_datadir}/ggz/ggz-config/${d}.dsc
done
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/ggz.modules

# ggz* domains
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
for d in chess chinese-checkers combat dots ggzcards hastings reversi spades tictactoe ; do
	%{_bindir}/ggz-config --install --modfile=%{_datadir}/ggz/ggz-config/${d}.dsc
done

%preun
if [ "$1" = "0" ]; then
	for d in chess chinese-checkers combat dots ggzcards hastings reversi spades tictactoe ; do
		%{_bindir}/ggz-config --install --modfile=%{_datadir}/ggz/ggz-config/${d}.dsc
	done
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS QuickStart.GGZ README README.GGZ TODO
%attr(755,root,root) %{_libdir}/ggz/ggz.ccheckers
%attr(755,root,root) %{_libdir}/ggz/ggz.chess
%attr(755,root,root) %{_libdir}/ggz/ggz.combat
%attr(755,root,root) %{_libdir}/ggz/ggz.dots
%attr(755,root,root) %{_libdir}/ggz/ggz.ggzcards
%attr(755,root,root) %{_libdir}/ggz/ggz.hastings
%attr(755,root,root) %{_libdir}/ggz/ggz.reversi
%attr(755,root,root) %{_libdir}/ggz/ggz.spades
%attr(755,root,root) %{_libdir}/ggz/ggz.ttt
%{_datadir}/ggz/ccheckers
%{_datadir}/ggz/chess
%{_datadir}/ggz/combat
%{_datadir}/ggz/hastings
%{_datadir}/ggz/pixmaps
%{_datadir}/ggz/reversi
%{_datadir}/ggz/tictactoe
%{_datadir}/ggz/ggz-config/chess.dsc
%{_datadir}/ggz/ggz-config/chinese-checkers.dsc
%{_datadir}/ggz/ggz-config/combat.dsc
%{_datadir}/ggz/ggz-config/dots.dsc
%{_datadir}/ggz/ggz-config/ggzcards.dsc
%{_datadir}/ggz/ggz-config/hastings.dsc
%{_datadir}/ggz/ggz-config/reversi.dsc
%{_datadir}/ggz/ggz-config/spades.dsc
%{_datadir}/ggz/ggz-config/tictactoe.dsc
