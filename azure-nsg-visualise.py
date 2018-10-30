
# Generates a Digraph from csv file export of NSG Rules for added visibility
# With complicated rulesets it looks a bit messier
# Take the graph and put into GVedit which is a nice frontend for this sort of thing

import csv


print("digraph NSG { \n\trankdir=LR; \n\tnode [shape = rectangle];")

with open('C:\\Users\\mikespinks\\Desktop\\Test\\NSG.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("\t\"", row['Name'], "\"", "->", "\"", row['SourceAddressPrefix'], "\""";")
            print ("\t\"",row['SourceAddressPrefix'], "\"", "->", "\"",row['DestinationAddressPrefix'], "\"", "[ label = ", "\"", row['Action'], "traffic", row['Type'], " to ", row['DestinationPortRange'], " using", row['Protocol'], "Protocol", "\"""];")

print("}")


