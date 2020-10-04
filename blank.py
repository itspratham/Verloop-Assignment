# import os
# j = open("saviance.txt","x")


import requests
image_url = "https://images-na.ssl-images-amazon.com/images/I/716a06L2ZXL.ACSL1500_.jpg"
img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)