Summary: nethserver collectd configuration
Name: nethserver-collectd
Version: 3.1.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}

BuildRequires: nethserver-devtools

Requires: nethserver-base
Requires: collectd >= 5.5.0
Requires: collectd-rrdtool
Requires: collectd-ping

%description
NethServer collectd configuration

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > e-smith-%{version}-filelist

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)
%config /etc/collectd.d/00plugins.conf
%config /etc/collectd.d/filter.conf
%config /etc/collectd.d/unixsock.conf
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Sep 05 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.1.0-1
- Exclude all tmpfs (#12)

* Wed May 22 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.0.8-1
- cron.daily: don't fails if dir names have spaces

* Thu Jul 12 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.0.7-1
- Hide QoS ifb devices - nethserver-collectd#10

* Thu Jun 15 2017 Stefano Fancello <stefano.fancello@nethesis.it> - 3.0.6-1
- collectd ping plugin segfault - Bug NethServer/dev#5316

* Wed May 10 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.0.5-1
- Upgrade from NS 6 via backup and restore - NethServer/dev#5234

* Thu Nov 10 2016 Davide Principi <davide.principi@nethesis.it> - 3.0.4-1
- collectd: unixsock plugin: bind failed: Address already in use - Bug NethServer/dev#5147

* Thu Oct 20 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.0.3-1
- NethServer joined to AD fail Kerberos ticket renewal - Bug #3428 [Forward port NethServer 6]

* Fri Oct 14 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.0.2-1
- Collectd: add memory plugin - NethServer/dev#5128

* Tue Sep 06 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.0.1-1
- Backup data: some files not included in backup - Bug NethServer/dev#5101

* Tue Sep 06 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.0.0-1
- Collectd graphs reset every night - NethServer/dev#5098
- Bump version to avoid conflicts with NS 6

* Fri Jul 08 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.1-1
- First NS 7 release

* Tue Jun 14 2016 Davide Principi <davide.principi@nethesis.it> - 2.0.0-1
- Collectd 5 - Feature #3403 [NethServer]

* Thu Feb 18 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.1-1
- Latency monitoring in multiwan - Enhancement #3351

* Tue Mar 17 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- Add collectd to backup-data - Enhancement #3072 [NethServer]
- collectd ping reload after wan change - Bug #3000 [NethServer]

* Tue Dec 02 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1.ns6
- collectd ping plugin to monitor network latency - Feature #2938 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.3-1.ns6
- Update URL tag in spec files - Task #1654 [NethServer]

* Mon Jul 29 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- Remove unused Runlevels property #2067

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
- Rebuild for automatic package handling. #1870

* Thu Feb 21 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> 1.0.0-1
- First release
