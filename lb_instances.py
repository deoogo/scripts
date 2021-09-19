import boto3,boto

elb = boto.connect_elb()
ec2 = boto3.resource('ec2')

load_balancer = elb.get_all_load_balancers(['efacil-lb-webapp-prd'])[0]

for x in load_balancer.instances:
	(host,id_host) = str(x).split(':')
	instance = ec2.Instance(id_host)
	print instance.private_ip_address



