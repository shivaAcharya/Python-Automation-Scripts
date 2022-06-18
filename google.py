#! python3
# google.py - Program to open several search results

import sys, webbrowser, bs4, requests

print('Searching....') #Print searching message while looking for query

res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))

res.raise_for_status()

# Retrieve top search results

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open browser tab for each result
linkElems = soup.select('#rso > div:nth-child(1) > div > div > div > div > div.yuRUbf > a > div > cite')
#linkElem = linkElems.select('div.yuRUbf a[href]')
#rso > div:nth-child(1) > div:nth-child(2) > div > div > div.yuRUbf > div > div.TbwUpd > cite

linkElem = linkElems[0].text()

print(f"There are {linkElem} links in this page.")

'''for i in range(1,5):
    urlToOpen = linkElem[i].getText()
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)'''

#<cite class="iUh30 Zu0yb qLRx3b tjvcx">https://en.wikipedia.org<span class="dyjrff qzEoUe"> › wiki › Python_(programming...</span></cite>
