import dns.resolver
import urllib3
import argparse
from sublister import sublist3r
from termcolor import colored
import re,sys
class TakeMe:
    
    def __init__(self,domain_name,file_name,sub_domain):
        self.domain_name = domain_name
        self.file_name = file_name
        self.sub_domain = sub_domain

    def check_input(self):
        """
        this method used to check the domain entred by the user 
        """
        domain_name_check = re.compile("^(https?:\/\/(www.|)[a-zA-Z0-9à@_-é]+"
                                       "\.[a-z]+|([a-z]+\.)?[a-zA-Zà@_-é]+\.[a-zA-Z0-9à@_-é]+$)")
        if not domain_name_check.match(self.domain_name):
            error = colored("Please enter a valid domain","red")
            print(error)
            sys.exit(0)

    def list_sub(self):
        """
        this method get the domain_name and use the sublister to list all the subdomains

        :return: list all subdomains of the domain name
        """
        subdomains = sublist3r.main(self.domain_name, None, None, ports=None, silent=False,
                                    verbose=False, enable_bruteforce=False, engines=None)
        return subdomains

    def list_sub_cname(self):
        """
        this method get the list returned by list_sub function and do dns resolve ( cname record )
        to all the subdomains of the domain name

        :return: list contain dict of domains and cname also return list of this subdomains
        """
        list_cname = []
        dict_cname = dict()
        def dns_recon(subdomain):
            list = []
            dict = {}
            result = dns.resolver.resolve(subdomain, 'cname')
            list.append(subdomain)
            for cname in result:
                dict[subdomain] = cname.to_text()
            return [list,dict]
        try:
            if self.sub_domain != False:
                list_cname.extend(dns_recon(self.domain_name)[0])
                dict_cname.update(dns_recon(self.domain_name)[1])
            else:
                subdomains = self.list_sub()
                for subdomain in subdomains:
                    list_cname.extend(dns_recon(subdomain)[0])
                    dict_cname.update(dns_recon(subdomain)[1])
        except BaseException:
            pass
        dns_recon_list = [list_cname, dict_cname]
        return dns_recon_list

    def list_takeover(self):
        """
        this method get the list returned by the list_sub_cname method and do request to those
        subdomains and check if this subdomains possible vulnerable to subdomain takeover

        :return: file and terminal output of all possible subdomains
                 that vulnerable to subdomain takeover
        """
        self.check_input()
        dict_takeover = dict()
        list_takeover = []
        list_sub_cname = self.list_sub_cname()[0]
        http = urllib3.PoolManager()
        for url in  list_sub_cname:
            resp = http.request('GET', url )
            if resp.status in [404,410]:
                list_takeover.append(url)
                dict_takeover[url] = self.list_sub_cname()[1][url]
            else:
                pass
        if self.file_name != None:
            if len(list_takeover) > 0:
                 with open(self.file_name,"w") as file :
                     print(
                         colored("######## the possible subdomains vulnerable to subdomain takeover are saved"
                                 " in {} file ########".format(self.file_name), "green"))
                     for sub_domain in dict_takeover:
                         all = sub_domain + "  " + "----->" + "  " + "CNAME:" + " " + dict_takeover[sub_domain] + "\n"
                         file.write(all)
            else:
                print(colored("######## No subdomain vulnerale to takeover ########","green"))
        else:
             if len(list_takeover) > 0:
                print(colored("######## the possible subdomains vulnerable to subdomain takeover ########","green"))
                for sub_domain in dict_takeover:
                    print(colored(sub_domain + "  " + "------->" + "  " + "CNAME:" + dict_takeover[sub_domain] + "\n","blue"))
             else:
                 print(colored("######## No subdomain vulnerale to takeover ########", "red"))


description = colored('TakeMe is a tool that give you all possible '
                              'subdomains that vulnerable to subdomain takeover', 'blue') + \
                              colored(" created by khireddine Belkhiri @khireddine10", "yellow")
domain_arg = colored('Domain name to enumerate subdomains of "Required" ', "green")
file_arg = colored("File to save the subdomains to", "green")
test_sub = colored("To check only this subdomain", "green")
parser = argparse.ArgumentParser(description=description)
parser.add_argument("-d", "--domain", required=True, help=domain_arg)
parser.add_argument("-f", "--file",required=False, help=file_arg)
parser.add_argument("-s",required=False, help=test_sub)
args = vars(parser.parse_args())
takeme = TakeMe(domain_name=args["domain"],file_name=args["file"],sub_domain=args["s"])
takeme.list_takeover()
