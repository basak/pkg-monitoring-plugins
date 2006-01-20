Name: nagios-plugins
Version: 1.4
Release: 1
Summary: Host/service/network monitoring program plugins for Nagios

Group: Applications/System
License: GPL
URL: http://nagiosplug.sourceforge.net/
Source0: http://dl.sf.net/sourceforge/nagiosplug/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Prefix: %{_prefix}/lib/nagios/plugins
Packager: Karl DeBisschop <kdebisschop@users.sourceforge.net>
Vendor: Nagios Plugin Development Group
Provides: nagios-plugins

%{!?custom:%global custom 0}
Obsoletes: nagios-plugins-custom nagios-plugins-extras


# Requires


%description

Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios. This package
contains those plugins.


%prep
%setup -q


%build
./configure \
--prefix=%{_prefix} \
--exec-prefix=%{_exec_prefix} \
--libexecdir=%{_exec_prefix}/lib/nagios/plugins \
--sysconfdir=%{_sysconfdir}/nagios \
--datadir=%{_datadir} \
--with-cgiurl=/nagios/cgi-bin
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make AM_INSTALL_PROGRAM_FLAGS="" DESTDIR=${RPM_BUILD_ROOT} install
install -d ${RPM_BUILD_ROOT}/etc/nagios
install -m 664 command.cfg ${RPM_BUILD_ROOT}/etc/nagios
%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root)
%config(missingok,noreplace) /etc/nagios/command.cfg
%doc CODING COPYING FAQ INSTALL LEGAL README REQUIREMENTS SUPPORT THANKS
%doc ChangeLog command.cfg
%defattr(775,root,root)
%dir %{_exec_prefix}/lib/nagios/plugins
%{_datadir}/locale/de/LC_MESSAGES/nagios-plugins.mo
%{_datadir}/locale/fr/LC_MESSAGES/nagios-plugins.mo

%if %custom

%{_exec_prefix}/lib/nagios/plugins/*

%else

%{_exec_prefix}/lib/nagios/plugins/check_by_ssh
%{_exec_prefix}/lib/nagios/plugins/check_breeze
%{_exec_prefix}/lib/nagios/plugins/check_dig
%{_exec_prefix}/lib/nagios/plugins/check_disk
%{_exec_prefix}/lib/nagios/plugins/check_disk_smb
%{_exec_prefix}/lib/nagios/plugins/check_dns
%{_exec_prefix}/lib/nagios/plugins/check_dummy
%{_exec_prefix}/lib/nagios/plugins/check_flexlm
%{_exec_prefix}/lib/nagios/plugins/check_ftp
%{_exec_prefix}/lib/nagios/plugins/check_http
%{_exec_prefix}/lib/nagios/plugins/check_ifoperstatus
%{_exec_prefix}/lib/nagios/plugins/check_ifstatus
%{_exec_prefix}/lib/nagios/plugins/check_imap
%{_exec_prefix}/lib/nagios/plugins/check_ircd
%{_exec_prefix}/lib/nagios/plugins/check_load
%{_exec_prefix}/lib/nagios/plugins/check_log
%{_exec_prefix}/lib/nagios/plugins/check_mailq
%{_exec_prefix}/lib/nagios/plugins/check_mrtg
%{_exec_prefix}/lib/nagios/plugins/check_mrtgtraf
%{_exec_prefix}/lib/nagios/plugins/check_nagios
%{_exec_prefix}/lib/nagios/plugins/check_nntp
%{_exec_prefix}/lib/nagios/plugins/check_nt
%{_exec_prefix}/lib/nagios/plugins/check_ntp
%{_exec_prefix}/lib/nagios/plugins/check_nwstat
%{_exec_prefix}/lib/nagios/plugins/check_oracle
%{_exec_prefix}/lib/nagios/plugins/check_overcr
%{_exec_prefix}/lib/nagios/plugins/check_ping
%{_exec_prefix}/lib/nagios/plugins/check_pop
%{_exec_prefix}/lib/nagios/plugins/check_procs
%{_exec_prefix}/lib/nagios/plugins/check_real
%{_exec_prefix}/lib/nagios/plugins/check_rpc
%{_exec_prefix}/lib/nagios/plugins/check_sensors
%{_exec_prefix}/lib/nagios/plugins/check_smtp
%{_exec_prefix}/lib/nagios/plugins/check_ssh
%{_exec_prefix}/lib/nagios/plugins/check_swap
%{_exec_prefix}/lib/nagios/plugins/check_tcp
%{_exec_prefix}/lib/nagios/plugins/check_time
%{_exec_prefix}/lib/nagios/plugins/check_udp
%{_exec_prefix}/lib/nagios/plugins/check_ups
%{_exec_prefix}/lib/nagios/plugins/check_users
%{_exec_prefix}/lib/nagios/plugins/check_wave
%{_exec_prefix}/lib/nagios/plugins/negate
%{_exec_prefix}/lib/nagios/plugins/utils.pm
%{_exec_prefix}/lib/nagios/plugins/utils.sh
%{_exec_prefix}/lib/nagios/plugins/urlize
%{_exec_prefix}/lib/nagios/plugins/check_file_age
%{_exec_prefix}/lib/nagios/plugins/check_fping
%{_exec_prefix}/lib/nagios/plugins/check_game
%{_exec_prefix}/lib/nagios/plugins/check_ldap
%{_exec_prefix}/lib/nagios/plugins/check_mysql
%{_exec_prefix}/lib/nagios/plugins/check_pgsql
%{_exec_prefix}/lib/nagios/plugins/check_radius
%{_exec_prefix}/lib/nagios/plugins/check_snmp
%{_exec_prefix}/lib/nagios/plugins/check_hpjd

%endif

%changelog
* Tue Mar 04 2004 Karl DeBisschop <karl[AT]debisschop.net> - 1.4.0alpha1
- extensive rewrite to facilitate processing into various distro-compatible specs
