import base64
import json
import urllib.request
import tkinter as tk
import bs4

key = "martin"

wiki = "https://www.google.com/search?yv=3&tbm=isch&q=" + key + "&start=100" + "&asearch=ichunk&async=_id:rg_s," \
                                                                               "_pms:s,_fmt:pc"
header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/43.0.2357.134 "
                        "Safari/537.36 ",
          }

req = urllib.request.Request(wiki, headers=header)

page = urllib.request.urlopen(req)

soup = bs4.BeautifulSoup(page, "html.parser")
rs = soup.find_all("div", {"class": "rg_meta"})
print(soup.prettify())

extension = json.loads(rs[1].text)["ou"], json.loads(rs[1].text)["ity"]
print(extension[0])


root = tk.Tk()
root.title("Feet to Meters")
mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
with urllib.request.urlopen(extension[0]) as url:
    s = url.read()
b64 = base64.encodebytes(s)
image = tk.PhotoImage(b64)
# label = ttk.Label(image=image)
# label.pack()
tk.Label(mainframe, image=image).grid(column=3, row=1, sticky=tk.W)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
