<h2>MAC Address Vendor lookup CLI</h2>
This simple python script can be used to query https://macaddress.io/ to get vendor related information about a device MAC Address

<h3>Getting Started</h3>
This scripting utility has be written using the standard library included in python 3.x All you need to get started is sign up for an account here and obtain your API key.

<h3>Prerequisites</h3>
You need a standard installation of Python3 that can be obtained here

<h3>Usage</h3>
Export the API key as an environment variable MACADDRESSIO_API_KEY before running the script

On linux and MacOS

Example:

`export MACADDRESS_API_KEY=at_`

###### Also note that if you don't have MACADDRESS_API_KEY generated, or you want to make a fast test, you shouldn't define any key, but script has a limit of 100 requests per day.

To run the script, please use the syntax below:

`./mac.py 14:7d:da:e0:23:e8,44:38:39:ff:ef:57 sdfkaor 14:54:12:da:dd:45`

This should give output of the company name. For the above example it would show:

`Your mac address 14:7d:da:e0:23:e8 belongs to the Apple, Inc`

`Your mac address 44:38:39:ff:ef:57 belongs to the Cumulus Networks, Inc`

`MacAddress sdfkaor is not valid`

`Your mac address 14:54:12:da:dd:45 belongs to the Entis Co, Ltd`

## Docker
To build docker image locally, please use next command from the current folder:

`docker build -t mac_info .` 

To run this application from inside the docker, please use the next one command:

`docker run mac_info ./mac.py 14:7d:da:e0:23:e8,44:38:39:ff:ef:57 sdfkaor 14:54:12:da:dd:45`

Or you can specify api key by using variable name `MACADDRESS_API_KEY`
Example: `docker run -e MACADDRESS_API_KEY=at_YYMd0kJCYOUecLN2vznzko8SCqXaD mac_info ./mac.py 14:7d:da:e0:23:e8,44:38:39:ff:ef:57 sdfkaor 14:54:12:da:dd:45`