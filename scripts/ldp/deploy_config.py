import argparse
from napalm import get_network_driver
driver = get_network_driver('junos')


parser = argparse.ArgumentParser(description='Deploy configuration to Junos Devices via Napalm')
parser.add_argument('-r', action='store', dest='Router', help='Pass the Router Name', type=str, required=True)
parser.add_argument('-f', action='store', dest='Filename', help='Pass the configuration file', type=str, required=True)
args     = parser.parse_args()
Router   = args.Router
Filename = args.Filename

def deploy_config(router, filename):

    device = driver(router, 'lab', 'lab123')
    device.open()
    device.load_merge_candidate(filename=filename)

    # viewing the diff
    difference_in_config = device.compare_config()
    print(difference_in_config)

    #commiting the config
    device.commit_config()

deploy_config(router=Router, filename=Filename)


