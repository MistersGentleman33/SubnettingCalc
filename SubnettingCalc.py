import sys
from os import system

try:
    def found_new_mask(ipaddress, n_subnetting):
        """
        Variable ipaddress looks like this: [192, 123, 1, 0, C] which contains the ip separate and the class
        The variable n_subnetting contains the number of subnets to calculate """

        new_mask = []
        n_subnetting_aux = n_subnetting
        while n_subnetting_aux >= 8:
            new_mask.append("1" * 8)
            n_subnetting_aux -= 8
        new_mask.append(n_subnetting_aux * "1" + "0" * (8 - n_subnetting_aux))
        while len(new_mask) < 4:
            new_mask.append("0" * 8)
        new_mask = [int(x, 2) for x in new_mask]
        print("The new mask is {}".format(new_mask))

        return new_mask

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
        n_subnetting = sys.argv[2]  # This takes args of subnetting from terminal

        try:
            n_subnetting = int(sys.argv[2])
        except ValueError:
            system('cls')
            print("!!!ERROR The Second argument '{}' is an invalid number !!!".format(n_subnetting))
            exit(1)

        ipaddress = sys.argv[1]  # This takes args of IP from terminal
        ipaddress = ipaddress.split(".")
        ipaddress = [int(x) for x in ipaddress]  # Converting to integer the IP
        ipaddress = identify_class(ipaddress)  # Return a list with the IP and the class

        # Function subnetting
        new_mask = found_new_mask(ipaddress, n_subnetting)


    if __name__ == "__main__":
        main()

except IndexError:
    system('cls')
    print("\n\t!!!!!!!!!!!! ERROR !!!!!!!!!!!!")
    print("[!] Use: python {} <ip_address> <subnet_number>".format(sys.argv[0]))
