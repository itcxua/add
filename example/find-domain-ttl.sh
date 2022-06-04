#!/bin/bash
# Usage: 
# Shell script too see Time-To-Live (TTL) for a DNS record in human readable
# format.
#
# Tested on:
# Ubuntu/Debian/macOS with bash shell v5.x
#
# Note:
# dig must be installed on your system this to work.
#
# Syntax:
# /path/to/find-domain-ttl cyberciti.biz
# /path/to/find-domain-ttl google.com | more
# /path/to/find-domain-ttl cyberciti.biz | grep  -i 'AAAA'
# ----------------------------------------------------------------------------
# Written by Vivek Gite <https://www.cyberciti.biz/>
# (c) 2021 Vivek Gite under GNU GPL v2.0+
# ----------------------------------------------------------------------------
# Last updated: 04/Jun/2021
# ----------------------------------------------------------------------------
set -eu -o pipefail
domain="${1:-NULL}"
 
# fail safe i.e. if no $1 passed to the script, die with an error
[ "$domain" == "NULL" ] && { echo "Usage: $0 domain-name"; exit 1; }
 
# make sure dig installed else die
if ! type -a dig &>/dev/null 
then
	echo "Error: $0 - dig command not found."
	exit 2
fi
 
# repeat given char 90 times
repeat(){
	for i in {1..90}; do echo -n "$1"; done
}
 
# get first ns for domain
# remove everything except domain.com 
str="${domain%.*.*}"
domain="${domain/$str./}"
 
ns="$(dig +nocmd +noall +answer ns "${domain}" | head -1 | awk '{ print $5}')"
 
# now print ttl for a, aaaa, and mx
repeat '-'
echo -e "\nDomain\t\t\tTTL\tIN\tRecord\tAnswer"
repeat '-'
echo 
 
for i in a aaaa mx
do   
	dig +nocmd +noall +answer +ttlunits "${i}" "${domain}" "@${ns}"
done

# Simply run it as:
./find-domain-ttl {domain-name}
./find-domain-ttl cyberciti.biz
