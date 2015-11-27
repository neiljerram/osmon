
import re
import uuid

months = {
    'Jan':'01',
    'Feb':'02',
    'Mar':'03',
    'Apr':'04',
    'May':'05',
    'Jun':'06',
    'Jul':'07',
    'Aug':'08',
    'Sep':'09',
    'Oct':'10',
    'Nov':'11',
    'Dec':'12',
}

def conv_time(s):
    m = re.match(r'([A-Za-z]+) ([0-9]+), ([0-9]+) ([0-9:.]+[0-9][0-9][0-9][0-9][0-9][0-9]).*', s)
    return '%s-%s-%02d %s+0000' % (m.group(3),
                                   months[m.group(1)],
                                   int(m.group(2)),
                                   m.group(4))

time_stamp = 'Nov 26, 2015 21:19:44.581903000 UTC'
source = '127.0.0.1:49201 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/os-availability-zone HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

time_stamp = 'Nov 26, 2015 21:19:44.612974000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49201 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 338
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-63d3430d-4255-4fd3-b8de-d0bc0685a697
    Date: Thu, 26 Nov 2015 21:19:44 GMT
    Connection: keep-alive

    Object
        Member Key: "availabilityZoneInfo"
            Array
                Object
                    Member Key: "zoneState"
                        Object
                            Member Key: "available"
                                True value
                    Member Key: "hosts"
                        Null value
                    Member Key: "zoneName"
                        String value: calico-vm18
                Object
                    Member Key: "zoneState"
                        Object
                            Member Key: "available"
                                True value
                    Member Key: "hosts"
                        Null value
                    Member Key: "zoneName"
                        String value: calico-vm17
                Object
                    Member Key: "zoneState"
                        Object
                            Member Key: "available"
                                True value
                    Member Key: "hosts"
                        Null value
                    Member Key: "zoneName"
                        String value: calico-vm19
                Object
                    Member Key: "zoneState"
                        Object
                            Member Key: "available"
                                True value
                    Member Key: "hosts"
                        Null value
                    Member Key: "zoneName"
                        String value: calico-vm23
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.621359000 UTC'
source = '127.0.0.1:49202 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/flavors/detail HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.637927000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49202 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 2089
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-6614f1bf-39a4-4612-87d0-b1631aea6fdd
    Date: Thu, 26 Nov 2015 21:19:44 GMT
    Connection: keep-alive

    Object
        Member Key: "flavors"
            Array
                Object
                    Member Key: "name"
                        String value: m1.tiny
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 512
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 1
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 1
                    Member Key: "id"
                        String value: 1
                Object
                    Member Key: "name"
                        String value: m1.small
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/2
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/2
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 2048
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 1
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 20
                    Member Key: "id"
                        String value: 2
                Object
                    Member Key: "name"
                        String value: m1.medium
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/3
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/3
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 4096
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 2
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 40
                    Member Key: "id"
                        String value: 3
                Object
                    Member Key: "name"
                        String value: m1.large
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/4
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/4
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 8192
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 4
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 80
                    Member Key: "id"
                        String value: 4
                Object
                    Member Key: "name"
                        String value: m1.xlarge
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/5
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/5
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 16384
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 8
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 160
                    Member Key: "id"
                        String value: 5
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.723859000 UTC'
source = '127.0.0.1:48241 (unknown)'
dest = '127.0.0.1:8776 (cinderv2/cinder)'
detail = """    GET /v2/410bd97d893c45c88ed7709cf936b673/os-volume-transfer/detail?bootable=1&status=available HTTP/1.1
    Host: calico-vm18:8776
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-cinderclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.733420000 UTC'
source = '127.0.0.1:8776 (cinderv2/cinder)'
dest = '127.0.0.1:48241 (unknown)'
detail = """    HTTP/1.1 200 OK
    X-Compute-Request-Id: req-a4d80fb0-9ecf-4009-b316-bcceb967722f
    Content-Type: application/json
    Content-Length: 17
    X-Openstack-Request-Id: req-a4d80fb0-9ecf-4009-b316-bcceb967722f
    Date: Thu, 26 Nov 2015 21:19:44 GMT
    Connection: keep-alive

    Object
        Member Key: "transfers"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.735712000 UTC'
source = '127.0.0.1:48242 (unknown)'
dest = '127.0.0.1:8776 (cinderv2/cinder)'
detail = """    GET /v2/410bd97d893c45c88ed7709cf936b673/volumes/detail?bootable=1&status=available HTTP/1.1
    Host: calico-vm18:8776
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-cinderclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.784162000 UTC'
source = '127.0.0.1:8776 (cinderv2/cinder)'
dest = '127.0.0.1:48242 (unknown)'
detail = """    HTTP/1.1 200 OK
    X-Compute-Request-Id: req-40c55126-e426-4b4e-8484-3b43b410c1c1
    Content-Type: application/json
    Content-Length: 15
    X-Openstack-Request-Id: req-40c55126-e426-4b4e-8484-3b43b410c1c1
    Date: Thu, 26 Nov 2015 21:19:44 GMT
    Connection: keep-alive

    Object
        Member Key: "volumes"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.786581000 UTC'
source = '127.0.0.1:48243 (unknown)'
dest = '127.0.0.1:8776 (cinderv2/cinder)'
detail = """    GET /v2/410bd97d893c45c88ed7709cf936b673/snapshots/detail?status=available HTTP/1.1
    Host: calico-vm18:8776
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-cinderclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.811336000 UTC'
source = '127.0.0.1:8776 (cinderv2/cinder)'
dest = '127.0.0.1:48243 (unknown)'
detail = """    HTTP/1.1 200 OK
    X-Compute-Request-Id: req-a61bf2da-31a9-483f-bfa0-199c7127a555
    Content-Type: application/json
    Content-Length: 17
    X-Openstack-Request-Id: req-a61bf2da-31a9-483f-bfa0-199c7127a555
    Date: Thu, 26 Nov 2015 21:19:44 GMT
    Connection: keep-alive

    Object
        Member Key: "snapshots"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.814594000 UTC'
source = '127.0.0.1:49209 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/extensions HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.846273000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49209 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 21496
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-5352e1a2-7b98-4fa0-bb06-55b0d6aa40c5
    Date: Thu, 26 Nov 2015 21:19:44 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: Multinic
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: NMN
                    Member Key: "description"
                        String value: Multiple network support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: DiskConfig
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-DCF
                    Member Key: "description"
                        String value: Disk Management Extension.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedAvailabilityZone
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-AZ
                    Member Key: "description"
                        String value: Extended Availability Zone support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ImageSize
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IMG-SIZE
                    Member Key: "description"
                        String value: Adds image size to image listings.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIps
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIpsMac
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS-MAC
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedServerAttributes
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-SRV-ATTR
                    Member Key: "description"
                        String value: Extended Server Attributes support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedStatus
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-STS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorDisabled
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-DISABLED
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorExtraData
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-EXT-DATA
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: SchedulerHints
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SCH-HNT
                    Member Key: "description"
                        String value: Pass arbitrary key/value pairs to the scheduler.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ServerUsage
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SRV-USG
                    Member Key: "description"
                        String value: Adds launched_at and terminated_at on Servers.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AccessIPs
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-access-ips
                    Member Key: "description"
                        String value: Access IPs support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AdminActions
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-admin-actions
                    Member Key: "description"
                        String value: Enable admin-only server actions
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.865562000 UTC'
source = '127.0.0.1:49210 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/os-keypairs HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.873213000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49210 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 525
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-c6915fdd-1dcf-488f-9782-a0652386a89c
    Date: Thu, 26 Nov 2015 21:19:44 GMT
    Connection: keep-alive

    Object
        Member Key: "keypairs"
            Array
                Object
                    Member Key: "keypair"
                        Object
                            Member Key: "public_key"
                                [truncated] String value: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCl6koJM/fTHwoMx2zCT1WoxXPZprPpegSgbvRANeapbD98ANVpOhNwFJWFfUe3FZKhdfQJ8ZfjiiHX1nj5afAkIsPCwWdrMMJy02VhAwyHNlVlIeAkRzogQbT9J/TndFONNkpZXOGbzWYNPHYv1AONOqErllFpK5HsG+62bk/cj7X3l
                            Member Key: "name"
                                String value: test
                            Member Key: "fingerprint"
                                String value: af:e5:7c:21:29:d0:7c:e7:09:3b:41:6e:3c:ca:75:aa
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.875837000 UTC'
source = '127.0.0.1:52529 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/extensions.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.878930000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52529 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 4074
    X-Openstack-Request-Id: req-f12f7eea-f867-492f-895b-499e5a230dcd
    Date: Thu, 26 Nov 2015 21:19:44 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "alias"
                        String value: dns-integration
                    Member Key: "updated"
                        String value: 2015-08-15T18:00:00-00:00
                    Member Key: "name"
                        String value: DNS Integration
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides integration with internal DNS.
                Object
                    Member Key: "alias"
                        String value: ext-gw-mode
                    Member Key: "updated"
                        String value: 2013-03-28T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Configurable external gateway mode
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extension of the router abstraction for specifying whether SNAT should occur on the external gateway
                Object
                    Member Key: "alias"
                        String value: binding
                    Member Key: "updated"
                        String value: 2014-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Binding
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose port bindings of a virtual port to external application
                Object
                    Member Key: "alias"
                        String value: agent
                    Member Key: "updated"
                        String value: 2013-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: agent
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The agent management extension.
                Object
                    Member Key: "alias"
                        String value: subnet_allocation
                    Member Key: "updated"
                        String value: 2015-03-30T10:00:00-00:00
                    Member Key: "name"
                        String value: Subnet Allocation
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables allocation of subnets from a subnet pool
                Object
                    Member Key: "alias"
                        String value: l3_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: L3 Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule routers among l3 agents
                Object
                    Member Key: "alias"
                        String value: external-net
                    Member Key: "updated"
                        String value: 2013-01-14T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron external network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Adds external network attribute to network resource.
                Object
                    Member Key: "alias"
                        String value: flavors
                    Member Key: "updated"
                        String value: 2014-07-06T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Service Flavors
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Service specification for advanced services
                Object
                    Member Key: "alias"
                        String value: net-mtu
                    Member Key: "updated"
                        String value: 2015-03-25T10:00:00-00:00
                    Member Key: "name"
                        String value: Network MTU
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides MTU attribute for a network resource.
                Object
                    Member Key: "alias"
                        String value: quotas
                    Member Key: "updated"
                        String value: 2012-07-29T10:00:00-00:00
                    Member Key: "name"
                        String value: Quota management support
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose functions for quotas management per tenant
                Object
                    Member Key: "alias"
                        String value: l3-ha
                    Member Key: "updated"
                        String value: 2014-04-26T00:00:00-00:00
                    Member Key: "name"
                        String value: HA Router extension
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Add HA capability to routers.
                Object
                    Member Key: "alias"
                        String value: provider
                    Member Key: "updated"
                        String value: 2012-09-07T10:00:00-00:00
                    Member Key: "name"
                        String value: Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to physical networks
                Object
                    Member Key: "alias"
                        String value: multi-provider
                    Member Key: "updated"
                        String value: 2013-06-27T10:00:00-00:00
                    Member Key: "name"
                        String value: Multi Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to multiple physical networks
                Object
                    Member Key: "alias"
                        String value: extraroute
                    Member Key: "updated"
                        String value: 2013-02-01T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra Route
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra routes configuration for L3 router
                Object
                    Member Key: "alias"
                        String value: router
                    Member Key: "updated"
                        String value: 2012-07-20T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Router abstraction for basic L3 forwarding between L2 Neutron networks and access to external networks via a NAT gateway.
                Object
                    Member Key: "alias"
                        String value: extra_dhcp_opt
                    Member Key: "updated"
                        String value: 2013-03-17T12:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra DHCP opts
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra options configuration for DHCP. For example PXE boot options to DHCP clients can be specified (e.g. tftp-server, server-ip-address, bootfile-name)
                Object
                    Member Key: "alias"
                        String value: security-group
                    Member Key: "updated"
                        String value: 2012-10-05T10:00:00-00:00
                    Member Key: "name"
                        String value: security-group
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The security groups extension.
                Object
                    Member Key: "alias"
                        String value: dhcp_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: DHCP Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule networks among dhcp agents
                Object
                    Member Key: "alias"
                        String value: rbac-policies
                    Member Key: "updated"
                        String value: 2015-06-17T12:15:12-30:00
                    Member Key: "name"
                        String value: RBAC Policies
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Allows creation and modification of policies that control tenant access to resources.
                Object
                    Member Key: "alias"
                        String value: port-security
                    Member Key: "updated"
                        String value: 2012-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Security
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides port security
                Object
                    Member Key: "alias"
                        String value: allowed-address-pairs
                    Member Key: "updated"
                        String value: 2013-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Allowed Address Pairs
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides allowed address pairs
                Object
                    Member Key: "alias"
                        String value: dvr
                    Member Key: "updated"
                        String value: 2014-06-1T10:00:00-00:00
                    Member Key: "name"
                        String value: Distributed Virtual Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables configuration of Distributed Virtual Routers.
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.880727000 UTC'
source = '127.0.0.1:52530 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/security-groups.json?tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.897915000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52530 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1550
    X-Openstack-Request-Id: req-4941b95b-63ed-43c0-8fa3-4348d5962595
    Date: Thu, 26 Nov 2015 21:19:44 GMT
    Connection: keep-alive

    Object
        Member Key: "security_groups"
            Array
                Object
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "description"
                        String value: Default security group
                    Member Key: "id"
                        String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "security_group_rules"
                        Array
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: 991a8e06-dd5e-4024-8773-c4e38e96cdc5
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c116db16-5fdf-4ae1-8c98-41999120f3a1
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c1f4a0f6-db06-4c6b-87a1-47aa837a657a
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: f1bca7e8-17cd-4833-a548-6fbbd8f07c64
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "name"
                        String value: default
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.901687000 UTC'
source = '127.0.0.1:52531 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/networks.json?shared=False&tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.924324000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52531 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 16
    X-Openstack-Request-Id: req-d3ec16d1-1d10-48bb-b2b3-2b68467fda7b
    Date: Thu, 26 Nov 2015 21:19:44 GMT
    Connection: keep-alive

    Object
        Member Key: "networks"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.926370000 UTC'
source = '127.0.0.1:52532 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/subnets.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.953768000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52532 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 961
    X-Openstack-Request-Id: req-9c2cddb4-eb52-426a-b257-5221c6d64ac5
    Date: Thu, 26 Nov 2015 21:19:44 GMT
    Connection: keep-alive

    Object
        Member Key: "subnets"
            Array
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: 10.28.0.1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: 10.28.0.2
                                Member Key: "end"
                                    String value: 10.28.255.254
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 4
                    Member Key: "ipv6_address_mode"
                        Null value
                    Member Key: "cidr"
                        String value: 10.28.0.0/16
                    Member Key: "id"
                        String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                    Member Key: "subnetpool_id"
                        Null value
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: fd5f:5d21:845:1c2e:2::1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: fd5f:5d21:845:1c2e:2::2
                                Member Key: "end"
                                    String value: fd5f:5d21:845:1c2e:2:ffff:ffff:ffff
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 6
                    Member Key: "ipv6_address_mode"
                        String value: dhcpv6-stateful
                    Member Key: "cidr"
                        String value: fd5f:5d21:845:1c2e:2::/80
                    Member Key: "id"
                        String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "subnetpool_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.955947000 UTC'
source = '127.0.0.1:52533 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/networks.json?shared=True HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.983310000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52533 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 454
    X-Openstack-Request-Id: req-2d186fe4-0404-453e-bbc1-412c72709b53
    Date: Thu, 26 Nov 2015 21:19:44 GMT
    Connection: keep-alive

    Object
        Member Key: "networks"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "subnets"
                        Array
                            String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                            String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "name"
                        String value: demo-net
                    Member Key: "provider:physical_network"
                        Null value
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mtu"
                        Number value: 0
                    Member Key: "router:external"
                        False value
                    Member Key: "shared"
                        True value
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "provider:network_type"
                        String value: local
                    Member Key: "id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "provider:segmentation_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:44.985471000 UTC'
source = '127.0.0.1:52534 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/subnets.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:45.016526000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52534 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 961
    X-Openstack-Request-Id: req-da344278-664a-435e-892d-33b669e82b26
    Date: Thu, 26 Nov 2015 21:19:45 GMT
    Connection: keep-alive

    Object
        Member Key: "subnets"
            Array
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: 10.28.0.1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: 10.28.0.2
                                Member Key: "end"
                                    String value: 10.28.255.254
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 4
                    Member Key: "ipv6_address_mode"
                        Null value
                    Member Key: "cidr"
                        String value: 10.28.0.0/16
                    Member Key: "id"
                        String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                    Member Key: "subnetpool_id"
                        Null value
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: fd5f:5d21:845:1c2e:2::1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: fd5f:5d21:845:1c2e:2::2
                                Member Key: "end"
                                    String value: fd5f:5d21:845:1c2e:2:ffff:ffff:ffff
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 6
                    Member Key: "ipv6_address_mode"
                        String value: dhcpv6-stateful
                    Member Key: "cidr"
                        String value: fd5f:5d21:845:1c2e:2::/80
                    Member Key: "id"
                        String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "subnetpool_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:45.065076000 UTC'
source = '127.0.0.1:49217 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/limits HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:45.086763000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49217 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 511
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-06d71339-a2a7-4d74-a88b-ccd7fc40322c
    Date: Thu, 26 Nov 2015 21:19:45 GMT
    Connection: keep-alive

    Object
        Member Key: "limits"
            Object
                Member Key: "rate"
                    Array
                Member Key: "absolute"
                    Object
                        Member Key: "maxServerMeta"
                            Number value: 128
                        Member Key: "maxPersonality"
                            Number value: 5
                        Member Key: "totalServerGroupsUsed"
                            Number value: 0
                        Member Key: "maxImageMeta"
                            Number value: 128
                        Member Key: "maxPersonalitySize"
                            Number value: 10240
                        Member Key: "maxTotalKeypairs"
                            Number value: 100
                        Member Key: "maxSecurityGroupRules"
                            Number value: 20
                        Member Key: "maxServerGroups"
                            Number value: 10
                        Member Key: "totalCoresUsed"
                            Number value: 0
                        Member Key: "totalRAMUsed"
                            Number value: 0
                        Member Key: "totalInstancesUsed"
                            Number value: 0
                        Member Key: "maxSecurityGroups"
                            Number value: 10
                        Member Key: "totalFloatingIpsUsed"
                            Number value: 0
                        Member Key: "maxTotalCores"
                            Number value: 20
                        Member Key: "maxServerGroupMembers"
                            Number value: 10
                        Member Key: "maxTotalFloatingIps"
                            Number value: 10
                        Member Key: "totalSecurityGroupsUsed"
                            Number value: 1
                        Member Key: "maxTotalInstances"
                            Number value: 10
                        Member Key: "maxTotalRAMSize"
                            Number value: 51200
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.512402000 UTC'
source = '127.0.0.1:49224 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/os-availability-zone HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.542692000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49224 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 338
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-e63d7aea-1a6c-4279-b5d1-cdc47859e39a
    Date: Thu, 26 Nov 2015 21:19:52 GMT
    Connection: keep-alive

    Object
        Member Key: "availabilityZoneInfo"
            Array
                Object
                    Member Key: "zoneState"
                        Object
                            Member Key: "available"
                                True value
                    Member Key: "hosts"
                        Null value
                    Member Key: "zoneName"
                        String value: calico-vm18
                Object
                    Member Key: "zoneState"
                        Object
                            Member Key: "available"
                                True value
                    Member Key: "hosts"
                        Null value
                    Member Key: "zoneName"
                        String value: calico-vm17
                Object
                    Member Key: "zoneState"
                        Object
                            Member Key: "available"
                                True value
                    Member Key: "hosts"
                        Null value
                    Member Key: "zoneName"
                        String value: calico-vm19
                Object
                    Member Key: "zoneState"
                        Object
                            Member Key: "available"
                                True value
                    Member Key: "hosts"
                        Null value
                    Member Key: "zoneName"
                        String value: calico-vm23
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.548065000 UTC'
source = '127.0.0.1:49225 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/flavors/detail HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.570363000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49225 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 2089
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-a11c3fc8-6e78-449c-a801-a1d3b23ca16b
    Date: Thu, 26 Nov 2015 21:19:52 GMT
    Connection: keep-alive

    Object
        Member Key: "flavors"
            Array
                Object
                    Member Key: "name"
                        String value: m1.tiny
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 512
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 1
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 1
                    Member Key: "id"
                        String value: 1
                Object
                    Member Key: "name"
                        String value: m1.small
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/2
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/2
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 2048
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 1
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 20
                    Member Key: "id"
                        String value: 2
                Object
                    Member Key: "name"
                        String value: m1.medium
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/3
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/3
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 4096
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 2
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 40
                    Member Key: "id"
                        String value: 3
                Object
                    Member Key: "name"
                        String value: m1.large
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/4
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/4
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 8192
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 4
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 80
                    Member Key: "id"
                        String value: 4
                Object
                    Member Key: "name"
                        String value: m1.xlarge
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/5
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/5
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 16384
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 8
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 160
                    Member Key: "id"
                        String value: 5
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.655258000 UTC'
source = '127.0.0.1:48264 (unknown)'
dest = '127.0.0.1:8776 (cinderv2/cinder)'
detail = """    GET /v2/410bd97d893c45c88ed7709cf936b673/os-volume-transfer/detail?bootable=1&status=available HTTP/1.1
    Host: calico-vm18:8776
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-cinderclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.666318000 UTC'
source = '127.0.0.1:8776 (cinderv2/cinder)'
dest = '127.0.0.1:48264 (unknown)'
detail = """    HTTP/1.1 200 OK
    X-Compute-Request-Id: req-4964fb4c-b84b-4f02-9b5b-e2d5bf616dae
    Content-Type: application/json
    Content-Length: 17
    X-Openstack-Request-Id: req-4964fb4c-b84b-4f02-9b5b-e2d5bf616dae
    Date: Thu, 26 Nov 2015 21:19:52 GMT
    Connection: keep-alive

    Object
        Member Key: "transfers"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.669578000 UTC'
