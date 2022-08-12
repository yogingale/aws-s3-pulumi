"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import ec2

config = pulumi.Config()
data = config.require_object("data")
machinename = data.get("machine_name")
instancetype = data.get("instance_type")
sg = data.get("vpc_security_group_ids")
subnet = data.get("subnet_id")
ami = data.get("ami")

#print (machinename + " : " + instancetype + " : " + sg + " : " + subnet + " : " + ami)


server = ec2.Instance(machinename,
                        instance_type=instancetype,
                        subnet_id=subnet,
                        tags= { 
                            "Name": machinename 
                        },
                        vpc_security_group_ids=[sg],
                        #key_name=keypair.id,
                        ami=ami)

pulumi.export('privateIP', server.private_ip)
pulumi.export('privateDNS', server.private_dns)
