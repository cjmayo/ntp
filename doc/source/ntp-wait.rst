``ntp-wait`` - waits until ntpd is in synchronized state
========================================================
.. program:: ntp-wait

Synopsis
--------

``ntp-wait [ -v ] [ -n tries ] [ -s seconds ]``

Description
-----------

The ``ntp-wait`` program blocks until ntpd is in synchronized state.
This can be useful at boot time, to delay the boot sequence until after
"ntpd -g" has set the time.

Command Line Options
--------------------

.. option:: -n <tries>

    Number of tries before giving up. The default is 1000.

.. option:: -s <seconds>

    Seconds to sleep between tries. The default is 6 seconds.

.. option:: -v

    Be verbose.
