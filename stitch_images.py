#!/usr/bin/python
import cv2, sys, itertools

images = []
n = 1 # Choose every nth element
for arg in itertools.islice(sys.argv, 1, None, n):
    print(arg)
    images.append(cv2.imread(arg))

stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

if status == 0:
    cv2.imwrite("stitched.jpg", stitched)
else:
    print("Error %d stitching image" % status)
