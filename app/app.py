import numpy
from PIL import Image


img = Image.open('/home/vidarr/Projects/TEC/Arqui_2/Proyecto_II/test_img/02.png')
array = numpy.array(img)
print(array.shape)
print(array)
print(len(array[0]))

mask = 123456732

for i in range(len(array)):
    for j in range(len(array[0])):
        for k in range(len(array[0][0])):
            array[i][j][k] = array[i][j][k] ^ mask

img = Image.fromarray(array)
img.save('test.png')

for i in range(len(array)):
    for j in range(len(array[0])):
        for k in range(len(array[0][0])):
            array[i][j][k] = array[i][j][k] ^ mask

img = Image.fromarray(array)
img.save('test1.png')