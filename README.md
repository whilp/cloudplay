# `cloudplay` -- play the cloud

`cloudplay` lets you stream music from your favorite cloud service using your
favorite music player. If you want to shuffle through
[http://soundcloud.com/r_co](rico)'s archive of techno mixes on
[http://soundcloud.com](Soundcloud) with [http://musicpd.org/](mpd), give this a
spin:

    $ cd ~/your/mpd/music/directory
    $ cloudplay r_co
    $ mpc add r_co.xspf
    $ mpc shuffle
    $ mpc crossfade 10
    $ mpc play

Use the power of `xargs` to load up:

    $ cat | xargs -n1 cloudplay
    smokemachinetaipei
    technopodcast
    johnosborn
    colonyparty
    ^D
    $ ls *.xspf | xargs -n1 mpc add
    $ mpc play

Supported services:

* <http://soundcloud.com>

Supported playlist formats:

* <http://xspf.org>

Powered by [http://python.org](python), [http://python-requests.org](requests),
[http://lxml.de](lxml) and techno.
