Name:		mdf2iso
Version:	0.3.0
Release:	%mkrel 1
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

