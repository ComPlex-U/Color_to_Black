from PIL import Image

open_image = Image.open(r"C:\Users\ASUS\Pictures\29513144_1869613019716571_1183242418938445824_n.jpg")
convert_to_bw = open_image.convert("L")
convert_to_bw.show()