#!/bin/bash


usage () {
  echo "script usage: $(basename $0) [-c country_code] / [-r region ]"
  printf "\n"
  echo "Pass the regions names with quotes : North America, Africa, Asia Pacific, Africa, South America "
  printf "\n"
  echo "OR"
  printf "\n"
  echo "Pass the country codes. eg. NP, IN, PK, BD ..."
}

while getopts "c:r:h" opt; do
        case $opt in
                c) CN="$OPTARG" ;;
                r) RG="$OPTARG" ;;
                h) echo "script usage: $(basename $0) [-c country_code] / [-r region ]"; exit 1;;
                                     
          \?) echo "Invalid Option: script usage: $(basename $0) [-c country_code] / [-r region ]"; exit 1;;
        esac
done
shift $(( $OPTIND -1 ))

if [ $OPTIND -eq 1 ]; then 
    echo  "No options were passed !! " 
    usage 
fi

printf "\n"

if [ "$CN" != "" ]; then
    echo "##### Fetching IX names for country : $CN #######"
    curl -sG https://peeringdb.com/api/ix --data-urlencode country=$CN | jq  -c '.data[]| ["https://peeringdb.com/ix/" + (.id|tostring) + " - " +.name_long, .city]' |  sed 's/\[//;s/\]//;s/\"//g' 
    
fi


if [ "$RG" != "" ]; then

    echo "##### Fetching IX names for Region : $RG #######"
    curl -sG https://peeringdb.com/api/ix --data-urlencode region_continent="$RG" | jq  -c '.data[]| ["https://peeringdb.com/ix/" + (.id|tostring) + " - " +.name_long, .city]' |  sed 's/\[//;s/\]//;s/\"//g'

fi

printf "\n"
