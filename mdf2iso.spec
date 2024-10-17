Name:		mdf2iso
Version:	0.3.1
Release:	1
Summary:	Alkohol 120 CD Images (.mdf) to ISO converter
License:	GPL
Group:		Archiving/Other
URL:		https://mdf2iso.berlios.de/
Source0:	https://cdn-aws.deb.debian.org/debian/pool/main/m/mdf2iso/mdf2iso_%{version}.orig.tar.gz

%description
MDF2ISO is a very simple utility to convert an Alcohol 120 bin images
to the standard ISO-9660 format.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%doc ChangeLog gpl.txt
%{_bindir}/mdf2iso