source = '127.0.0.1:48265 (unknown)'
dest = '127.0.0.1:8776 (cinderv2/cinder)'
detail = """    GET /v2/410bd97d893c45c88ed7709cf936b673/volumes/detail?bootable=1&status=available HTTP/1.1
    Host: calico-vm18:8776
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-cinderclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.717233000 UTC'
source = '127.0.0.1:8776 (cinderv2/cinder)'
dest = '127.0.0.1:48265 (unknown)'
detail = """    HTTP/1.1 200 OK
    X-Compute-Request-Id: req-7bc4c36b-4acf-4b7f-8d3b-e524dcd9a70d
    Content-Type: application/json
    Content-Length: 15
    X-Openstack-Request-Id: req-7bc4c36b-4acf-4b7f-8d3b-e524dcd9a70d
    Date: Thu, 26 Nov 2015 21:19:52 GMT
    Connection: keep-alive

    Object
        Member Key: "volumes"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.719597000 UTC'
source = '127.0.0.1:48266 (unknown)'
dest = '127.0.0.1:8776 (cinderv2/cinder)'
detail = """    GET /v2/410bd97d893c45c88ed7709cf936b673/snapshots/detail?status=available HTTP/1.1
    Host: calico-vm18:8776
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-cinderclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.736859000 UTC'
source = '127.0.0.1:8776 (cinderv2/cinder)'
dest = '127.0.0.1:48266 (unknown)'
detail = """    HTTP/1.1 200 OK
    X-Compute-Request-Id: req-1a6bd00a-e1c7-483a-a950-cef40b4a72ae
    Content-Type: application/json
    Content-Length: 17
    X-Openstack-Request-Id: req-1a6bd00a-e1c7-483a-a950-cef40b4a72ae
    Date: Thu, 26 Nov 2015 21:19:52 GMT
    Connection: keep-alive

    Object
        Member Key: "snapshots"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.739958000 UTC'
source = '127.0.0.1:49232 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/extensions HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.782025000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49232 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 21496
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-816a2a63-6092-48ab-8d64-70c94bf4c707
    Date: Thu, 26 Nov 2015 21:19:52 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: Multinic
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: NMN
                    Member Key: "description"
                        String value: Multiple network support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: DiskConfig
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-DCF
                    Member Key: "description"
                        String value: Disk Management Extension.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedAvailabilityZone
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-AZ
                    Member Key: "description"
                        String value: Extended Availability Zone support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ImageSize
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IMG-SIZE
                    Member Key: "description"
                        String value: Adds image size to image listings.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIps
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIpsMac
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS-MAC
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedServerAttributes
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-SRV-ATTR
                    Member Key: "description"
                        String value: Extended Server Attributes support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedStatus
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-STS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorDisabled
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-DISABLED
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorExtraData
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-EXT-DATA
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: SchedulerHints
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SCH-HNT
                    Member Key: "description"
                        String value: Pass arbitrary key/value pairs to the scheduler.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ServerUsage
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SRV-USG
                    Member Key: "description"
                        String value: Adds launched_at and terminated_at on Servers.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AccessIPs
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-access-ips
                    Member Key: "description"
                        String value: Access IPs support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AdminActions
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-admin-actions
                    Member Key: "description"
                        String value: Enable admin-only server actions
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.789381000 UTC'
source = '127.0.0.1:52551 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/extensions.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.793096000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52551 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 4074
    X-Openstack-Request-Id: req-e3e5ef17-f433-40fd-b140-53c46add09a8
    Date: Thu, 26 Nov 2015 21:19:52 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "alias"
                        String value: dns-integration
                    Member Key: "updated"
                        String value: 2015-08-15T18:00:00-00:00
                    Member Key: "name"
                        String value: DNS Integration
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides integration with internal DNS.
                Object
                    Member Key: "alias"
                        String value: ext-gw-mode
                    Member Key: "updated"
                        String value: 2013-03-28T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Configurable external gateway mode
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extension of the router abstraction for specifying whether SNAT should occur on the external gateway
                Object
                    Member Key: "alias"
                        String value: binding
                    Member Key: "updated"
                        String value: 2014-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Binding
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose port bindings of a virtual port to external application
                Object
                    Member Key: "alias"
                        String value: agent
                    Member Key: "updated"
                        String value: 2013-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: agent
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The agent management extension.
                Object
                    Member Key: "alias"
                        String value: subnet_allocation
                    Member Key: "updated"
                        String value: 2015-03-30T10:00:00-00:00
                    Member Key: "name"
                        String value: Subnet Allocation
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables allocation of subnets from a subnet pool
                Object
                    Member Key: "alias"
                        String value: l3_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: L3 Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule routers among l3 agents
                Object
                    Member Key: "alias"
                        String value: external-net
                    Member Key: "updated"
                        String value: 2013-01-14T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron external network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Adds external network attribute to network resource.
                Object
                    Member Key: "alias"
                        String value: flavors
                    Member Key: "updated"
                        String value: 2014-07-06T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Service Flavors
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Service specification for advanced services
                Object
                    Member Key: "alias"
                        String value: net-mtu
                    Member Key: "updated"
                        String value: 2015-03-25T10:00:00-00:00
                    Member Key: "name"
                        String value: Network MTU
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides MTU attribute for a network resource.
                Object
                    Member Key: "alias"
                        String value: quotas
                    Member Key: "updated"
                        String value: 2012-07-29T10:00:00-00:00
                    Member Key: "name"
                        String value: Quota management support
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose functions for quotas management per tenant
                Object
                    Member Key: "alias"
                        String value: l3-ha
                    Member Key: "updated"
                        String value: 2014-04-26T00:00:00-00:00
                    Member Key: "name"
                        String value: HA Router extension
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Add HA capability to routers.
                Object
                    Member Key: "alias"
                        String value: provider
                    Member Key: "updated"
                        String value: 2012-09-07T10:00:00-00:00
                    Member Key: "name"
                        String value: Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to physical networks
                Object
                    Member Key: "alias"
                        String value: multi-provider
                    Member Key: "updated"
                        String value: 2013-06-27T10:00:00-00:00
                    Member Key: "name"
                        String value: Multi Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to multiple physical networks
                Object
                    Member Key: "alias"
                        String value: extraroute
                    Member Key: "updated"
                        String value: 2013-02-01T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra Route
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra routes configuration for L3 router
                Object
                    Member Key: "alias"
                        String value: router
                    Member Key: "updated"
                        String value: 2012-07-20T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Router abstraction for basic L3 forwarding between L2 Neutron networks and access to external networks via a NAT gateway.
                Object
                    Member Key: "alias"
                        String value: extra_dhcp_opt
                    Member Key: "updated"
                        String value: 2013-03-17T12:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra DHCP opts
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra options configuration for DHCP. For example PXE boot options to DHCP clients can be specified (e.g. tftp-server, server-ip-address, bootfile-name)
                Object
                    Member Key: "alias"
                        String value: security-group
                    Member Key: "updated"
                        String value: 2012-10-05T10:00:00-00:00
                    Member Key: "name"
                        String value: security-group
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The security groups extension.
                Object
                    Member Key: "alias"
                        String value: dhcp_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: DHCP Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule networks among dhcp agents
                Object
                    Member Key: "alias"
                        String value: rbac-policies
                    Member Key: "updated"
                        String value: 2015-06-17T12:15:12-30:00
                    Member Key: "name"
                        String value: RBAC Policies
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Allows creation and modification of policies that control tenant access to resources.
                Object
                    Member Key: "alias"
                        String value: port-security
                    Member Key: "updated"
                        String value: 2012-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Security
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides port security
                Object
                    Member Key: "alias"
                        String value: allowed-address-pairs
                    Member Key: "updated"
                        String value: 2013-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Allowed Address Pairs
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides allowed address pairs
                Object
                    Member Key: "alias"
                        String value: dvr
                    Member Key: "updated"
                        String value: 2014-06-1T10:00:00-00:00
                    Member Key: "name"
                        String value: Distributed Virtual Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables configuration of Distributed Virtual Routers.
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.795097000 UTC'
source = '127.0.0.1:49234 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/os-quota-sets/410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.813589000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49234 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 371
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-c9d3a8e8-e4d5-42a7-a637-8f63fd0a5dc7
    Date: Thu, 26 Nov 2015 21:19:52 GMT
    Connection: keep-alive

    Object
        Member Key: "quota_set"
            Object
                Member Key: "injected_file_content_bytes"
                    Number value: 10240
                Member Key: "metadata_items"
                    Number value: 128
                Member Key: "server_group_members"
                    Number value: 10
                Member Key: "server_groups"
                    Number value: 10
                Member Key: "ram"
                    Number value: 51200
                Member Key: "floating_ips"
                    Number value: 10
                Member Key: "key_pairs"
                    Number value: 100
                Member Key: "id"
                    String value: 410bd97d893c45c88ed7709cf936b673
                Member Key: "instances"
                    Number value: 10
                Member Key: "security_group_rules"
                    Number value: 20
                Member Key: "injected_files"
                    Number value: 5
                Member Key: "cores"
                    Number value: 20
                Member Key: "fixed_ips"
                    Number value: -1
                Member Key: "injected_file_path_bytes"
                    Number value: 255
                Member Key: "security_groups"
                    Number value: 10
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:52.816468000 UTC'
source = '127.0.0.1:48270 (unknown)'
dest = '127.0.0.1:8776 (cinderv2/cinder)'
detail = """    GET /v2/410bd97d893c45c88ed7709cf936b673/os-quota-sets/410bd97d893c45c88ed7709cf936b673?usage=False HTTP/1.1
    Host: calico-vm18:8776
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-cinderclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.066524000 UTC'
source = '127.0.0.1:8776 (cinderv2/cinder)'
dest = '127.0.0.1:48270 (unknown)'
detail = """    HTTP/1.1 200 OK
    X-Compute-Request-Id: req-bf03407e-0b57-4a3a-9cde-f7263f3f8e23
    Content-Type: application/json
    Content-Length: 262
    X-Openstack-Request-Id: req-bf03407e-0b57-4a3a-9cde-f7263f3f8e23
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "quota_set"
            Object
                Member Key: "per_volume_gigabytes"
                    Number value: -1
                Member Key: "volumes_lvmdriver-1"
                    Number value: -1
                Member Key: "gigabytes"
                    Number value: 1000
                Member Key: "backup_gigabytes"
                    Number value: 1000
                Member Key: "snapshots"
                    Number value: 10
                Member Key: "gigabytes_lvmdriver-1"
                    Number value: -1
                Member Key: "volumes"
                    Number value: 10
                Member Key: "snapshots_lvmdriver-1"
                    Number value: -1
                Member Key: "backups"
                    Number value: 10
                Member Key: "id"
                    String value: 410bd97d893c45c88ed7709cf936b673
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.069360000 UTC'
source = '127.0.0.1:52558 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/quotas/410bd97d893c45c88ed7709cf936b673.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.073980000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52558 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 171
    X-Openstack-Request-Id: req-0193794c-9603-41c8-ba6f-a37b265e4cfc
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "quota"
            Object
                Member Key: "subnet"
                    Number value: 10
                Member Key: "network"
                    Number value: 10
                Member Key: "floatingip"
                    Number value: 50
                Member Key: "subnetpool"
                    Number value: -1
                Member Key: "security_group_rule"
                    Number value: 100
                Member Key: "security_group"
                    Number value: 10
                Member Key: "router"
                    Number value: 10
                Member Key: "rbac_policy"
                    Number value: -1
                Member Key: "port"
                    Number value: 50
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.076278000 UTC'
source = '127.0.0.1:49241 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/servers/detail?all_tenants=True&tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.121917000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49241 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 15
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-8fd3097f-a7aa-4cd6-86d5-aec30214f55f
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "servers"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.124486000 UTC'
source = '127.0.0.1:52560 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/floatingips.json?tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.130633000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52560 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 19
    X-Openstack-Request-Id: req-3bb8cf1b-6f01-4122-8737-914f87bcf7a0
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "floatingips"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.134407000 UTC'
source = '127.0.0.1:52561 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/ports.json?tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.152870000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52561 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 13
    X-Openstack-Request-Id: req-63f93e6f-4345-477f-889f-11c2d5c3100c
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.154742000 UTC'
source = '127.0.0.1:52562 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/security-groups.json?tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.178712000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52562 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1550
    X-Openstack-Request-Id: req-0f03fb1d-2406-48ec-9866-f47f6d79fc75
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "security_groups"
            Array
                Object
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "description"
                        String value: Default security group
                    Member Key: "id"
                        String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "security_group_rules"
                        Array
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: 991a8e06-dd5e-4024-8773-c4e38e96cdc5
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c116db16-5fdf-4ae1-8c98-41999120f3a1
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c1f4a0f6-db06-4c6b-87a1-47aa837a657a
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: f1bca7e8-17cd-4833-a548-6fbbd8f07c64
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "name"
                        String value: default
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.181040000 UTC'
source = '127.0.0.1:52563 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/networks.json?shared=False HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.205725000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52563 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 16
    X-Openstack-Request-Id: req-8f1e49a5-7740-47f4-93f7-40b9ca2002b2
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "networks"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.208085000 UTC'
source = '127.0.0.1:52564 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/subnets.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.236394000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52564 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 961
    X-Openstack-Request-Id: req-f90d00c2-c763-4588-bba7-4ec6263039e8
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "subnets"
            Array
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: 10.28.0.1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: 10.28.0.2
                                Member Key: "end"
                                    String value: 10.28.255.254
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 4
                    Member Key: "ipv6_address_mode"
                        Null value
                    Member Key: "cidr"
                        String value: 10.28.0.0/16
                    Member Key: "id"
                        String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                    Member Key: "subnetpool_id"
                        Null value
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: fd5f:5d21:845:1c2e:2::1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: fd5f:5d21:845:1c2e:2::2
                                Member Key: "end"
                                    String value: fd5f:5d21:845:1c2e:2:ffff:ffff:ffff
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 6
                    Member Key: "ipv6_address_mode"
                        String value: dhcpv6-stateful
                    Member Key: "cidr"
                        String value: fd5f:5d21:845:1c2e:2::/80
                    Member Key: "id"
                        String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "subnetpool_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.238811000 UTC'
source = '127.0.0.1:52565 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/subnets.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.265768000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52565 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 961
    X-Openstack-Request-Id: req-fe32c2f8-00c6-4a80-82cb-938ba68555a5
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "subnets"
            Array
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: 10.28.0.1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: 10.28.0.2
                                Member Key: "end"
                                    String value: 10.28.255.254
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 4
                    Member Key: "ipv6_address_mode"
                        Null value
                    Member Key: "cidr"
                        String value: 10.28.0.0/16
                    Member Key: "id"
                        String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                    Member Key: "subnetpool_id"
                        Null value
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: fd5f:5d21:845:1c2e:2::1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: fd5f:5d21:845:1c2e:2::2
                                Member Key: "end"
                                    String value: fd5f:5d21:845:1c2e:2:ffff:ffff:ffff
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 6
                    Member Key: "ipv6_address_mode"
                        String value: dhcpv6-stateful
                    Member Key: "cidr"
                        String value: fd5f:5d21:845:1c2e:2::/80
                    Member Key: "id"
                        String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "subnetpool_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.267836000 UTC'
source = '127.0.0.1:52566 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/routers.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.290402000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52566 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 15
    X-Openstack-Request-Id: req-2df23010-7f34-4483-8824-32579ec7110c
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "routers"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.293268000 UTC'
source = '127.0.0.1:48284 (unknown)'
dest = '127.0.0.1:8776 (cinderv2/cinder)'
detail = """    GET /v2/410bd97d893c45c88ed7709cf936b673/os-volume-transfer/detail?project_id=410bd97d893c45c88ed7709cf936b673&all_tenants=1 HTTP/1.1
    Host: calico-vm18:8776
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-cinderclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.301062000 UTC'
source = '127.0.0.1:8776 (cinderv2/cinder)'
dest = '127.0.0.1:48284 (unknown)'
detail = """    HTTP/1.1 200 OK
    X-Compute-Request-Id: req-df983541-8f91-4c8f-9b1f-1ba2f470e8fc
    Content-Type: application/json
    Content-Length: 17
    X-Openstack-Request-Id: req-df983541-8f91-4c8f-9b1f-1ba2f470e8fc
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "transfers"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.302964000 UTC'
source = '127.0.0.1:48285 (unknown)'
dest = '127.0.0.1:8776 (cinderv2/cinder)'
detail = """    GET /v2/410bd97d893c45c88ed7709cf936b673/volumes/detail?all_tenants=1&project_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:8776
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-cinderclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.345106000 UTC'
source = '127.0.0.1:8776 (cinderv2/cinder)'
dest = '127.0.0.1:48285 (unknown)'
detail = """    HTTP/1.1 200 OK
    X-Compute-Request-Id: req-03098066-d4b9-4352-83d4-c8c5b379c821
    Content-Type: application/json
    Content-Length: 15
    X-Openstack-Request-Id: req-03098066-d4b9-4352-83d4-c8c5b379c821
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "volumes"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.347364000 UTC'
source = '127.0.0.1:48286 (unknown)'
dest = '127.0.0.1:8776 (cinderv2/cinder)'
detail = """    GET /v2/410bd97d893c45c88ed7709cf936b673/snapshots/detail?all_tenants=1&project_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:8776
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-cinderclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.363275000 UTC'
source = '127.0.0.1:8776 (cinderv2/cinder)'
dest = '127.0.0.1:48286 (unknown)'
detail = """    HTTP/1.1 200 OK
    X-Compute-Request-Id: req-0c7ab605-b496-452f-b47a-6925dde1d21a
    Content-Type: application/json
    Content-Length: 17
    X-Openstack-Request-Id: req-0c7ab605-b496-452f-b47a-6925dde1d21a
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "snapshots"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.365949000 UTC'
source = '127.0.0.1:49252 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/os-keypairs HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.382607000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49252 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 525
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-21a92c52-add4-4c42-9112-542c49d79ad0
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "keypairs"
            Array
                Object
                    Member Key: "keypair"
                        Object
                            Member Key: "public_key"
                                [truncated] String value: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCl6koJM/fTHwoMx2zCT1WoxXPZprPpegSgbvRANeapbD98ANVpOhNwFJWFfUe3FZKhdfQJ8ZfjiiHX1nj5afAkIsPCwWdrMMJy02VhAwyHNlVlIeAkRzogQbT9J/TndFONNkpZXOGbzWYNPHYv1AONOqErllFpK5HsG+62bk/cj7X3l
                            Member Key: "name"
                                String value: test
                            Member Key: "fingerprint"
                                String value: af:e5:7c:21:29:d0:7c:e7:09:3b:41:6e:3c:ca:75:aa
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.385791000 UTC'
source = '127.0.0.1:52571 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/security-groups.json?tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.401689000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52571 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1550
    X-Openstack-Request-Id: req-84f88afc-396e-419b-9652-786fdc53de32
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "security_groups"
            Array
                Object
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "description"
                        String value: Default security group
                    Member Key: "id"
                        String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "security_group_rules"
                        Array
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: 991a8e06-dd5e-4024-8773-c4e38e96cdc5
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c116db16-5fdf-4ae1-8c98-41999120f3a1
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c1f4a0f6-db06-4c6b-87a1-47aa837a657a
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: f1bca7e8-17cd-4833-a548-6fbbd8f07c64
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "name"
                        String value: default
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.404193000 UTC'
source = '127.0.0.1:52572 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/networks.json?shared=False&tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.429736000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52572 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 16
    X-Openstack-Request-Id: req-ca66b3b1-1927-4eed-a562-eab8db66a97b
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "networks"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.431905000 UTC'
source = '127.0.0.1:52573 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/subnets.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.455102000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52573 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 961
    X-Openstack-Request-Id: req-d8d4bdd8-53cf-451b-8c1f-8494ee638894
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "subnets"
            Array
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: 10.28.0.1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: 10.28.0.2
                                Member Key: "end"
                                    String value: 10.28.255.254
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 4
                    Member Key: "ipv6_address_mode"
                        Null value
                    Member Key: "cidr"
                        String value: 10.28.0.0/16
                    Member Key: "id"
                        String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                    Member Key: "subnetpool_id"
                        Null value
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: fd5f:5d21:845:1c2e:2::1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: fd5f:5d21:845:1c2e:2::2
                                Member Key: "end"
                                    String value: fd5f:5d21:845:1c2e:2:ffff:ffff:ffff
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 6
                    Member Key: "ipv6_address_mode"
                        String value: dhcpv6-stateful
                    Member Key: "cidr"
                        String value: fd5f:5d21:845:1c2e:2::/80
                    Member Key: "id"
                        String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "subnetpool_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.457036000 UTC'
