===================
nethserver-collectd 
===================

This package automatically configure basic :index:`collectd` plugins and it's part of ``nethserver-statistics`` yum package group.

This package will install a base collectd configuration. Default enabled modules:

* cpu
* load
* processes
* memory
* swap
* uptime
* df
* disk
* interface
* network
* rrdtool

No configuration is needed, collectd is enabled by default when installed.

Web interface
=============

To view graphs of collected data, install  and nethserver-cgp.

Cleanup
=======

Every day a cronjob (:file:`/etc/cron.daily/collectd_cleanup`) takes care to clean up all RRD files not updated
during the last day.


Interesting plugins
===================

The following can be manually installed:

* collectd-nut
* collectd-sensors


Database
========

Configuration is saved inside the ``configuration`` database. Example: ::

 collectd=service
    PingHosts=
    status=enabled

