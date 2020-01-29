import sys
import os
from PIL import Image

# image_folder = sys.argv[1]
image_folder = 'new'
# output_folder = sys.argv[2]
output_folder = 'newer'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir('C:/Users/ADMIN/PycharmProjects/basic/' + image_folder):
    img = Image.open('{}/{}'.format(image_folder, filename))
    clean_name = os.path.splitext(filename)[0]
    img.save('{}/{}'.format(output_folder, filename), 'png')
print('all done!')
