#! /usr/bin/perl -w -I ..
#
# Process Tests via check_procs
#
# $Id: check_procs.t,v 1.3 2005/07/25 01:47:15 illumino Exp $
#

use strict;
use Test;
use NPTest;

use vars qw($tests);
BEGIN {$tests = 10; plan tests => $tests}

my $t;

$t += checkCmd( "./check_procs -w 100000 -c   100000",      0, '/^PROCS OK: [0-9]+ process(es)?$/' );
$t += checkCmd( "./check_procs -w 100000 -c   100000 -s Z", 0, '/^PROCS OK: [0-9]+ process(es)? with /' );
$t += checkCmd( "./check_procs -w      0 -c 10000000",      1, '/^PROCS WARNING: [0-9]+ process(es)?$/' );
$t += checkCmd( "./check_procs -w 0      -c        0",      2, '/^PROCS CRITICAL: [0-9]+ process(es)?$/' );
$t += checkCmd( "./check_procs -w 0      -c        0 -s S", 2, '/^PROCS CRITICAL: [0-9]+ process(es)? with /' );

exit(0) if defined($Test::Harness::VERSION);
exit($tests - $t);
