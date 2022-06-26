import streamlit as st
from PIL import Image, ImageFilter
from PIL import ImageEnhance
import numpy as np
import cv2
import matplotlib.pyplot as plt
plt.style.use('seaborn')
st.title("Image Editing Application")
st.balloons()
path = st.text_input('Enter the file name / Path : ')
if st.button("original"):
	im = Image.open(path) 
	im.show()  
if st.button("blurr"):  
	Original_Image = Image.open(path)
	blur_Image = Original_Image.filter(ImageFilter.BLUR) 
	blur_Image.show() 
if st.button("edit"):
	image = Image.open(path)  
	r, g, b = image.split()    
	image = Image.merge("RGB", (b, g, r))  
	image.show() 
if st.button("flip"):
	imageObject = Image.open(path)  
	hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)  
	hori_flippedImage.show()
if st.button("rotate"):
	imageObject = Image.open(path)   
	hori_flippedImage = imageObject.transpose(Image.FLIP_TOP_BOTTOM)    
	hori_flippedImage.show()  
if st.button("edit2"):
	im = Image.open(path)
	enh = ImageEnhance.Contrast(im)
	enh.enhance(1.5).show("30% more contrast")
if st.button("red"):
	im = np.array(Image.open(path))
	im_R = im.copy()
	im_R[:, :, (1, 2)] = 0
	pil_img = Image.fromarray(im_R)
	pil_img.show()
if st.button("blue"):
	im = np.array(Image.open(path))
	im_B = im.copy()
	im_B[:, :, (0, 1)] = 0
	pil_img = Image.fromarray(im_B)
	pil_img.show()
if st.button("green"):
	im = np.array(Image.open(path))
	im_G = im.copy()
	im_G[:, :, (0, 2)] = 0
	pil_img = Image.fromarray(im_G)
	pil_img.show()
if st.button("dots"):
	img = Image.open(path)
	imgs=img.convert("1")
	imgs.show()
if st.button("black & white"):
	img = Image.open(path)
	imgs=img.convert("L")
	imgs.show()
if st.button("black edit"):
	img = Image.open(path)
	imgs=img.convert("LA")
	imgs.show()
if st.button("emboss"):
	img = Image.open(path)
	img2 = img.filter(ImageFilter.EMBOSS)
	img2.show()
if st.button("contour"):
	img = Image.open(path)
	img2 = img.filter(ImageFilter.CONTOUR)
	img2.show()
if st.button("sharpen"):
	img = Image.open(path)
	img2 = img.filter(ImageFilter.SHARPEN)
	img2.show()
if st.button("maxfilter"):
	img = Image.open(path)
	img2 = img.filter(ImageFilter.MaxFilter(size=3))
	img2.show()
if st.button("minfilter"):
	img = Image.open(path)
	img2 = img.filter(ImageFilter.MinFilter(size=3))
	img2.show()
if st.button("bright"):
	img = Image.open(path)
	applier = ImageEnhance.Brightness(img)
	applier.enhance(3).show()
if st.button("sharp"):
	img = Image.open(path)
	applier = ImageEnhance.Sharpness(img)
	applier.enhance(8).show()
if st.button("colour"):
	img = Image.open(path)
	applier = ImageEnhance.Color(img)
	applier.enhance(0.5).show()
if st.button("pencil"):
	img = cv2.imread(path)
	grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	invert = cv2.bitwise_not(grey_img) 
	blur = cv2.GaussianBlur(invert, (21, 21), 0)
	invertedblur = cv2.bitwise_not(blur)
	sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
	cv2.imwrite("sketch.png", sketch)
	im = Image.open(r"sketch.png") 
	im.show() 
if st.button("logo"):
	image = Image.open(path)
	logo = Image.open('logo.png')
	image_copy = image.copy()
	position = ((image_copy.width - logo.width),(image_copy.height - logo.height))
	image_copy.paste(logo, position)
	image_copy.save('pasted_image.jpg')
	im = Image.open(r"pasted_image.jpg")
	im.show()
if st.button("resize"):
	image = Image.open(path)
	new_image = image.resize((400, 400))
	new_image.save('image_400.jpg')
	im = Image.open(r"image_400.jpg")
	im.show()
if st.button("thumbnail"):
	image = Image.open(path)
	image.thumbnail((400, 400))
	image.save('image_thumbnail.jpg')
	im = Image.open(r"image_thumbnail.jpg")
	im.show()
if st.button("crop"):
	image = Image.open(path)
	box = (200, 300, 700, 600)
	cropped_image = image.crop(box)
	cropped_image.save('cropped_image.jpg')
	im = Image.open(r"cropped_image.jpg")
	im.show()
if st.button("edit3"):
	image = Image.open(path)
	red, green, blue = image.split()	
	new_image = Image.merge("RGB", (green, red, blue))
	new_image.save('new_image.jpg')
	im = Image.open(r"new_image.jpg")
	im.show()
if st.button("enhance"):
	image = Image.open(path)
	contrast = ImageEnhance.Contrast(image)
	contrast.enhance(1.5).save('contrast.jpg')
	im = Image.open(r"contrast.jpg")
	im.show()

