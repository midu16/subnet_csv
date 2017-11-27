########################################################################################################################
#
#
#
#   IDU MIHAI (c) : 2017 - 2018
#
#   Subneting and writing to a csv file the results
########################################################################################################################
import csv
import sys

#compute the no of valid addresses
########################################################################################################################
no_addr = 256

#or get the keyboard inputs
(addr_string,cidr_string)=sys.argv[1].split('/')
#
########################################################################################################################

#Get the address and the CIDR
addr = addr_string.split('.')
cidr_int = int(cidr_string)

#
mask = [0,0,0,0]
for i in range(cidr_int):
    mask[int(i/8)]=mask[int(i/8)]+(1<<(7-i%8))

net = []
for i in range(4):
    net.append(int(addr[i])&mask[i])

broad = list(net)
brange = 32 - cidr_int
for i in range(brange):
    broad[3-int(i/8)]=broad[3-int(i/8)]+(1<< (i%8))

print(broad)
#read the .csv file
with open('subnet.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
        print(row['item'], row['IP_address'], row['No_of_addresses'])


#Convert the types
addr = ".".join(map(str,addr))
net  = ".".join(map(str,net))
mask = ".".join(map(str,mask))
broad = ".".join(map(str,broad))

#write to the .csv file
with open('subnet.csv', 'w') as csvfile:
    fieldnames = ['item', 'IP_address', 'No_of_addresses']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'item': 'Address', 'IP_address': addr,'No_of_addresses':no_addr})
    writer.writerow({'item': 'Netmask', 'IP_address': mask,'No_of_addresses':no_addr})
    writer.writerow({'item': 'Network', 'IP_address': net,'No_of_addresses':no_addr})
    writer.writerow({'item': 'Broadcast', 'IP_address': broad,'No_of_addresses':no_addr})
########################################################################################################################
