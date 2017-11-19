#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Cino Jose'
__email__  = 'cinojose91@yahoo.com'


import os
import boto.iam
import boto.regioninfo
import signal
import boto.ec2.elb


#--------------------------------------------------
#  Script to check the location of an EIP
#   note : looping through all the profiles
#          across multiple region for a given credential file
#
#-------------------------------------------------



AWS_CREDENTIALS_FILENAME = os.path.expanduser('~/.aws/credentials')


aws_regions = {
    "us-east-1": "US East (N. Virginia)",
    "us-east-2": "US East (Ohio)",
    "us-west-1": "US West (N. California)",
    "us-west-2": "US West (Oregon)",
    "ca-central-1": "Canada (Central)",
    "eu-central-1": "EU (Frankfurt)",
    "eu-west-1": "EU (Ireland)",
    "eu-west-2": "EU (London)",
    "ap-northeast-1": "Asia Pacific (Tokyo)",
    "ap-northeast-2": "Asia Pacific (Seoul)",
    "ap-southeast-1": "Asia Pacific (Singapore)",
    "ap-southeast-2": "Asia Pacific (Sydney)",
    "ap-south-1": "Asia Pacific (Mumbai)",
    "sa-east-1": "South America (Sao Paulo)",
    # "us-gov-west-1": "US Gov West 1"
}


def load_aws_credentials():
    profiles = {}
    p = None
    with open(AWS_CREDENTIALS_FILENAME, "rb") as f:
        for line in f:
            line = line.strip()
            if len(line) == 0 or line[0] == '#':
                continue
            if line[0] == '[':
                if p != None:
                    kid = p['aws_access_key_id']
                    if kid in profiles:
                        profiles[kid]['regions'].extend(r)
                        profiles[kid]['names'].extend(p['names'])
                    else:
                        p['regions'] = r
                        # del p['aws_access_key_id']
                        profiles[ kid ] = p
                n = line[1:line.index(']')]
                if n in profiles:
                    p = profiles[n]
                    r = p['regions']
                else:
                    p = { 'names' : [n] }
                    r = []
                continue
            if p == None:
                continue
            kv = line.split('=')
            k,v = (kv[0].strip(), kv[1].strip())
            if k == 'region':
                r.append(v)
            else:
                p[k] = v
    if p != None:
                    kid = p['aws_access_key_id']
                    if kid in profiles:
                        profiles[kid]['regions'].extend(r)
                        profiles[kid]['names'].extend(p['names'])
                    else:
                        p['regions'] = r
                        # del p['aws_access_key_id']
                        profiles[ kid ] = p
    return profiles

def get_ip_list(profile_dict,p,r):
    conn = boto.connect_ec2(aws_access_key_id=profile_dict['aws_access_key_id'],
                                          aws_secret_access_key=profile_dict['aws_secret_access_key'],
                                          region=boto.ec2.get_region(r))
    try:
        addresses = conn.get_all_addresses()

    except:
        print "Error in fetching ip from ",profile_dict,p
    return addresses

def do_check(ip_list,ip):
    found = False
    for i in ip_list:
        if i.public_ip == ip:
            found = True
            break
    return found


def checkIp(ip):
    aws_profiles = load_aws_credentials()
    for p in sorted(aws_profiles, key=lambda kid:aws_profiles[kid]['names'][0]):
        for name in aws_profiles[p]['names']:
                for r in sorted(aws_regions):
                    try:
                        list_ip = get_ip_list(aws_profiles[p],name,r)
                        if do_check(list_ip,ip):
                            print "Ip found in ",aws_profiles[p],name,r
                            return
                    except:
                        print "Error fetching ip for this profile",aws_profiles[p],name
                        continue




def _main():
    #ip = "52.55.96.20"
    ip = "52.221.166.119"
    checkIp(ip)

if __name__ == "__main__":

    def signal_handler(signal, frame):
        print('Catching INT signal')
        os._exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    _main()
