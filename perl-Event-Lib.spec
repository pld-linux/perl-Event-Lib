#
# Conditional build:
%bcond_with	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Event
%define	pnam	Lib
Summary:	Event::Lib - Perl extentions for event-based programming
Summary(pl.UTF-8):	Event::Lib - rozszerzenie Perla dla programowania opertego na zdarzeniach
Name:		perl-Event-Lib
Version:	1.03
Release:	3
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Event/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	90b60028f7f5836072e95c6d5b1d069e
URL:		http://search.cpan.org/dist/Event-Lib/
BuildRequires:	libevent-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-dirs >= 2.1-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a Perl wrapper around libevent(3) as available from
http://www.monkey.org/~provos/libevent/. It allows to execute a
function whenever a given event on a filehandle happens, a timeout
occurs or a signal is received.

Under the hood, one of the available mechanisms for asynchronously
dealing with events is used. This could be select, poll, epoll,
devpoll or kqueue. The idea is that you don't have to worry about
those details and the various interfaces they offer. Event::Lib offers
a unified interface to all of them (but see "CONFIGURATION" further
below).

Once you've skimmed through the next two sections (or maybe even now),
you should have a look at "EXAMPLE: A SIMPLE TCP SERVER" to get a
feeling about how it all fits together.

There's also a section briefly mentioning other event modules on the
CPAN and how they differ from Event::Lib further below ("OTHER EVENT
MODULES").

%description -l pl.UTF-8
Moduł ten opakowuje libevent.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Event/*.pm
%dir %{perl_vendorarch}/auto/Event/Lib
%{perl_vendorarch}/auto/Event/Lib/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Event/Lib/*.so
%{_mandir}/man3/*
