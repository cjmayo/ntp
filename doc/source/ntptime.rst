``ntptime`` - read and set kernel time variables
================================================
.. program:: ntptime

Synopsis
--------

``ntptime [ -chr ] [ -e est_error ] [ -f frequency ] [ -m max_error ] [ -o offset ] [ -s status ] [ -t time_constant]``

Description
-----------

This program is useful only with special kernels described in the
:doc:`A Kernel Model for Precision Timekeeping
<kern>` page. It reads and displays
time-related kernel variables using the ``ntp_gettime()`` system call. A
similar display can be obtained using the ``ntpdc`` program and
``kerninfo`` command.

Options
-------

.. option:: -c

    Display the execution time of ``ntptime`` itself.

.. option:: -e <est_error>

    Specify estimated error, in microseconds.

.. option:: -f <frequency>

    Specify frequency offset, in parts per million.

.. option:: -h

    Display help information.

.. option:: -m <max_error>

    Specify max possible errors, in microseconds.

.. option:: -o <offset>

    Specify clock offset, in microseconds.

.. option:: -r

    Display Unix and NTP times in raw format.

.. option:: -s <status>

    Specify clock status. Better know what you are doing.

.. option:: -t <time_constant>

    Specify time constant, an integer in the range 0-10.
