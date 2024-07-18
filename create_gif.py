import imageio.v3 as iio

filenames = ['name.png', 'name.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('pic.gif', images, duration = 500, loop = 0)
