# mDNS_Extract
Simple script in python to extract name of devices and their model (especially Apple) from mDND packets and save it to excel

It works by using the PyShark module to 
- open and filter packetcapture to only contain mDNS responses
- extract device name
- search for dns_text field and extract the model of the device
