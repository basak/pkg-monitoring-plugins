#! /usr/bin/perl -w -I ..
#
# TCP Connection Based Tests via check_tcp
#
# $Id: check_tcp.t,v 1.3 2005/07/25 01:47:15 illumino Exp $
#

use strict;
use Test;
use NPTest;

use vars qw($tests);
BEGIN {$tests = 5; plan tests => $tests}

my $host_tcp_http      = getTestParameter( "host_tcp_http",      "NP_HOST_TCP_HTTP",      "localhost",
					   "A host providing the HTTP Service (a web server)" );

my $host_nonresponsive = getTestParameter( "host_nonresponsive", "NP_HOST_NONRESPONSIVE", "10.0.0.1",
					   "The hostname of system not responsive to network requests" );

my $hostname_invalid   = getTestParameter( "hostname_invalid",   "NP_HOSTNAME_INVALID",   "nosuchhost",
                                           "An invalid (not known to DNS) hostname" );

my $successOutput = '/^TCP OK\s-\s+[0-9]?\.?[0-9]+ second response time on port [0-9]+/';

my $t;

$t += checkCmd( "./check_tcp $host_tcp_http      -p 80 -wt 300 -ct 600",       0, $successOutput );
$t += checkCmd( "./check_tcp $host_tcp_http      -p 81 -wt   0 -ct   0 -to 1", 2 ); # use invalid port for this test
$t += checkCmd( "./check_tcp $host_nonresponsive -p 80 -wt   0 -ct   0 -to 1", 2 );
$t += checkCmd( "./check_tcp $hostname_invalid   -p 80 -wt   0 -ct   0 -to 1", 2 );

exit(0) if defined($Test::Harness::VERSION);
exit($tests - $t);