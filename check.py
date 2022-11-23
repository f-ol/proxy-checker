import requests
r = requests.Session()
list = open('proxies.txt')
url = input('Enter the website\'s url : ')
time = input('proxy\'s speed (in sec) : ')
if 'http' not in url:
	url = 'https://' + url
for proxy in list:
	try:
		proxies = {
			'http': f'http://{proxy}',
			'https': f'https://{proxy}'
		}
		check = r.get(url, proxies=proxies, timeout=int(time))
		print(f'good proxy : {proxy}')
		with open('goodproxy.txt', 'a') as save:
			save.write(proxy + '\n')
	except:
		print(f'bad proxy : {proxy}')
