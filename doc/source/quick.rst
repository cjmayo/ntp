Quick Start
===========

For the rank amateur the sheer volume of the documentation collection
must be intimidating. However, it doesn't take much to fly the ``ntpd``
daemon with a simple configuration where a workstation needs to
synchronize to some server elsewhere in the Internet. The first thing is
to build the distribution for the particular workstation and install in
the usual place. The :doc:`Building and
Installing the Distribution <build>` page
describes how to do this.

While it is possible that certain configurations do not need a
configuration file, most do. The file, called by default
``/etc/ntp.conf``, need only contain one command specifying a remote
server, for instance

``server foo.bar.com``

Choosing an appropriate remote server is somewhat of a black art, but a
suboptimal choice is seldom a problem. The simplest and best is to use
the Server Pool Scheme on the :doc:`Automatic
Server Discovery <discover>` page. There are
about two dozen public time servers operated by the `National Institutes
of Science and Technology
(NIST) <http://tf.nist.gov/tf-cgi/servers.cgi>`__, `US Naval Observatory
(USNO) <http://tycho.usno.navy.mil/ntp.html>`__, `Canadian National
Research Council
(NRC) <http://www.nrc-cnrc.gc.ca/eng/services/time/network_time.html>`__
and many others available on the Internet. Lists of public primary and
secondary NTP servers maintained on the `Public NTP Time
Servers <http://support.ntp.org/Servers/WebHome>`__ page, which is
updated frequently. The lists are sorted by country and, in the case of
the US, by state. Usually, the best choice is the nearest in
geographical terms, but the terms of engagement specified in each list
entry should be carefully respected.

During operation ``ntpd`` measures and corrects for incidental clock
frequency error and occasionally writes the current value to a file
specified by the

``driftfile /etc/ntp.drift``

configuration command. If ``ntpd`` is stopped and restarted, it
initializes the frequency from this file and avoids the potentially
lengthy interval to relearn the correction.

That's all there is to it, unless some problem in network connectivity
or local operating system configuration occurs. The most common problem
is some firewall between the workstation and server. System
administrators should understand NTP uses UDP port 123 as both the
source and destination port and that NTP does not involve any operating
system interaction other than to set the system clock. While almost all
modern Unix systems have included NTP and UDP port 123 defined in the
services file, this should be checked if ``ntpd`` fails to come up at
all.

The best way to confirm NTP is working is using the
:doc:`ntpq <ntpq>`
utility, although the :doc:`ntpdc
<ntpdc>` utility may be useful in extreme
cases. See the documentation pages for further information. Don't forget
to check for :doc:`system log messages
<msyslog>`. In the most extreme cases the
``-d`` option on the ``ntpd`` command line results in a blow-by-blow
trace of the daemon operations. While the trace output can be cryptic,
to say the least, it gives a general idea of what the program is doing
and, in particular, details the arriving and departing packets and any
errors found.
