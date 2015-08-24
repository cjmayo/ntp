``ntpdsim`` - Network Time Protocol (NTP) simulator
===================================================
.. program:: ntpdsim

.. _ntpdsim-synop:

Synopsis
-------------------------------------

``ntpdsim [ -B bdly ] [ -C snse ] [ -O clk_time ] [ -S sim_time ] [ -T ferr ] [ -W fsne ] [ -Y ndly ] [ -X pdly ]``

.. _ntpdsim-descr:

Description
----------------------------------------

The ``ntpdsim`` program is an adaptation of the ``ntpd`` operating
system daemon. The program operates as a discrete time simulator using
specified systematic and random driving sources. It includes all the
mitigation and discipline algorithms of the actual daemon, but with the
packet I/O and system clock algorithms driven by simulation. Most
functions of the real ``ntpd`` remain intact, including the monitoring,
statistics recording, trace and host name resolution features. Further
information on the simulator is on the `NTP Discrete Event
Simulator <http://www.eecis.udel.edu/%7emills/ntpsim.html>`__ page.

The simulator is most useful to study NTP behavior in response to time
and/or frequency transients under specific conditions of network jitter
and oscillator wander. For this purpose the daemon can be driven by
pseudorandom jitter and wander sample sequences characteristic of real
networks and oscillators. The jitter generator produces samples from a
Poisson distribution, while the wander generator produces samples from a
Guassian distribution.

The easiest way to use this program is to create a ``ntpstats``
directory, configuration file ``ntp.conf`` and frequency file
``ntp.drift`` and test shell ``test.sh`` in the base directory. The
``ntp.drift`` file and ``ntpstats`` directory can be empty to start. The
``test.sh`` script can contain something like

::

    rm ./ntpstats/*
    ntpdsim -O 0.1 -C .001 -T 400 -W 1 -c ./ntp.conf,

which starts the simulator with a time offset 100 ms, network jitter 1
ms, frequency offset 400 PPM and oscillator wander 1 PPM/s. These
parameters represent typical conditions with modern workstations on a
Ethernet LAN. The ntp.conf file should contain something like

::

    disable kernel
    server pogo
    driftfile ./ntp.drift
    statsdir ./ntpstats/
    filegen loopstats type day enable
    filegen peerstats type day enable

.. _ntpdsim-cmd:

Command Line Options
-----------------------------------------------

Note: The NTP development team is moving to the use of a syntax-directed
configuration file design. When complete these options will be replaced
by a :doc:`new one
<ntpdsim\_new>`. Most of the ``ntpd`` command
line options apply also to ``ntpdsim``. In addition, the following
command line options apply to ``ntpdsim.``

.. option:: -B <bdly>

    Specify beep delay (3600) s.

.. option:: -C <snse>

    Specify network jitter parameter (0) s.

.. option:: -O <clk_time>

    Specify initial time offset (0) s.

.. option:: -S <sim_time>

    Specify simulation duration (86400) s.

.. option:: -T <ferr>

    Specify initial frequency offset (0) PPM.

.. option:: -W <fnse>

    Specify oscillator wander parameter (0) PPM/s.

.. option:: -Y <ndly>

    Specify network propagation delay (.001) s.

.. option:: -Z <pdly>

    Specify server processing delay (.001) s.

.. _ntpdsim-files:

Files
----------------------------------

| ``/etc/ntp.conf`` - the default name of the configuration file
|  ``/etc/ntp.drift`` - the default name of the drift file
|  ``/etc/ntp.keys`` - the default name of the key file
