The Network Time Protocol (NTP) Distribution
============================================

Note: The NTP Version 4 software contained in this distribution is
available without charge under the conditions set forth in the
:doc:`Copyright Notice
<copyright>`.

.. raw:: html

   <dl>

.. raw:: html

   <dd>

It is very important that readers understand that the NTP document
collection began 25 years ago and remains today a work in progress. It
has evolved as new features were invented and old features retired. It
has been widely copied, cached and morphed to other formats, including
man pages, with varying loss of fidelity. However, these HTML pages are
the ONLY authoritative and definitive reference. Readers should always
use the collection that comes with the distribution they use. A copy of
the online collection at `www.ntp.org <http://www.ntp.org>`__ is
normally included in the most recent snapshot, but might not agree with
an earlier snapshot or release version.

.. raw:: html

   </dd>

.. raw:: html

   </dl>

| This distribution is an implementation of RFC-5905 "Network Time
  Protocol Version 4: Protocol and Algorithms Specification".
|  NTP is widely used to synchronize a computer to Internet time servers
  or other sources, such as a radio or satellite receiver or telephone
  modem service. It can also be used as a server for dependent clients.
  It provides accuracies typically less than a millisecond on LANs and
  up to a few milliseconds on WANs. Typical NTP configurations utilize
  multiple redundant servers and diverse network paths in order to
  achieve high accuracy and reliability.

This distribution includes a simulation framework in which substantially
all the runtime NTP operations and most features can be tested and
evaluated. This has been very useful in exploring in vitro response to
unusual circumstances or over time periods impractical in vivo. Details
are on the :doc:`Network Time Protocol (NTP)
Simulator <ntpdsim>` page.

.. _index-hand:

The Handbook
----------------------------------------

A good deal of tutorial and directive information is available on the
handbook pages. These should be read in conjunction with the command and
option information available on the pages listed on the
:doc:`sitemap
<sitemap>` page.

:doc:`NTP Version 4 Release Notes
<release>`
    Lists recent changes and new features in the current distribution.
:doc:`Association Management
<assoc>`
    Describes how to configure servers and peers and manage the various
    options. Includes automatic server discovery schemes.
:doc:`Automatic Server Discovery Schemes
<discover>`
    Describes automatic server discovery using broadcast, multicast,
    manycast and server pool scheme.
:doc:`Access Control Support
<access>`
    Describes the access control mechanisms that can be used to limit
    client access to various time and management functions.
:doc:`Authentication Support
<authentic>`
    Describes the authentication mechanisms for symmetric-key and
    public-key cryptography.
:doc:`Rate Management
<rate>`
    Describes the principles of rate management to minimize network load
    and defend against DoS attacks.
:doc:`Reference Clock Support
<refclock>`
    Describes the collection of radio clocks used to synchronize primary
    servers.
:doc:`How NTP Works
<warp>`
    Gives an overview of the NTP daemon architecture and how it works.

.. _index-build:

Building and Installing NTP
--------------------------------------------------------

NTP supports Unix, VMS and Windows (2000 and later) systems. The
:doc:`Building and Installing the Distribution
<build>` page details the procedures for
building and installing on a typical system. This distribution includes
drivers for many radio and satellite receivers and telephone modem
services in the US, Canada and Europe. A list of supported drivers is on
the :doc:`Reference Clock Drivers
<refclock>` page. The default build includes
the debugging options and all drivers that run on the target machine;
however, options and drivers can be included or excluded using options
on the :doc:`Configuration Options
<config>` page.

.. _index-prob:

Resolving Problems
----------------------------------------------

Like other things in modern Internet life, NTP problems can be
devilishly intricate. This distribution includes a number of utilities
designed to identify and repair problems using an integrated management
protocol supported by the :doc:`ntpq
<ntpq>` utility program.

The :doc:`NTP Debugging Techniques
<debug>` and
:doc:`Hints and Kinks
<hints>` pages contain useful information for
identifying problems and devising solutions. Additional information on
reference clock driver construction and debugging is in the
:doc:`Debugging Hints for Reference Clock
Drivers <rdebug>` page.

Users are invited to report bugs and offer suggestions via the
:doc:`NTP Bug Reporting Procedures
<bugs>` page.

.. _index-info:

Further Information
-----------------------------------------------

The :doc:`Site Map
<sitemap>` page contains a list of document
collections arranged by topic. The Program Manual Pages collection may
be the best place to start. The :doc:`Command
Index <comdex>` collection contains a list of
all configuration file commands together with a short function
description. A great wealth of additional information is available via
the External Links collection, including a book and numerous background
papers and briefing presentations.

Background information on computer network time synchronization is on
the `Executive Summary - Computer Network Time
Synchronization <http://www.eecis.udel.edu/%7emills/exec.html>`__ page.
Discussion on new features and interoperability with previous NTP
versions is on the :doc:`NTP Version 4 Release
Notes <release>` page. Background information,
bibliography and briefing slides suitable for presentations are on the
`Network Time Synchronization Research
Project <http://www.eecis.udel.edu/%7emills/ntp.html>`__ page.
Additional information is at the NTP web site
`www.ntp.org <http://www.ntp.org>`__.
