# qlik-sense-ticket-python
## Description

Example of how to request a ticket from Qlik Sense Proxy Service API using Python using ReST

## Requirements

    Python 3 - Download
    Certificates exported from Qlik Sense in PEM format (stored on local drive)

### Introduction

Note: This is purely an example, and probably not suitable for production.  It provides a process to create a ticket in Python.  This code is not supported by Qlik in anyway.

### Configure Qlik Sense

    Configure a virtual proxy for ticketing to use with this code. Virtual proxy configuration examples may be found on QlikCommunity. 
    Export the Qlik Sense certificates in PEM format and store them locally.
    Ensure port 4243 is open on the firewall to Qlik Sense

