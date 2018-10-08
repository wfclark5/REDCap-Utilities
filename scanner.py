from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2 
 

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to the input image")
# args = vars(ap.parse_args())

image = cv2.imread('test.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
docCnt = None
 
# ensure that at least one contour was found
if len(cnts) > 0:
	# sort the contours according to their size in
	# descending order
	cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
 
	# loop over the sorted contours
	for c in cnts:
		# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
		# if our approximated contour has four points,
		# then we can assume we have found the paper
		if len(approx) == 4:
			docCnt = approx
			break

paper = four_point_transform(image, docCnt.reshape(4, 2))
warped = four_point_transform(gray, docCnt.reshape(4, 2))

thresh = cv2.threshold(warped, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

print thresh

	# find contours in the thresholded image, then initialize
# the list of contours that correspond to questions
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
questionCnts = []
 
# loop over the contours
for c in cnts:
	# compute the bounding box of the contour, then use the
	# bounding box to derive the aspect ratio
	(x, y, w, h) = cv2.boundingRect(c)
	ar = w / float(h)
 
	# in order to label the contour as a question, region
	# should be sufficiently wide, sufficiently tall, and
	# have an aspect ratio approximately equal to 1
	if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
		questionCnts.append(c)

# questionCnts = contours.sort_contours(questionCnts,
# 	method="top-to-bottom")[0]
# correct = 0
 
# # each question has 5 possible answers, to loop over the
# # question in batches of 5
# for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
# 	# sort the contours for the current question from
# 	# left to right, then initialize the index of the
# 	# bubbled answer
# 	cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
# 	bubbled = None

# 	# loop over the sorted contours
# for (j, c) in enumerate(cnts):
# 		# construct a mask that reveals only the current
# 		# "bubble" for the question
# 		mask = np.zeros(thresh.shape, dtype="uint8")
# 		cv2.drawContours(mask, [c], -1, 255, -1)
 
# 		# apply the mask to the thresholded image, then
# 		# count the number of non-zero pixels in the
# 		# bubble area
# 		mask = cv2.bitwise_and(thresh, thresh, mask=mask)
# 		total = cv2.countNonZero(mask)
 
# 		# if the current total has a larger number of total
# 		# non-zero pixels, then we are examining the currently
# 		# bubbled-in answer
# 		if bubbled is None or total > bubbled[0]:
# 			bubbled = (total, j)
