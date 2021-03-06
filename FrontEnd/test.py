import base64
import json
import tkinter as tk
import urllib.request
from io import BytesIO

import bs4
from PIL import Image
from PIL.ImageTk import PhotoImage

# with urllib.request.urlopen(extension[0]) as url:
#     s = url.read()
# image = PhotoImage(Image.open(BytesIO(s)))
# tk.Label(mainframe, image=image).grid(column=3, row=1, sticky=tk.W)
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# root.mainloop()

class BrowseImage:
    key = ""

    def __init__(self, searchKey):
        self.key = searchKey
        self.header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/43.0.2357.134 "
                                "Safari/537.36 ",
                  }

    def getURL(self):
        url = "https://www.google.com/search?yv=3&tbm=isch&q=" + self.key + "&start=800" + "&asearch=ichunk&async=_id:rg_s," \
                                                                                       "_pms:s,_fmt:pc"
        req = urllib.request.Request(url, headers=self.header)
        page = urllib.request.urlopen(req)
        soup = bs4.BeautifulSoup(page, "html.parser")
        rs = soup.find_all("div", {"class": "rg_meta"})
        extension = json.loads(rs[1].text)["ou"], json.loads(rs[1].text)["ity"]
        return extension


