import sys
from zabbix_api import ZabbixAPI
zusername = "Admin"
zpassword = "xxxxxxxxxxxxxx"
zserver = "https://localhost/zabbix/"

#conexao
zapi = ZabbixAPI(server = zserver)
zapi.login(zusername, zpassword)

#Lista os chave e o valor dos hosts
hostgroups = zapi.hostgroup.get({"output": "extend", "sortfield": "name"})

# filtra id de um determinado GRUPO
for h in hostgroups:
	if sys.argv[1] in h['name']:
		hostsG_id = h["groupid"]
#                print hostsG_id

#lista id de um determidado grupo
hosts = zapi.host.get({"groupids": hostsG_id, "output": ["hostid","name", "host", "status"]})


# Verificar se o host esta desabilitado se sim REMOVE
for h in hosts:
	if "1" in  h["status"]  :
		id_hosts = h["hostid"]
		name_hosts = h["name"] 
		print name_hosts
#		zapi.host.delete({"hostid": id_hosts})

                print "Hosts foram removidos com sucesso ===> %s %s " %(id_hosts,name_hosts)



#Desativa a monitoracaoo do Host
#zapi.host.update({"hostid": "10099", "status": "1"})
 
#Ativa a monitoracao do Host
#zapi.host.update({"hostid": "10099", "status": "0"})









 
