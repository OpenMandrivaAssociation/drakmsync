Summary:  Mobile device synchronization tool
Name:     drakmsync
Version:  0.6.1
Release:  2
Source0:  %name-%version.tar.bz2
License:  GPL
Group:    System/Configuration/Other
Url:      https://www.mandrivalinux.com/en/cvs.php3
Requires: drakxtools => 10.4.53-1mdv2007.0
Requires: msynctool
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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%_bindir/*
%{_datadir}/applications/drakmsync.desktop
%_datadir/drakmsync/*.pm
%attr(644,root,root) %_datadir/drakmsync/profiles/*
/usr/lib/libDrakX/icons/pda_section.png


%changelog
* Wed Apr 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.6.1-1mdv2009.1
+ Revision: 367391
- translation updates

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.6-2mdv2009.1
+ Revision: 350648
- rebuild

* Mon Sep 22 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6-1mdv2009.0
+ Revision: 287079
- translation updates

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.5-3mdv2009.0
+ Revision: 244527
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Mar 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.5-1mdv2008.1
+ Revision: 190159
- translation updates

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.4-2mdv2008.1
+ Revision: 136380
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 04 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.4-2mdv2008.0
+ Revision: 95321
- requires msynctool (#34465)

* Wed Oct 03 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.4-1mdv2008.0
+ Revision: 95063
- updated translation

* Tue Sep 25 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.3-1mdv2008.0
+ Revision: 92941
- updated translations

* Wed Sep 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.2-1mdv2008.0
+ Revision: 90961
- add syncML profiles
- updated translation

* Thu Aug 16 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1-2mdv2008.0
+ Revision: 64184
- fix description & summary (adamw)

* Tue Aug 14 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1-1mdv2008.0
+ Revision: 63391
- Import drakmsync




* Tue Aug 14 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1-1mdv2008.0
- initial release