source = '127.0.0.1:52574 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/networks.json?shared=True HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.493592000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52574 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 454
    X-Openstack-Request-Id: req-93bf9803-9c75-4573-aa45-1972bdcab713
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "networks"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "subnets"
                        Array
                            String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                            String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "name"
                        String value: demo-net
                    Member Key: "provider:physical_network"
                        Null value
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mtu"
                        Number value: 0
                    Member Key: "router:external"
                        False value
                    Member Key: "shared"
                        True value
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "provider:network_type"
                        String value: local
                    Member Key: "id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "provider:segmentation_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.495673000 UTC'
source = '127.0.0.1:52575 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/subnets.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.525460000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52575 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 961
    X-Openstack-Request-Id: req-c846c4fd-e8cb-4732-9ee6-3b224b9c70ac
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "subnets"
            Array
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: 10.28.0.1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: 10.28.0.2
                                Member Key: "end"
                                    String value: 10.28.255.254
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 4
                    Member Key: "ipv6_address_mode"
                        Null value
                    Member Key: "cidr"
                        String value: 10.28.0.0/16
                    Member Key: "id"
                        String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                    Member Key: "subnetpool_id"
                        Null value
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: fd5f:5d21:845:1c2e:2::1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: fd5f:5d21:845:1c2e:2::2
                                Member Key: "end"
                                    String value: fd5f:5d21:845:1c2e:2:ffff:ffff:ffff
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 6
                    Member Key: "ipv6_address_mode"
                        String value: dhcpv6-stateful
                    Member Key: "cidr"
                        String value: fd5f:5d21:845:1c2e:2::/80
                    Member Key: "id"
                        String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "subnetpool_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.531914000 UTC'
source = '127.0.0.1:49258 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    POST /v2.1/410bd97d893c45c88ed7709cf936b673/servers HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Content-Length: 242
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient
    Content-Type: application/json

    Object
        Member Key: "server"
            Object
                Member Key: "name"
                    String value: AAA
                Member Key: "imageRef"
                    String value: 4bc635c1-0abb-4a7a-9519-80522deaf327
                Member Key: "key_name"
                    String value: test
                Member Key: "flavorRef"
                    String value: 1
                Member Key: "OS-DCF:diskConfig"
                    String value: AUTO
                Member Key: "max_count"
                    Number value: 1
                Member Key: "min_count"
                    Number value: 1
                Member Key: "networks"
                    Array
                        Object
                            Member Key: "uuid"
                                String value: eb463966-6328-427c-964d-2134a835dc8f
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.575940000 UTC'
source = '127.0.0.1:52238 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/networks.json?id=eb463966-6328-427c-964d-2134a835dc8f HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.600284000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52238 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 454
    X-Openstack-Request-Id: req-0f41f913-501f-40b2-8c97-d00d100f3dd6
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "networks"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "subnets"
                        Array
                            String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                            String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "name"
                        String value: demo-net
                    Member Key: "provider:physical_network"
                        Null value
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mtu"
                        Number value: 0
                    Member Key: "router:external"
                        False value
                    Member Key: "shared"
                        True value
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "provider:network_type"
                        String value: local
                    Member Key: "id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "provider:segmentation_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.604969000 UTC'
source = '127.0.0.1:52238 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/ports.json?tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.638582000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52238 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 13
    X-Openstack-Request-Id: req-647aa30b-2260-4151-a073-af78a157564b
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.640802000 UTC'
source = '127.0.0.1:52238 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/quotas/410bd97d893c45c88ed7709cf936b673.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.646624000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52238 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 171
    X-Openstack-Request-Id: req-4fc84b8b-e3a7-4037-9627-39b99a934702
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "quota"
            Object
                Member Key: "subnet"
                    Number value: 10
                Member Key: "network"
                    Number value: 10
                Member Key: "floatingip"
                    Number value: 50
                Member Key: "subnetpool"
                    Number value: -1
                Member Key: "security_group_rule"
                    Number value: 100
                Member Key: "security_group"
                    Number value: 10
                Member Key: "router"
                    Number value: 10
                Member Key: "rbac_policy"
                    Number value: -1
                Member Key: "port"
                    Number value: 50
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.796004000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49258 (unknown)'
detail = """    HTTP/1.1 202 Accepted
    Location: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
    Content-Type: application/json
    Content-Length: 438
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-d245805d-7949-4cb3-9710-4f53438fd1b9
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "server"
            Object
                Member Key: "security_groups"
                    Array
                        Object
                            Member Key: "name"
                                String value: default
                Member Key: "OS-DCF:diskConfig"
                    String value: AUTO
                Member Key: "id"
                    String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                Member Key: "links"
                    Array
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                            Member Key: "rel"
                                String value: self
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                            Member Key: "rel"
                                String value: bookmark
                Member Key: "adminPass"
                    String value: Cnw2jyJ7x87X
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.818918000 UTC'
source = '127.0.0.1:49262 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/servers/detail?limit=21&project_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.878550000 UTC'
source = '127.0.0.1:52238 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/ports.json?device_id=a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.900591000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52238 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 13
    X-Openstack-Request-Id: req-6f08373c-75c9-45f1-baab-b12fde0b2e4e
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.902675000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49262 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 1419
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-75dabb7d-fb79-4469-8b35-daf0f8cc2ca8
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "servers"
            Array
                Object
                    Member Key: "status"
                        String value: BUILD
                    Member Key: "updated"
                        String value: 2015-11-26T21:19:53Z
                    Member Key: "hostId"
                        String value:
                    Member Key: "OS-EXT-SRV-ATTR:host"
                        Null value
                    Member Key: "addresses"
                        Object
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "key_name"
                        String value: test
                    Member Key: "image"
                        Object
                            Member Key: "id"
                                String value: 4bc635c1-0abb-4a7a-9519-80522deaf327
                            Member Key: "links"
                                Array
                                    Object
                                        Member Key: "href"
                                            String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/images/4bc635c1-0abb-4a7a-9519-80522deaf327
                                        Member Key: "rel"
                                            String value: bookmark
                    Member Key: "OS-EXT-STS:task_state"
                        String value: scheduling
                    Member Key: "OS-EXT-STS:vm_state"
                        String value: building
                    Member Key: "OS-EXT-SRV-ATTR:instance_name"
                        String value: instance-00000018
                    Member Key: "OS-SRV-USG:launched_at"
                        Null value
                    Member Key: "OS-EXT-SRV-ATTR:hypervisor_hostname"
                        Null value
                    Member Key: "flavor"
                        Object
                            Member Key: "id"
                                String value: 1
                            Member Key: "links"
                                Array
                                    Object
                                        Member Key: "href"
                                            String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                                        Member Key: "rel"
                                            String value: bookmark
                    Member Key: "id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "OS-SRV-USG:terminated_at"
                        Null value
                    Member Key: "OS-EXT-AZ:availability_zone"
                        String value:
                    Member Key: "user_id"
                        String value: 9eced15c8e6e42d7bee315954927129e
                    Member Key: "name"
                        String value: AAA
                    Member Key: "created"
                        String value: 2015-11-26T21:19:53Z
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "OS-DCF:diskConfig"
                        String value: AUTO
                    Member Key: "os-extended-volumes:volumes_attached"
                        Array
                    Member Key: "accessIPv4"
                        String value:
                    Member Key: "accessIPv6"
                        String value:
                    Member Key: "progress"
                        Number value: 0
                    Member Key: "OS-EXT-STS:power_state"
                        Number value: 0
                    Member Key: "config_drive"
                        String value:
                    Member Key: "metadata"
                        Object
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.905626000 UTC'
source = '127.0.0.1:52581 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/ports.json?device_id=a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.925848000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52581 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 13
    X-Openstack-Request-Id: req-a5400979-6d8e-4213-8581-5d2481cdeb56
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.929022000 UTC'
source = '127.0.0.1:52582 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/floatingips.json?tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.935487000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52582 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 19
    X-Openstack-Request-Id: req-472aba5c-d225-4532-9c61-83920cee293e
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "floatingips"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.937453000 UTC'
source = '127.0.0.1:52583 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/ports.json?tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.957383000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52583 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 13
    X-Openstack-Request-Id: req-cb47aacd-8904-42f1-96a1-dc801c38e5ad
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.959709000 UTC'
source = '127.0.0.1:52584 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/networks.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.985343000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52584 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 454
    X-Openstack-Request-Id: req-9c6beaf2-c9f8-447f-b12b-e5170e5dca11
    Date: Thu, 26 Nov 2015 21:19:53 GMT
    Connection: keep-alive

    Object
        Member Key: "networks"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "subnets"
                        Array
                            String value: b83ccd70-35c7-4877-8034-5e58c631411f
                            String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                    Member Key: "name"
                        String value: demo-net
                    Member Key: "provider:physical_network"
                        Null value
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mtu"
                        Number value: 0
                    Member Key: "router:external"
                        False value
                    Member Key: "shared"
                        True value
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "provider:network_type"
                        String value: local
                    Member Key: "id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "provider:segmentation_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:53.987375000 UTC'
source = '127.0.0.1:52585 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/subnets.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.016749000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52585 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 961
    X-Openstack-Request-Id: req-80eaf44b-ddce-413f-8de4-d4b5798ee765
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "subnets"
            Array
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: 10.28.0.1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: 10.28.0.2
                                Member Key: "end"
                                    String value: 10.28.255.254
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 4
                    Member Key: "ipv6_address_mode"
                        Null value
                    Member Key: "cidr"
                        String value: 10.28.0.0/16
                    Member Key: "id"
                        String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                    Member Key: "subnetpool_id"
                        Null value
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: fd5f:5d21:845:1c2e:2::1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: fd5f:5d21:845:1c2e:2::2
                                Member Key: "end"
                                    String value: fd5f:5d21:845:1c2e:2:ffff:ffff:ffff
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 6
                    Member Key: "ipv6_address_mode"
                        String value: dhcpv6-stateful
                    Member Key: "cidr"
                        String value: fd5f:5d21:845:1c2e:2::/80
                    Member Key: "id"
                        String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "subnetpool_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.019003000 UTC'
source = '127.0.0.1:49268 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/flavors/detail HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.038999000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49268 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 2089
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-578b2650-6a7c-4f5e-8bc4-72af964fb7db
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "flavors"
            Array
                Object
                    Member Key: "name"
                        String value: m1.tiny
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 512
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 1
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 1
                    Member Key: "id"
                        String value: 1
                Object
                    Member Key: "name"
                        String value: m1.small
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/2
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/2
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 2048
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 1
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 20
                    Member Key: "id"
                        String value: 2
                Object
                    Member Key: "name"
                        String value: m1.medium
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/3
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/3
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 4096
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 2
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 40
                    Member Key: "id"
                        String value: 3
                Object
                    Member Key: "name"
                        String value: m1.large
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/4
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/4
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 8192
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 4
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 80
                    Member Key: "id"
                        String value: 4
                Object
                    Member Key: "name"
                        String value: m1.xlarge
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/5
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/5
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 16384
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 8
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 160
                    Member Key: "id"
                        String value: 5
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.096382000 UTC'
source = '127.0.0.1:52589 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/extensions.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.098991000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52589 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 4074
    X-Openstack-Request-Id: req-1912d2b8-3490-48e7-be8e-f244bbc1b759
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "alias"
                        String value: dns-integration
                    Member Key: "updated"
                        String value: 2015-08-15T18:00:00-00:00
                    Member Key: "name"
                        String value: DNS Integration
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides integration with internal DNS.
                Object
                    Member Key: "alias"
                        String value: ext-gw-mode
                    Member Key: "updated"
                        String value: 2013-03-28T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Configurable external gateway mode
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extension of the router abstraction for specifying whether SNAT should occur on the external gateway
                Object
                    Member Key: "alias"
                        String value: binding
                    Member Key: "updated"
                        String value: 2014-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Binding
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose port bindings of a virtual port to external application
                Object
                    Member Key: "alias"
                        String value: agent
                    Member Key: "updated"
                        String value: 2013-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: agent
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The agent management extension.
                Object
                    Member Key: "alias"
                        String value: subnet_allocation
                    Member Key: "updated"
                        String value: 2015-03-30T10:00:00-00:00
                    Member Key: "name"
                        String value: Subnet Allocation
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables allocation of subnets from a subnet pool
                Object
                    Member Key: "alias"
                        String value: l3_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: L3 Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule routers among l3 agents
                Object
                    Member Key: "alias"
                        String value: external-net
                    Member Key: "updated"
                        String value: 2013-01-14T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron external network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Adds external network attribute to network resource.
                Object
                    Member Key: "alias"
                        String value: flavors
                    Member Key: "updated"
                        String value: 2014-07-06T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Service Flavors
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Service specification for advanced services
                Object
                    Member Key: "alias"
                        String value: net-mtu
                    Member Key: "updated"
                        String value: 2015-03-25T10:00:00-00:00
                    Member Key: "name"
                        String value: Network MTU
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides MTU attribute for a network resource.
                Object
                    Member Key: "alias"
                        String value: quotas
                    Member Key: "updated"
                        String value: 2012-07-29T10:00:00-00:00
                    Member Key: "name"
                        String value: Quota management support
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose functions for quotas management per tenant
                Object
                    Member Key: "alias"
                        String value: l3-ha
                    Member Key: "updated"
                        String value: 2014-04-26T00:00:00-00:00
                    Member Key: "name"
                        String value: HA Router extension
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Add HA capability to routers.
                Object
                    Member Key: "alias"
                        String value: provider
                    Member Key: "updated"
                        String value: 2012-09-07T10:00:00-00:00
                    Member Key: "name"
                        String value: Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to physical networks
                Object
                    Member Key: "alias"
                        String value: multi-provider
                    Member Key: "updated"
                        String value: 2013-06-27T10:00:00-00:00
                    Member Key: "name"
                        String value: Multi Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to multiple physical networks
                Object
                    Member Key: "alias"
                        String value: extraroute
                    Member Key: "updated"
                        String value: 2013-02-01T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra Route
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra routes configuration for L3 router
                Object
                    Member Key: "alias"
                        String value: router
                    Member Key: "updated"
                        String value: 2012-07-20T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Router abstraction for basic L3 forwarding between L2 Neutron networks and access to external networks via a NAT gateway.
                Object
                    Member Key: "alias"
                        String value: extra_dhcp_opt
                    Member Key: "updated"
                        String value: 2013-03-17T12:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra DHCP opts
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra options configuration for DHCP. For example PXE boot options to DHCP clients can be specified (e.g. tftp-server, server-ip-address, bootfile-name)
                Object
                    Member Key: "alias"
                        String value: security-group
                    Member Key: "updated"
                        String value: 2012-10-05T10:00:00-00:00
                    Member Key: "name"
                        String value: security-group
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The security groups extension.
                Object
                    Member Key: "alias"
                        String value: dhcp_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: DHCP Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule networks among dhcp agents
                Object
                    Member Key: "alias"
                        String value: rbac-policies
                    Member Key: "updated"
                        String value: 2015-06-17T12:15:12-30:00
                    Member Key: "name"
                        String value: RBAC Policies
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Allows creation and modification of policies that control tenant access to resources.
                Object
                    Member Key: "alias"
                        String value: port-security
                    Member Key: "updated"
                        String value: 2012-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Security
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides port security
                Object
                    Member Key: "alias"
                        String value: allowed-address-pairs
                    Member Key: "updated"
                        String value: 2013-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Allowed Address Pairs
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides allowed address pairs
                Object
                    Member Key: "alias"
                        String value: dvr
                    Member Key: "updated"
                        String value: 2014-06-1T10:00:00-00:00
                    Member Key: "name"
                        String value: Distributed Virtual Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables configuration of Distributed Virtual Routers.
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.102346000 UTC'
source = '127.0.0.1:49272 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/extensions HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.138044000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49272 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 21496
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-1db507a1-6788-4464-ac81-76b843982686
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: Multinic
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: NMN
                    Member Key: "description"
                        String value: Multiple network support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: DiskConfig
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-DCF
                    Member Key: "description"
                        String value: Disk Management Extension.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedAvailabilityZone
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-AZ
                    Member Key: "description"
                        String value: Extended Availability Zone support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ImageSize
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IMG-SIZE
                    Member Key: "description"
                        String value: Adds image size to image listings.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIps
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIpsMac
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS-MAC
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedServerAttributes
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-SRV-ATTR
                    Member Key: "description"
                        String value: Extended Server Attributes support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedStatus
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-STS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorDisabled
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-DISABLED
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorExtraData
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-EXT-DATA
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: SchedulerHints
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SCH-HNT
                    Member Key: "description"
                        String value: Pass arbitrary key/value pairs to the scheduler.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ServerUsage
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SRV-USG
                    Member Key: "description"
                        String value: Adds launched_at and terminated_at on Servers.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AccessIPs
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-access-ips
                    Member Key: "description"
                        String value: Access IPs support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AdminActions
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-admin-actions
                    Member Key: "description"
                        String value: Enable admin-only server actions
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.167134000 UTC'
source = '127.0.0.1:49273 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/limits?reserved=1 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.187037000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49273 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 513
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-28c14de7-0059-4616-a458-6ca5d1229b73
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "limits"
            Object
                Member Key: "rate"
                    Array
                Member Key: "absolute"
                    Object
                        Member Key: "maxServerMeta"
                            Number value: 128
                        Member Key: "maxPersonality"
                            Number value: 5
                        Member Key: "totalServerGroupsUsed"
                            Number value: 0
                        Member Key: "maxImageMeta"
                            Number value: 128
                        Member Key: "maxPersonalitySize"
                            Number value: 10240
                        Member Key: "maxTotalKeypairs"
                            Number value: 100
                        Member Key: "maxSecurityGroupRules"
                            Number value: 20
                        Member Key: "maxServerGroups"
                            Number value: 10
                        Member Key: "totalCoresUsed"
                            Number value: 1
                        Member Key: "totalRAMUsed"
                            Number value: 512
                        Member Key: "totalInstancesUsed"
                            Number value: 1
                        Member Key: "maxSecurityGroups"
                            Number value: 10
                        Member Key: "totalFloatingIpsUsed"
                            Number value: 0
                        Member Key: "maxTotalCores"
                            Number value: 20
                        Member Key: "maxServerGroupMembers"
                            Number value: 10
                        Member Key: "maxTotalFloatingIps"
                            Number value: 10
                        Member Key: "totalSecurityGroupsUsed"
                            Number value: 1
                        Member Key: "maxTotalInstances"
                            Number value: 10
                        Member Key: "maxTotalRAMSize"
                            Number value: 51200
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.224916000 UTC'
source = '127.0.0.1:49274 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/limits?reserved=1 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.230383000 UTC'
source = '172.18.203.99:37182 (unknown)'
dest = '172.18.203.95:9696 (neutron)'
detail = """    GET /v2.0/networks.json?id=eb463966-6328-427c-964d-2134a835dc8f HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.258811000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49274 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 513
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-fe07f826-f174-4c75-a59c-e536c5d2b412
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "limits"
            Object
                Member Key: "rate"
                    Array
                Member Key: "absolute"
                    Object
                        Member Key: "maxServerMeta"
                            Number value: 128
                        Member Key: "maxPersonality"
                            Number value: 5
                        Member Key: "totalServerGroupsUsed"
                            Number value: 0
                        Member Key: "maxImageMeta"
                            Number value: 128
                        Member Key: "maxPersonalitySize"
                            Number value: 10240
                        Member Key: "maxTotalKeypairs"
                            Number value: 100
                        Member Key: "maxSecurityGroupRules"
                            Number value: 20
                        Member Key: "maxServerGroups"
                            Number value: 10
                        Member Key: "totalCoresUsed"
                            Number value: 1
                        Member Key: "totalRAMUsed"
                            Number value: 512
                        Member Key: "totalInstancesUsed"
                            Number value: 1
                        Member Key: "maxSecurityGroups"
                            Number value: 10
                        Member Key: "totalFloatingIpsUsed"
                            Number value: 0
                        Member Key: "maxTotalCores"
                            Number value: 20
                        Member Key: "maxServerGroupMembers"
                            Number value: 10
                        Member Key: "maxTotalFloatingIps"
                            Number value: 10
                        Member Key: "totalSecurityGroupsUsed"
                            Number value: 1
                        Member Key: "maxTotalInstances"
                            Number value: 10
                        Member Key: "maxTotalRAMSize"
                            Number value: 51200
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.274208000 UTC'
source = '172.18.203.95:9696 (neutron)'
dest = '172.18.203.99:37182 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 454
    X-Openstack-Request-Id: req-fc5d7924-607f-46ba-817d-d0974957392a
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "networks"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "subnets"
                        Array
                            String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                            String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "name"
                        String value: demo-net
                    Member Key: "provider:physical_network"
                        Null value
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mtu"
                        Number value: 0
                    Member Key: "router:external"
                        False value
                    Member Key: "shared"
                        True value
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "provider:network_type"
                        String value: local
                    Member Key: "id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "provider:segmentation_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.277143000 UTC'
