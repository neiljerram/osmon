# Usage

## Capture of HTTP packets to and from OpenStack services

Run `./osmon.sh > capture.txt` on an OpenStack node.

## Grabbing interesting events from OpenStack log files

`md4.py` does the DB -> DB translation (and also had the prototype
websequencediagram code, but the version at
`https://github.com/neiljerram/StackLadder/blob/master/Ladders/views.py` is
probably better).

`log_watcher.py` is self-explanatory.
