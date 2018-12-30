from PIL import Image
from PIL import ImageEnhance, ImageFilter


pic1 =Image.open('developer.png')
pic2= Image.open('hiring.png')
pic3= Image.open('mountain.jpg')

# print('size:'+ str(pic1.size))
# print('mode:'+ str(pic2.mode))

box = (200, 200, 600, 300)
# pic3.crop(box).show()
# pic3.rotate(45,expand = True).show()
# expand:باعث میشه عکس حاشیش نزنه بیرون

# pic1.rotate(45).show()
# pic1.convert(mode ='1').show()
# pic1.convert(mode ='L').show()
# pic1.convert(mode ='RGBA').show()

# pic2.resize((500, 500)).show()
# pic2.resize((pic2.width//2, pic2.height//2)).show()

# n = pic2.copy()
# print('size:'+ str(pic2.size))
# n.thumbnail((500, 500))
# print('size:'+ str(pic2.size))

# pic1.show()
# pic2.show()

# h = pic3.crop(box)
# c=h.convert(mode = "L")

# v = pic2.copy()
# v.paste(c, box)
# v.show()

# pic1.transpose(Image.FLIP_TOP_BOTTOM).show()

# ===>>برعکس میکنه فلیپ
# # ##############################################
ImageEnhance.Color(pic3).enhance(0.2).show()
# 0.2شفافیتو کم میکنه
# ##############################################
# pic3.filter(ImageFilter.GaussianBlur(radius = 10)).show()
# مات میکنه عکسو