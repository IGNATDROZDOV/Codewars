def ips_between(ip1,ip2):
    first_ip = sum([value * (256**index) for index,value in enumerate(reversed(list(map(int,ip1.split('.')))))])
    second_ip = sum([value * (256**index) for index,value in enumerate(reversed(list(map(int,ip2.split('.')))))])
    return second_ip - first_ip