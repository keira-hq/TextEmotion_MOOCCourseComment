import urllib, urllib.request, sys
import ssl


host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EwvhPMMOMDaofCSW1RTdfFR6&client_secret=wMGB3Eus76iqtx2HHreTsxEVnB0g3gvy'# client_id 为官网获取的AK， client_secret 为官网获取的SK
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if content:
    print(content)