from termcolor import colored
import requests

class Arsen():
    def __init__(self):
        self.subdomain = 0

    def banner(self):
        print(colored("#     _    ____  ____  _____ _   _ ", "green"))
        print(colored("#    / \  |  _ \/ ___|| ____| \ | |", "green"))
        print(colored("#   / _ \ | |_) \___ \|  _| |  \| |", "green"))
        print(colored("#  / ___ \|  _ < ___) | |___| |\  |", "green"))
        print(colored("# /_/   \_\_| \_\____/|_____|_| \_|", "green"))
        print(colored("# Author      :", "green") + "Red-X")
        print(colored("# Instagram   :", "green") + "https://www.instagram.com/kiziilyildiz")
        print(colored("# GitHub      :", "green") + "https://github.com/Zeynel-Cubuk")
        print(colored("# Title       :", "green") + "arsen.py")
        print(colored("# Description :", "green") + "Subdomain Enumeration")
        print(colored("# Date        :", "green") + "7/10/2020")
        print(colored("# Version     :", "green") + "1.0")
        print(colored("#==============================================================================", "green"))

    def requester(self,url):
        try:
            if "http://" in url or "https://" in url:
                return requests.get(url)
            else:
                return requests.get("http://" + url)

        except requests.exceptions.ConnectionError:
            pass

        except requests.exceptions.InvalidURL:
            pass

        except UnicodeError:
            pass

    def discover(self,domain):
        with open("subdomain.txt", "r") as subdomainlist:
            for line in subdomainlist:
                line = line.strip()
                url = line + "." + domain

                response = self.requester(url)

                if response:
                    self.subdomain += 1
                    print(colored("[+] Found: ", "blue") + str(url))
                else:
                    print(colored("[-] Not Found: ", "magenta") + str(url))

    def keyboardinterrupt_message(self):
        print("[!] Exiting...")

if __name__ == "__main__":
    arsen = Arsen()
    try:
        arsen.banner()
        target = input(colored("| [!] Host/IP: ", "green"))
        print(colored("#==============================================================================", "green"))
        arsen.discover(target)

    except KeyboardInterrupt:
        arsen.keyboardinterrupt_message()