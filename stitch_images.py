#!/usr/bin/python
import cv2, sys

images = []
for arg in sys.argv[1:]:
    images.append(cv2.imread(arg))

stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

if status == 0:
    cv2.imwrite("stitched.jpg", stitched)
else:
    print("Error %d stitching image" % status)
