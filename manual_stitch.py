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

def get_diffs_user_input(images):
    # I can't figure out how else to get keypresses along with ginput(), but this is
    # a bit gross :-(
    fig = plt.figure()
    fig.canvas.mpl_connect('key_press_event', press)

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

def load_images(dirname):
    images = []
    for p in sorted(glob.glob(os.path.join(dirname, '*.jpg'))):
        im = cv2.imread(p)
        cv2.cvtColor(im, cv2.COLOR_BGR2RGB, im)
        assert(im.dtype == np.uint8)
        images.append(im.astype(np.double) / float(255))
    print('%i images loaded' % len(images))
    return images

def get_diffs(dirname, images):
    diffspath = os.path.join(dirname, 'diffs.py')
    diffs = ()
    if os.path.isfile(diffspath):
        with open(diffspath, 'r') as f:
            diffs = ast.literal_eval(f.read())
        print('Diffs loaded from', diffspath)
    else:
        diffs = get_diffs_user_input(images)
        save_diffs(diffs, diffspath)
    return diffs

def stitch(dirname):
    # Load all images in folder
    images = load_images(dirname)

    # Either load diffs from cache file or get from user input
    diffs = get_diffs(dirname, images)

    # Do stitching
    height, width, channels = images[0].shape
    cdiffs = cumsum(diffs[0])
    from_left = cdiffs[-1] < 0 # camera might have been going left or right
    cmax = round(max(abs(c) for c in cdiffs))
    panorama = np.empty(((height, width + cmax, channels)), images[0].dtype)
    panorama[:] = np.NaN
    for i in range(len(images)):
        hlo = round(cdiffs[i])
        if from_left:
            hlo = -hlo
        else:
            hlo = panorama.shape[1] - width - hlo

        # Overlay current image on top of panorama (excluding nans)
        ims = np.empty((height, width, channels, 2), dtype=np.double)
        ims[:,:,:,0] = images[i]
        ims[:,:,:,1] = panorama[:, hlo:(hlo + width), :]
        panorama[:, hlo:(hlo+width), :] = np.nanmean(ims,3)
    return panorama

if __name__ == '__main__':
    panorama = stitch(sys.argv[1])
    plt.imshow(panorama)
    plt.show()
