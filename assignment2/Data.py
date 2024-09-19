import requests
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt

url="http://scstac.oceanguide.org.cn/index.htm"

x_vals = []
y_vals = []

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
trs = soup.select('table.table02  tr')
for tr in trs:
    tds = tr.select('td')
    x_vals.append(datetime.fromisoformat(tds[2].string))
    y_vals.append(int(tds[3].string))


fig, ax = plt.subplots()

# plot some data on the axis
ax.plot(x_vals, y_vals)

print(y_vals)
# show the plot
plt.show()
    
    


