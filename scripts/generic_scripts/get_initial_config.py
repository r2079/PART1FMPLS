from jnpr.junos import Device
from lxml import etree
import os 
import sys

folder = sys.argv[1]
router_list = sys.argv[2:]

path = f"/home/rakesh/initial_configurations/{folder}"  # Replace with your desired path
if not os.path.exists(path):
    os.makedirs(path)
    print(f"Folder '{folder}' created in '{path}'")
else:
    print(f"Folder '{folder}' already exists in '{path}'")



def get_initial_config(router):
    with Device(host=router,user='lab',password='lab123') as dev:
        data = dev.rpc.get_config(options={'format':'text'})
        with open(f'/home/rakesh/initial_configurations/{folder}/{router}.conf','w') as file:
            file.write(etree.tostring(data, encoding='unicode', pretty_print=True))

    os.system(f"sed -i '1d;$d' /home/rakesh/initial_configurations/{folder}/{router}.conf")

for router in router_list:
    get_initial_config(router)
