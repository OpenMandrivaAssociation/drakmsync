Summary:  Mobile device synchronization tool
Name:     drakmsync
Version:  0.3
Release:  %mkrel 1
Source0:  %name-%version.tar.bz2
License:  GPL
Group:    System/Configuration/Other
Url:      http://www.mandrivalinux.com/en/cvs.php3
Requires: drakxtools => 10.4.53-1mdv2007.0
Requires: perl-Gtk2 >= 1.023-1mdk
BuildRoot: %_tmppath/%name-%version-buildroot
BuildArch: noarch

%description
Drakmsync is a tool that makes it easy to synchronize
mobile devices.

%prep
%setup -q

%build
%make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

#install lang
%find_lang %name

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%_bindir/*
%{_datadir}/applications/drakmsync.desktop
%_datadir/drakmsync/*.pm
%attr(644,root,root) %_datadir/drakmsync/profiles/*
/usr/lib/libDrakX/icons/pda_section.png
