from PIL import Image
image = Image.new('RGBA', (10, 10), color=(255,255,255,0))
image.save("test.png", quality=95)