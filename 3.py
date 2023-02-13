import requests
from bs4 import BeautifulSoup

def count_tags(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers = headers)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    tags = soup.find_all()
    attrs = 0
    for tag in tags:
      if tag.attrs:
        attrs+=1
  
    return len(tags),attrs


url = "https://greenatom.ru/"
tag_count_total, cnt_with_attrs = count_tags(url)
print("Number of HTML tags", tag_count_total)
print("Number of HTML tags with attrs:", cnt_with_attrs)
