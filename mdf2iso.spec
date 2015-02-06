Name:		mdf2iso
Version:	0.3.0
Release:	2
Summary:	Alkohol 120 CD Images (.mdf) to ISO converter
License:	GPL
Group:		Archiving/Other
URL:		http://mdf2iso.berlios.de/
Source:		%{name}-%{version}-src.tar.bz2
Patch0:		mdf2iso-0.3.0-largefiles.patch

%description
MDF2ISO is a very simple utility to convert an Alcohol 120 bin images
to the standard ISO-9660 format.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%doc ChangeLog gpl.txt
%{_bindir}/mdf2iso



%changelog
* Wed Apr 18 2012 Andrey Bondrov <abondrov@mandriva.org> 0.3.0-1
+ Revision: 791639
- imported package mdf2iso


* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-07-14 18:41:13 (41135)
- rebuild

* Fri Jun 23 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-06-23 14:43:25 (37937)
- import mdf2iso-0.3.0-1mdk

* Wed May 25 2005 Lenny Cartier <lenny@mandriva.com> 0.3.0-1mdk
- 0.3.0

* Thu Mar 31 2005 Olivier Thauvin <nanardon@mandrake.org> 0.2.2-1mdk
- from Michael Berger <webmaster@hmb-linux.de>
  - 0.2.2

