import sys
from os import system

try:
    def subnetting(ipaddress, n_subnetting):
        pass


    def identify_class(ipaddress):
        if 1 <= ipaddress[0] <= 126:
            print("\nYour IP address is class A")
            ipaddress.append("A")
            return ipaddress

        elif 128 <= ipaddress[0] <= 191:
            print("\nYour IP address is class B")
            ipaddress.append("B")
            return ipaddress

        elif 192 <= ipaddress[0] <= 223:
            print("\nYour IP address is class C")
            ipaddress.append("C")
            return ipaddress

        else:
            print("Invalid IP address")
            exit(1)


    def main():
        n_subnetting = sys.argv[2]     # This takes args of subnetting from terminal

        try:
            n_subnetting = int(sys.argv[2])
        except ValueError:
            system('cls')
            print("!!!ERROR The Second argument '{}' is an invalid number !!!".format(n_subnetting))
            exit(1)

        ipaddress = sys.argv[1]  # This takes args of IP from terminal
        ipaddress = ipaddress.split(".")
        ipaddress = [int(x) for x in ipaddress]  # Converting to integer the IP
        ip_class = identify_class(ipaddress)  # Return a list with the IP and the class

        # Function subnetting
        subnetting(ip_class, n_subnetting)


    if __name__ == "__main__":
        main()

except IndexError:
    system('cls')
    print("\n\t!!!!!!!!!!!! ERROR !!!!!!!!!!!!")
    print("[!] Use: python {} <ip_address> <subnet_number>".format(sys.argv[0]))
