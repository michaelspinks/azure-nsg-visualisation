
#This is Michael Spinks 2018-10-28
import csv


print("digraph NSG { \n\trankdir=LR; \n\tsize=""8.5""; \n\tnode [shape = rectangle];")

print("[ label = ];")

with open('C:\\Users\\Michael\\Desktop\\Graphviz\\TestNSG01.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print ("\t\"",row['SourceAddressPrefix'],"\"","->","\"",row['DestinationAddressPrefix'],"\"","[ label = ","\"",row['Access'],row['DestinationPortRange'],row['Direction'],"\"","];")

print("}")


