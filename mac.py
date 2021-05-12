#!/usr/bin/env python3
import os
import re
import sys

import requests

'''
Defining api key in case user doesn't have it and don't want to create an account.
'''
apiKey = os.getenv("MACADDRESS_API_KEY") or "at_YYMd0kJCYOUecLN2vznzko8SCqXaD"


def generate_address_list(addresses=sys.argv[1:]):  # getting the list of macaddress from the console parameters
    address_list = []
    for address in addresses:
        if "," in address:
            for addr in address.split(","):
                address_list.append(addr)
        else:
            address_list.append(address)
    return address_list


'''
Defining function that will return company name of a macaddress
'''


def final(mac_address):
    output = "json"
    url = "https://api.macaddress.io/v1?apiKey={0}&output={1}&search={2}".format(apiKey, output, mac_address)
    response = requests.get(url)
    company_name = response.json().get("vendorDetails").get("companyName")
    return "Your mac address " + mac_address + " belongs to the " + company_name


'''
Function to validate macaddress
'''


def check_mac_address(mac_address):
    return re.match("^([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})$", mac_address.strip())


'''
Main function
'''


def main():
    for address in generate_address_list():
        if check_mac_address(mac_address=address):
            print(final(address))
        else:
            print("MacAddress", address, "is not valid")
    return True


if __name__ == '__main__':
    main()
