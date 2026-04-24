#AND logic for IPv4 that gives the network address based on host address and subnetmask
ip=input("Ipv4 Host address:\n")
def check(list):
    for i in list:
        if i > 255:
            print("No numbers bigger then 255 or lower then 0")
        else:
            pass
try:
    ip1,ip2,ip3,ip4=[int(x) for x in ip.split(".")]
except Exception as e:
    print(e)
ipb=[ip1,ip2,ip3,ip4]
check(ipb)
check(ipb)
print(f"{ip1:08b}.{ip2:08b}.{ip3:08b}.{ip4:08b}")
print("="*21)
sub=input("Subnetmask:\n")
try:
    sub1,sub2,sub3,sub4=[int(x) for x in sub.split(".")]
except Exception as e:
    print(e)
subn=[sub1,sub2,sub3,sub4]
check(subn)
print(f"{sub1:08b}.{sub2:08b}.{sub3:08b}.{sub4:08b}")
net1,net2,net3,net4=ip1&sub1,ip2&sub2,ip3&sub3,ip4&sub4
print("="*21)
print("Ipv4 network address:")
print(f"{net1}.{net2}.{net3}.{net4}")
print(f"{net1:08b}.{net2:08b}.{net3:08b}.{net4:08b}")
