import requests

url = 'http://dmacc.blackboard.com/'
response = requests.get(url)
html = response.content
f = open("requestResult.txt", "w+")
f.writelines(str(html))
f.close()

#soup = bs.BeautifulSoup(open("requestResult.txt"), 'html.parser')
