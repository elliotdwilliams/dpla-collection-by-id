# This script takes a list of DPLA identifiers, then queries the DPLA API to get the collection name for that item.
# Developed to take a list of items from the DPLA Analytics Dashboard (such as catalog views or click-throughs), and analyze them by collection.
# Accepts a filename as a command line argument; that file should include a list of DPLA identifiers

from dpla.api import DPLA
from time import sleep
import sys, pandas, numpy
from credentials import *

#get filename from command line argument
input_filename = sys.argv[1]

#create DPLA object using dpla module and your API key
#API key should be stored in a separate file called credentials.py
dpla = DPLA(DPLA_KEY)

#Opens file with identifiers and then reads them into a list
df = pandas.read_csv(input_filename, encoding='latin1')
identifiers = df["Item ID"]

#open file for writing results
file_results = open(r"SearchResults.txt","w")
file_results.write("IDENTIFIER"+"\t"+"INSTITUTION"+"\t"+"COLLECTION"+"\n")

for identifier in identifiers:
    identifier = identifier.rstrip()

    try:
        result = dpla.fetch_by_id([identifier])

        institution = result.items[0]["dataProvider"]["name"]
        collection = result.items[0]["sourceResource"]["collection"][0]["title"]

        print(identifier+"\t"+institution+"\t"+collection)
        file_results.write(identifier+"\t"+institution+"\t"+collection+"\n")

    #error handling for when DPLA API doesn't return the item record (i.e. the item is no longer in DPLA)
    except AttributeError:
        print(identifier+"\t"+"record not found"+"\t"+"record not found")
        file_results.write(identifier+"\t"+"record not found"+"\t"+"record not found"+"\n")

    sleep(0.50)

file_results.close()
