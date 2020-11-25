# TakeMe
TakeMe is a python tool used to check if the target domain name have subdomains that can be takeovred.

# How The tool works
1- The tool have three functions.

2- The First Function list all the subdomain of the target domain using the sublist3r tool.

3- The Second Function Check if the subdomains returned by the function one have a CNAME Record in the dns.

4- The Third Function do http request and check the status code of each subdomain that have CNAME Record.

5- The tool return all the subdomain returned by the sublister tool

6- The tool also return all the subdomains that can be takeovred ( in the terminal output or in a file entred by the user )

![alt text](https://github.com/khireddine10/TakeMe/blob/main/takeme.png)

# Installation
```
git clone https://github.com/khireddine10/TakeMe
```
