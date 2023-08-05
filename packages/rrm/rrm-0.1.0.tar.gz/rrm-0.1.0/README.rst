.. image:: https://img.shields.io/pypi/v/rrm?style=flat-square
   :target: https://pypi.org/project/rrm/
   :alt: PyPI

.. image:: https://img.shields.io/pypi/l/rrm?style=flat-square
   :target: https://gitlab.com/szs/rrm/-/raw/master/LICENSE
   :alt: PyPI - License

.. image:: https://img.shields.io/pypi/pyversions/rrm?style=flat-square
   :target: https://python.org
   :alt: PyPI - Python Version

rrm
===

Really, relentlessly and repeatedly remove files and all of their copies.

Installation
============

The installation is straight forward. You can install the package via ``pip``, ``pipenv``, ``poetry``
and alike or by downloading the source from the gitlab repository.

From pypi.org (recommended)
---------------------------

Install by typing

.. code-block:: shell

                pip install rrm

or

.. code-block:: shell

                pip install --user rrm

if you do not have root access.

From gitlab.com
---------------

To get the latest features or contribute to the development, you can clone the whole project using
`git <https://git-scm.com/>`_:

.. code-block:: shell

                git clone https://gitlab.com/szs/rrm.git

Usage
=====

Delete files
------------

To delete files and add information about them to a local database, type

.. code-block:: shell

                rrm a_file.txt "another file.log"

Find exact copies of deleted files and delete them (not implemented yet)
------------------------------------------------------------------------

To search a directory for files which have been deleted (and appended to the database)
by to command above, type

.. code-block:: shell

                rrm some_directory_with_obsolete_copies

Documentation
=============

Please (for now) refer to `rrm --help` for documentation::

  usage: rrm [-h] [-m [DIR]] [-d DB] [-r] [-i] [-I] [-n] [-H HASH] [-l] [-V] [-q] [-v] [-D]
           PATH [PATH ...]

  Really, relentlessly and repeatedly remove files and all of their copies.

  positional arguments:
    PATH                  each PATH is checked whether it is a regular file or a directory. If it is
                          a regular file it will be deleted or moved to DIR (see -m option), unless
                          -n is used, and added the the database. If it is a directory, the
                          directory is scanned for matches to the files in the database (not
                          implemented yet). Note that there is a huge difference between
                          'some_directory/' and 'some_directory/*'!!

  optional arguments:
    -h, --help            show this help message and exit
    -m [DIR], --move [DIR]
                          move to a directory instead of deleting the files permanently. If DIR is
                          not set (but the option is used), $HOME/.config/rrm/deleted_files/ is
                          used. The directory will be created if
    -d DB, --db-file DB   the name of the database file. If DB does not exist, it will be created,
                          otherwise rrm will append to the file. If DB is a directory, rrm will look
                          for 'DB/.rrmdb.csv' and create the file if it does not exist. If this
                          option is omitted, rrm will use (and create if inexistent)
                          $HOME/.config/rrm/rrmdb.csv (default: $HOME/.config/rrm/rrmdb.csv)
    -r, --recursive       check for files to be deleted recursively. (not implemented yet) (default:
                          False)
    -i, --interactive     gather the files to be deleted, display them and ask once to delete all of
                          them.The files are only added to the database if the deletion is confirmed
                          (default: False)
    -I, --very-interactive
                          gather the files to be deleted, display them and ask for every file before
                          deleting it.The files are only added to the database if the deletion is
                          confirmed (default: False)
    -n, --no-action       gather the files to be processed, and only add them to the database
                          without actually deleting or moving them. (default: False)
    -H HASH, --hash-algorithm HASH
                          which hash algorithm to use. Currently supported are: sha1, sha224,
                          sha256, sha384, sha512, blake2b, blake2s, md5, sha3_224, sha3_256,
                          sha3_384, sha3_512, shake_128, shake_256 (default: sha1)
    -l, --follow-symlinks
                          whether to follow symlinks (default: False)
    -V, --version         show the version of this software
    -q, --quiet           switch off text output except for error messages. This will overwrite -v.
                          (default: False)
    -v, --verbose         more verbose text output (default: False)
    -D, --debug           switch on debug mode. This will show a lot of debugging information.
                          (default: False)



TODOs
=====

Project
-------

* proper documentation
* automated tests and CI

Basic features
--------------

* process directories (i.e., look for file that match previously deleted files
* process files in subdirectories (option `-r`)

Enhancements
------------

* add timestamps (UNIX epoch time) to the database entries,
  option to delete older than `x` or deleted before `y`
* add check for user id
* use sqlite instead of csv files for the databases, save hashes as integers
* maintenance of database files: Listing, splitting, merging

How to Contribute
=================

If you find a bug, want to propose a feature or need help getting this package to work,
please don't hesitate to file an `issue <https://gitlab.com/szs/rrm/-/issues>`_ or write
an email.

Merge requests are also much appreciated!

Project links
=============

* `Repository <https://gitlab.com/szs/rrm>`_
* `Documentation <https://rrm.readthedocs.io/en/latest/>`_ (not done yet)
* `pypi page <https://pypi.org/project/rrm/>`_
