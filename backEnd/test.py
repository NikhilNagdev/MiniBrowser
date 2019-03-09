import json
import urllib.request
from bs4 import BeautifulSoup

key = "martin"

wiki = "https://www.google.com/search?yv=3&tbm=isch&q=" + key + "&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc"

page = urllib.request.urlopen(wiki)

soup = BeautifulSoup(page, "html.parser")
rs = soup.find_all("div", {"class": "rg_meta"})
print(soup.prettify())

extension = json.loads(rs[1].text)["ity"]
print(extension)