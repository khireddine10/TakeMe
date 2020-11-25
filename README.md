# TakeMe
TakeMe tool is used to check if the target domain name have subdomains that can be takeovred.

# How The tool works
The tool have three parties.
The First Function list all the subdomain of the target domain using the sublist3r tool
The Second Function Check if the subdomains returned by the function one have a CNAME Record in the dns
The Third Function do http request and check the status code of each subdomain that have CNAME Record


