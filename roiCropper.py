# roiCropper.py
# Run this script to use the GUI. Check the console while using it, as some useful info will be printed there
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button
from matplotlib.patches import Rectangle
from termcolor import colored
import os

###################### Modify the following variables if needed 

# Path to your images directory (input)
input_path = 'images/'

# Colour map used to show and save images
cmap = 'gray'

# Coordinates text files directory (output)
coords_path = 'coordinates/'

# Cropped images directory (output)
cropped_path = 'cropped/'

# Format of both the input and output images
img_format = 'jpg'

######################


# variables initialization
img_list = sorted([
    os.path.join(input_path, f)
    for f in os.listdir(input_path)
    if f.lower().endswith(img_format)
])
coords = []
drawn_points = []
rectangles = []
parity = False

rect_palette = plt.get_cmap('Dark2')
current_colour = 0


# functions
def load_img(index):
    ax.clear()
    img = mpimg.imread(img_list[index])
    ax.imshow(img, cmap=cmap)
    ax.set_title(f'Select rectangles on image: {os.path.basename(img_list[index])}')
    print(colored(f'\nCurrent image: {os.path.basename(img_list[index])}', 'blue'))
    fig.canvas.draw()

def save(index):
    # save point coordinates into text file
    output_path = os.path.join(coords_path, os.path.basename(img_list[index])).replace(img_format, 'txt')
    with open(output_path, 'w') as f:
        to_write = ''
        for lin in coords:
            cont = 0
            for n in lin:
                if cont != 0:
                    to_write += f',{n}'
                else:
                    to_write += f'{n}'
                cont += 1
            to_write += '\n'
        f.write(to_write)
    # crop and save image
    img = mpimg.imread(img_list[index])
    output_path = os.path.join(cropped_path, os.path.basename(img_list[index])).replace(f'.{img_format}', '')
    cont = 0
    for lin in coords:
        # skip if there aren't 2 points
        if len(lin) != 4:
            continue
        plt.imsave(f"{output_path}_{cont}.{img_format}",
                   img[lin[1]:lin[3], lin[0]:lin[2]], # [y:h, x,w]
                    cmap=cmap)
        cont += 1

def onclick_point(event):
    global parity, coords, drawn_points, rect_palette, current_colour
    if event.inaxes != ax:
        return
    if event.xdata is not None and event.ydata is not None:
        x,y = int(event.xdata), int(event.ydata)
        print(f'\nSelected point: ({x}, {y})')
        # paridad para que cada 2 puntos se guarden en 1 linea
        if parity:
            punto, = ax.plot(x, y, 'ro')
            coords[-1].append(x)
            coords[-1].append(y)
            r = ax.add_patch(Rectangle((coords[-1][0], coords[-1][1]), x-coords[-1][0], y-coords[-1][1],
                            edgecolor = rect_palette(current_colour % rect_palette.N),
                            fill=False))
            current_colour += 2
            rectangles.append(r)
            print(f'Formed rectangle from ({coords[-1][0]},{coords[-1][1]}) to ({coords[-1][2]},{coords[-1][3]})')
        else:
            punto, = ax.plot(x, y, 'bo')
            coords.append([x,y])

        drawn_points.append(punto)
        parity = not parity
        fig.canvas.draw()

def onclick_next(event):
    global current_img, coords, parity
    save(current_img)
    print(colored(f'\nImage {current_img + 1}/{len(img_list)} saved', 'green'))
    
    if current_img + 1 >= len(img_list):
        print("───────────── No images left, exiting! ─────────────\n")
        exit()
    else:
        print('─────────────────────── Next! ───────────────────────')
    
    current_img += 1
    coords = []
    load_img(current_img)

def onclick_undo(event):
    global coords, drawn_points, parity, rectangles
    if coords and drawn_points:
        print()
        if not parity:
            print(f'Deleted point: ({coords[-1][-2]}, {coords[-1][-1]})')
            print(f'Removed rectangle from ({coords[-1][0]},{coords[-1][1]}) to ({coords[-1][2]},{coords[-1][3]})')
            coords[-1].pop()
            coords[-1].pop()
            r = rectangles.pop()
            r.remove()
        else:
            print(f'Deleted point: ({coords[-1][0]}, {coords[-1][1]})')
            coords.pop()

        print(f'Remaining points for image: {coords}')
        last_point = drawn_points.pop()
        last_point.remove()
        parity = not parity
        fig.canvas.draw()


# main
current_img = 0
fig, ax = plt.subplots()
load_img(current_img)
plt.subplots_adjust(bottom=0.2)
cid = fig.canvas.mpl_connect('button_press_event', onclick_point)

# buttons
button_next_ax = plt.axes([0.55, 0.05, 0.2, 0.075])
button_next = Button(button_next_ax, 'Next image')

button_undo_ax = plt.axes([0.25, 0.05, 0.2, 0.075])
button_undo = Button(button_undo_ax, 'Undo')

button_next.on_clicked(onclick_next)
button_undo.on_clicked(onclick_undo)

plt.show()

save(current_img)