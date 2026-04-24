#AND logic for IPv4 that gives the network address based on host address and subnetmask
ip=input("Ipv4 Host address:\n")
sub=input("Subnetmask:\n")
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
try:
    sub1,sub2,sub3,sub4=[int(x) for x in sub.split(".")]
except Exception as e:
    print(e)
subn=[sub1,sub2,sub3,sub4]
check(subn)
check(ipb)
print("="*21)
print(f"{ip1}.{ip2}.{ip3}.{ip4}")
print(f"{sub1}.{sub2}.{sub3}.{sub4}")
net1=ip1&sub1
net2=ip2&sub2
net3=ip3&sub3
net4=ip4&sub4
print("="*21)
print("Ipv4 network address:")
print(f"{net1}.{net2}.{net3}.{net4}")