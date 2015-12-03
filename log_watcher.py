import pymysql.cursors
import re
import time
import uuid

connection = pymysql.connect(host='172.18.203.220',
                             port=3306,
                             user='root',
                             password='mng1',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def watch_logfile(logfile):
    logfile.seek(0,2)
    while True:
        line = logfile.readline()
        if not line:
            time.sleep(0.1)
            continue
        info = {}
        # Some logs have PIDs
        match1 = re.search(r"([0-9\-]+) ([0-9.:]+) (\d+) (\w+) ([\w.]+) \[([\w\d\s-]+)\] (.*)", line)
        # Some don't
        match2 = re.search(r"([0-9\-]+) ([0-9.:]+) (\w+) ([\w.]+) \[([\w\d\s-]+)\](.*)", line)
        if match1:
            info = {
                'date': match1.groups()[0],
                'time': match1.groups()[1],
                'pid': match1.groups()[2],
                'level': match1.groups()[3],
                'source': match1.groups()[4],
                'req': match1.groups()[5],
                'message': match1.groups()[6].strip(),
            }
        elif match2:
            info = {
                'date': match2.groups()[0],
                'time': match2.groups()[1],
                'level': match2.groups()[2],
                'source': match2.groups()[3],
                'req': match2.groups()[4],
                'message': match2.groups()[5].strip(),
            }
        else:
            print "SKIP!!!", line
            continue

        if (info['level'] == 'ERROR') or (info['level'] == 'WARNING') or (info['level'] == 'INFO'):
            # Build an event for it
            with connection.cursor() as cursor:
                sql_insert = "INSERT INTO `nj_record2` (`event_id`, `detail`, `src_name`, `dst_name`, `time_stamp`, `summary`, `src_ip`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                try:
                    summary = "%s %s: %s" % (info['level'], info['source'], info['message'])
                    detail = "%s" % info['message']
                    id = "%s" % uuid.uuid4()
                    date = "%s %s" % (info['date'], info['time'])
                    cursor.execute(sql_insert, (id, detail, "nova-nova_legacy", "", date, summary, "172.18.203.95"))

                    connection.commit()
                except:
                    print "Failed: ", info
                    raise

watch_logfile(open("/opt/stack/logs/n-api.log", "r"))