import sys
from os import system

try:
    def subnetting_class_a(ipaddress, nets, new_mask, n_subnetting):
        pass


    def subnetting_class_b(ipaddress, nets, new_mask, n_subnetting):
        pass


    def subnetting_class_c(ipaddress, nets, new_mask, n_subnetting):
        #   Here I calculate the jump between nets (256 - new mask)
        jump_net = 256 - new_mask[3]
        jump_net_aux = jump_net
        print("\n")

        for i in range(2 ** nets):
            if i + 1 == 1:
                print("{}.".format(i + 1))
                print("Network: ", end="")
                print(*ipaddress[:4], sep=".", end="")
                print("/{}".format(n_subnetting))
                print("HostMin: ", end="")
                print(*ipaddress[:3], sep=".", end="")
                print(".{}".format(ipaddress[3] + 1))
                print("HostMax: ", end="")
                print(*ipaddress[:4], sep=".", end="")
                print(".{}".format(jump_net - 2))
                print("Broadcast: ", sep="", end="")
                print(*ipaddress[:3], sep=".", end="")
                print(".{}".format(jump_net - 1))
                print("Hosts/Net: {}".format(jump_net - 2))
            else:
                print("{}.".format(i + 1))
                print("Network:   ", end="")
                print(*ipaddress[:3], sep=".", end="")
                print(".{}/{}".format(jump_net, n_subnetting))
                print("HostMin:   ", end="")
                print(*ipaddress[:3], sep=".", end="")
                print(".{}".format(jump_net + 1))
                jump_net += jump_net_aux
                print("HostMax:   ", end="")
                print(*ipaddress[:3], sep=".", end="")
                print(".{}".format(jump_net - 2))
                print("Broadcast: ", end="")
                print(*ipaddress[:3], sep=".", end="")
                print(".{}".format(jump_net - 1))
                print("Hosts/Net: {}".format(jump_net_aux - 2))


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

        # n from the formula 2^n = subnet
        nets = None
        if ipaddress[4] == "A":
            nets = n_subnetting - 8
        elif ipaddress[4] == "B":
            nets = n_subnetting - 16
        elif ipaddress[4] == "C":
            nets = n_subnetting - 24
        return new_mask, nets


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

        # Function that finds the new mask
        new_mask, nets = found_new_mask(ipaddress, n_subnetting)

        # Function that calculate the subnets
        if ipaddress[4] == "A":
            subnetting_class_a(ipaddress, nets, new_mask, n_subnetting)

        elif ipaddress[4] == "B":
            subnetting_class_b(ipaddress, nets, new_mask, n_subnetting)

        elif ipaddress[4] == "C":
            subnetting_class_c(ipaddress, nets, new_mask, n_subnetting)


    if __name__ == "__main__":
        main()

except IndexError:
    system('cls')
    print("\n\t!!!!!!!!!!!! ERROR !!!!!!!!!!!!")
    print("[!] Use: python {} <ip_address> <subnet_number>".format(sys.argv[0]))
