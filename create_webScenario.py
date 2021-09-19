from zabbix.api import ZabbixAPI
import json

zapi = ZabbixAPI(url='http://0.0.0.0/zabbix/', user='Admin', password='senha')


f = open('names.txt')
for web_names in f:
    web_name = web_names.rstrip()
    json_web = ('{"name": "Availability of '+ str(web_name) +'", "hostid": "11270", "steps": [{"name": "'+ str(web_name) +'", "url": "'+ str(web_name) +'.url", "status_codes": 204, "no": 1 }]}')
    parsed_web = json.loads(json_web)
    newweb = zapi.htttest.create(parsed_web)
    json_zabbix = ('{"description": "'+ str(web_name) +' DOWN", "expression": "{Template Healthchecks:web.test.fail[Availability of '+ str(web_name) +'].sum(#3)}<>0", "priority": "2"}')
    parsed_zabbix = json.loads(json_zabbix)
    newtrigger = zapi.trigger.create(parsed_zabbix)
