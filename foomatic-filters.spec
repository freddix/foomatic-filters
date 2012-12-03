%include	/usr/lib/rpm/macros.perl

Summary:	System for using free software printer drivers
Name:		foomatic-filters
Version:	4.0.17
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-%{version}.tar.gz
# Source0-md5:	bc0764a562b32c9aabba9f1b0276bf7d
URL:		http://www.linuxfoundation.org/en/OpenPrinting/Database/Foomatic
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

%description
Foomatic is a system for using free software printer drivers with
common spoolers on Unix. It supports LPD, PDQ, CUPS, the VA Linux LPD,
LPRng, PPR, and direct spooler-less printing and any free software
driver for which execution data has been entered in the database.

%package -n cups-filter-foomatic
Summary:	cupsomatic - CUPS filter
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}
Requires:	cups

%description -n cups-filter-foomatic
Cupsomatic is intended to be used as a CUPS filter for printers
defined in a PPD file (CUPS-O-Matic or PPD-O-Matic) obtained from the
Linux Printing Database.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure \
	TEXTTOPS=/usr/lib/cups/filter/texttops \
	--with-file-converter=texttops
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

ln -sf %{_bindir}/foomatic-rip $RPM_BUILD_ROOT%{_ulibdir}/cups/filter/cupsomatic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README USAGE
%dir %{_sysconfdir}/foomatic
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/foomatic/direct
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/foomatic/filter.conf
%attr(755,root,root) %{_bindir}/foomatic-rip
%{_mandir}/man1/foomatic-rip*

%files -n cups-filter-foomatic
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/cups/backend/beh
%attr(755,root,root) %{_ulibdir}/cups/filter/cupsomatic
%attr(755,root,root) %{_ulibdir}/cups/filter/foomatic-rip

