
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

    print service_dict

    dst_port = None
    state = INIT

    try:
        cnct = db.Connection(host = '172.18.203.220',
                             port = 3306,
                             user = 'root',
                             passwd = 'mng1',
                             database = 'db')
        
        for line in sys.stdin:
            line = line.rstrip('\n')

            match = re.match(r' *Arrival Time: (.*)', line)
            if match:
                frame_arrival_time = match.group(1)

            match = re.match(r'Internet Protocol Version 4, Src: ([0-9.]+) \([^)]+\), Dst: ([0-9.]+)', line)
            if match:
                src_ip = match.group(1)
                dst_ip = match.group(2)

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
                src = "%s:%s (%s)" % (src_ip,
                                      src_port,
                                      service_dict.get(src_port, 'unknown'))
                dst = "%s:%s (%s)" % (dst_ip,
                                      dst_port,
                                      service_dict.get(dst_port, 'unknown'))
                print "Frame arrival at %s" % frame_arrival_time
                print "Src %s" % src
                print "Dst %s" % dst
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

            dbhandler = cnct.cursor()
            dbhandler.execute("INSERT INTO 'nj_njrecord' (event_id, source, dest, time_stamp, detail) VALUES (%s, %s, %s, %s, %s)" %
                              ("Event", src, dst, frame_arrival_time, blob))
            cnct.commit()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
