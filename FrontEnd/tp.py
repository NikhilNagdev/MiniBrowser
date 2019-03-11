import io
import base64
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
image_url = "http://i46.tinypic.com/r9oh0j.gif"
image_byt = urlopen(image_url).read()
image_b64 = base64.encodestring(image_byt)
photo = tk.PhotoImage(data=image_b64)
# create a white canvas
tk.Label(mainframe, image=photo).grid(column=3, row=1, sticky=tk.W)
tk.Label(mainframe, text="nikhjli").grid(column=3, row=1, sticky=tk.W)
root.mainloop()
