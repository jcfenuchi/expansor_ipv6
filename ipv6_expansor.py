class IPV6_analizer():
    def __init__(self,print=False):
        self.print = print

    def show_ipv6(self,ipv6,result="no"):
        ''' Func to convert ipv6 in 8 blocks expanded '''
        if ipv6.find("::") != -1:
            splited_slice = []
            for blocks in ipv6.split(":"):
                if "" == blocks:
                    for _ in range(9 - len(ipv6.split(":"))):
                        splited_slice.append("0000")
                elif (len_of_block := len(blocks)) < 4:
                    splited_slice.append("0"*(4-len_of_block)+blocks)
                elif blocks != "":
                    splited_slice.append(blocks)
        else:
            splited_slice = []
            for blocks in ipv6.split(":"):
                if (len_of_block := len(blocks)) < 4:
                    splited_slice.append("0"*(4-len_of_block)+blocks)
                else:
                    splited_slice.append(blocks)

        if len("".join(splited_slice)) != 32:
            error = f"error in Ipv6 {ipv6} please check the address inserted."
            return error if self.print == False else print(error)
        
        ipv6_expanded = ":".join(splited_slice)
        return ipv6_expanded if self.print == False or result == "yes" else print(ipv6_expanded)

    def show_ipv6_to_dns(self,ipv6,mask="/128"):
        ''' the mask needs to be divisible by 4 '''
        try:
            if int(mask[1:]) <= 128 and int(mask[1:]) > 0:
                ipv6 = self.show_ipv6(ipv6,"yes")
                ipv6 = "".join(ipv6.split(":"))[::-1]
                ipv6_for_DNS = ".".join(list(ipv6)[-int(mask[1:])//4:])+".ip6.arpa."
                return ipv6_for_DNS if self.print == False else print(ipv6_for_DNS)
            else:
                error = f"error in mask {mask} please check"
                return error if self.print == False else print(error)
        except Exception as err:
            pass
    
    


# print is set default == False if you turn True the methods print result in terminal
# if print is False the method return one string if all Okay
print("this ipv6_expand --------------")
ipv6_expand = IPV6_analizer(print=True)
ipv6_expand.show_ipv6("2800:3f0:4004:80333:200e") # wrong Ipv6 address
ipv6_expand.show_ipv6("2800:3f0:4004:80333::200e") # wrong Ipv6 address
ipv6_expand.show_ipv6("2800:3f0:4004:803::200e")
ipv6_expand.show_ipv6_to_dns("2800:3f0:4004::803:200e",mask="/64")
print("this ipv6_expand_no_print --------------")
ipv6_expand_no_print = IPV6_analizer(print=False)
print(ipv6_expand_no_print.show_ipv6("2800:3f0:4004:803::200e"))
print(ipv6_expand_no_print.show_ipv6_to_dns("2800:3f0:4004::803:200e",mask="/32"))

