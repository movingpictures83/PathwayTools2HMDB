# PathwayTools2HMDB
# Language: Python
# Input: TXT
# Output: TXT
# Tested with: PluMA 1.1, Python 3.6
# Dependency: Pathway Tools Database

Map Pathway Tools (Karp et al, 2015) metabolite identifiers to HMDB identifiers.

The plugin accepts an input TXT file with one tab-delimited keyword-value pair,
the hostname on which Pathway Tools is running (keyword: "hostname")

The mapping of identifiers will be output to another TXT file in tabular format,
once again tab-delimited.

Note: The plugin depends on PathwayTools being installed and executing on a host.
