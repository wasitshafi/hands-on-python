from PIL import Image, ImageFilter

original = Image.open("squareBoat.jpg")
blurred  = original.filter(ImageFilter.BLUR)

original.show()
blurred.show()