source = '172.18.203.99:37182 (unknown)'
dest = '172.18.203.95:9696 (neutron)'
detail = """    GET /v2.0/security-groups.json?tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.319859000 UTC'
source = '172.18.203.95:9696 (neutron)'
dest = '172.18.203.99:37182 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1550
    X-Openstack-Request-Id: req-9339699b-3370-48ca-83ac-2848271cb3a8
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "security_groups"
            Array
                Object
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "description"
                        String value: Default security group
                    Member Key: "id"
                        String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "security_group_rules"
                        Array
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: 991a8e06-dd5e-4024-8773-c4e38e96cdc5
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c116db16-5fdf-4ae1-8c98-41999120f3a1
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c1f4a0f6-db06-4c6b-87a1-47aa837a657a
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: f1bca7e8-17cd-4833-a548-6fbbd8f07c64
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "name"
                        String value: default
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.322544000 UTC'
source = '172.18.203.99:37182 (unknown)'
dest = '172.18.203.95:9696 (neutron)'
detail = """    POST /v2.0/ports.json HTTP/1.1
    Host: calico-vm18:9696
    Content-Length: 317
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 133fef552c2d4596a0d3f2a5636664f3
    Connection: keep-alive
    User-Agent: python-neutronclient
    Content-Type: application/json

    Object
        Member Key: "port"
            Object
                Member Key: "binding:host_id"
                    String value: calico-vm23
                Member Key: "admin_state_up"
                    True value
                Member Key: "network_id"
                    String value: eb463966-6328-427c-964d-2134a835dc8f
                Member Key: "tenant_id"
                    String value: 410bd97d893c45c88ed7709cf936b673
                Member Key: "device_owner"
                    String value: compute:None
                Member Key: "security_groups"
                    Array
                        String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                Member Key: "device_id"
                    String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.600366000 UTC'
