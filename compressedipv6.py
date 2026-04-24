#gives a ipv6 adress with no leading zeroes
ip_og=input("ipv6-adress:\n")
ip1,ip2,ip3,ip4,ip5,ip6,ip7,ip8=ip_og.split(":")
ip_bits=[ip1,ip2,ip3,ip4,ip5,ip6,ip7,ip8]
def clean_string(v):
    result = v.lstrip("0")
    return result if result != "" else "0"
ip_bits = [clean_string(i) for i in ip_bits]
ip1,ip2,ip3,ip4,ip5,ip6,ip7,ip8 = ip_bits
print(ip_bits)
print("="*34)
print("No leading zeroes")
print(f"{ip1}:{ip2}:{ip3}:{ip4}:{ip5}:{ip6}:{ip7}:{ip8}")