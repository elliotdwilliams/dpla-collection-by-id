# dpla-collection-by-id

This is a simple script that queries the [DPLA API](https://pro.dp.la/developers/api-codex) to return the institution (Data Provider) and collection name for the record in DPLA.

The script accepts a CSV file with DPLA identifiers as an argument, then prints the results to a tab-delimited file called SearchResults.txt.  The input file should be a CSV file with column header "Item ID" for the column that contains the DPLA identifiers; this is the format used when you download data from the DPLA Analytics Dashboard, so you should be able to use those files without needing to edit them.

You will need to provide your DPLA API key, either in the script itself or in a separate credentials.py file.  

_Example input:_
| DPLA website click throughs | Item | Item ID | Contributor |
|---|---|---|---|
| 1 | Country singer sketch                               | 0c91407fa5fb432d6ed7874ff8150f5d | Houston Public Library |
| 1 | Kudos to the Astrodome, home of Modernism, memories | 0d0f9b4a0288ce6916d7a47893ab8da0 | Houston Public Library |
| 1 | Letter from Flo Dew (Mrs. W.B.) to Goldie Dodge     | 0d191493da6de226a32e8e0fdbe380bd | Houston Public Library |

_Example output:_  
IDENTIFIER	INSTITUTION	COLLECTION  
0c91407fa5fb432d6ed7874ff8150f5d	Houston Public Library	Sidney Van Ulm Collection  
0d0f9b4a0288ce6916d7a47893ab8da0	Houston Public Library	Evelyn Norton Anderson Papers  
0d191493da6de226a32e8e0fdbe380bd	Houston Public Library	Clayton Vertical File Collection  

**TO-DO**: Handle items without a collection name value

Built in Python 3.9.15. Uses the [DPLA API](https://pro.dp.la/developers/api-codex) for interacting with DPLA dataset, and [DPyLA](https://github.com/bibliotechy/DPyLA/blob/master/README.md) for interacting with the api.
