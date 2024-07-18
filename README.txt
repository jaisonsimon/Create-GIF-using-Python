Let’s open up a code editor like VS Code and create a new file called create_gif.py.
To use the imageio library, you need to import it in your code:
import imageio.v3 as iio
The "v3" in the import statement means you're using version 3 of the imageio library. The as part allows you to give the library a shorter name to work with (a nickname/alias), making it more convenient. So we've renamed imageio.v3 to iio moving forward.

Now, run the code to make sure it works. Hopefully there's no error!
Here are two images that you can use for this project(Its in the repository):
pic1.png
pic2.png
Note: Make sure to store the image files in the same folder as your Python program file. 💡

In our Python program, we'll create a list that contains the locations of the image files. We also need to create an empty list that will be used to store the actual image data from these files.

filenames = ['pic1.png', 'pic2.png']
images = [ ]

Next, let’s use a for loop to go through the file paths and read the images using imageio library’s .imread() method:
for filename in filenames:
  images.append(iio.imread(filename))

The .imread() method loads an image based on the file path. So now, our images variable has all the images!

Lastly, let’s use the .imwrite() method to turn the images into a GIF:

iio.imwrite('pic.gif', images, duration = 500, loop = 0)

This takes in four arguments:

'pic.gif': This is the name you want to give to your new GIF file.
images: The list containing the image data.
duration = 500: How long each picture should show in the GIF, in milliseconds.
loop = 0: How many times the GIF should repeat (0 means it keeps looping forever).
And that’s it! 

Let’s run this program and see what happens!

In the terminal, navigate to the folder with the Python file using cd (change directory as taught in the Command Line course. For example, if your file and images are in the Desktop folder, you can do:

cd Desktop

Run python3 and the file name:

python3 create_gif.py

If you are in VS Code, you can run the program by clicking the play button ▶️ (might need to also "Select Interpreter" to run the correct version of Python).

A new pic.gif should appear in the same folder.
