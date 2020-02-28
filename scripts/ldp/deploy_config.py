import argparse
from colorama import Fore
from colorama import Style
from napalm import get_network_driver
driver = get_network_driver('junos')

parser = argparse.ArgumentParser(description='Deploy configuration to Junos Devices via Napalm')
parser.add_argument('-r', action='store', dest='Router', help='Pass the Router Name', type=str, required=True)
parser.add_argument('-f', action='store', dest='Filename', help='Pass the configuration file', type=str, required=True)
args     = parser.parse_args()
Router   = args.Router
Filename = args.Filename


def colorprint(message):
    
    print('\n{} [*]{} {}'.format(Fore.YELLOW,message,Style.RESET_ALL))

def  deploy_config(router, filename):

    #opening the connection to the device 
    device = driver(router, 'lab', 'lab123')
    try:
        device.open()
        colorprint('opened the Device, loading the configuration')
        device.load_merge_candidate(filename=filename)
    except:
        print('Error opening connection to Device')

    # viewing the diff
    colorprint('Difference between Candidate and Active Configuration')
    difference_in_config = device.compare_config()
    if difference_in_config:
        colorprint(difference_in_config)
    else:
        colorprint("No Difference in the config! Will not commit anything!")
    #commiting the config
    device.commit_config()
    colorprint('Configuration has been commited successfully')

deploy_config(router=Router, filename=Filename)


