## urlFilter
Perform a deduplication of a list of urls based on the following primitives:

1. Root URL (Scheme + Netloc): Ensures uniqueness of URLs based on the main domain and protocol.
2. First Directory: The initial part of the path helps in determining the primary endpoint or section of the URL.
3. Number of Subdirectories: Counts the depth of the path to consider URLs with different hierarchical structures.
4. Query Parameter Names: Considers the query parameters present in the URL to distinguish URLs with different sets of parameters.

```
usage: urlFilter.py [-h] inputfile outputfile

I filter a list of urls

positional arguments:
  inputfile   Input file location
  outputfile  Output file location

optional arguments:
  -h, --help  show this help message and exit
```