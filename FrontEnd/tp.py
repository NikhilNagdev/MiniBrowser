import io


import requests
import base64

from PIL import Image
from PIL.ImageTk import PhotoImage

try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen
root = tk.Tk()

root.title("display a website image")
mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
# a little more than width and height of image
w = 520
h = 320
x = 80
y = 100
# use width x height + x_offset + y_offset (no spaces!)

# this GIF picture previously downloaded to tinypic.com
image_url = "https://images-na.ssl-images-amazon.com/images/I/71jos2ODTuL._RI_.jpg"
image_byt = urlopen(image_url).read()
p = Image.open(io.BytesIO(image_byt))
photo = PhotoImage(p)
l = tk.Label(mainframe, image=photo)
l.grid(column=3, row=1, sticky=tk.W)
tk.Label(mainframe, text="nikhjli").grid(column=3, row=1, sticky=tk.W)
root.mainloop()
