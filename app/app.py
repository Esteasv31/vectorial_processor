from scipy import misc
import matplotlib.pyplot as plt

f1 = misc.imread('../test_img/01.jpeg')
f2 = misc.imread('../test_img/02.jpg')
f3 = misc.imread('../test_img/03.jpeg')

misc.imsave('../test_img/01.png', f1)
misc.imsave('../test_img/02.png', f2)
misc.imsave('../test_img/03.png', f3)

f1 = misc.imread('../test_img/01.png')
f2 = misc.imread('../test_img/02.png')
f3 = misc.imread('../test_img/03.png')

# plt.imshow(f1)
# plt.show()
print(type(f1) + ' / ' + f1.shape + ' - ' + f1.dtype)

# plt.imshow(f2)
# plt.show()
#
# plt.imshow(f3)
# plt.show()