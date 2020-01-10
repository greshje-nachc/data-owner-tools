# Data Owner Tools

Tools for CODI data owners to garble PII to send to the data coordinating center (DCC) for matching. These tools facilitate hashing / Bloom filter creation part of a Privacy-Preserving Record Linkage (PPRL) process.

## Installation

This software expects [clkhash](https://github.com/data61/clkhash) to be installed. Please follow the directions followed on the clkhash website to install. Scripts provided in these tools require Python 3 (which is also required for clkhash). They have been tested with Python 3.7.4.

## Garbling Information

clkhash will garble personally identifiable information (PII) in a way that it can be used for linkage later on. The CODI PPRL process garbles information a number of different ways. The `garble.py` script will manage
executing clkhash multiple times and package the information for transmission to the DCC.

`garble.py` requires 3 different inputs:
1. The location of a directory of clkhash linkage schema files
1. The salt values to use in the garbling process
1. The location of a CSV file containing the PII to garble

`garble.py` requires that the location of the PII and schema files are provided via command line flags. The salt values are collected while the application is running, to avoid them being captured in command line execution history.

`garble.py` will provide usage information with the `-h` flag:

```
$ python3 garble.py -h
usage: garble.py [-h] --source SOURCE --schema SCHEMA

Tool for garbling PII in for PPRL purposes in the CODI project

optional arguments:
  -h, --help       show this help message and exit
  --source SOURCE  Source PII CSV file
  --schema SCHEMA  Directory of linkage schema
```
