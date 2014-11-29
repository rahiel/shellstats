shellstats
==========

Shellstats reads your shell history and shows you the most used
commands. Typical output looks like:

::

       Command              Count      Percentage
     1 ls                   326        17.0%
     2 cd                   254        13.3%
     3 less                 172        8.99%
     4 sudo                 162        8.47%
     5 emacs                159        8.31%
     6 screen               146        7.63%
     7 echo                 103        5.38%
     8 top                  100        5.23%
     9 du                   85         4.44%
    10 grep                 70         3.66%

Installation
------------

Install it with a simple:

::

    $ pip install shellstats

In addition if you want to see a pie chart of the above output, you need
to have matplotlib installed (package 'python-matplotlib' in
Debian/Ubuntu/Fedora).

Usage
-----

::

    Usage: shellstats [OPTIONS]

      Print the most frequently used shell commands.

    Options:
      --n INTEGER          How many commands to show.
      --plot               Plot command usage in pie chart.
      --command TEXT       Most frequent subcommands for command, e.g. sudo, git.
      --history-file PATH  Read shell history from history-file.
      --shell TEXT         Specify shell history format: bash, fish or zsh.
      --help               Show this message and exit.

