import cv2
import numpy as np

fileloc = "C:\\Users\\Aryan\\Desktop\\vietnamMap.png"
img = cv2.imread(fileloc)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 3, 3, 0.04)
img[dst>0.01*dst.max()] = [0, 0, 255]
ret, dst = cv2.threshold(dst, 0.01*dst.max(), 255, 0)
dst = np.uint8(dst)

ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
print(type(corners))
for i in range(int(corners.size/2)):
    print("(" + str(corners.item(2*i)-140) + " , " + str(-corners.item(2*i+1)+300) + ")")


res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]


cv2.imshow('dst', img)


infile = open("coordList.txt", 'r')
outfile = open("equationList4.txt", 'w')

#Run the loop twice: remove the first and last coord from coordList.txt
for coord1, coord2 in zip(infile, infile):
    pt1x = float(coord1[1:coord1.index(' ')])
    pt1y = float(coord1[(coord1.index(',') + 2):(len(coord1)-2)])
    pt2x = float(coord2[1:coord2.index(' ')])
    pt2y = float(coord2[(coord2.index(',') + 2):(len(coord2)-2)])
    slope = (pt2y - pt1y)/(pt2x - pt1x)
    y_intercept = pt1y - (slope * pt1x)
    equation = "y = " + str(slope) + "x + " + str(y_intercept) + " {" + str(min(pt1x, pt2x)) + "<=x<=" + str(max(pt1x, pt2x)) + "}\n"
    outfile.write(equation)
outfile.close()
    

