from zabbix_api import ZabbixAPI
zusername = "Admin"
zpassword = "mon-int.om-Nu1oaja0"
zserver = "https://monitoramento.orama.com.br/zabbix/"

zapi = ZabbixAPI(server = zserver)
zapi.login(zusername, zpassword)

hosts = zapi.host.get({"output": ["host","name"]})

for x in hosts:
	if sys.argv[1] in x['name']:
		list_Id_Host = []
		list_Id_Host.append(x['hostid'])
		list_Id_Host.append(x['name'])

#zapi.host.delete({"hostid": list_Id_Host[0]})
print "Hosts foram removidos com sucesso ===> %s %s " %(list_Id_Host[0],list_Id_Host[1])
#os.system("echo estouaqui")