source = '172.18.203.95:9696 (neutron)'
dest = '172.18.203.99:37182 (unknown)'
detail = """    HTTP/1.1 201 Created
    Content-Type: application/json; charset=UTF-8
    Content-Length: 886
    X-Openstack-Request-Id: req-acc82f22-bdb1-41df-8eb1-33d418eaecf1
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "port"
            Object
                Member Key: "status"
                    String value: DOWN
                Member Key: "binding:host_id"
                    String value: calico-vm23
                Member Key: "allowed_address_pairs"
                    Array
                Member Key: "extra_dhcp_opts"
                    Array
                Member Key: "device_owner"
                    String value: compute:None
                Member Key: "port_security_enabled"
                    True value
                Member Key: "binding:profile"
                    Object
                Member Key: "fixed_ips"
                    Array
                        Object
                            Member Key: "subnet_id"
                                String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                            Member Key: "ip_address"
                                String value: 10.28.0.24
                        Object
                            Member Key: "subnet_id"
                                String value: b83ccd70-35c7-4877-8034-5e58c631411f
                            Member Key: "ip_address"
                                String value: fd5f:5d21:845:1c2e:2::18
                Member Key: "id"
                    String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                Member Key: "security_groups"
                    Array
                        String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                Member Key: "device_id"
                    String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                Member Key: "name"
                    String value:
                Member Key: "admin_state_up"
                    True value
                Member Key: "network_id"
                    String value: eb463966-6328-427c-964d-2134a835dc8f
                Member Key: "dns_name"
                    String value:
                Member Key: "binding:vif_details"
                    Object
                        Member Key: "port_filter"
                            True value
                        Member Key: "mac_address"
                            String value: 00:61:fe:ed:ca:fe
                Member Key: "binding:vnic_type"
                    String value: normal
                Member Key: "binding:vif_type"
                    String value: tap
                Member Key: "tenant_id"
                    String value: 410bd97d893c45c88ed7709cf936b673
                Member Key: "mac_address"
                    String value: fa:16:3e:24:ac:4e
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.623995000 UTC'
source = '172.18.203.99:37182 (unknown)'
dest = '172.18.203.95:9696 (neutron)'
detail = """    GET /v2.0/ports.json?tenant_id=410bd97d893c45c88ed7709cf936b673&device_id=a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 133fef552c2d4596a0d3f2a5636664f3
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.641445000 UTC'
source = '172.18.203.95:9696 (neutron)'
dest = '172.18.203.99:37182 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1159
    X-Openstack-Request-Id: req-b9de2b79-3a1e-49fd-8a25-cfdf032239e7
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                            Object
                                Member Key: "hostname"
                                    String value: host-10-28-0-24
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                                Member Key: "fqdn"
                                    String value: host-10-28-0-24.openstacklocal.
                            Object
                                Member Key: "hostname"
                                    String value: host-fd5f-5d21-845-1c2e-2--18
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                                Member Key: "fqdn"
                                    String value: host-fd5f-5d21-845-1c2e-2--18.openstacklocal.
                    Member Key: "device_owner"
                        String value: compute:None
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                            Object
                                Member Key: "subnet_id"
                                    String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                            Object
                                Member Key: "subnet_id"
                                    String value: b83ccd70-35c7-4877-8034-5e58c631411f
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                    Member Key: "id"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "security_groups"
                        Array
                            String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "device_id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "mac_address"
                        String value: fa:16:3e:24:ac:4e
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.646038000 UTC'
source = '172.18.203.99:37182 (unknown)'
dest = '172.18.203.95:9696 (neutron)'
detail = """    GET /v2.0/floatingips.json?fixed_ip_address=10.28.0.24&port_id=9792cbef-b9a4-4860-9cc6-342695aa80be HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 133fef552c2d4596a0d3f2a5636664f3
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.652847000 UTC'
source = '172.18.203.95:9696 (neutron)'
dest = '172.18.203.99:37182 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 19
    X-Openstack-Request-Id: req-5166d331-3c3e-434e-bd96-a7135b9f1eee
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "floatingips"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.656698000 UTC'
source = '172.18.203.99:37182 (unknown)'
dest = '172.18.203.95:9696 (neutron)'
detail = """    GET /v2.0/floatingips.json?fixed_ip_address=fd5f%3A5d21%3A845%3A1c2e%3A2%3A%3A18&port_id=9792cbef-b9a4-4860-9cc6-342695aa80be HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 133fef552c2d4596a0d3f2a5636664f3
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.661311000 UTC'
source = '172.18.203.95:9696 (neutron)'
dest = '172.18.203.99:37182 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 19
    X-Openstack-Request-Id: req-50a63064-897f-4873-a6c5-77affc34308f
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "floatingips"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.664869000 UTC'
source = '172.18.203.99:37182 (unknown)'
dest = '172.18.203.95:9696 (neutron)'
detail = """    GET /v2.0/subnets.json?id=886e3c9e-e4cc-4616-8b64-82b11b55e801&id=b83ccd70-35c7-4877-8034-5e58c631411f HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.704289000 UTC'
source = '172.18.203.95:9696 (neutron)'
dest = '172.18.203.99:37182 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 961
    X-Openstack-Request-Id: req-4a9dfe07-91ef-42ae-ac01-da86fca8d3fd
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "subnets"
            Array
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: 10.28.0.1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: 10.28.0.2
                                Member Key: "end"
                                    String value: 10.28.255.254
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 4
                    Member Key: "ipv6_address_mode"
                        Null value
                    Member Key: "cidr"
                        String value: 10.28.0.0/16
                    Member Key: "id"
                        String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                    Member Key: "subnetpool_id"
                        Null value
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: fd5f:5d21:845:1c2e:2::1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: fd5f:5d21:845:1c2e:2::2
                                Member Key: "end"
                                    String value: fd5f:5d21:845:1c2e:2:ffff:ffff:ffff
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 6
                    Member Key: "ipv6_address_mode"
                        String value: dhcpv6-stateful
                    Member Key: "cidr"
                        String value: fd5f:5d21:845:1c2e:2::/80
                    Member Key: "id"
                        String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "subnetpool_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.706879000 UTC'
source = '172.18.203.99:37182 (unknown)'
dest = '172.18.203.95:9696 (neutron)'
detail = """    GET /v2.0/ports.json?network_id=eb463966-6328-427c-964d-2134a835dc8f&device_owner=network%3Adhcp HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.715315000 UTC'
source = '127.0.0.1:49275 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.755311000 UTC'
source = '172.18.203.95:9696 (neutron)'
dest = '172.18.203.99:37182 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 2864
    X-Openstack-Request-Id: req-7d708732-2135-48f5-9aaa-b9dc26370d20
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm18
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                    Member Key: "device_owner"
                        String value: network:dhcp
                    Member Key: "port_security_enabled"
                        False value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                    Member Key: "id"
                        String value: 0cb7527a-484c-4426-908f-fc8580aba415
                    Member Key: "security_groups"
                        Array
                    Member Key: "device_id"
                        String value: dhcp1c3a1810-9e84-55d5-b84c-6858362693a2-eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: unbound
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mac_address"
                        String value: fa:16:3e:9b:9b:a4
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm17
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                    Member Key: "device_owner"
                        String value: network:dhcp
                    Member Key: "port_security_enabled"
                        False value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                    Member Key: "id"
                        String value: 5be6038d-77da-4d2c-b633-53487fd91021
                    Member Key: "security_groups"
                        Array
                    Member Key: "device_id"
                        String value: dhcpe8e7e5ac-0ced-52f6-a70a-68749fb9cbbd-eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mac_address"
                        String value: fa:16:3e:e1:b4:eb
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                    Member Key: "device_owner"
                        String value: network:dhcp
                    Member Key: "port_security_enabled"
                        False value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                    Member Key: "id"
                        String value: 8bfa1972-db85-4096-af3c-74e2b6ebc770
                    Member Key: "security_groups"
                        Array
                    Member Key: "device_id"
                        String value: dhcp9d9e10c9-f991-5b96-ac46-867a0f3c3286-eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mac_address"
                        String value: fa:16:3e:21:9f:a1
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm19
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                    Member Key: "device_owner"
                        String value: network:dhcp
                    Member Key: "port_security_enabled"
                        False value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                    Member Key: "id"
                        String value: 8cf6e4d1-4f30-4f15-99c7-9ec91c67ca44
                    Member Key: "security_groups"
                        Array
                    Member Key: "device_id"
                        String value: dhcp964a5cf7-c416-5f67-ac30-cc3d75a5dae2-eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mac_address"
                        String value: fa:16:3e:61:76:57
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.760432000 UTC'
source = '172.18.203.99:37182 (unknown)'
dest = '172.18.203.95:9696 (neutron)'
detail = """    GET /v2.0/ports.json?network_id=eb463966-6328-427c-964d-2134a835dc8f&device_owner=network%3Adhcp HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.774411000 UTC'
source = '127.0.0.1:52238 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/ports.json?device_id=a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.802150000 UTC'
source = '172.18.203.95:9696 (neutron)'
dest = '172.18.203.99:37182 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 2864
    X-Openstack-Request-Id: req-985c3938-6e9f-4c5f-b90a-5b4555d199c3
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm18
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                    Member Key: "device_owner"
                        String value: network:dhcp
                    Member Key: "port_security_enabled"
                        False value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                    Member Key: "id"
                        String value: 0cb7527a-484c-4426-908f-fc8580aba415
                    Member Key: "security_groups"
                        Array
                    Member Key: "device_id"
                        String value: dhcp1c3a1810-9e84-55d5-b84c-6858362693a2-eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: unbound
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mac_address"
                        String value: fa:16:3e:9b:9b:a4
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm17
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                    Member Key: "device_owner"
                        String value: network:dhcp
                    Member Key: "port_security_enabled"
                        False value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                    Member Key: "id"
                        String value: 5be6038d-77da-4d2c-b633-53487fd91021
                    Member Key: "security_groups"
                        Array
                    Member Key: "device_id"
                        String value: dhcpe8e7e5ac-0ced-52f6-a70a-68749fb9cbbd-eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mac_address"
                        String value: fa:16:3e:e1:b4:eb
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                    Member Key: "device_owner"
                        String value: network:dhcp
                    Member Key: "port_security_enabled"
                        False value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                    Member Key: "id"
                        String value: 8bfa1972-db85-4096-af3c-74e2b6ebc770
                    Member Key: "security_groups"
                        Array
                    Member Key: "device_id"
                        String value: dhcp9d9e10c9-f991-5b96-ac46-867a0f3c3286-eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mac_address"
                        String value: fa:16:3e:21:9f:a1
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm19
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                    Member Key: "device_owner"
                        String value: network:dhcp
                    Member Key: "port_security_enabled"
                        False value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                    Member Key: "id"
                        String value: 8cf6e4d1-4f30-4f15-99c7-9ec91c67ca44
                    Member Key: "security_groups"
                        Array
                    Member Key: "device_id"
                        String value: dhcp964a5cf7-c416-5f67-ac30-cc3d75a5dae2-eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mac_address"
                        String value: fa:16:3e:61:76:57
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.803898000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52238 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1159
    X-Openstack-Request-Id: req-03be36a7-8253-4bb7-bba8-c8c5135a6ca7
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                            Object
                                Member Key: "hostname"
                                    String value: host-10-28-0-24
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                                Member Key: "fqdn"
                                    String value: host-10-28-0-24.openstacklocal.
                            Object
                                Member Key: "hostname"
                                    String value: host-fd5f-5d21-845-1c2e-2--18
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                                Member Key: "fqdn"
                                    String value: host-fd5f-5d21-845-1c2e-2--18.openstacklocal.
                    Member Key: "device_owner"
                        String value: compute:None
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                            Object
                                Member Key: "subnet_id"
                                    String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                            Object
                                Member Key: "subnet_id"
                                    String value: b83ccd70-35c7-4877-8034-5e58c631411f
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                    Member Key: "id"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "security_groups"
                        Array
                            String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "device_id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "mac_address"
                        String value: fa:16:3e:24:ac:4e
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.805981000 UTC'
source = '127.0.0.1:52238 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/security-groups.json?id=e6adf5ab-bcd8-41c0-91aa-4d73354d39e7 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.821585000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52238 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1550
    X-Openstack-Request-Id: req-5c22f8b7-1ffe-4dc2-adcc-2c778aa1b6d0
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "security_groups"
            Array
                Object
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "description"
                        String value: Default security group
                    Member Key: "id"
                        String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "security_group_rules"
                        Array
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: 991a8e06-dd5e-4024-8773-c4e38e96cdc5
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c116db16-5fdf-4ae1-8c98-41999120f3a1
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c1f4a0f6-db06-4c6b-87a1-47aa837a657a
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: f1bca7e8-17cd-4833-a548-6fbbd8f07c64
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "name"
                        String value: default
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.823387000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49275 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 1541
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-19626030-ecef-4150-a030-66913c9cb142
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "server"
            Object
                Member Key: "status"
                    String value: BUILD
                Member Key: "updated"
                    String value: 2015-11-26T21:19:54Z
                Member Key: "hostId"
                    String value: 3da7ee3dfd5690185ffc85c0c6459cbd4b496ea3b036f5972243109c
                Member Key: "OS-EXT-SRV-ATTR:host"
                    String value: calico-vm23
                Member Key: "addresses"
                    Object
                Member Key: "links"
                    Array
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                            Member Key: "rel"
                                String value: self
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                            Member Key: "rel"
                                String value: bookmark
                Member Key: "key_name"
                    String value: test
                Member Key: "image"
                    Object
                        Member Key: "id"
                            String value: 4bc635c1-0abb-4a7a-9519-80522deaf327
                        Member Key: "links"
                            Array
                                Object
                                    Member Key: "href"
                                        String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/images/4bc635c1-0abb-4a7a-9519-80522deaf327
                                    Member Key: "rel"
                                        String value: bookmark
                Member Key: "OS-EXT-STS:task_state"
                    String value: spawning
                Member Key: "OS-EXT-STS:vm_state"
                    String value: building
                Member Key: "OS-EXT-SRV-ATTR:instance_name"
                    String value: instance-00000018
                Member Key: "OS-SRV-USG:launched_at"
                    Null value
                Member Key: "OS-EXT-SRV-ATTR:hypervisor_hostname"
                    String value: calico-vm23
                Member Key: "flavor"
                    Object
                        Member Key: "id"
                            String value: 1
                        Member Key: "links"
                            Array
                                Object
                                    Member Key: "href"
                                        String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                                    Member Key: "rel"
                                        String value: bookmark
                Member Key: "id"
                    String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                Member Key: "security_groups"
                    Array
                        Object
                            Member Key: "name"
                                String value: default
                Member Key: "OS-SRV-USG:terminated_at"
                    Null value
                Member Key: "OS-EXT-AZ:availability_zone"
                    String value: calico-vm23
                Member Key: "user_id"
                    String value: 9eced15c8e6e42d7bee315954927129e
                Member Key: "name"
                    String value: AAA
                Member Key: "created"
                    String value: 2015-11-26T21:19:53Z
                Member Key: "tenant_id"
                    String value: 410bd97d893c45c88ed7709cf936b673
                Member Key: "OS-DCF:diskConfig"
                    String value: AUTO
                Member Key: "os-extended-volumes:volumes_attached"
                    Array
                Member Key: "accessIPv4"
                    String value:
                Member Key: "accessIPv6"
                    String value:
                Member Key: "progress"
                    Number value: 0
                Member Key: "OS-EXT-STS:power_state"
                    Number value: 0
                Member Key: "config_drive"
                    String value:
                Member Key: "metadata"
                    Object
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.826144000 UTC'
source = '127.0.0.1:49276 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.841958000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49276 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 422
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-79c7cb47-440b-4985-a59b-574ef3489e4a
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "flavor"
            Object
                Member Key: "name"
                    String value: m1.tiny
                Member Key: "links"
                    Array
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1
                            Member Key: "rel"
                                String value: self
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                            Member Key: "rel"
                                String value: bookmark
                Member Key: "ram"
                    Number value: 512
                Member Key: "OS-FLV-DISABLED:disabled"
                    False value
                Member Key: "vcpus"
                    Number value: 1
                Member Key: "swap"
                    String value:
                Member Key: "os-flavor-access:is_public"
                    True value
                Member Key: "rxtx_factor"
                    Number value: 1.0
                Member Key: "OS-FLV-EXT-DATA:ephemeral"
                    Number value: 0
                Member Key: "disk"
                    Number value: 1
                Member Key: "id"
                    String value: 1
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.872127000 UTC'
source = '127.0.0.1:52597 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/extensions.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.874666000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52597 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 4074
    X-Openstack-Request-Id: req-7491fce4-9346-4a41-9464-829d518301d5
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "alias"
                        String value: dns-integration
                    Member Key: "updated"
                        String value: 2015-08-15T18:00:00-00:00
                    Member Key: "name"
                        String value: DNS Integration
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides integration with internal DNS.
                Object
                    Member Key: "alias"
                        String value: ext-gw-mode
                    Member Key: "updated"
                        String value: 2013-03-28T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Configurable external gateway mode
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extension of the router abstraction for specifying whether SNAT should occur on the external gateway
                Object
                    Member Key: "alias"
                        String value: binding
                    Member Key: "updated"
                        String value: 2014-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Binding
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose port bindings of a virtual port to external application
                Object
                    Member Key: "alias"
                        String value: agent
                    Member Key: "updated"
                        String value: 2013-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: agent
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The agent management extension.
                Object
                    Member Key: "alias"
                        String value: subnet_allocation
                    Member Key: "updated"
                        String value: 2015-03-30T10:00:00-00:00
                    Member Key: "name"
                        String value: Subnet Allocation
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables allocation of subnets from a subnet pool
                Object
                    Member Key: "alias"
                        String value: l3_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: L3 Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule routers among l3 agents
                Object
                    Member Key: "alias"
                        String value: external-net
                    Member Key: "updated"
                        String value: 2013-01-14T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron external network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Adds external network attribute to network resource.
                Object
                    Member Key: "alias"
                        String value: flavors
                    Member Key: "updated"
                        String value: 2014-07-06T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Service Flavors
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Service specification for advanced services
                Object
                    Member Key: "alias"
                        String value: net-mtu
                    Member Key: "updated"
                        String value: 2015-03-25T10:00:00-00:00
                    Member Key: "name"
                        String value: Network MTU
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides MTU attribute for a network resource.
                Object
                    Member Key: "alias"
                        String value: quotas
                    Member Key: "updated"
                        String value: 2012-07-29T10:00:00-00:00
                    Member Key: "name"
                        String value: Quota management support
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose functions for quotas management per tenant
                Object
                    Member Key: "alias"
                        String value: l3-ha
                    Member Key: "updated"
                        String value: 2014-04-26T00:00:00-00:00
                    Member Key: "name"
                        String value: HA Router extension
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Add HA capability to routers.
                Object
                    Member Key: "alias"
                        String value: provider
                    Member Key: "updated"
                        String value: 2012-09-07T10:00:00-00:00
                    Member Key: "name"
                        String value: Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to physical networks
                Object
                    Member Key: "alias"
                        String value: multi-provider
                    Member Key: "updated"
                        String value: 2013-06-27T10:00:00-00:00
                    Member Key: "name"
                        String value: Multi Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to multiple physical networks
                Object
                    Member Key: "alias"
                        String value: extraroute
                    Member Key: "updated"
                        String value: 2013-02-01T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra Route
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra routes configuration for L3 router
                Object
                    Member Key: "alias"
                        String value: router
                    Member Key: "updated"
                        String value: 2012-07-20T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Router abstraction for basic L3 forwarding between L2 Neutron networks and access to external networks via a NAT gateway.
                Object
                    Member Key: "alias"
                        String value: extra_dhcp_opt
                    Member Key: "updated"
                        String value: 2013-03-17T12:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra DHCP opts
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra options configuration for DHCP. For example PXE boot options to DHCP clients can be specified (e.g. tftp-server, server-ip-address, bootfile-name)
                Object
                    Member Key: "alias"
                        String value: security-group
                    Member Key: "updated"
                        String value: 2012-10-05T10:00:00-00:00
                    Member Key: "name"
                        String value: security-group
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The security groups extension.
                Object
                    Member Key: "alias"
                        String value: dhcp_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: DHCP Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule networks among dhcp agents
                Object
                    Member Key: "alias"
                        String value: rbac-policies
                    Member Key: "updated"
                        String value: 2015-06-17T12:15:12-30:00
                    Member Key: "name"
                        String value: RBAC Policies
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Allows creation and modification of policies that control tenant access to resources.
                Object
                    Member Key: "alias"
                        String value: port-security
                    Member Key: "updated"
                        String value: 2012-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Security
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides port security
                Object
                    Member Key: "alias"
                        String value: allowed-address-pairs
                    Member Key: "updated"
                        String value: 2013-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Allowed Address Pairs
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides allowed address pairs
                Object
                    Member Key: "alias"
                        String value: dvr
                    Member Key: "updated"
                        String value: 2014-06-1T10:00:00-00:00
                    Member Key: "name"
                        String value: Distributed Virtual Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables configuration of Distributed Virtual Routers.
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.878616000 UTC'
source = '127.0.0.1:49280 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/extensions HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:54.915767000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49280 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 21496
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-d4138ed7-4118-4223-a1b9-268604ea7935
    Date: Thu, 26 Nov 2015 21:19:54 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: Multinic
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: NMN
                    Member Key: "description"
                        String value: Multiple network support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: DiskConfig
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-DCF
                    Member Key: "description"
                        String value: Disk Management Extension.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedAvailabilityZone
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-AZ
                    Member Key: "description"
                        String value: Extended Availability Zone support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ImageSize
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IMG-SIZE
                    Member Key: "description"
                        String value: Adds image size to image listings.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIps
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIpsMac
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS-MAC
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedServerAttributes
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-SRV-ATTR
                    Member Key: "description"
                        String value: Extended Server Attributes support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedStatus
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-STS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorDisabled
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-DISABLED
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorExtraData
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-EXT-DATA
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: SchedulerHints
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SCH-HNT
                    Member Key: "description"
                        String value: Pass arbitrary key/value pairs to the scheduler.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ServerUsage
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SRV-USG
                    Member Key: "description"
                        String value: Adds launched_at and terminated_at on Servers.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AccessIPs
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-access-ips
                    Member Key: "description"
                        String value: Access IPs support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AdminActions
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-admin-actions
                    Member Key: "description"
                        String value: Enable admin-only server actions
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.524934000 UTC'
source = '127.0.0.1:49281 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.580029000 UTC'
source = '127.0.0.1:48975 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    POST /v2.1/33afd0ae6b4c48ea8f2fb109449df342/os-server-external-events HTTP/1.1
    Host: calico-vm18:8774
    Content-Length: 170
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 20c3f172aa1a46d9bf9acd0a93fc028d
    Connection: keep-alive
    User-Agent: python-novaclient
    Content-Type: application/json

    Object
        Member Key: "events"
            Array
                Object
                    Member Key: "status"
                        String value: completed
                    Member Key: "tag"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "name"
                        String value: network-vif-plugged
                    Member Key: "server_uuid"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.592819000 UTC'
source = '127.0.0.1:52238 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/ports.json?device_id=a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.612506000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52238 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1161
    X-Openstack-Request-Id: req-28994e8b-ebc8-4bb7-95cd-9475bfb7f920
    Date: Thu, 26 Nov 2015 21:19:57 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                            Object
                                Member Key: "hostname"
                                    String value: host-10-28-0-24
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                                Member Key: "fqdn"
                                    String value: host-10-28-0-24.openstacklocal.
                            Object
                                Member Key: "hostname"
                                    String value: host-fd5f-5d21-845-1c2e-2--18
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                                Member Key: "fqdn"
                                    String value: host-fd5f-5d21-845-1c2e-2--18.openstacklocal.
                    Member Key: "device_owner"
                        String value: compute:None
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                            Object
                                Member Key: "subnet_id"
                                    String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                            Object
                                Member Key: "subnet_id"
                                    String value: b83ccd70-35c7-4877-8034-5e58c631411f
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                    Member Key: "id"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "security_groups"
                        Array
                            String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "device_id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "mac_address"
                        String value: fa:16:3e:24:ac:4e
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.614755000 UTC'
source = '127.0.0.1:52238 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/security-groups.json?id=e6adf5ab-bcd8-41c0-91aa-4d73354d39e7 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.625225000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:48975 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 183
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-3c5ce9e0-bedd-4341-b44c-3ca27b586ddd
    Date: Thu, 26 Nov 2015 21:19:57 GMT
    Connection: keep-alive

    Object
        Member Key: "events"
            Array
                Object
                    Member Key: "status"
                        String value: completed
                    Member Key: "tag"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "name"
                        String value: network-vif-plugged
                    Member Key: "server_uuid"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "code"
                        Number value: 200
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.631262000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52238 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1550
    X-Openstack-Request-Id: req-cee26c75-d6f5-4657-8f9b-98ee6aafada1
    Date: Thu, 26 Nov 2015 21:19:57 GMT
    Connection: keep-alive

    Object
        Member Key: "security_groups"
            Array
                Object
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "description"
                        String value: Default security group
                    Member Key: "id"
                        String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "security_group_rules"
                        Array
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: 991a8e06-dd5e-4024-8773-c4e38e96cdc5
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c116db16-5fdf-4ae1-8c98-41999120f3a1
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c1f4a0f6-db06-4c6b-87a1-47aa837a657a
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: f1bca7e8-17cd-4833-a548-6fbbd8f07c64
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "name"
                        String value: default
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.633230000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49281 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 1795
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-1536baf8-45f8-4b8e-880f-269c94896caf
    Date: Thu, 26 Nov 2015 21:19:57 GMT
    Connection: keep-alive

    Object
        Member Key: "server"
            Object
                Member Key: "status"
                    String value: BUILD
                Member Key: "updated"
                    String value: 2015-11-26T21:19:54Z
                Member Key: "hostId"
                    String value: 3da7ee3dfd5690185ffc85c0c6459cbd4b496ea3b036f5972243109c
                Member Key: "OS-EXT-SRV-ATTR:host"
                    String value: calico-vm23
                Member Key: "addresses"
                    Object
                        Member Key: "demo-net"
                            Array
                                Object
                                    Member Key: "OS-EXT-IPS-MAC:mac_addr"
                                        String value: fa:16:3e:24:ac:4e
                                    Member Key: "version"
                                        Number value: 4
                                    Member Key: "addr"
                                        String value: 10.28.0.24
                                    Member Key: "OS-EXT-IPS:type"
                                        String value: fixed
                                Object
                                    Member Key: "OS-EXT-IPS-MAC:mac_addr"
                                        String value: fa:16:3e:24:ac:4e
                                    Member Key: "version"
                                        Number value: 6
                                    Member Key: "addr"
                                        String value: fd5f:5d21:845:1c2e:2::18
                                    Member Key: "OS-EXT-IPS:type"
                                        String value: fixed
                Member Key: "links"
                    Array
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                            Member Key: "rel"
                                String value: self
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                            Member Key: "rel"
                                String value: bookmark
                Member Key: "key_name"
                    String value: test
                Member Key: "image"
                    Object
                        Member Key: "id"
                            String value: 4bc635c1-0abb-4a7a-9519-80522deaf327
                        Member Key: "links"
                            Array
                                Object
                                    Member Key: "href"
                                        String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/images/4bc635c1-0abb-4a7a-9519-80522deaf327
                                    Member Key: "rel"
                                        String value: bookmark
                Member Key: "OS-EXT-STS:task_state"
                    String value: spawning
                Member Key: "OS-EXT-STS:vm_state"
                    String value: building
                Member Key: "OS-EXT-SRV-ATTR:instance_name"
                    String value: instance-00000018
                Member Key: "OS-SRV-USG:launched_at"
                    Null value
                Member Key: "OS-EXT-SRV-ATTR:hypervisor_hostname"
                    String value: calico-vm23
                Member Key: "flavor"
                    Object
                        Member Key: "id"
                            String value: 1
                        Member Key: "links"
                            Array
                                Object
                                    Member Key: "href"
                                        String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                                    Member Key: "rel"
                                        String value: bookmark
                Member Key: "id"
                    String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                Member Key: "security_groups"
                    Array
                        Object
                            Member Key: "name"
                                String value: default
                Member Key: "OS-SRV-USG:terminated_at"
                    Null value
                Member Key: "OS-EXT-AZ:availability_zone"
                    String value: calico-vm23
                Member Key: "user_id"
                    String value: 9eced15c8e6e42d7bee315954927129e
                Member Key: "name"
                    String value: AAA
                Member Key: "created"
                    String value: 2015-11-26T21:19:53Z
                Member Key: "tenant_id"
                    String value: 410bd97d893c45c88ed7709cf936b673
                Member Key: "OS-DCF:diskConfig"
                    String value: AUTO
                Member Key: "os-extended-volumes:volumes_attached"
                    Array
                Member Key: "accessIPv4"
                    String value:
                Member Key: "accessIPv6"
                    String value:
                Member Key: "progress"
                    Number value: 0
                Member Key: "OS-EXT-STS:power_state"
                    Number value: 0
                Member Key: "config_drive"
                    String value:
                Member Key: "metadata"
                    Object
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.636031000 UTC'
source = '127.0.0.1:49282 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.818054000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49282 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 422
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-7e5c0f0c-efcb-4f5a-b357-1528b44b23a4
    Date: Thu, 26 Nov 2015 21:19:57 GMT
    Connection: keep-alive

    Object
        Member Key: "flavor"
            Object
                Member Key: "name"
                    String value: m1.tiny
                Member Key: "links"
                    Array
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1
                            Member Key: "rel"
                                String value: self
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                            Member Key: "rel"
                                String value: bookmark
                Member Key: "ram"
                    Number value: 512
                Member Key: "OS-FLV-DISABLED:disabled"
                    False value
                Member Key: "vcpus"
                    Number value: 1
                Member Key: "swap"
                    String value:
                Member Key: "os-flavor-access:is_public"
                    True value
                Member Key: "rxtx_factor"
                    Number value: 1.0
                Member Key: "OS-FLV-EXT-DATA:ephemeral"
                    Number value: 0
                Member Key: "disk"
                    Number value: 1
                Member Key: "id"
                    String value: 1
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.849639000 UTC'
source = '127.0.0.1:52603 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/extensions.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.852195000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52603 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 4074
    X-Openstack-Request-Id: req-93afe406-36bd-422d-b82e-1458d55600f4
    Date: Thu, 26 Nov 2015 21:19:57 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "alias"
                        String value: dns-integration
                    Member Key: "updated"
                        String value: 2015-08-15T18:00:00-00:00
                    Member Key: "name"
                        String value: DNS Integration
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides integration with internal DNS.
                Object
                    Member Key: "alias"
                        String value: ext-gw-mode
                    Member Key: "updated"
                        String value: 2013-03-28T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Configurable external gateway mode
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extension of the router abstraction for specifying whether SNAT should occur on the external gateway
                Object
                    Member Key: "alias"
                        String value: binding
                    Member Key: "updated"
                        String value: 2014-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Binding
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose port bindings of a virtual port to external application
                Object
                    Member Key: "alias"
                        String value: agent
                    Member Key: "updated"
                        String value: 2013-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: agent
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The agent management extension.
                Object
                    Member Key: "alias"
                        String value: subnet_allocation
                    Member Key: "updated"
                        String value: 2015-03-30T10:00:00-00:00
                    Member Key: "name"
                        String value: Subnet Allocation
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables allocation of subnets from a subnet pool
                Object
                    Member Key: "alias"
                        String value: l3_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: L3 Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule routers among l3 agents
                Object
                    Member Key: "alias"
                        String value: external-net
                    Member Key: "updated"
                        String value: 2013-01-14T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron external network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Adds external network attribute to network resource.
                Object
                    Member Key: "alias"
                        String value: flavors
                    Member Key: "updated"
                        String value: 2014-07-06T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Service Flavors
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Service specification for advanced services
                Object
                    Member Key: "alias"
                        String value: net-mtu
                    Member Key: "updated"
                        String value: 2015-03-25T10:00:00-00:00
                    Member Key: "name"
                        String value: Network MTU
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides MTU attribute for a network resource.
                Object
                    Member Key: "alias"
                        String value: quotas
                    Member Key: "updated"
                        String value: 2012-07-29T10:00:00-00:00
                    Member Key: "name"
                        String value: Quota management support
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose functions for quotas management per tenant
                Object
                    Member Key: "alias"
                        String value: l3-ha
                    Member Key: "updated"
                        String value: 2014-04-26T00:00:00-00:00
                    Member Key: "name"
                        String value: HA Router extension
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Add HA capability to routers.
                Object
                    Member Key: "alias"
                        String value: provider
                    Member Key: "updated"
                        String value: 2012-09-07T10:00:00-00:00
                    Member Key: "name"
                        String value: Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to physical networks
                Object
                    Member Key: "alias"
                        String value: multi-provider
                    Member Key: "updated"
                        String value: 2013-06-27T10:00:00-00:00
                    Member Key: "name"
                        String value: Multi Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to multiple physical networks
                Object
                    Member Key: "alias"
                        String value: extraroute
                    Member Key: "updated"
                        String value: 2013-02-01T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra Route
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra routes configuration for L3 router
                Object
                    Member Key: "alias"
                        String value: router
                    Member Key: "updated"
                        String value: 2012-07-20T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Router abstraction for basic L3 forwarding between L2 Neutron networks and access to external networks via a NAT gateway.
                Object
                    Member Key: "alias"
                        String value: extra_dhcp_opt
                    Member Key: "updated"
                        String value: 2013-03-17T12:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra DHCP opts
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra options configuration for DHCP. For example PXE boot options to DHCP clients can be specified (e.g. tftp-server, server-ip-address, bootfile-name)
                Object
                    Member Key: "alias"
                        String value: security-group
                    Member Key: "updated"
                        String value: 2012-10-05T10:00:00-00:00
                    Member Key: "name"
                        String value: security-group
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The security groups extension.
                Object
                    Member Key: "alias"
                        String value: dhcp_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: DHCP Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule networks among dhcp agents
                Object
                    Member Key: "alias"
                        String value: rbac-policies
                    Member Key: "updated"
                        String value: 2015-06-17T12:15:12-30:00
                    Member Key: "name"
                        String value: RBAC Policies
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Allows creation and modification of policies that control tenant access to resources.
                Object
                    Member Key: "alias"
                        String value: port-security
                    Member Key: "updated"
                        String value: 2012-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Security
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides port security
                Object
                    Member Key: "alias"
                        String value: allowed-address-pairs
                    Member Key: "updated"
                        String value: 2013-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Allowed Address Pairs
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides allowed address pairs
                Object
                    Member Key: "alias"
                        String value: dvr
                    Member Key: "updated"
                        String value: 2014-06-1T10:00:00-00:00
                    Member Key: "name"
                        String value: Distributed Virtual Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables configuration of Distributed Virtual Routers.
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.856568000 UTC'
source = '127.0.0.1:49286 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/extensions HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:19:57.885954000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49286 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 21496
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-decc65d1-886d-43dc-a6d0-b16b6a9bfa15
    Date: Thu, 26 Nov 2015 21:19:57 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: Multinic
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: NMN
                    Member Key: "description"
                        String value: Multiple network support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: DiskConfig
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-DCF
                    Member Key: "description"
                        String value: Disk Management Extension.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedAvailabilityZone
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-AZ
                    Member Key: "description"
                        String value: Extended Availability Zone support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ImageSize
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IMG-SIZE
                    Member Key: "description"
                        String value: Adds image size to image listings.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIps
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIpsMac
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS-MAC
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedServerAttributes
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-SRV-ATTR
                    Member Key: "description"
                        String value: Extended Server Attributes support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedStatus
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-STS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorDisabled
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-DISABLED
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorExtraData
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-EXT-DATA
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: SchedulerHints
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SCH-HNT
                    Member Key: "description"
                        String value: Pass arbitrary key/value pairs to the scheduler.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ServerUsage
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SRV-USG
                    Member Key: "description"
                        String value: Adds launched_at and terminated_at on Servers.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AccessIPs
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-access-ips
                    Member Key: "description"
                        String value: Access IPs support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AdminActions
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-admin-actions
                    Member Key: "description"
                        String value: Enable admin-only server actions
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:02.965184000 UTC'
source = '127.0.0.1:49287 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:03.032269000 UTC'
source = '127.0.0.1:52299 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/ports.json?device_id=a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:03.055579000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52299 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1161
    X-Openstack-Request-Id: req-dbc27bba-ba9e-4634-94f6-d90e9b45003e
    Date: Thu, 26 Nov 2015 21:20:03 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                            Object
                                Member Key: "hostname"
                                    String value: host-10-28-0-24
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                                Member Key: "fqdn"
                                    String value: host-10-28-0-24.openstacklocal.
                            Object
                                Member Key: "hostname"
                                    String value: host-fd5f-5d21-845-1c2e-2--18
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                                Member Key: "fqdn"
                                    String value: host-fd5f-5d21-845-1c2e-2--18.openstacklocal.
                    Member Key: "device_owner"
                        String value: compute:None
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                            Object
                                Member Key: "subnet_id"
                                    String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                            Object
                                Member Key: "subnet_id"
                                    String value: b83ccd70-35c7-4877-8034-5e58c631411f
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                    Member Key: "id"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "security_groups"
                        Array
                            String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "device_id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "mac_address"
                        String value: fa:16:3e:24:ac:4e
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:03.059675000 UTC'
source = '127.0.0.1:52299 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/security-groups.json?id=e6adf5ab-bcd8-41c0-91aa-4d73354d39e7 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:03.081107000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52299 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1550
    X-Openstack-Request-Id: req-58e0c934-b4f4-43d7-951d-e37386d6fc65
    Date: Thu, 26 Nov 2015 21:20:03 GMT
    Connection: keep-alive

    Object
        Member Key: "security_groups"
            Array
                Object
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "description"
                        String value: Default security group
                    Member Key: "id"
                        String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "security_group_rules"
                        Array
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: 991a8e06-dd5e-4024-8773-c4e38e96cdc5
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c116db16-5fdf-4ae1-8c98-41999120f3a1
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c1f4a0f6-db06-4c6b-87a1-47aa837a657a
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: f1bca7e8-17cd-4833-a548-6fbbd8f07c64
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "name"
                        String value: default
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:03.085418000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49287 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 1816
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-ca35c807-aee3-4bb6-8145-1c14ab424d79
    Date: Thu, 26 Nov 2015 21:20:03 GMT
    Connection: keep-alive

    Object
        Member Key: "server"
            Object
                Member Key: "status"
                    String value: ACTIVE
                Member Key: "updated"
                    String value: 2015-11-26T21:19:57Z
                Member Key: "hostId"
                    String value: 3da7ee3dfd5690185ffc85c0c6459cbd4b496ea3b036f5972243109c
                Member Key: "OS-EXT-SRV-ATTR:host"
                    String value: calico-vm23
                Member Key: "addresses"
                    Object
                        Member Key: "demo-net"
                            Array
                                Object
                                    Member Key: "OS-EXT-IPS-MAC:mac_addr"
                                        String value: fa:16:3e:24:ac:4e
                                    Member Key: "version"
                                        Number value: 4
                                    Member Key: "addr"
                                        String value: 10.28.0.24
                                    Member Key: "OS-EXT-IPS:type"
                                        String value: fixed
                                Object
                                    Member Key: "OS-EXT-IPS-MAC:mac_addr"
                                        String value: fa:16:3e:24:ac:4e
                                    Member Key: "version"
                                        Number value: 6
                                    Member Key: "addr"
                                        String value: fd5f:5d21:845:1c2e:2::18
                                    Member Key: "OS-EXT-IPS:type"
                                        String value: fixed
                Member Key: "links"
                    Array
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                            Member Key: "rel"
                                String value: self
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                            Member Key: "rel"
                                String value: bookmark
                Member Key: "key_name"
                    String value: test
                Member Key: "image"
                    Object
                        Member Key: "id"
                            String value: 4bc635c1-0abb-4a7a-9519-80522deaf327
                        Member Key: "links"
                            Array
                                Object
                                    Member Key: "href"
                                        String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/images/4bc635c1-0abb-4a7a-9519-80522deaf327
                                    Member Key: "rel"
                                        String value: bookmark
                Member Key: "OS-EXT-STS:task_state"
                    Null value
                Member Key: "OS-EXT-STS:vm_state"
                    String value: active
                Member Key: "OS-EXT-SRV-ATTR:instance_name"
                    String value: instance-00000018
                Member Key: "OS-SRV-USG:launched_at"
                    String value: 2015-11-26T21:19:57.000000
                Member Key: "OS-EXT-SRV-ATTR:hypervisor_hostname"
                    String value: calico-vm23
                Member Key: "flavor"
                    Object
                        Member Key: "id"
                            String value: 1
                        Member Key: "links"
                            Array
                                Object
                                    Member Key: "href"
                                        String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                                    Member Key: "rel"
                                        String value: bookmark
                Member Key: "id"
                    String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                Member Key: "security_groups"
                    Array
                        Object
                            Member Key: "name"
                                String value: default
                Member Key: "OS-SRV-USG:terminated_at"
                    Null value
                Member Key: "OS-EXT-AZ:availability_zone"
                    String value: calico-vm23
                Member Key: "user_id"
                    String value: 9eced15c8e6e42d7bee315954927129e
                Member Key: "name"
                    String value: AAA
                Member Key: "created"
                    String value: 2015-11-26T21:19:53Z
                Member Key: "tenant_id"
                    String value: 410bd97d893c45c88ed7709cf936b673
                Member Key: "OS-DCF:diskConfig"
                    String value: AUTO
                Member Key: "os-extended-volumes:volumes_attached"
                    Array
                Member Key: "accessIPv4"
                    String value:
                Member Key: "accessIPv6"
                    String value:
                Member Key: "progress"
                    Number value: 0
                Member Key: "OS-EXT-STS:power_state"
                    Number value: 1
                Member Key: "config_drive"
                    String value: True
                Member Key: "metadata"
                    Object
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:03.088774000 UTC'
source = '127.0.0.1:49288 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:03.104564000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49288 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 422
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-444e8e0b-be5e-4302-9be6-e0789a7a5985
    Date: Thu, 26 Nov 2015 21:20:03 GMT
    Connection: keep-alive

    Object
        Member Key: "flavor"
            Object
                Member Key: "name"
                    String value: m1.tiny
                Member Key: "links"
                    Array
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1
                            Member Key: "rel"
                                String value: self
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                            Member Key: "rel"
                                String value: bookmark
                Member Key: "ram"
                    Number value: 512
                Member Key: "OS-FLV-DISABLED:disabled"
                    False value
                Member Key: "vcpus"
                    Number value: 1
                Member Key: "swap"
                    String value:
                Member Key: "os-flavor-access:is_public"
                    True value
                Member Key: "rxtx_factor"
                    Number value: 1.0
                Member Key: "OS-FLV-EXT-DATA:ephemeral"
                    Number value: 0
                Member Key: "disk"
                    Number value: 1
                Member Key: "id"
                    String value: 1
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:03.136276000 UTC'
source = '127.0.0.1:52609 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/extensions.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:03.138739000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52609 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 4074
    X-Openstack-Request-Id: req-7bfefc9d-0edc-4336-a76a-3af570bdba9a
    Date: Thu, 26 Nov 2015 21:20:03 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "alias"
                        String value: dns-integration
                    Member Key: "updated"
                        String value: 2015-08-15T18:00:00-00:00
                    Member Key: "name"
                        String value: DNS Integration
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides integration with internal DNS.
                Object
                    Member Key: "alias"
                        String value: ext-gw-mode
                    Member Key: "updated"
                        String value: 2013-03-28T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Configurable external gateway mode
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extension of the router abstraction for specifying whether SNAT should occur on the external gateway
                Object
                    Member Key: "alias"
                        String value: binding
                    Member Key: "updated"
                        String value: 2014-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Binding
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose port bindings of a virtual port to external application
                Object
                    Member Key: "alias"
                        String value: agent
                    Member Key: "updated"
                        String value: 2013-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: agent
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The agent management extension.
                Object
                    Member Key: "alias"
                        String value: subnet_allocation
                    Member Key: "updated"
                        String value: 2015-03-30T10:00:00-00:00
                    Member Key: "name"
                        String value: Subnet Allocation
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables allocation of subnets from a subnet pool
                Object
                    Member Key: "alias"
                        String value: l3_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: L3 Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule routers among l3 agents
                Object
                    Member Key: "alias"
                        String value: external-net
                    Member Key: "updated"
                        String value: 2013-01-14T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron external network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Adds external network attribute to network resource.
                Object
                    Member Key: "alias"
                        String value: flavors
                    Member Key: "updated"
                        String value: 2014-07-06T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Service Flavors
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Service specification for advanced services
                Object
                    Member Key: "alias"
                        String value: net-mtu
                    Member Key: "updated"
                        String value: 2015-03-25T10:00:00-00:00
                    Member Key: "name"
                        String value: Network MTU
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides MTU attribute for a network resource.
                Object
                    Member Key: "alias"
                        String value: quotas
                    Member Key: "updated"
                        String value: 2012-07-29T10:00:00-00:00
                    Member Key: "name"
                        String value: Quota management support
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose functions for quotas management per tenant
                Object
                    Member Key: "alias"
                        String value: l3-ha
                    Member Key: "updated"
                        String value: 2014-04-26T00:00:00-00:00
                    Member Key: "name"
                        String value: HA Router extension
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Add HA capability to routers.
                Object
                    Member Key: "alias"
                        String value: provider
                    Member Key: "updated"
                        String value: 2012-09-07T10:00:00-00:00
                    Member Key: "name"
                        String value: Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to physical networks
                Object
                    Member Key: "alias"
                        String value: multi-provider
                    Member Key: "updated"
                        String value: 2013-06-27T10:00:00-00:00
                    Member Key: "name"
                        String value: Multi Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to multiple physical networks
                Object
                    Member Key: "alias"
                        String value: extraroute
                    Member Key: "updated"
                        String value: 2013-02-01T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra Route
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra routes configuration for L3 router
                Object
                    Member Key: "alias"
                        String value: router
                    Member Key: "updated"
                        String value: 2012-07-20T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Router abstraction for basic L3 forwarding between L2 Neutron networks and access to external networks via a NAT gateway.
                Object
                    Member Key: "alias"
                        String value: extra_dhcp_opt
                    Member Key: "updated"
                        String value: 2013-03-17T12:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra DHCP opts
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra options configuration for DHCP. For example PXE boot options to DHCP clients can be specified (e.g. tftp-server, server-ip-address, bootfile-name)
                Object
                    Member Key: "alias"
                        String value: security-group
                    Member Key: "updated"
                        String value: 2012-10-05T10:00:00-00:00
                    Member Key: "name"
                        String value: security-group
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The security groups extension.
                Object
                    Member Key: "alias"
                        String value: dhcp_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: DHCP Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule networks among dhcp agents
                Object
                    Member Key: "alias"
                        String value: rbac-policies
                    Member Key: "updated"
                        String value: 2015-06-17T12:15:12-30:00
                    Member Key: "name"
                        String value: RBAC Policies
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Allows creation and modification of policies that control tenant access to resources.
                Object
                    Member Key: "alias"
                        String value: port-security
                    Member Key: "updated"
                        String value: 2012-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Security
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides port security
                Object
                    Member Key: "alias"
                        String value: allowed-address-pairs
                    Member Key: "updated"
                        String value: 2013-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Allowed Address Pairs
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides allowed address pairs
                Object
                    Member Key: "alias"
                        String value: dvr
                    Member Key: "updated"
                        String value: 2014-06-1T10:00:00-00:00
                    Member Key: "name"
                        String value: Distributed Virtual Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables configuration of Distributed Virtual Routers.
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:03.143228000 UTC'
source = '127.0.0.1:49292 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/extensions HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:03.174154000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49292 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 21496
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-d3aa0873-64d1-4ecc-b113-8de3880d02eb
    Date: Thu, 26 Nov 2015 21:20:03 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: Multinic
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: NMN
                    Member Key: "description"
                        String value: Multiple network support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: DiskConfig
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-DCF
                    Member Key: "description"
                        String value: Disk Management Extension.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedAvailabilityZone
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-AZ
                    Member Key: "description"
                        String value: Extended Availability Zone support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ImageSize
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IMG-SIZE
                    Member Key: "description"
                        String value: Adds image size to image listings.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIps
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIpsMac
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS-MAC
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedServerAttributes
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-SRV-ATTR
                    Member Key: "description"
                        String value: Extended Server Attributes support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedStatus
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-STS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorDisabled
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-DISABLED
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorExtraData
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-EXT-DATA
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: SchedulerHints
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SCH-HNT
                    Member Key: "description"
                        String value: Pass arbitrary key/value pairs to the scheduler.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ServerUsage
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SRV-USG
                    Member Key: "description"
                        String value: Adds launched_at and terminated_at on Servers.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AccessIPs
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-access-ips
                    Member Key: "description"
                        String value: Access IPs support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AdminActions
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-admin-actions
                    Member Key: "description"
                        String value: Enable admin-only server actions
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.565406000 UTC'
source = '127.0.0.1:49293 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/servers/detail?limit=21&project_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.626173000 UTC'
source = '127.0.0.1:52299 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/ports.json?device_id=a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.645393000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52299 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1161
    X-Openstack-Request-Id: req-e7234ca2-abfe-4331-874f-c464f70eda0c
    Date: Thu, 26 Nov 2015 21:20:07 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                            Object
                                Member Key: "hostname"
                                    String value: host-10-28-0-24
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                                Member Key: "fqdn"
                                    String value: host-10-28-0-24.openstacklocal.
                            Object
                                Member Key: "hostname"
                                    String value: host-fd5f-5d21-845-1c2e-2--18
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                                Member Key: "fqdn"
                                    String value: host-fd5f-5d21-845-1c2e-2--18.openstacklocal.
                    Member Key: "device_owner"
                        String value: compute:None
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                            Object
                                Member Key: "subnet_id"
                                    String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                            Object
                                Member Key: "subnet_id"
                                    String value: b83ccd70-35c7-4877-8034-5e58c631411f
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                    Member Key: "id"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "security_groups"
                        Array
                            String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "device_id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "mac_address"
                        String value: fa:16:3e:24:ac:4e
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.651767000 UTC'
source = '127.0.0.1:52299 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/security-groups.json?id=e6adf5ab-bcd8-41c0-91aa-4d73354d39e7 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.672685000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52299 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1550
    X-Openstack-Request-Id: req-75135459-c8c8-4c12-a8e3-1d25e8ac09a9
    Date: Thu, 26 Nov 2015 21:20:07 GMT
    Connection: keep-alive

    Object
        Member Key: "security_groups"
            Array
                Object
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "description"
                        String value: Default security group
                    Member Key: "id"
                        String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "security_group_rules"
                        Array
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: 991a8e06-dd5e-4024-8773-c4e38e96cdc5
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c116db16-5fdf-4ae1-8c98-41999120f3a1
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c1f4a0f6-db06-4c6b-87a1-47aa837a657a
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: f1bca7e8-17cd-4833-a548-6fbbd8f07c64
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "name"
                        String value: default
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.676269000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49293 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 1819
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-fc7d5f9a-5dfa-40ef-bc89-76c8c663a6b9
    Date: Thu, 26 Nov 2015 21:20:07 GMT
    Connection: keep-alive

    Object
        Member Key: "servers"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "updated"
                        String value: 2015-11-26T21:19:57Z
                    Member Key: "hostId"
                        String value: 3da7ee3dfd5690185ffc85c0c6459cbd4b496ea3b036f5972243109c
                    Member Key: "OS-EXT-SRV-ATTR:host"
                        String value: calico-vm23
                    Member Key: "addresses"
                        Object
                            Member Key: "demo-net"
                                Array
                                    Object
                                        Member Key: "OS-EXT-IPS-MAC:mac_addr"
                                            String value: fa:16:3e:24:ac:4e
                                        Member Key: "version"
                                            Number value: 4
                                        Member Key: "addr"
                                            String value: 10.28.0.24
                                        Member Key: "OS-EXT-IPS:type"
                                            String value: fixed
                                    Object
                                        Member Key: "OS-EXT-IPS-MAC:mac_addr"
                                            String value: fa:16:3e:24:ac:4e
                                        Member Key: "version"
                                            Number value: 6
                                        Member Key: "addr"
                                            String value: fd5f:5d21:845:1c2e:2::18
                                        Member Key: "OS-EXT-IPS:type"
                                            String value: fixed
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "key_name"
                        String value: test
                    Member Key: "image"
                        Object
                            Member Key: "id"
                                String value: 4bc635c1-0abb-4a7a-9519-80522deaf327
                            Member Key: "links"
                                Array
                                    Object
                                        Member Key: "href"
                                            String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/images/4bc635c1-0abb-4a7a-9519-80522deaf327
                                        Member Key: "rel"
                                            String value: bookmark
                    Member Key: "OS-EXT-STS:task_state"
                        Null value
                    Member Key: "OS-EXT-STS:vm_state"
                        String value: active
                    Member Key: "OS-EXT-SRV-ATTR:instance_name"
                        String value: instance-00000018
                    Member Key: "OS-SRV-USG:launched_at"
                        String value: 2015-11-26T21:19:57.000000
                    Member Key: "OS-EXT-SRV-ATTR:hypervisor_hostname"
                        String value: calico-vm23
                    Member Key: "flavor"
                        Object
                            Member Key: "id"
                                String value: 1
                            Member Key: "links"
                                Array
                                    Object
                                        Member Key: "href"
                                            String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                                        Member Key: "rel"
                                            String value: bookmark
                    Member Key: "id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "security_groups"
                        Array
                            Object
                                Member Key: "name"
                                    String value: default
                    Member Key: "OS-SRV-USG:terminated_at"
                        Null value
                    Member Key: "OS-EXT-AZ:availability_zone"
                        String value: calico-vm23
                    Member Key: "user_id"
                        String value: 9eced15c8e6e42d7bee315954927129e
                    Member Key: "name"
                        String value: AAA
                    Member Key: "created"
                        String value: 2015-11-26T21:19:53Z
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "OS-DCF:diskConfig"
                        String value: AUTO
                    Member Key: "os-extended-volumes:volumes_attached"
                        Array
                    Member Key: "accessIPv4"
                        String value:
                    Member Key: "accessIPv6"
                        String value:
                    Member Key: "progress"
                        Number value: 0
                    Member Key: "OS-EXT-STS:power_state"
                        Number value: 1
                    Member Key: "config_drive"
                        String value: True
                    Member Key: "metadata"
                        Object
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.682184000 UTC'
source = '127.0.0.1:52612 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/ports.json?device_id=a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.703529000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52612 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1161
    X-Openstack-Request-Id: req-4b2263fa-3075-41e4-a577-be7ba9b6dd4c
    Date: Thu, 26 Nov 2015 21:20:07 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                            Object
                                Member Key: "hostname"
                                    String value: host-10-28-0-24
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                                Member Key: "fqdn"
                                    String value: host-10-28-0-24.openstacklocal.
                            Object
                                Member Key: "hostname"
                                    String value: host-fd5f-5d21-845-1c2e-2--18
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                                Member Key: "fqdn"
                                    String value: host-fd5f-5d21-845-1c2e-2--18.openstacklocal.
                    Member Key: "device_owner"
                        String value: compute:None
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                            Object
                                Member Key: "subnet_id"
                                    String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                            Object
                                Member Key: "subnet_id"
                                    String value: b83ccd70-35c7-4877-8034-5e58c631411f
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                    Member Key: "id"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "security_groups"
                        Array
                            String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "device_id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "mac_address"
                        String value: fa:16:3e:24:ac:4e
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.709851000 UTC'
source = '127.0.0.1:52613 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/floatingips.json?tenant_id=410bd97d893c45c88ed7709cf936b673&port_id=9792cbef-b9a4-4860-9cc6-342695aa80be HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.715169000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52613 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 19
    X-Openstack-Request-Id: req-cb11bf1d-5b29-499b-beb1-30b7d74cd921
    Date: Thu, 26 Nov 2015 21:20:07 GMT
    Connection: keep-alive

    Object
        Member Key: "floatingips"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.716978000 UTC'
source = '127.0.0.1:52614 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/ports.json?tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.735582000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52614 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1161
    X-Openstack-Request-Id: req-bca6bf34-2ea6-4912-a3cc-43a7e3c4c73a
    Date: Thu, 26 Nov 2015 21:20:07 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                            Object
                                Member Key: "hostname"
                                    String value: host-10-28-0-24
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                                Member Key: "fqdn"
                                    String value: host-10-28-0-24.openstacklocal.
                            Object
                                Member Key: "hostname"
                                    String value: host-fd5f-5d21-845-1c2e-2--18
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                                Member Key: "fqdn"
                                    String value: host-fd5f-5d21-845-1c2e-2--18.openstacklocal.
                    Member Key: "device_owner"
                        String value: compute:None
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                            Object
                                Member Key: "subnet_id"
                                    String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                            Object
                                Member Key: "subnet_id"
                                    String value: b83ccd70-35c7-4877-8034-5e58c631411f
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                    Member Key: "id"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "security_groups"
                        Array
                            String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "device_id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "mac_address"
                        String value: fa:16:3e:24:ac:4e
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.739770000 UTC'
source = '127.0.0.1:52615 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/networks.json?id=eb463966-6328-427c-964d-2134a835dc8f HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.761957000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52615 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 454
    X-Openstack-Request-Id: req-922ddf2f-fffa-4ce5-9207-01ca67c4550e
    Date: Thu, 26 Nov 2015 21:20:07 GMT
    Connection: keep-alive

    Object
        Member Key: "networks"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "subnets"
                        Array
                            String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                            String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "name"
                        String value: demo-net
                    Member Key: "provider:physical_network"
                        Null value
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mtu"
                        Number value: 0
                    Member Key: "router:external"
                        False value
                    Member Key: "shared"
                        True value
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "provider:network_type"
                        String value: local
                    Member Key: "id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "provider:segmentation_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.766009000 UTC'
source = '127.0.0.1:52616 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/subnets.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.790191000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52616 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 961
    X-Openstack-Request-Id: req-e5b34e07-9b4e-4f13-b9f9-9d58bcb7c4b4
    Date: Thu, 26 Nov 2015 21:20:07 GMT
    Connection: keep-alive

    Object
        Member Key: "subnets"
            Array
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: 10.28.0.1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: 10.28.0.2
                                Member Key: "end"
                                    String value: 10.28.255.254
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 4
                    Member Key: "ipv6_address_mode"
                        Null value
                    Member Key: "cidr"
                        String value: 10.28.0.0/16
                    Member Key: "id"
                        String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                    Member Key: "subnetpool_id"
                        Null value
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: fd5f:5d21:845:1c2e:2::1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: fd5f:5d21:845:1c2e:2::2
                                Member Key: "end"
                                    String value: fd5f:5d21:845:1c2e:2:ffff:ffff:ffff
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 6
                    Member Key: "ipv6_address_mode"
                        String value: dhcpv6-stateful
                    Member Key: "cidr"
                        String value: fd5f:5d21:845:1c2e:2::/80
                    Member Key: "id"
                        String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "subnetpool_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.792944000 UTC'
source = '127.0.0.1:49299 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/flavors/detail HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.813174000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49299 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 2089
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-cbd4b476-9958-464c-b043-d9fdc271ef7e
    Date: Thu, 26 Nov 2015 21:20:07 GMT
    Connection: keep-alive

    Object
        Member Key: "flavors"
            Array
                Object
                    Member Key: "name"
                        String value: m1.tiny
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 512
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 1
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 1
                    Member Key: "id"
                        String value: 1
                Object
                    Member Key: "name"
                        String value: m1.small
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/2
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/2
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 2048
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 1
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 20
                    Member Key: "id"
                        String value: 2
                Object
                    Member Key: "name"
                        String value: m1.medium
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/3
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/3
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 4096
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 2
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 40
                    Member Key: "id"
                        String value: 3
                Object
                    Member Key: "name"
                        String value: m1.large
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/4
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/4
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 8192
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 4
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 80
                    Member Key: "id"
                        String value: 4
                Object
                    Member Key: "name"
                        String value: m1.xlarge
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/5
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/5
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 16384
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 8
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 160
                    Member Key: "id"
                        String value: 5
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:07.865920000 UTC'
source = '127.0.0.1:49302 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    DELETE /v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Content-Length: 0
    Accept: application/json
    User-Agent: python-novaclient
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.012831000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49302 (unknown)'
detail = """    HTTP/1.1 204 No Content
    Content-Length: 0
    Content-Type: application/json
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-31cdf7a2-b2d6-45f8-9f7c-2589c96f4078
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.033187000 UTC'
source = '127.0.0.1:49303 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/servers/detail?limit=21&project_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.091242000 UTC'
source = '127.0.0.1:52238 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/ports.json?device_id=a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.118243000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52238 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1161
    X-Openstack-Request-Id: req-508df88a-a42b-412f-a5cb-8493933b8af1
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                            Object
                                Member Key: "hostname"
                                    String value: host-10-28-0-24
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                                Member Key: "fqdn"
                                    String value: host-10-28-0-24.openstacklocal.
                            Object
                                Member Key: "hostname"
                                    String value: host-fd5f-5d21-845-1c2e-2--18
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                                Member Key: "fqdn"
                                    String value: host-fd5f-5d21-845-1c2e-2--18.openstacklocal.
                    Member Key: "device_owner"
                        String value: compute:None
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                            Object
                                Member Key: "subnet_id"
                                    String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                            Object
                                Member Key: "subnet_id"
                                    String value: b83ccd70-35c7-4877-8034-5e58c631411f
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                    Member Key: "id"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "security_groups"
                        Array
                            String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "device_id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "mac_address"
                        String value: fa:16:3e:24:ac:4e
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.120429000 UTC'
source = '127.0.0.1:52238 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/security-groups.json?id=e6adf5ab-bcd8-41c0-91aa-4d73354d39e7 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.137834000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52238 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1550
    X-Openstack-Request-Id: req-8d4e1dfb-caa6-4d46-b726-f6d64f153ccb
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "security_groups"
            Array
                Object
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "description"
                        String value: Default security group
                    Member Key: "id"
                        String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "security_group_rules"
                        Array
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: 991a8e06-dd5e-4024-8773-c4e38e96cdc5
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                                Member Key: "direction"
                                    String value: ingress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c116db16-5fdf-4ae1-8c98-41999120f3a1
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv6
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: c1f4a0f6-db06-4c6b-87a1-47aa837a657a
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                            Object
                                Member Key: "remote_group_id"
                                    Null value
                                Member Key: "direction"
                                    String value: egress
                                Member Key: "remote_ip_prefix"
                                    Null value
                                Member Key: "protocol"
                                    Null value
                                Member Key: "ethertype"
                                    String value: IPv4
                                Member Key: "tenant_id"
                                    String value: 410bd97d893c45c88ed7709cf936b673
                                Member Key: "port_range_max"
                                    Null value
                                Member Key: "port_range_min"
                                    Null value
                                Member Key: "id"
                                    String value: f1bca7e8-17cd-4833-a548-6fbbd8f07c64
                                Member Key: "security_group_id"
                                    String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "name"
                        String value: default
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.140026000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49303 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 1825
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-0e751cec-e5a6-442b-9b9e-8d4771a3b1a3
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "servers"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "updated"
                        String value: 2015-11-26T21:20:07Z
                    Member Key: "hostId"
                        String value: 3da7ee3dfd5690185ffc85c0c6459cbd4b496ea3b036f5972243109c
                    Member Key: "OS-EXT-SRV-ATTR:host"
                        String value: calico-vm23
                    Member Key: "addresses"
                        Object
                            Member Key: "demo-net"
                                Array
                                    Object
                                        Member Key: "OS-EXT-IPS-MAC:mac_addr"
                                            String value: fa:16:3e:24:ac:4e
                                        Member Key: "version"
                                            Number value: 4
                                        Member Key: "addr"
                                            String value: 10.28.0.24
                                        Member Key: "OS-EXT-IPS:type"
                                            String value: fixed
                                    Object
                                        Member Key: "OS-EXT-IPS-MAC:mac_addr"
                                            String value: fa:16:3e:24:ac:4e
                                        Member Key: "version"
                                            Number value: 6
                                        Member Key: "addr"
                                            String value: fd5f:5d21:845:1c2e:2::18
                                        Member Key: "OS-EXT-IPS:type"
                                            String value: fixed
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "key_name"
                        String value: test
                    Member Key: "image"
                        Object
                            Member Key: "id"
                                String value: 4bc635c1-0abb-4a7a-9519-80522deaf327
                            Member Key: "links"
                                Array
                                    Object
                                        Member Key: "href"
                                            String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/images/4bc635c1-0abb-4a7a-9519-80522deaf327
                                        Member Key: "rel"
                                            String value: bookmark
                    Member Key: "OS-EXT-STS:task_state"
                        String value: deleting
                    Member Key: "OS-EXT-STS:vm_state"
                        String value: active
                    Member Key: "OS-EXT-SRV-ATTR:instance_name"
                        String value: instance-00000018
                    Member Key: "OS-SRV-USG:launched_at"
                        String value: 2015-11-26T21:19:57.000000
                    Member Key: "OS-EXT-SRV-ATTR:hypervisor_hostname"
                        String value: calico-vm23
                    Member Key: "flavor"
                        Object
                            Member Key: "id"
                                String value: 1
                            Member Key: "links"
                                Array
                                    Object
                                        Member Key: "href"
                                            String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                                        Member Key: "rel"
                                            String value: bookmark
                    Member Key: "id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "security_groups"
                        Array
                            Object
                                Member Key: "name"
                                    String value: default
                    Member Key: "OS-SRV-USG:terminated_at"
                        Null value
                    Member Key: "OS-EXT-AZ:availability_zone"
                        String value: calico-vm23
                    Member Key: "user_id"
                        String value: 9eced15c8e6e42d7bee315954927129e
                    Member Key: "name"
                        String value: AAA
                    Member Key: "created"
                        String value: 2015-11-26T21:19:53Z
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "OS-DCF:diskConfig"
                        String value: AUTO
                    Member Key: "os-extended-volumes:volumes_attached"
                        Array
                    Member Key: "accessIPv4"
                        String value:
                    Member Key: "accessIPv6"
                        String value:
                    Member Key: "progress"
                        Number value: 0
                    Member Key: "OS-EXT-STS:power_state"
                        Number value: 1
                    Member Key: "config_drive"
                        String value: True
                    Member Key: "metadata"
                        Object
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.143041000 UTC'
source = '127.0.0.1:52622 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/ports.json?device_id=a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.164026000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52622 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1159
    X-Openstack-Request-Id: req-d1b21bac-ffc2-4900-83c6-2338f6a32083
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                            Object
                                Member Key: "hostname"
                                    String value: host-10-28-0-24
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                                Member Key: "fqdn"
                                    String value: host-10-28-0-24.openstacklocal.
                            Object
                                Member Key: "hostname"
                                    String value: host-fd5f-5d21-845-1c2e-2--18
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                                Member Key: "fqdn"
                                    String value: host-fd5f-5d21-845-1c2e-2--18.openstacklocal.
                    Member Key: "device_owner"
                        String value: compute:None
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                            Object
                                Member Key: "subnet_id"
                                    String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                            Object
                                Member Key: "subnet_id"
                                    String value: b83ccd70-35c7-4877-8034-5e58c631411f
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                    Member Key: "id"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "security_groups"
                        Array
                            String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "device_id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "mac_address"
                        String value: fa:16:3e:24:ac:4e
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.166004000 UTC'
source = '127.0.0.1:52623 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/floatingips.json?tenant_id=410bd97d893c45c88ed7709cf936b673&port_id=9792cbef-b9a4-4860-9cc6-342695aa80be HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.176610000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52623 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 19
    X-Openstack-Request-Id: req-84152adf-91b7-40a0-9ebe-dd605e600c1f
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "floatingips"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.181033000 UTC'
source = '127.0.0.1:52624 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/ports.json?tenant_id=410bd97d893c45c88ed7709cf936b673 HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.200807000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52624 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1159
    X-Openstack-Request-Id: req-b3e32327-b8cf-4415-86b8-9c1b1e514379
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                            Object
                                Member Key: "hostname"
                                    String value: host-10-28-0-24
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                                Member Key: "fqdn"
                                    String value: host-10-28-0-24.openstacklocal.
                            Object
                                Member Key: "hostname"
                                    String value: host-fd5f-5d21-845-1c2e-2--18
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                                Member Key: "fqdn"
                                    String value: host-fd5f-5d21-845-1c2e-2--18.openstacklocal.
                    Member Key: "device_owner"
                        String value: compute:None
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                            Object
                                Member Key: "subnet_id"
                                    String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                            Object
                                Member Key: "subnet_id"
                                    String value: b83ccd70-35c7-4877-8034-5e58c631411f
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                    Member Key: "id"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "security_groups"
                        Array
                            String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "device_id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "mac_address"
                        String value: fa:16:3e:24:ac:4e
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.202869000 UTC'
source = '127.0.0.1:52625 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/networks.json?id=eb463966-6328-427c-964d-2134a835dc8f HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.224531000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52625 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 454
    X-Openstack-Request-Id: req-eb445840-24ee-4fdf-898b-f9bee9b01649
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "networks"
            Array
                Object
                    Member Key: "status"
                        String value: ACTIVE
                    Member Key: "subnets"
                        Array
                            String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                            String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "name"
                        String value: demo-net
                    Member Key: "provider:physical_network"
                        Null value
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "mtu"
                        Number value: 0
                    Member Key: "router:external"
                        False value
                    Member Key: "shared"
                        True value
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "provider:network_type"
                        String value: local
                    Member Key: "id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "provider:segmentation_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.226474000 UTC'
