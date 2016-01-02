Building and Installing the Distribution
========================================

It is not possible in a software distribution such as this to support
every individual computer and operating system with a common executable,
even with the same system but different versions and options. Therefore,
it is necessary to configure, build and install for each system and
version. In almost all cases, these procedures are completely automatic,
The user types ``./configure``, and ``make install`` in that order and
the autoconfigure system does the rest. There are some exceptions, as
noted below and on the :doc:`hints` page.

If available, the OpenSSL library from http://www.openssl.org is used to
support public key cryptography. The library must be built and installed
prior to building NTP. The procedures for doing that are included in the
OpenSSL documentation. The library is found during the normal NTP
configure phase and the interface routines compiled automatically. Only
the ``libcrypto.a`` library file and ``openssl`` header files are
needed. If the library is not available or disabled, this step is not
required.

The :doc:`Build Options <config>` page describes a number of options
that determine whether debug support is included, whether and which
reference clock drivers are included and the locations of the
executables and library files, if not the default. By default debugging
options and all reference clock drivers are included.

.. _build-unix:

Building and Installing for Unix
------------------------------------------------------------

This distribution uses common compilers and tools that come with most
Unix distributions. Not all of these tools exist in the standard
distribution of modern Unix versions (compilers are likely to be an
add-on product). If this is the case, consider using the GNU tools and
``gcc`` compiler included as freeware in some systems. For a successful
build, all of these tools should be accessible via the current path.

The first thing to do is uncompress the distribution and extract the
source tree. In the distribution base directory use the ``./configure``
command to perform an automatic configuration procedure. This command
inspects the hardware and software environment and configures the build
process accordingly. Use the ``make`` command to compile and link the
distribution and the ``install`` command to install the executables by
default in ``/usr/local/bin``.

If your site supports multiple architectures and uses NFS to share
files, you can use a single source tree to build executables for
multiple architectures. While running on a particular architecture,
change to the base directory and create a subdirectory using a command
like ``mkdir A.machine``, which will create an architecture-specific
directory, then change to this directory and mumble ``../configure``.
The remaining steps are the same whether building in the base directory
or in the subdirectory.

.. _build-win:

Building and Installing for Windows
--------------------------------------------------------------

NTP supports Windows 2000 and later. See the `NTP 4.x for Windows
NT <hints/winnt.html>`__ page for directions to compile the sources and
install the executables. A precompiled executable is available.

.. _build-conf:

Configuration
-----------------------------------------

You are now ready to configure the daemon. You will need to create a NTP
configuration file by default in ``/etc/ntp.conf``. Newbies should see
the :doc:`quick` page for orientation. Seasoned veterans can start with
the :doc:`ntpd - Network Time Protocol (NTP) daemon <ntpd>` page
and move on to the specific configuration option pages from there.

.. _build-prob:

If You Have Problems
------------------------------------------------

If you have problems with your hardware and software environment (e.g.
operating system-specific issues), browse the :doc:`hints` pages.
For other problems a tutorial on debugging technique is in the
:doc:`debug` page. A list of important system log messages is on the
:doc:`msyslog` page.

The first line of general assistance is the NTP web site
:ntp_home:`\ ` and the helpful documents resident
there. Requests for assistance of a general nature and of interest to
other timekeepers should be sent to the
NTP newsgroup :newsgroup:`comp.protocols.time.ntp`.

Users are invited to report bugs and offer suggestions via the
:doc:`bugs` page.

.. _build-make:

Additional ``make`` commands
--------------------------------------------------------

:command:`make clean`

    Cleans out object files, programs and temporary files.

:command:`make distclean`

    Does the work of ``clean``, but cleans out all directories in
    preparation for a new distribution release.

:command:`make dist`

    Does the work of ``make distclean``, but constructs compressed tar
    files for distribution. You must have GNU automake to perform this
    function.
