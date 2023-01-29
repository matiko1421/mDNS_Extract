from openpyxl import *
import pyshark

packet_capture = input('Enter the path to your pcap file:')
save = input("Would you like to save the results to an excel spreadsheet?Type [Yes] or [No]:")

if save == 'Yes':
    wb = Workbook()
    ws = wb.active
    ws.title = "mdns_scrap"
    ws.append(['Name','Model'])
    title = input("Please specify the name of created excel file:")
# Determining whether to save the results to an excel file and asking for the name of the resulting file

input
pkt = pyshark.FileCapture(packet_capture, display_filter="mdns" and "dns.flags.response == 1" and "dns.resp.type == 16")
# Opening pcap file capture and assigning it to a variable (in form of a list)

x = 0
z = 0
# Setting starting values for key variables

c = input("How many packets would you like to examine? Enter value here:")
# Choosing the restraint (number of packets)


while x < int(c):    # Loop for going over every packet until it meets the required number of packets          
    packet = pkt[x]
    name = packet.mdns.dns_resp_name   # Taking the name of the device from the dns response name field
    print("Name: " + name) 
    if "dns_txt" in packet.mdns.field_names: # Checking whether the packet contains "dns_txt" field so that model can be extracted
        while z < len(packet.mdns.dns_txt.all_fields): # Searching for the 'model' keyword in all of the subfields of 'dns_txt' field
            if "model" in packet.mdns.dns_txt.fields[z].showname_value:
                model = packet.mdns.dns_txt.fields[z].showname_value.removeprefix("model=") # Extracting name of the model and deleting the prefix so that only model is shown
                print("Model: "+ model)
            z = z + 1
        if save == 'Yes':
            ws.append([name, model]) # Inserting data into excel rows so that it matches key:value pairs notation
        z = 0
    x = x + 1 

if save == 'Yes':
   wb.save(title + '.xlsx') 
# Saving the file with the .xlsx extension (to be found in the same folder where Python file)
