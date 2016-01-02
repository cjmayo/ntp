``tickadj`` - set time-related kernel variables
===============================================
.. program:: tickadj

Synopsis
--------

``tickadj [ -Aqs ] [ -a tickadj ] [ -t tick ]``

Description
-----------

The ``tickadj`` program reads, and optionally modifies, several
timekeeping-related variables in older kernels that do not have support
for precision timekeeping, including HP-UX, SunOS, Ultrix, SGI and
probably others. Those machines provide means to patch the kernel
``/dev/kmem``. Newer machines with kernel time support, including
Solaris, Tru64, FreeBSD and Linux, should NOT use the program, even if
it appears to work, as it will destabilize the kernel time support. Use
the :doc:`ntptime
<ntptime>` program instead.

The particular variables that can be changed with ``tickadj`` include
``tick``, which is the number of microseconds added to the system time
for a clock interrupt, ``tickadj``, which sets the slew rate and
resolution used by the ``adjtime`` system call, and ``dosynctodr``,
which indicates to the kernels on some machines whether they should
internally adjust the system clock to keep it in line with time-of-day
clock or not.

By default, with no arguments, ``tickadj`` reads the variables of
interest in the kernel and displays them. At the same time, it
determines an "optimal" value for the value of the ``tickadj`` variable
if the intent is to run the ``ntpd`` Network Time Protocol (NTP) daemon,
and prints this as well. Since the operation of ``tickadj`` when reading
the kernel mimics the operation of similar parts of the ``ntpd`` program
fairly closely, this can be useful when debugging problems with
``ntpd``.

Note that ``tickadj`` should be run with some caution when being used
for the first time on different types of machines. The operations which
``tickadj`` tries to perform are not guaranteed to work on all Unix
machines and may in rare cases cause the kernel to crash.

Command Line Options
--------------------

.. option:: -a <tickadj>

    Set the kernel variable ``tickadj`` to the value
    *``tickadj specified.``*

.. option:: -A

    Set the kernel variable ``tickadj`` to an internally computed
    "optimal" value.

.. option:: -t <tick>

    Set the kernel variable ``tick`` to the value *``tick``* specified.

.. option:: -s

    Set the kernel variable ``dosynctodr`` to zero, which disables the
    hardware time-of-year clock, a prerequisite for running the ``ntpd``
    daemon under SunOS 4.x.

.. option:: -q

    Normally, ``tickadj`` is quite verbose about what it is doing. The
    ``-q`` flag tells it to shut up about everything except errors.

Files
-----

``/vmunix /unix /dev/kmem``

Bugs
----

Fiddling with kernel variables at run time as a part of ordinary
operations is a hideous practice which is only necessary to make up for
deficiencies in the implementation of ``adjtime`` in many kernels and/or
brokenness of the system clock in some vendors' kernels. It would be
much better if the kernels were fixed and the ``tickadj`` program went
away.
