


import sys
import requests

def usage():
    print ('''
           ##########Usage############

            # python3 -m venv myenv
            # source myenv/bin/activate
            # pip3 install requests
            # python comm-locs.py ASN1 ASN2...ASN<N> 

            ###########################
           ''')

def get_peer_details(asn):
    url = 'https://www.peeringdb.com/api/netixlan?asn={}'.format(asn)
    response = requests.request('GET',url)
    if response.status_code == 200:
        return response.json().get('data')
        
def main():
    peer_details = []
    all_list = []
    if len(sys.argv[1:]) > 1:
        for asn in sys.argv[1:]:
            details = get_peer_details(asn)
            peer_details.append(details)
            indiv_list = []
            for data in details:
                indiv_list.append(data.get('ix_id'))
            all_list.append(indiv_list)
    else:
        print ("\nGive at least two ASNs to continue.. See Usage.. Exiting...\n")
        usage()
        sys.exit(0)
        
    comm_list = list(set(all_list[0]).intersection(*all_list[1:]))
    if len(comm_list) > 1:  
        print (f"\n### Found {len(comm_list)} overlapping exchanges### \n ")
        for x in range(len(sys.argv[1:])):
            print("\nDetails for AS{}".format(sys.argv[1:][x]))
            print("===========================================")
            for data in peer_details[x]:
                if data.get('ix_id') in comm_list:
                    print("{} | Speed: {}G | IPv4: {} | IPv6: {} | ".format(data.get('name'), int(int(data.get('speed'))/1000), data.get('ipaddr4'), data.get('ipaddr6')))
            print("===========================================")
    
    else:
        print (f"\nDid not find any exchange where all {len(sys.argv[1:])} networks overlap \n")    
    
if __name__=='__main__':
    main()

