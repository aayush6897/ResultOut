from bs4 import BeautifulSoup
import urllib2
from twilio.rest import Client

account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client = Client(account_sid, auth_token)


url="http://ggsipu.ac.in/ExamResults/ExamResultsmain.htm"
page = urllib2.urlopen(url)
sop=BeautifulSoup(page,'lxml')

hh=[]
for i in sop.find_all('td'):
    try:
        content=i.a.contents[0]
        links="http://ggsipu.ac.in/ExamResults/"+i.a['href']
        if "B.Tech.(IT)" in content:
            if "5th Sem" in content:
                hh.append([links,content])
                break
    except:
        continue

if len(hh)>0:
    message = client.messages.create(to="+917011446762",from_="+17609069175",body="result out "+hh[0][0])        