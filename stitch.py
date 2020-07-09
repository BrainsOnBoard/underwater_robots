#!/usr/bin/python
import ast
import cv2
import glob
import numpy as np
import os
import sys
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


def get_image_paths(dirname):
    return sorted(glob.glob(os.path.join(dirname, '*.jpg')))


def load_images(dirname):
    images = []
    for path in get_image_paths(dirname):
        images.append(read_image(path))
    print('%i images loaded' % len(images))
    return images


def read_image(path):
    im = cv2.imread(path)
    cv2.cvtColor(im, cv2.COLOR_BGR2RGB, im)
    assert(im.dtype == np.uint8)
    return im.astype(np.double) / float(255)


def read_image_greyscale(path):
    im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    assert(im.dtype == np.uint8)
    return im.astype(np.double) / float(255)


def load_images_greyscale(dirname):
    images = []
    for path in get_image_paths(dirname):
        images.append(read_image_greyscale(path))
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


def stitch_interactive(dirname):
    # Load all images in folder
    images = load_images(dirname)

    # Either load diffs from cache file or get from user input
    diffs = get_diffs(dirname, images)

    # Do stitching
    cdiffs = cumsum(diffs[0])
    from_left = cdiffs[-1] < 0  # camera might have been going left or right
    if from_left:
        cdiffs = [abs(c) for c in cdiffs]
    return stitch(images, cdiffs, from_left)


def stitch_static_mean(dirname, from_left, mean_diff):
    return stitch_static_images(dirname, from_left, load_images(dirname), mean_diff)


def stitch_static(dirname, from_left):
    images = load_images(dirname)
    xdiffs, _ = get_diffs(dirname, images)
    mean_diff = sum(xdiffs) / len(xdiffs)
    return stitch_static_images(dirname, from_left, images, mean_diff)


def stitch_static_images(dirname, from_left, images, mean_diff):
    print('Mean difference:', mean_diff)
    cdiffs = cumsum([mean_diff] * len(get_image_paths(dirname)))
    return stitch(images, cdiffs[:-1], from_left)


def stitch(images, cdiffs, from_left):
    assert(len(images) == len(cdiffs))
    # Do stitching
    height, width, channels = images[0].shape
    cmax = round(max(cdiffs))
    panorama = np.empty(((height, width + cmax, channels, len(images))), images[0].dtype)
    panorama[:] = np.NaN
    for i in range(len(images)):
        hlo = round(cdiffs[i])
        if not from_left:
            hlo = cmax - hlo

        # Overlay current image on top of panorama (excluding nans)
        panorama[:, hlo:(hlo + width),:, i] = images[i]
    panorama = np.nanmean(panorama, 3)
    return panorama


if __name__ == '__main__':
    panorama = stitch_interactive(sys.argv[1])
    plt.imshow(panorama)
    plt.show()
