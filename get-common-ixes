
## Install jq before using

#### For MAC
## ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
## brew install jq

#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "No arguments supplied!!"
    echo "Usage: $0 ASN1 ASN2"
    exit 0
fi

id_first_peer=$(curl -sG https://peeringdb.com/api/net?asn=$1 | jq  -c '.data[] | [.id]' | sed 's/\[//;s/\]//')
id_second_peer=$(curl -sG https://peeringdb.com/api/net?asn=$2 | jq  -c '.data[] | [.id]' | sed 's/\[//;s/\]//')

echo "## Fetching Data from peeringdb ##"
printf "\n"
curl -sG https://peeringdb.com/api/netixlan --data-urlencode net_id__in=$id_first_peer \
--data-urlencode ix_id__in=`curl -sG https://peeringdb.com/api/netixlan --data-urlencode net_id__in=$id_second_peer | 
jq -c '[.data[].ix_id]' | \
sed 's/\[//;s/\]//'` | \
jq -c '.data[] | ["Exchange: " + .name + " - " + "AS" +(.asn|tostring) + ":  IPv4: " + .ipaddr4, "  IPv6: " + .ipaddr6]' | sed 's/\[//;s/\]//;s/\"//g' | sort -V

printf "\n"



