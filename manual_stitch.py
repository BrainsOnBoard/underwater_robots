#!/usr/bin/python
import ast, cv2, glob, numpy as np, os, sys
from matplotlib import pyplot as plt

def press(event):
    global key
    key = event.key

def get_ref_point(image):
    plt.imshow(image)
    plt.draw()
    return plt.ginput()[0]

def get_diffs(images):
    global key
    refxy = ()
    diffs = ([], [])
    i = 0
    while i < len(images):
        key = None
        curxy = get_ref_point(images[i])
        if i > 0 and key == 'n':
            print('Choose new reference point')
            refxy = get_ref_point(images[i - 1])
        else:
            if i > 0:
                diffs[0].append(curxy[0] - refxy[0])
                diffs[1].append(curxy[1] - refxy[1])
            refxy = curxy
            i += 1
    return diffs

def save_diffs(diffs, diffspath):
    with open(diffspath, 'w') as f:
        f.write(repr(diffs))
    print('Diffs saved to', diffspath)

def cumsum(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length + 1)]
    return cu_list


# I can't figure out how else to get keypresses along with ginput(), but this is
# a bit gross :-(
fig = plt.figure()
fig.canvas.mpl_connect('key_press_event', press)

# Load all the images in the folder
images = []
for p in sorted(glob.glob(os.path.join(sys.argv[1], '*.jpg'))):
    print("Loading", p)
    im = cv2.imread(p)
    assert(im.dtype == np.uint8)
    images.append(im.astype(np.double) / float(255))

# Either load diffs from cache file or get from user input
diffspath = os.path.join(sys.argv[1], 'diffs.py')
diffs = ()
if os.path.isfile(diffspath):
    with open(diffspath, 'r') as f:
        diffs = ast.literal_eval(f.read())
    print('Diffs loaded from', diffspath)
else:
    diffs = get_diffs(images)
    save_diffs(diffs, diffspath)

height, width, channels = images[0].shape
cdiffs = cumsum(diffs[0])
newim = np.empty(((height, width + round(max(cdiffs)), channels)), images[0].dtype)
newim[:] = np.NaN
for i in range(len(images)):
    c = round(cdiffs[i])
    ims = np.empty((height, width, channels, 2), dtype=np.double)
    ims[:,:,:,0] = images[i]
    ims[:,:,:,1] = newim[:, newim.shape[1] - width - c:newim.shape[1] - c, :]
    newim[:, newim.shape[1] - width - c:newim.shape[1] - c, :] = np.nanmean(ims,3)
plt.imshow(newim)
plt.show()
