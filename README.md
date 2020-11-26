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

## Installation
```
git clone https://github.com/khireddine10/TakeMe
```
## Recommended Python Version:
TakeMe currently supports **Python 3**.

## Dependencies:
TakeMe depends on the `urllib3`, `dnspython` and `argparse` python modules.

Sublist3r depends on the `requests`, `dnspython` and `argparse` python modules.

All these dependencies can be installed using the requirements file:

```
pip install -r requirements.txt
```

## Usage

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-d            | --domain      | Domain name to enumerate subdomains of
-f            | --file        | Domain name to enumerate subdomains of
-sS           |               | This used for check the subdomain gived only "without create subdomain list"
## how to use takeme
* To list all the basic options use -h argument

```python takeme.py -h```

* To enumerate vulnerable subdomains of specific domain

```python takeme.py -d example.com```

```python takeme.py --domain example.com```

* To save the output to a file

```python takeme.py -d example.com -f exemple.txt ```

```python takeme.py --domain example.com --file exemple.txt ```

* To check one subdomain if vulnerable to subdomain takeover
``` python takeme.py -d ex.exemple.com -sS  ```

## License

TakeMe is licensed under the GNU GPL license. take a look at the [LICENSE](https://github.com/khireddine10/TakeMe/blob/main/LICENSE) for more information.