source = '127.0.0.1:52626 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/subnets.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.253729000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52626 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 961
    X-Openstack-Request-Id: req-76dbc19a-4e93-4609-a92d-e860d1ab6ae4
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "subnets"
            Array
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: 10.28.0.1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: 10.28.0.2
                                Member Key: "end"
                                    String value: 10.28.255.254
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 4
                    Member Key: "ipv6_address_mode"
                        Null value
                    Member Key: "cidr"
                        String value: 10.28.0.0/16
                    Member Key: "id"
                        String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                    Member Key: "subnetpool_id"
                        Null value
                Object
                    Member Key: "name"
                        String value:
                    Member Key: "enable_dhcp"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "tenant_id"
                        String value: 6f33bcda80c848969b28b9d37a90d11b
                    Member Key: "dns_nameservers"
                        Array
                    Member Key: "gateway_ip"
                        String value: fd5f:5d21:845:1c2e:2::1
                    Member Key: "ipv6_ra_mode"
                        Null value
                    Member Key: "allocation_pools"
                        Array
                            Object
                                Member Key: "start"
                                    String value: fd5f:5d21:845:1c2e:2::2
                                Member Key: "end"
                                    String value: fd5f:5d21:845:1c2e:2:ffff:ffff:ffff
                    Member Key: "host_routes"
                        Array
                    Member Key: "ip_version"
                        Number value: 6
                    Member Key: "ipv6_address_mode"
                        String value: dhcpv6-stateful
                    Member Key: "cidr"
                        String value: fd5f:5d21:845:1c2e:2::/80
                    Member Key: "id"
                        String value: b83ccd70-35c7-4877-8034-5e58c631411f
                    Member Key: "subnetpool_id"
                        Null value
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.255988000 UTC'
source = '127.0.0.1:49309 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/flavors/detail HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.281430000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49309 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 2089
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-f321d239-67d7-4472-a38e-607940f07329
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "flavors"
            Array
                Object
                    Member Key: "name"
                        String value: m1.tiny
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 512
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 1
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 1
                    Member Key: "id"
                        String value: 1
                Object
                    Member Key: "name"
                        String value: m1.small
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/2
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/2
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 2048
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 1
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 20
                    Member Key: "id"
                        String value: 2
                Object
                    Member Key: "name"
                        String value: m1.medium
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/3
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/3
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 4096
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 2
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 40
                    Member Key: "id"
                        String value: 3
                Object
                    Member Key: "name"
                        String value: m1.large
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/4
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/4
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 8192
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 4
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 80
                    Member Key: "id"
                        String value: 4
                Object
                    Member Key: "name"
                        String value: m1.xlarge
                    Member Key: "links"
                        Array
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/5
                                Member Key: "rel"
                                    String value: self
                            Object
                                Member Key: "href"
                                    String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/5
                                Member Key: "rel"
                                    String value: bookmark
                    Member Key: "ram"
                        Number value: 16384
                    Member Key: "OS-FLV-DISABLED:disabled"
                        False value
                    Member Key: "vcpus"
                        Number value: 8
                    Member Key: "swap"
                        String value:
                    Member Key: "os-flavor-access:is_public"
                        True value
                    Member Key: "rxtx_factor"
                        Number value: 1.0
                    Member Key: "OS-FLV-EXT-DATA:ephemeral"
                        Number value: 0
                    Member Key: "disk"
                        Number value: 160
                    Member Key: "id"
                        String value: 5
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.353170000 UTC'
source = '127.0.0.1:52630 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/extensions.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.356492000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52630 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 4074
    X-Openstack-Request-Id: req-6a05eb2c-1ebb-4d7a-a281-267da58d7959
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "alias"
                        String value: dns-integration
                    Member Key: "updated"
                        String value: 2015-08-15T18:00:00-00:00
                    Member Key: "name"
                        String value: DNS Integration
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides integration with internal DNS.
                Object
                    Member Key: "alias"
                        String value: ext-gw-mode
                    Member Key: "updated"
                        String value: 2013-03-28T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Configurable external gateway mode
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extension of the router abstraction for specifying whether SNAT should occur on the external gateway
                Object
                    Member Key: "alias"
                        String value: binding
                    Member Key: "updated"
                        String value: 2014-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Binding
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose port bindings of a virtual port to external application
                Object
                    Member Key: "alias"
                        String value: agent
                    Member Key: "updated"
                        String value: 2013-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: agent
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The agent management extension.
                Object
                    Member Key: "alias"
                        String value: subnet_allocation
                    Member Key: "updated"
                        String value: 2015-03-30T10:00:00-00:00
                    Member Key: "name"
                        String value: Subnet Allocation
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables allocation of subnets from a subnet pool
                Object
                    Member Key: "alias"
                        String value: l3_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: L3 Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule routers among l3 agents
                Object
                    Member Key: "alias"
                        String value: external-net
                    Member Key: "updated"
                        String value: 2013-01-14T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron external network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Adds external network attribute to network resource.
                Object
                    Member Key: "alias"
                        String value: flavors
                    Member Key: "updated"
                        String value: 2014-07-06T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Service Flavors
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Service specification for advanced services
                Object
                    Member Key: "alias"
                        String value: net-mtu
                    Member Key: "updated"
                        String value: 2015-03-25T10:00:00-00:00
                    Member Key: "name"
                        String value: Network MTU
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides MTU attribute for a network resource.
                Object
                    Member Key: "alias"
                        String value: quotas
                    Member Key: "updated"
                        String value: 2012-07-29T10:00:00-00:00
                    Member Key: "name"
                        String value: Quota management support
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose functions for quotas management per tenant
                Object
                    Member Key: "alias"
                        String value: l3-ha
                    Member Key: "updated"
                        String value: 2014-04-26T00:00:00-00:00
                    Member Key: "name"
                        String value: HA Router extension
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Add HA capability to routers.
                Object
                    Member Key: "alias"
                        String value: provider
                    Member Key: "updated"
                        String value: 2012-09-07T10:00:00-00:00
                    Member Key: "name"
                        String value: Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to physical networks
                Object
                    Member Key: "alias"
                        String value: multi-provider
                    Member Key: "updated"
                        String value: 2013-06-27T10:00:00-00:00
                    Member Key: "name"
                        String value: Multi Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to multiple physical networks
                Object
                    Member Key: "alias"
                        String value: extraroute
                    Member Key: "updated"
                        String value: 2013-02-01T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra Route
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra routes configuration for L3 router
                Object
                    Member Key: "alias"
                        String value: router
                    Member Key: "updated"
                        String value: 2012-07-20T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Router abstraction for basic L3 forwarding between L2 Neutron networks and access to external networks via a NAT gateway.
                Object
                    Member Key: "alias"
                        String value: extra_dhcp_opt
                    Member Key: "updated"
                        String value: 2013-03-17T12:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra DHCP opts
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra options configuration for DHCP. For example PXE boot options to DHCP clients can be specified (e.g. tftp-server, server-ip-address, bootfile-name)
                Object
                    Member Key: "alias"
                        String value: security-group
                    Member Key: "updated"
                        String value: 2012-10-05T10:00:00-00:00
                    Member Key: "name"
                        String value: security-group
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The security groups extension.
                Object
                    Member Key: "alias"
                        String value: dhcp_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: DHCP Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule networks among dhcp agents
                Object
                    Member Key: "alias"
                        String value: rbac-policies
                    Member Key: "updated"
                        String value: 2015-06-17T12:15:12-30:00
                    Member Key: "name"
                        String value: RBAC Policies
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Allows creation and modification of policies that control tenant access to resources.
                Object
                    Member Key: "alias"
                        String value: port-security
                    Member Key: "updated"
                        String value: 2012-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Security
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides port security
                Object
                    Member Key: "alias"
                        String value: allowed-address-pairs
                    Member Key: "updated"
                        String value: 2013-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Allowed Address Pairs
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides allowed address pairs
                Object
                    Member Key: "alias"
                        String value: dvr
                    Member Key: "updated"
                        String value: 2014-06-1T10:00:00-00:00
                    Member Key: "name"
                        String value: Distributed Virtual Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables configuration of Distributed Virtual Routers.
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.361601000 UTC'
source = '127.0.0.1:49313 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/extensions HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.402760000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49313 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 21496
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-d58e6d61-0bc7-45d0-abee-2fee7709a5c5
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: Multinic
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: NMN
                    Member Key: "description"
                        String value: Multiple network support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: DiskConfig
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-DCF
                    Member Key: "description"
                        String value: Disk Management Extension.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedAvailabilityZone
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-AZ
                    Member Key: "description"
                        String value: Extended Availability Zone support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ImageSize
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IMG-SIZE
                    Member Key: "description"
                        String value: Adds image size to image listings.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIps
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIpsMac
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS-MAC
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedServerAttributes
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-SRV-ATTR
                    Member Key: "description"
                        String value: Extended Server Attributes support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedStatus
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-STS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorDisabled
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-DISABLED
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorExtraData
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-EXT-DATA
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: SchedulerHints
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SCH-HNT
                    Member Key: "description"
                        String value: Pass arbitrary key/value pairs to the scheduler.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ServerUsage
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SRV-USG
                    Member Key: "description"
                        String value: Adds launched_at and terminated_at on Servers.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AccessIPs
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-access-ips
                    Member Key: "description"
                        String value: Access IPs support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AdminActions
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-admin-actions
                    Member Key: "description"
                        String value: Enable admin-only server actions
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.434939000 UTC'
source = '127.0.0.1:49314 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/limits?reserved=1 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.460476000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49314 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 513
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-3a3f1fdd-855a-4352-b661-18d41ad524b0
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "limits"
            Object
                Member Key: "rate"
                    Array
                Member Key: "absolute"
                    Object
                        Member Key: "maxServerMeta"
                            Number value: 128
                        Member Key: "maxPersonality"
                            Number value: 5
                        Member Key: "totalServerGroupsUsed"
                            Number value: 0
                        Member Key: "maxImageMeta"
                            Number value: 128
                        Member Key: "maxPersonalitySize"
                            Number value: 10240
                        Member Key: "maxTotalKeypairs"
                            Number value: 100
                        Member Key: "maxSecurityGroupRules"
                            Number value: 20
                        Member Key: "maxServerGroups"
                            Number value: 10
                        Member Key: "totalCoresUsed"
                            Number value: 1
                        Member Key: "totalRAMUsed"
                            Number value: 512
                        Member Key: "totalInstancesUsed"
                            Number value: 1
                        Member Key: "maxSecurityGroups"
                            Number value: 10
                        Member Key: "totalFloatingIpsUsed"
                            Number value: 0
                        Member Key: "maxTotalCores"
                            Number value: 20
                        Member Key: "maxServerGroupMembers"
                            Number value: 10
                        Member Key: "maxTotalFloatingIps"
                            Number value: 10
                        Member Key: "totalSecurityGroupsUsed"
                            Number value: 1
                        Member Key: "maxTotalInstances"
                            Number value: 10
                        Member Key: "maxTotalRAMSize"
                            Number value: 51200
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.481291000 UTC'
source = '127.0.0.1:49315 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/limits?reserved=1 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.506267000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49315 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 513
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-32d3611e-0ab4-49dd-9dc0-bcabbdde7eb9
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "limits"
            Object
                Member Key: "rate"
                    Array
                Member Key: "absolute"
                    Object
                        Member Key: "maxServerMeta"
                            Number value: 128
                        Member Key: "maxPersonality"
                            Number value: 5
                        Member Key: "totalServerGroupsUsed"
                            Number value: 0
                        Member Key: "maxImageMeta"
                            Number value: 128
                        Member Key: "maxPersonalitySize"
                            Number value: 10240
                        Member Key: "maxTotalKeypairs"
                            Number value: 100
                        Member Key: "maxSecurityGroupRules"
                            Number value: 20
                        Member Key: "maxServerGroups"
                            Number value: 10
                        Member Key: "totalCoresUsed"
                            Number value: 1
                        Member Key: "totalRAMUsed"
                            Number value: 512
                        Member Key: "totalInstancesUsed"
                            Number value: 1
                        Member Key: "maxSecurityGroups"
                            Number value: 10
                        Member Key: "totalFloatingIpsUsed"
                            Number value: 0
                        Member Key: "maxTotalCores"
                            Number value: 20
                        Member Key: "maxServerGroupMembers"
                            Number value: 10
                        Member Key: "maxTotalFloatingIps"
                            Number value: 10
                        Member Key: "totalSecurityGroupsUsed"
                            Number value: 1
                        Member Key: "maxTotalInstances"
                            Number value: 10
                        Member Key: "maxTotalRAMSize"
                            Number value: 51200
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.651022000 UTC'
source = '172.18.203.99:37182 (unknown)'
dest = '172.18.203.95:9696 (neutron)'
detail = """    GET /v2.0/ports.json?device_id=a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.678284000 UTC'
source = '172.18.203.95:9696 (neutron)'
dest = '172.18.203.99:37182 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 1159
    X-Openstack-Request-Id: req-ff034b7e-ff67-4c7a-8ac5-aa3a52b38e3d
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
                Object
                    Member Key: "status"
                        String value: DOWN
                    Member Key: "binding:host_id"
                        String value: calico-vm23
                    Member Key: "allowed_address_pairs"
                        Array
                    Member Key: "extra_dhcp_opts"
                        Array
                    Member Key: "dns_assignment"
                        Array
                            Object
                                Member Key: "hostname"
                                    String value: host-10-28-0-24
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                                Member Key: "fqdn"
                                    String value: host-10-28-0-24.openstacklocal.
                            Object
                                Member Key: "hostname"
                                    String value: host-fd5f-5d21-845-1c2e-2--18
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                                Member Key: "fqdn"
                                    String value: host-fd5f-5d21-845-1c2e-2--18.openstacklocal.
                    Member Key: "device_owner"
                        String value: compute:None
                    Member Key: "port_security_enabled"
                        True value
                    Member Key: "binding:profile"
                        Object
                    Member Key: "fixed_ips"
                        Array
                            Object
                                Member Key: "subnet_id"
                                    String value: 886e3c9e-e4cc-4616-8b64-82b11b55e801
                                Member Key: "ip_address"
                                    String value: 10.28.0.24
                            Object
                                Member Key: "subnet_id"
                                    String value: b83ccd70-35c7-4877-8034-5e58c631411f
                                Member Key: "ip_address"
                                    String value: fd5f:5d21:845:1c2e:2::18
                    Member Key: "id"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "security_groups"
                        Array
                            String value: e6adf5ab-bcd8-41c0-91aa-4d73354d39e7
                    Member Key: "device_id"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                    Member Key: "name"
                        String value:
                    Member Key: "admin_state_up"
                        True value
                    Member Key: "network_id"
                        String value: eb463966-6328-427c-964d-2134a835dc8f
                    Member Key: "dns_name"
                        String value:
                    Member Key: "binding:vif_details"
                        Object
                            Member Key: "port_filter"
                                True value
                            Member Key: "mac_address"
                                String value: 00:61:fe:ed:ca:fe
                    Member Key: "binding:vnic_type"
                        String value: normal
                    Member Key: "binding:vif_type"
                        String value: tap
                    Member Key: "tenant_id"
                        String value: 410bd97d893c45c88ed7709cf936b673
                    Member Key: "mac_address"
                        String value: fa:16:3e:24:ac:4e
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.681785000 UTC'
source = '172.18.203.99:37182 (unknown)'
dest = '172.18.203.95:9696 (neutron)'
detail = """    DELETE /v2.0/ports/9792cbef-b9a4-4860-9cc6-342695aa80be.json HTTP/1.1
    Host: calico-vm18:9696
    Content-Length: 0
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.961262000 UTC'
source = '172.18.203.95:9696 (neutron)'
dest = '172.18.203.99:37182 (unknown)'
detail = """    HTTP/1.1 204 No Content
    Content-Length: 0
    X-Openstack-Request-Id: req-2dd7430c-6bd4-4e63-8a0e-36a47848e0f6
    Date: Thu, 26 Nov 2015 21:20:08 GMT
    Connection: keep-alive

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:08.994809000 UTC'
source = '127.0.0.1:49316 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:09.063828000 UTC'
source = '127.0.0.1:52238 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET /v2.0/ports.json?device_id=a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:09.099154000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52238 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 13
    X-Openstack-Request-Id: req-e556b656-27ea-4dfd-84d9-a6044e669f9b
    Date: Thu, 26 Nov 2015 21:20:09 GMT
    Connection: keep-alive

    Object
        Member Key: "ports"
            Array
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:09.101069000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49316 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 1526
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-04989993-1325-4a88-8cae-3e6cbf141d11
    Date: Thu, 26 Nov 2015 21:20:09 GMT
    Connection: keep-alive

    Object
        Member Key: "server"
            Object
                Member Key: "status"
                    String value: ACTIVE
                Member Key: "updated"
                    String value: 2015-11-26T21:20:08Z
                Member Key: "hostId"
                    String value: 3da7ee3dfd5690185ffc85c0c6459cbd4b496ea3b036f5972243109c
                Member Key: "OS-EXT-SRV-ATTR:host"
                    String value: calico-vm23
                Member Key: "addresses"
                    Object
                Member Key: "links"
                    Array
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                            Member Key: "rel"
                                String value: self
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                            Member Key: "rel"
                                String value: bookmark
                Member Key: "key_name"
                    String value: test
                Member Key: "image"
                    Object
                        Member Key: "id"
                            String value: 4bc635c1-0abb-4a7a-9519-80522deaf327
                        Member Key: "links"
                            Array
                                Object
                                    Member Key: "href"
                                        String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/images/4bc635c1-0abb-4a7a-9519-80522deaf327
                                    Member Key: "rel"
                                        String value: bookmark
                Member Key: "OS-EXT-STS:task_state"
                    String value: deleting
                Member Key: "OS-EXT-STS:vm_state"
                    String value: active
                Member Key: "OS-EXT-SRV-ATTR:instance_name"
                    String value: instance-00000018
                Member Key: "OS-SRV-USG:launched_at"
                    String value: 2015-11-26T21:19:57.000000
                Member Key: "OS-EXT-SRV-ATTR:hypervisor_hostname"
                    String value: calico-vm23
                Member Key: "flavor"
                    Object
                        Member Key: "id"
                            String value: 1
                        Member Key: "links"
                            Array
                                Object
                                    Member Key: "href"
                                        String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                                    Member Key: "rel"
                                        String value: bookmark
                Member Key: "id"
                    String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
                Member Key: "OS-SRV-USG:terminated_at"
                    Null value
                Member Key: "OS-EXT-AZ:availability_zone"
                    String value: calico-vm23
                Member Key: "user_id"
                    String value: 9eced15c8e6e42d7bee315954927129e
                Member Key: "name"
                    String value: AAA
                Member Key: "created"
                    String value: 2015-11-26T21:19:53Z
                Member Key: "tenant_id"
                    String value: 410bd97d893c45c88ed7709cf936b673
                Member Key: "OS-DCF:diskConfig"
                    String value: AUTO
                Member Key: "os-extended-volumes:volumes_attached"
                    Array
                Member Key: "accessIPv4"
                    String value:
                Member Key: "accessIPv6"
                    String value:
                Member Key: "progress"
                    Number value: 0
                Member Key: "OS-EXT-STS:power_state"
                    Number value: 1
                Member Key: "config_drive"
                    String value: True
                Member Key: "metadata"
                    Object
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:09.103782000 UTC'
source = '127.0.0.1:49317 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:09.124813000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49317 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 422
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-3d545406-0f81-4dbf-8ac1-bbdf6ef8fea2
    Date: Thu, 26 Nov 2015 21:20:09 GMT
    Connection: keep-alive

    Object
        Member Key: "flavor"
            Object
                Member Key: "name"
                    String value: m1.tiny
                Member Key: "links"
                    Array
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/v2.1/410bd97d893c45c88ed7709cf936b673/flavors/1
                            Member Key: "rel"
                                String value: self
                        Object
                            Member Key: "href"
                                String value: http://calico-vm18:8774/410bd97d893c45c88ed7709cf936b673/flavors/1
                            Member Key: "rel"
                                String value: bookmark
                Member Key: "ram"
                    Number value: 512
                Member Key: "OS-FLV-DISABLED:disabled"
                    False value
                Member Key: "vcpus"
                    Number value: 1
                Member Key: "swap"
                    String value:
                Member Key: "os-flavor-access:is_public"
                    True value
                Member Key: "rxtx_factor"
                    Number value: 1.0
                Member Key: "OS-FLV-EXT-DATA:ephemeral"
                    Number value: 0
                Member Key: "disk"
                    Number value: 1
                Member Key: "id"
                    String value: 1
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:09.154772000 UTC'
source = '127.0.0.1:52638 (unknown)'
dest = '127.0.0.1:9696 (neutron)'
detail = """    GET //v2.0/extensions.json HTTP/1.1
    Host: calico-vm18:9696
    Connection: keep-alive
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Accept-Encoding: gzip, deflate
    Accept: application/json
    User-Agent: python-neutronclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:09.160188000 UTC'
