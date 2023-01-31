"""Query DPLA API to get collection name for a given list of DPLA identifiers.

Accepts a filename as a command line argument. That file should include a list of DPLA
identifiers with heading "Item ID".  Designed to accept an export file from the DPLA
Analytics Dashboard (such as catalog views or click-throughs).
"""

import sys
from time import sleep

from pandas import read_csv
from dpla.api import DPLA

from credentials import DPLA_KEY

# Get filename from command line argument
INPUT_FILE = sys.argv[1]

# Create DPLA object using dpla module and your API key
# API key should be stored in a separate file called credentials.py
dpla = DPLA(DPLA_KEY)

# Open file with identifiers and then reads them into a list
df = read_csv(INPUT_FILE, encoding="latin1")
identifiers = df["Item ID"]

# Open file for writing results
file_results = open(r"SearchResults.txt", "w")
file_results.write("IDENTIFIER" + "\t" + "INSTITUTION" + "\t" + "COLLECTION" + "\n")

for identifier in identifiers:
    identifier = identifier.rstrip()

    try:
        result = dpla.fetch_by_id([identifier])

        institution = result.items[0]["dataProvider"]["name"]
        collection = result.items[0]["sourceResource"]["collection"][0]["title"]

        print(identifier + "\t" + institution + "\t" + collection)
        file_results.write(identifier + "\t" + institution + "\t" + collection + "\n")

    # Error handling for when DPLA API doesn't return item record (e.g. the item is no longer in DPLA)
    except AttributeError:
        print(identifier + "\t" + "record not found" + "\t" + "record not found")
        file_results.write(identifier + "\t" + "record not found" + "\t" + "record not found" + "\n")

    # Error handling for no collection field in record (dataProvider will always be present)
    except KeyError:
        print(identifier + "\t" + institution + "\t" + "collection not found")
        file_results.write(identifier + "\t" + institution + "\t" + "collection not found" + "\n")

    sleep(0.50)

file_results.close()
