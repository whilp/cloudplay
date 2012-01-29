# `cloudplay` -- play the cloud

`cloudplay` lets you stream music from your favorite cloud service using your
favorite music player. 

Install it:

    $ pip install cloudplay

Shuffle through [rico](http://soundcloud.com/r_co)'s archive of techno mixes on
[Soundcloud](http://soundcloud.com) with [mpd](http://musicpd.org/):

    $ cd ~/your/mpd/music/directory
    $ cloudplay http://soundcloud.com/r_co
    $ mpc add r_co.xspf
    $ mpc shuffle
    $ mpc crossfade 10
    $ mpc play

Use the power of `xargs` to load up:

    $ xargs -n1 -I@ cloudplay http://soundcloud.com/@
    smokemachinetaipei
    technopodcast
    johnosborn
    colonyparty
    ^D
    $ ls *.xspf | xargs -n1 mpc add
    $ mpc play

Get some help:

    $ cloudplay -h
    Usage: cloudplay [options] user

    Build a playlist of all the tracks published by <user>. <user> must be a URL in
    one of the following formats:

        http://soundcloud.com/<user>
        http://official.fm/users/<user>

    The playlist is written to the file <user>.xspf.


    Options:
      -v VERBOSE, --verbose=VERBOSE
                            logging verbosity
      -h, --help            show this help message and exit

Supported services:

* <http://soundcloud.com>
* <http://official.fm>

Supported playlist formats:

* <http://xspf.org>

Powered by [python](http://python.org), [requests](http://python-requests.org),
[lxml](http://lxml.de) and techno. Provided under the MIT/ISC/X11 license (see
`LICENSE` file for details).
