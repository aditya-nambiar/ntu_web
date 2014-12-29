import urllib.request as url
import time
for i in range(11,14):
    u = "http://www.wunderground.com/history/airport/WSSS/2014/5/"+str(i)+"/DailyHistory.html?MR=1&format=1"
    #print(u)
    resp = url.urlopen(u)
    html = str(resp.read())
    all = html.split(',')
    prev = ""
    for j in range(0,int(len(all)/13)):
        temp = all[13+j*13][-5]+all[13+j*13][-4]
        if temp == "00":
            if prev != all[13+j*13][-7] :
                prev = all[13+j*13][-7]
                print(all[14+j*13])
                
