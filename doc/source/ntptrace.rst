``ntptrace`` - trace a chain of NTP servers back to the primary source
======================================================================
.. program:: ntptrace

Synopsis
--------

``ntptrace [ -n ] [ -m maxhosts ] [ server ]``

Description
-----------

``ntptrace`` is a ``perl`` script that uses the ``ntpq`` utility program
to follow the chain of NTP servers from a given host back to the primary
time source. For ``ntptrace`` to work properly, each of these servers
must implement the NTP Control and Monitoring Protocol specified in
:rfc:`1305` and enable NTP Mode 6 packets.

If given no arguments, ``ntptrace`` starts with ``localhost``. Here is
an example of the output from ``ntptrace``:

::

    % ntptrace
    localhost: stratum 4, offset 0.0019529, synch distance 0.144135
    server2ozo.com: stratum 2, offset 0.0124263, synch distance 0.115784
    usndh.edu: stratum 1, offset 0.0019298, synch distance 0.011993, refid 'WWVB'

On each line, the fields are (left to right): the host name, the host
stratum, the time offset between that host and the local host (as
measured by ``ntptrace``; this is why it is not always zero for
"``localhost``\ "), the host synchronization distance, and (only for
stratum-1 servers) the reference clock ID. All times are given in
seconds. Note that the stratum is the server hop count to the primary
source, while the synchronization distance is the estimated error
relative to the primary source. These terms are precisely defined in
:rfc:`1305`.

Options
-------

.. option:: -m <max_hosts>

    Sets the upper limit of the number of hosts to check (default:
    unlimited).

.. option:: -n

    Turns off the printing of host names; instead, host IP addresses are
    given. This may be useful if a nameserver is down.

Bugs
----

This program makes no attempt to improve accuracy by doing multiple
samples.
