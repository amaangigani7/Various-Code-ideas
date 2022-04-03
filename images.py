from PIL import Image

m = Image.open('my.jpg')
# m.show()
# print(m.filename)
# print(m.size)
m.crop((0, 0, 1000, 1000))
m.show()
