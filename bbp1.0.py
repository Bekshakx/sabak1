import subprocess
osname = subprocess.check_output(['uname'])
user_name = subprocess.check_output(['whoami'])
if osname == 'Linux' or 'Unix':
    ip_add_info = subprocess.check_output(['ifconfig']).decode('utf-8')
    ip_add=ip_add_info.split('\n')
    for i in ip_add:
        if '' == i:
            ip_add.remove(i)

    std_ip_add=[]
    a=[]
    for i in ip_add:
        std_ip_add.append(i.split(' '))
    a = std_ip_add[9]

    for i in a:
        if '' == i:
            a.remove(i)
    
    gateway_info = subprocess.check_output(['ip','route']).decode('utf-8')
    gateway_info=gateway_info.split(' ')
    gateway=gateway_info[75]
    print("OS name: {}".format(osname.decode('utf-8')))
    print("User name: {}".format(user_name.decode('utf-8')))
    print("User IP: {}".format(a[3]))
    print("Router IP: {}".format(gateway))


