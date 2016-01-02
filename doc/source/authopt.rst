Authentication Commands and Options
===================================

Commands and Options
--------------------

Unless noted otherwise, further information about these commands is on
the :doc:`Authentication Support <authentic>` page.

.. _authopt-automax:

.. confval:: automax [<logsec>]

    Specifies the interval between regenerations of the session key list
    used with the Autokey protocol, as a power of 2 in seconds. Note
    that the size of the key list for each association depends on this
    interval and the current poll interval. The default interval is 12
    (about 1.1 hr). For poll intervals above the specified interval, a
    session key list with a single entry will be regenerated for every
    message sent.
    See the :doc:`Autokey Public Key Authentication <autokey>` page
    for further information.

.. _authopt-controlkey:

.. confval:: controlkey <keyid>

    Specifies the key ID for the :doc:`ntpq <ntpq>` utility,
    which uses the standard protocol defined in :rfc:`1305`.
    The ``keyid`` argument is the key ID
    for a :ref:`trusted key <authopt-trustedkey>`, where the value can
    be in the range 1 to 65534, inclusive.

.. _authopt-crypto:

.. confval:: crypto [digest <digest>] [host <name>] [ident <name>] [pw <password>] [randfile <file>]

    This command activates the Autokey public key cryptography and loads
    the required host keys and certificate. If one or more files are
    unspecified, the default names are used. Unless the complete path
    and name of the file are specified, the location of a file is
    relative to the keys directory specified in the ``keysdir``
    configuration command with default ``/usr/local/etc``. See the
    :doc:`Autokey Public Key Authentication  <autokey>` page for further information.
    Following are the options.

    .. confval:: digest <digest>

        Specify the message digest algorithm, with default MD5. If the
        OpenSSL library is installed, ``digest`` can be be any message
        digest algorithm supported by the library. The current
        selections are: ``MD2``, ``MD4``, ``MD5,`` ``MDC2``,
        ``RIPEMD160``, ``SHA`` and ``SHA1``. All participants in an
        Autokey subnet must use the same algorithm. The Autokey message
        digest algorithm is separate and distinct from the symmetric key
        message digest algorithm. Note: If compliance with FIPS 140-2 is
        required, the algorithm must be ether ``SHA`` or ``SHA1``.

    .. confval:: host <name>

        Specify the cryptographic media names for the host, sign and
        certificate files. If this option is not specified, the default
        name is the string returned by the Unix ``gethostname()``
        routine.

        .. note::

          In the latest Autokey version, this option has no effect
          other than to change the cryptographic media file names.

    .. confval:: ident <name>

        Specify the cryptographic media names for the identity scheme
        files. If this option is not specified, the default name is the
        string returned by the Unix ``gethostname()`` routine.

        .. note::

          In the latest Autokey version, this option has no effect
          other than to change the cryptographic media file names.

    .. confval:: pw <password>

        Specifies the password to decrypt files previously encrypted by
        the ``ntp-keygen`` program with the ``-p`` option. If this
        option is not specified, the default password is the string
        returned by the Unix ``gethostname()`` routine.

    .. confval:: randfile <file>

        Specifies the location of the random seed file used by the
        OpenSSL library. The defaults are described on the
        :doc:`ntp-keygen page <keygen>`.

.. _authopt-ident:

.. confval:: ident <group>

    Specifies the group name for ephemeral associations mobilized by
    broadcast and symmetric passive modes. See the
    :doc:`Autokey Public-Key Authentication <autokey>` page
    for further information.

.. _authopt-keys:

.. confval:: keys <path>

    Specifies the complete directory path for the key file containing
    the key IDs, key types and keys used by ``ntpd``, ``ntpq`` and
    ``ntpdc`` when operating with symmetric key cryptography. The format
    of the keyfile is described on the
    :doc:`ntp-keygen page <keygen>`. This is the same operation as
    the ``-k`` command line option. Note that the directory path for
    Autokey cryptographic media is specified by the ``keysdir`` command.

.. _authopt-keysdir:

.. confval:: keysdir <path>

    Specifies the complete directory path for the Autokey cryptographic
    keys, parameters and certificates. The default is
    ``/usr/local/etc/``. Note that the path for the symmetric keys file
    is specified by the ``keys`` command.

.. _authopt-requestkey:

.. confval:: requestkey <keyid>

    Specifies the key ID for the :doc:`ntpdc <ntpdc>` utility program,
    which uses a proprietary protocol specific to this implementation
    of ``ntpd``.
    The ``keyid`` argument is a key ID for a
    :ref:`trusted key <authopt-trustedkey>`,
    in the range 1 to 65534, inclusive.

.. _authopt-revoke:

.. confval:: revoke [<logsec>]

    Specifies the interval between re-randomization of certain
    cryptographic values used by the Autokey scheme, as a power of 2 in
    seconds, with default 17 (36 hr). See the
    :doc:`Autokey Public-Key Authentication <autokey>` page
    for further information.

.. _authopt-trustedkey:

.. confval:: trustedkey [<keyid> | (<lowid> ... <highid>)] [...]

    Specifies the key ID(s) which are trusted for the purposes of
    authenticating peers with symmetric key cryptography. Key IDs used
    to authenticate ``ntpq`` and ``ntpdc`` operations must be listed
    here and additionally be enabled with
    :ref:`controlkey <authopt-controlkey>` and/or
    :ref:`requestkey <authopt-requestkey>`. The authentication
    procedure for time transfer requires that both the local and remote
    NTP servers employ the same key ID and secret for this purpose,
    although different keys IDs may be used with different servers.
    Ranges of trusted key IDs may be specified:
    ``trustedkey (1 ... 19) 1000 (100 ... 199)`` enables the lowest 120
    key IDs which start with the digit 1. The spaces surrounding the
    ellipsis are required when specifying a range.
