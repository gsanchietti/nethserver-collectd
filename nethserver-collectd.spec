Summary: nethserver collectd configuration
Name: nethserver-collectd
Version: 1.1.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}

BuildRequires: nethserver-devtools

AutoReq: no
Requires: nethserver-base
Requires: collectd, collectd-rrdtool, collectd-ping

%description
NethServer collectd configuration

%prep
%setup

%post

%preun

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} $RPM_BUILD_ROOT > e-smith-%{version}-filelist
echo "%doc COPYING"          >> e-smith-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)

%changelog
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

