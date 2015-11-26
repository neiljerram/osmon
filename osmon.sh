#!/bin/bash

set - `openstack catalog list --format csv | gawk '{ if (match($0, "publicURL: http://[^:]*:([^/]*)/", arr)) { print arr[1]; } }' | sort | uniq`

display_filter_for_port () {
    echo "-d tcp.port==$1,http"
}

capture_filter_for_port() {
    echo "tcp port $1"
}

display_filters=`display_filter_for_port $1`
capture_filters=`capture_filter_for_port $1`
shift

for port in $*; do
    display_filters="$display_filters `display_filter_for_port $port`"
    capture_filters="$capture_filters or `capture_filter_for_port $port`"
done

sudo tshark -i any $display_filters -f "$capture_filters" -V -Y http | python osmon.py
