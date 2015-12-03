import pymysql.cursors
import re
import time

connection = pymysql.connect(host='172.18.203.220',
                             port=3306,
                             user='root',
                             password='mng1',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def read_nj_records():
    with connection.cursor() as cursor:
        sql_read = "SELECT * FROM nj_record2"
        # | id | event_id | source | dest | time_stamp | summary | detail
        cursor.execute(sql_read)
        results = cursor.fetchall()
        return results


def dump_to_nt1_table(results):
    with connection.cursor() as cursor:
        sql_insert = "INSERT INTO `Ladders_event` (`event_id`, `detail`, `source`, `dest`, `time_stamp`, `summary`) VALUES (%s, %s, %s, %s, %s, %s)"
        for result in results:
            try:
                if result['dst_ip'] != "":
                    dest = "%s@%s" % (result['dst_name'], result['dst_ip'])
                else:
                    dest = ""
                cursor.execute(sql_insert,
                               (result['event_id'],
                                result['detail'],
                                "%s@%s" % (result['src_name'], result['src_ip']),
                                dest,
                                result['time_stamp'].strftime('%Y-%m-%d %H:%M:%S'),
                                result['summary']))
                connection.commit()
            except:
                print "Failed: ", result


def generate_web_sequence_diagram(results):
    output = ""
    for result in results:
        src_match = re.search(r"\((.+)\)", result['source'])
        if src_match:
            src = src_match.groups()[0]
            dst_match = re.search(r"\((.+)\)", result['dest'])
            if dst_match:
                dst = dst_match.groups()[0]
                seq_string = "%s->%s: %s" % (src,dst,result['summary'])
                print seq_string



r = read_nj_records()
# generate_web_sequence_diagram(r)
dump_to_nt1_table(r)