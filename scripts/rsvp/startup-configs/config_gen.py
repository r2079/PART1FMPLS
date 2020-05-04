import sys
import yaml
import argparse
from jinja2 import Template

parser = argparse.ArgumentParser(description='Input YAML file and Router Name to generate configuration')
parser.add_argument('-y', action='store',dest='interface_yaml',help='Pass the yaml file ',type=str,required=True)
parser.add_argument('-r', action='store',dest='router_name',help='Pass the Router Name',type=str,required=True)
parser.add_argument('-j', action='store',dest='jinja_template',help='Pass Jinja Template name used for this config',type=str,required=True)
args = parser.parse_args()




interface_yaml = args.interface_yaml
router_name    = args.router_name+'.cfg'
jinja_template = args.jinja_template

def output_config(interface_yaml,router_name,jinja_template):

    try:
        with open(interface_yaml,'r') as yamlfile:
            yaml_data = yaml.safe_load(yamlfile.read())
    except:
        print('Check your YAML file')
    try:    
        with open(jinja_template,'r') as jinjafile:
            jinja_data = jinjafile.read()
            template = Template(jinja_data)
    except:
        print('Exception occured in Jinja Processing! Exiting')

    final_config = template.render(yaml_data)
    with open(router_name, 'w') as configfile:
        configfile.write(final_config)
    print(final_config)


output_config(interface_yaml, router_name, jinja_template)

