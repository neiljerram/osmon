for r in NJRecord.objects.all():
    modified = False
    if '127.0.0.1' in r.source:
        r.source = r.source.replace('127.0.0.1', '172.18.203.95')
        modified = True
    if '127.0.0.1' in r.dest:
        r.dest = r.dest.replace('127.0.0.1', '172.18.203.95')
        modified = True
    if modified:
        r.save()
