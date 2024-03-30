from PIL import Image
trees = [Image.open(f'tree{i}.png') for i in range(25)]


trees[0].save('seasons.gif',
              save_all=True,
              append_images=trees[1:],
              optimize=True,
              duration=1000,
              loop=0)