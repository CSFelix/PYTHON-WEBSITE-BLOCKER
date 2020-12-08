import time
from datetime import datetime as dt

hosts_path = '/etc/hosts' # linux and mac
#hosts_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts' # windows
redirect = '127.0.0.1'
website_list = ["www.facebook.com", "facebook.com"]

while True:
	# hour of work: 8:00 - 18:00
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print('WebSite Not Allowed!!')

        # write blocked websites in the file
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in website_list:
                if site in content: pass
                else: file.write(redirect + ' ' + site + '\n')
    else:
    	# take off blocked websites in the file
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)

            file.truncate()
        print('WebSite is Allowed')

    # check the time for each 5 seconds
    time.sleep(5)
