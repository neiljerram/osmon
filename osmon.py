
import logging
import re
import subprocess
import sys

logging.basicConfig(filename='osmon.log',level=logging.DEBUG)
LOG = logging

# Dump reading states.
INIT = 1
HTTP = 2
JSON = 3

def main():
    service_dict = {}
    proc = subprocess.Popen(['openstack',
                             'catalog',
                             'list',
                             '--format',
                             'value'], stdout=subprocess.PIPE)
    for line in proc.stdout:
        match = re.match(r'([^ ]+) ', line)
        if match:
            service_name = match.group(1)

        match = re.match(r'  publicURL: http://[^:]*:([^/]*)/', line)
        if match:
            if match.group(1) in service_dict:
                service_dict[match.group(1)] = (service_dict[match.group(1)]
                                                + '/'
                                                + service_name)
            else:
                service_dict[match.group(1)] = service_name

    LOG.info('service_dict is %s', service_dict)

    proc = subprocess.Popen(['hostname',
                             '-I'], stdout=subprocess.PIPE)
    for line in proc.stdout:
        my_ip = line.split(' ')[0]

    LOG.info('my IP is %s', my_ip)

    dst_port = None
    state = INIT

    for line in sys.stdin:
        line = line.rstrip('\n')

        match = re.match(r' *Arrival Time: (.*)', line)
        if match:
            frame_arrival_time = match.group(1)

        match = re.match(r'Internet Protocol Version 4, Src: ([0-9.]+) \([^)]+\), Dst: ([0-9.]+)', line)
        if match:
            src_ip = match.group(1)
            dst_ip = match.group(2)
            if src_ip == '127.0.0.1':
                src_ip = my_ip
            if dst_ip == '127.0.0.1':
                dst_ip = my_ip

        match = re.match(r'Transmission Control Protocol, Src Port: ([0-9]+) \([^)]+\), Dst Port: ([0-9]+)', line)
        if match:
            src_port = match.group(1)
            dst_port = match.group(2)

        if re.match(r'^Hypertext', line):
            state = HTTP
            blob = ''
            continue
        elif re.match(r'^Java', line):
            state = JSON
            continue
        elif re.match(r'^[A-Z]', line):
            state = INIT
            continue

        if state == INIT:
            continue

        if dst_port and not line:
            print "Frame arrival at %s" % frame_arrival_time
            print "Src %s:%s (%s)" % (src_ip,
                                      src_port,
                                      service_dict.get(src_port, 'unknown'))
            print "Dst %s:%s (%s)" % (dst_ip,
                                      dst_port,
                                      service_dict.get(dst_port, 'unknown'))
            print "Blob:\n%s" % blob
            dst_port = None

        if state == HTTP:
            if re.match(r'        ', line):
                continue
            if re.match(r'    \[', line):
                continue
            blob = blob + line + '\n'
            continue

        if state == JSON:
            blob = blob + line + '\n'
            continue

if __name__ == '__main__':
    main()
