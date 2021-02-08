
### Print outs the public peering information for an organization using
### the data from the peeringdb. 

## TO USE: python3 whoispeer.py <ASN>

## Requirements
### pip3 install requests
### pip3 install prettytable

import json
import sys
import requests
from prettytable import PrettyTable
from requests.auth import HTTPBasicAuth

master_url = 'https://www.peeringdb.com/api/'
auth = HTTPBasicAuth('pdb_username', 'pdb_pass')

class Peer():
    def __init__(self, asn):
        self.asn=asn


    def get_org_details(self):
        local_url ='net?asn={}'.format(self.asn) 
        response = get_response(local_url)
        if response.ok:
            data  = response.json()
            return data
        else:
            print("Unable to fetch the infromation!!")
            sys.exit(1)
    
    def get_org_contacts(self,id):
        local_url = 'poc?net_id={}'.format(id)
        response = get_response(local_url)
        if response.ok:
            data = response.json()
            return data
        else:
            print("Unable to fetch contact information ")
    
    def get_org_peeringData(self):
        local_url = 'netixlan?asn={}'.format(self.asn)
        response = get_response(local_url)
        if response.ok:
            data = response.json()
            return data
        else:
            print("Unable to fetch the peering information")


def get_response(local_url):
    master_url = 'https://www.peeringdb.com/api/'
    url = master_url + local_url
    response = requests.request('GET', url, auth=auth)
    return response

def print_org_details(org_data):
    print ("\nOrg. Name: {}".format(org_data.get('data')[0].get('name')))
    print("Website: {}".format(org_data.get('data')[0].get('website')))
    print("Primary ASN: {}".format(org_data.get('data')[0].get('asn')))
    print("Policy: {}".format(org_data.get('data')[0].get('policy_general')))
    print("Prefixes: {}/{}".format(org_data.get('data')[0].get('info_prefixes4'),org_data.get('data')[0].get('info_prefixes6')))
    print("Traffic: {}".format(org_data.get('data')[0].get('info_traffic')))

def print_org_contact_info(org_contact_data):
    contact_data = org_contact_data.get('data')
    if contact_data != None:
        for contact in contact_data:
            print("{}: {}".format(contact.get('role'), contact.get('email')))
    else:
        print("Contact information hasn't been listed..")

def print_org_peeringData(org_peering_data):
    peering_data = org_peering_data.get('data')
    if peering_data != []:
        table = PrettyTable(["Exchange", "ASN", "IPv4", "IPv6"])
        for data in peering_data:
            ix_name = data.get('name')
            asn = data.get('asn')
            ipaddr4 = data.get('ipaddr4')
            ipaddr6 = data.get('ipaddr6')
            table.add_row([ix_name, asn, ipaddr4, ipaddr6])
        print(table)
    else:
        print("No public peering infromation listed !!")

def main():
    p = Peer(sys.argv[1])
    org_data = p.get_org_details()
    org_id = org_data.get('data')[0].get('id')
    org_contact_data = p.get_org_contacts(org_id)
    org_peering_data = p.get_org_peeringData()
    print_org_details(org_data)
    print("\nContact Information:")
    print_org_contact_info(org_contact_data)
    print("\nPeering Details:")
    print_org_peeringData(org_peering_data)

if __name__ == '__main__':
    main()
