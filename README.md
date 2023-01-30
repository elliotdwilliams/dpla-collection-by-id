# dpla-collection-by-id

This is a simple script that queries the [DPLA API](https://pro.dp.la/developers/api-codex) to return the institution (Data Provider) and collection name for the record in DPLA.

The script accepts a file with DPLA identifiers as an argument, then prints the results to a file called SearchResults.txt.  You will need to provide your DPLA API key, either in the script itself or in a separate credentials.py file.  The input file should be a CSV file with column header "Item ID" for the column that contains the DPLA identifiers; this is the format used when you download data from the DPLA Analytics Dashboard, so you should be able to use those files without needing to edit them.

TO-DO: Handle items without a collection name value

Built in Python 3.9.15. Uses the [DPLA API](https://pro.dp.la/developers/api-codex) for interacting with DPLA dataset, and [DPyLA](https://github.com/bibliotechy/DPyLA/blob/master/README.md) for interacting with the api.
