# %%
from PIL import Image, ImageEnhance

resize_factor = 8
contrast_factor = 1.5

scale = ['@', '%', '#', '*', '+', '=', '-', ':'
, '.', ' ']

# %%
scale = list(reversed(scale))

img = Image.open("monalisa.jpg").convert("L")
img = ImageEnhance.Contrast(img).enhance(contrast_factor)
w = img.width
h = img.height
img = img.resize((w//resize_factor, h//resize_factor))
raw = list(img.getdata())

text = []
for p in raw:
  x = int( (p / 255) * (len(scale)-1) )
  text.append(scale[x] + scale[x])

rows = img.height
cols = img.width

data = []
for row in range(rows):
  data.append(text[row*cols:(row+1)*cols])

file = open("index.html", 'w')
file.write("""<!DOCTYPE html><html><body><code><span style="display: block;
line-height:8px;font-size:8px;font-weight:bold;white-space:pre;font-family:
monospace;color:white;background:black;">\n""")
for line in data:
  file.write(''.join(line) + "\n")
file.write("\n</span></code></html>")
file.close()

# 2x3
# [" ", "@", " ", " ", "@", " "]
# with cols=2
# [
  # [" ", "@"]   0:2, row 0
  # [" ", " "]   2:4, row 1
  # ["@", " "]   4:6, row 2
# ]

#new = [t*2 for t in raw]

# from 0 to 255 (i.e. from black to white)



new_img = Image.new("L", img.size)
new_img.putdata(raw)
new_img.save("output.jpg")









'''
1. Get an image
  - load a local file (".jpg" or ".png")
  - get an image from the internet
  - generate your own image
2. Process the image as lists
  - img.getdata
3. Manipulate the image
  - looping over the raw data and changing the RGB pixel values
4. Save the image
  - Image.new()
  - Image.putdata()
  - Image.save()
'''

'''
img.jpg

4, 3
[(255, 255, 255), (127, 255, 127), (0, 0, 255), (0, 0, 255),
(255, 255, 255), (127, 255, 127), (0, 0, 255), (0, 0, 255),
(255, 255, 255), (127, 255, 127), (0, 0, 255), (0, 0, 255)]

4, 3
[255, 127, 0, 65, 0, 127]

'''

# 255 = completely white (space)
# 0   = completely black (#)
# 127 = approximate gray ($)