Summary: Enable audit on samba shared 
Name: nethserver-samba-audit
Version: 1.2.0
Release: 1%{?dist}
License: GPLv2
Source: %{name}-%{version}.tar.gz
URL: %{url_prefix}/%{name} 
BuildArch: noarch 
Requires: nethserver-ibays, nethserver-httpd, nethserver-mysql, nethserver-samba
Requires: php-mysql
BuildRequires: nethserver-devtools

%description
Enable audit on samba shared and browse log using a simple web interface.

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} \
    --file /var/log/smbaudit.log 'attr(0640,root,root)' \
%{buildroot} > %{name}-%{version}-filelist


%pre

%preun

%post

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%config /var/log/smbaudit.log
%doc COPYING
%dir %{_nseventsdir}/%{name}-update


%changelog
* Mon Oct 28 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- SambaAudit: improve perfomance - NethServer/dev#5881

* Tue May 28 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.6-1
- File server Cockpit UI - NethServer/dev#5754

* Tue Jun 19 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.5-1
- SambaAudit: support SME 8 migration - Bug NethServer/dev#5530

* Thu Jun 07 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.4-1
- SambaAudit: improve search performance - NethServer/dev#5519

* Fri Oct 20 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.3-1
- Fix pagination for paths with spaces - nethserver-samba-audit#4

* Wed Jan 11 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1
- httpd-admin: use KillMode=process - NethServer/dev#5190

* Wed Nov 02 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- SambAudit: "Reload" button doesn't work - NethServer/dev#5139

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.1.0-1
- First NS7 release

* Tue Sep 29 2015 Davide Principi <davide.principi@nethesis.it> - 1.0.5-1
- Make Italian language pack optional - Enhancement #3265 [NethServer]

* Thu Oct 02 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.4-1.ns6
- Smbaudit doesn't show the name of the file for some operations - Bug #2870 [NethServer]

* Mon Jul 29 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.3-1.ns6
- Relocated scripts under /usr/bin/ - Feature #1963 [NethServer]

* Mon Jul 29 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- Execute nethserver-samba-audit-conf action before expand-template #1963
- Add nethserver-mysql and nethserver-samba dependencies #1963

* Fri Jul 26 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
- Implement FHS 2.3 compliance #2065
- Various fixes #1963 

* Fri Jun 21 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1.ns6
- First release. Refs #1963

