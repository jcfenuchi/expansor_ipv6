
class IPV6_analizer():
    def __init__(self,ipv6):
        self.ipv6 = ipv6
        self.tratament01()

    def tratament01(self):
        pos_dpts = self.ipv6.find("::")
        if pos_dpts != -1:
            casas = self.ipv6.split(":")
            self.coloque_zeros(pos_dpts,9-len(casas))
        self.arrume_os04_digitos()
                            
    def coloque_zeros(self,pos_dpts,qtd_de_zeros):
        zero = ":0000"*qtd_de_zeros + ":"
        self.ipv6 = self.ipv6[:pos_dpts]+zero+self.ipv6[pos_dpts+2:]
    
    def arrume_os04_digitos(self):
        ipv6_split = self.ipv6.split(":")   
        for pos,four_bytes in enumerate(ipv6_split):
            if len(four_bytes) < 4:
                new_sequence = "0"*(4-len(four_bytes)) + four_bytes
                ipv6_split[pos] = new_sequence
        self.ipv6 = ":".join(ipv6_split)

    def show_ipv6(self):
        print(self.ipv6)

    def show_ipv6_for_Zone(self):
        ip =  self.ipv6.replace(":","")
        r = [ print(j,end=".") if i != len(ip)-1 else print(j,end="") for i,j in enumerate(ip[::-1]) ]
        print(".ip6.arpa.")


IPV6_analizer("2800:3f0:4004:803::200e").show_ipv6()
IPV6_analizer("2800:3f0:4004:803::200e").show_ipv6_for_Zone()
