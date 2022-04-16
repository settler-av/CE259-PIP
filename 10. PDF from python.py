# Generate PDF file of your 3rd Semester Mark-sheet
from PIL import Image

image_1 = Image.open(r'test.png')
im_1 = image_1.convert('RGB')
im_1.save(r'test.pdf', 'PDF', resolution=100.0)