source = '127.0.0.1:9696 (neutron)'
dest = '127.0.0.1:52638 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json; charset=UTF-8
    Content-Length: 4074
    X-Openstack-Request-Id: req-a1463925-f365-4e29-94ce-71b77b0f6ba7
    Date: Thu, 26 Nov 2015 21:20:09 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "alias"
                        String value: dns-integration
                    Member Key: "updated"
                        String value: 2015-08-15T18:00:00-00:00
                    Member Key: "name"
                        String value: DNS Integration
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides integration with internal DNS.
                Object
                    Member Key: "alias"
                        String value: ext-gw-mode
                    Member Key: "updated"
                        String value: 2013-03-28T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Configurable external gateway mode
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extension of the router abstraction for specifying whether SNAT should occur on the external gateway
                Object
                    Member Key: "alias"
                        String value: binding
                    Member Key: "updated"
                        String value: 2014-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Binding
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose port bindings of a virtual port to external application
                Object
                    Member Key: "alias"
                        String value: agent
                    Member Key: "updated"
                        String value: 2013-02-03T10:00:00-00:00
                    Member Key: "name"
                        String value: agent
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The agent management extension.
                Object
                    Member Key: "alias"
                        String value: subnet_allocation
                    Member Key: "updated"
                        String value: 2015-03-30T10:00:00-00:00
                    Member Key: "name"
                        String value: Subnet Allocation
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables allocation of subnets from a subnet pool
                Object
                    Member Key: "alias"
                        String value: l3_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: L3 Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule routers among l3 agents
                Object
                    Member Key: "alias"
                        String value: external-net
                    Member Key: "updated"
                        String value: 2013-01-14T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron external network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Adds external network attribute to network resource.
                Object
                    Member Key: "alias"
                        String value: flavors
                    Member Key: "updated"
                        String value: 2014-07-06T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Service Flavors
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Service specification for advanced services
                Object
                    Member Key: "alias"
                        String value: net-mtu
                    Member Key: "updated"
                        String value: 2015-03-25T10:00:00-00:00
                    Member Key: "name"
                        String value: Network MTU
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides MTU attribute for a network resource.
                Object
                    Member Key: "alias"
                        String value: quotas
                    Member Key: "updated"
                        String value: 2012-07-29T10:00:00-00:00
                    Member Key: "name"
                        String value: Quota management support
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose functions for quotas management per tenant
                Object
                    Member Key: "alias"
                        String value: l3-ha
                    Member Key: "updated"
                        String value: 2014-04-26T00:00:00-00:00
                    Member Key: "name"
                        String value: HA Router extension
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Add HA capability to routers.
                Object
                    Member Key: "alias"
                        String value: provider
                    Member Key: "updated"
                        String value: 2012-09-07T10:00:00-00:00
                    Member Key: "name"
                        String value: Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to physical networks
                Object
                    Member Key: "alias"
                        String value: multi-provider
                    Member Key: "updated"
                        String value: 2013-06-27T10:00:00-00:00
                    Member Key: "name"
                        String value: Multi Provider Network
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Expose mapping of virtual networks to multiple physical networks
                Object
                    Member Key: "alias"
                        String value: extraroute
                    Member Key: "updated"
                        String value: 2013-02-01T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra Route
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra routes configuration for L3 router
                Object
                    Member Key: "alias"
                        String value: router
                    Member Key: "updated"
                        String value: 2012-07-20T10:00:00-00:00
                    Member Key: "name"
                        String value: Neutron L3 Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Router abstraction for basic L3 forwarding between L2 Neutron networks and access to external networks via a NAT gateway.
                Object
                    Member Key: "alias"
                        String value: extra_dhcp_opt
                    Member Key: "updated"
                        String value: 2013-03-17T12:00:00-00:00
                    Member Key: "name"
                        String value: Neutron Extra DHCP opts
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Extra options configuration for DHCP. For example PXE boot options to DHCP clients can be specified (e.g. tftp-server, server-ip-address, bootfile-name)
                Object
                    Member Key: "alias"
                        String value: security-group
                    Member Key: "updated"
                        String value: 2012-10-05T10:00:00-00:00
                    Member Key: "name"
                        String value: security-group
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: The security groups extension.
                Object
                    Member Key: "alias"
                        String value: dhcp_agent_scheduler
                    Member Key: "updated"
                        String value: 2013-02-07T10:00:00-00:00
                    Member Key: "name"
                        String value: DHCP Agent Scheduler
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Schedule networks among dhcp agents
                Object
                    Member Key: "alias"
                        String value: rbac-policies
                    Member Key: "updated"
                        String value: 2015-06-17T12:15:12-30:00
                    Member Key: "name"
                        String value: RBAC Policies
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Allows creation and modification of policies that control tenant access to resources.
                Object
                    Member Key: "alias"
                        String value: port-security
                    Member Key: "updated"
                        String value: 2012-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Port Security
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides port security
                Object
                    Member Key: "alias"
                        String value: allowed-address-pairs
                    Member Key: "updated"
                        String value: 2013-07-23T10:00:00-00:00
                    Member Key: "name"
                        String value: Allowed Address Pairs
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Provides allowed address pairs
                Object
                    Member Key: "alias"
                        String value: dvr
                    Member Key: "updated"
                        String value: 2014-06-1T10:00:00-00:00
                    Member Key: "name"
                        String value: Distributed Virtual Router
                    Member Key: "links"
                        Array
                    Member Key: "description"
                        String value: Enables configuration of Distributed Virtual Routers.
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:09.166514000 UTC'
source = '127.0.0.1:49321 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/extensions HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:09.194989000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49321 (unknown)'
detail = """    HTTP/1.1 200 OK
    Content-Type: application/json
    Content-Length: 21496
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    X-Compute-Request-Id: req-83d269c4-1834-48ab-abb2-950ac12de3f0
    Date: Thu, 26 Nov 2015 21:20:09 GMT
    Connection: keep-alive

    Object
        Member Key: "extensions"
            Array
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: Multinic
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: NMN
                    Member Key: "description"
                        String value: Multiple network support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: DiskConfig
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-DCF
                    Member Key: "description"
                        String value: Disk Management Extension.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedAvailabilityZone
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-AZ
                    Member Key: "description"
                        String value: Extended Availability Zone support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ImageSize
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IMG-SIZE
                    Member Key: "description"
                        String value: Adds image size to image listings.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIps
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedIpsMac
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-IPS-MAC
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedServerAttributes
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-SRV-ATTR
                    Member Key: "description"
                        String value: Extended Server Attributes support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ExtendedStatus
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-EXT-STS
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorDisabled
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-DISABLED
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: FlavorExtraData
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-FLV-EXT-DATA
                    Member Key: "description"
                        String value:
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: SchedulerHints
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SCH-HNT
                    Member Key: "description"
                        String value: Pass arbitrary key/value pairs to the scheduler.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: ServerUsage
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: OS-SRV-USG
                    Member Key: "description"
                        String value: Adds launched_at and terminated_at on Servers.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AccessIPs
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-access-ips
                    Member Key: "description"
                        String value: Access IPs support.
                Object
                    Member Key: "updated"
                        String value: 2014-12-03T00:00:00Z
                    Member Key: "name"
                        String value: AdminActions
                    Member Key: "links"
                        Array
                    Member Key: "namespace"
                        String value: http://docs.openstack.org/compute/ext/fake_xml
                    Member Key: "alias"
                        String value: os-admin-actions
                    Member Key: "description"
                        String value: Enable admin-only server actions
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:10.105074000 UTC'
source = '127.0.0.1:48975 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    POST /v2.1/33afd0ae6b4c48ea8f2fb109449df342/os-server-external-events HTTP/1.1
    Host: calico-vm18:8774
    Content-Length: 172
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 20c3f172aa1a46d9bf9acd0a93fc028d
    Connection: keep-alive
    User-Agent: python-novaclient
    Content-Type: application/json

    Object
        Member Key: "events"
            Array
                Object
                    Member Key: "status"
                        String value: completed
                    Member Key: "tag"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "name"
                        String value: network-vif-unplugged
                    Member Key: "server_uuid"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:10.148705000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:48975 (unknown)'
detail = """    HTTP/1.1 404 Not Found
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    Content-Length: 78
    Content-Type: application/json; charset=UTF-8
    X-Compute-Request-Id: req-1183acf1-f27c-4dfc-a0d6-ea198c8a7e11
    Date: Thu, 26 Nov 2015 21:20:10 GMT
    Connection: keep-alive

    Object
        Member Key: "itemNotFound"
            Object
                Member Key: "message"
                    String value: No instances found for any event
                Member Key: "code"
                    Number value: 404
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:10.938625000 UTC'
source = '127.0.0.1:49008 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    POST /v2.1/33afd0ae6b4c48ea8f2fb109449df342/os-server-external-events HTTP/1.1
    Host: calico-vm18:8774
    Content-Length: 147
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 23539fd2ede848eabee9971d32f52ad4
    Connection: keep-alive
    User-Agent: python-novaclient
    Content-Type: application/json

    Object
        Member Key: "events"
            Array
                Object
                    Member Key: "tag"
                        String value: 9792cbef-b9a4-4860-9cc6-342695aa80be
                    Member Key: "name"
                        String value: network-vif-deleted
                    Member Key: "server_uuid"
                        String value: a1707e2c-b4ec-4541-b691-e0fcb4e60cee
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:10.980915000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49008 (unknown)'
detail = """    HTTP/1.1 404 Not Found
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    Content-Length: 78
    Content-Type: application/json; charset=UTF-8
    X-Compute-Request-Id: req-13744775-d70a-4adc-ab98-8985fa2fd79e
    Date: Thu, 26 Nov 2015 21:20:10 GMT
    Connection: keep-alive

    Object
        Member Key: "itemNotFound"
            Object
                Member Key: "message"
                    String value: No instances found for any event
                Member Key: "code"
                    Number value: 404
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:11.793580000 UTC'
source = '127.0.0.1:49322 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/servers/a1707e2c-b4ec-4541-b691-e0fcb4e60cee HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient

"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:11.847170000 UTC'
source = '127.0.0.1:8774 (nova/nova_legacy)'
dest = '127.0.0.1:49322 (unknown)'
detail = """    HTTP/1.1 404 Not Found
    X-Openstack-Nova-Api-Version: 2.1
    Vary: X-OpenStack-Nova-API-Version
    Content-Length: 111
    Content-Type: application/json; charset=UTF-8
    X-Compute-Request-Id: req-5b497758-d98d-4cb0-bbc7-9b737590ad5a
    Date: Thu, 26 Nov 2015 21:20:11 GMT
    Connection: keep-alive

    Object
        Member Key: "itemNotFound"
            Object
                Member Key: "message"
                    String value: Instance a1707e2c-b4ec-4541-b691-e0fcb4e60cee could not be found.
                Member Key: "code"
                    Number value: 404
"""
summary = detail.split('\n')[0]
r = NJRecord(event_id=str(uuid.uuid1()),
             source=source,
             dest=dest,
             time_stamp=conv_time(time_stamp),
             summary=summary,
             detail=detail)
r.save()

timestamp = 'Nov 26, 2015 21:20:11.882140000 UTC'
source = '127.0.0.1:49323 (unknown)'
dest = '127.0.0.1:8774 (nova/nova_legacy)'
detail = """    GET /v2.1/410bd97d893c45c88ed7709cf936b673/limits?reserved=1 HTTP/1.1
    Host: calico-vm18:8774
    X-Auth-Project-Id: 410bd97d893c45c88ed7709cf936b673
    Accept-Encoding: gzip, deflate
    Accept: application/json
    X-Auth-Token: 30043a02858445f78c9f7d24cb57ccbe
    Connection: keep-alive
    User-Agent: python-novaclient
