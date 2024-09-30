import imageio
filenames = ["D:/Python/Gif Creator/mountains.jpg","D:/Python/Gif Creator/lakes.png"]
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('D:/Python/Gif Creator/movie.gif', images,'GIF',duration=1)