from PIL import Image
img = Image.open('C:/Users/DELL/Downloads/demo.png')
width, height = img.size
print(f"Image Resolution: {width} x {height}")
