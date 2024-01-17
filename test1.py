import cv2 as cv
import numpy

img = cv.imread('10.jpg')
cv.imshow('orginal image',img)


blurImg = cv.blur(img,(5,5))
cv.imshow('blurred image',blurImg)

gausBlur = cv.GaussianBlur(img, (5,5),0)
cv.imshow('gausBlur image',gausBlur)

blurImg = cv.medianBlur(img,5)
cv.imshow('blurImg image',blurImg)


##################################################################################


#HIGH DETILE

image_gray = cv.cvtColor(blurImg,cv.COLOR_BGR2GRAY)
filtered_image =cv.Canny(image_gray,threshold1=30, threshold2=80)
cv.imshow('filtered_image',filtered_image)

image_gray1 = cv.cvtColor(gausBlur,cv.COLOR_BGR2GRAY)
filtered_image1 =cv.Canny(image_gray1,threshold1=30, threshold2=80)
cv.imshow('filtered_image1',filtered_image1)

image_gray2 = cv.cvtColor(blurImg,cv.COLOR_BGR2GRAY)
filtered_image2 =cv.Canny(image_gray2,threshold1=30, threshold2=80)
cv.imshow('median blurring',filtered_image2)

#LOW DETILE
image_gray = cv.cvtColor(blurImg,cv.COLOR_BGR2GRAY)
filtered_image =cv.Canny(image_gray,threshold1=100, threshold2=110)
cv.imshow('filtered_image',filtered_image)

 #################################################################################
 
 
 #HIGH DETILE
 
 #Erosion
kernel = numpy.ones((1,1),numpy.uint8)
erosion = cv.erode(filtered_image1,kernel,iterations= 1)
cv.imshow("erosionH",erosion)

#Dilation
kernel = numpy.ones((3,3),numpy.uint8)
dilation = cv.dilate(filtered_image1,kernel,iterations= 1)
cv.imshow("dilationH", dilation)

#Opening
kernel = numpy.ones((1,1),numpy.uint8)
opening=cv.morphologyEx(filtered_image1,cv.MORPH_OPEN,kernel)
cv.imshow("openingH",opening)

#Closing
kernel = numpy.ones((6,6),numpy.uint8)
Closing=cv.morphologyEx(filtered_image1,cv.MORPH_CLOSE,kernel)
cv.imshow("closingH",Closing)

#Gradient
kernel = numpy.ones((3,3),numpy.uint8)
Gradient=cv.morphologyEx(filtered_image1,cv.MORPH_GRADIENT,kernel)
cv.imshow("GradientH ", Gradient)


#LOW DETILE

#Erosion
kernel = numpy.ones((1,1),numpy.uint8)
erosionlow = cv.erode(filtered_image,kernel,iterations= 1)
cv.imshow("erosion",erosionlow)

#Dilation
kernel = numpy.ones((2,2),numpy.uint8)
dilationlow = cv.dilate(filtered_image,kernel,iterations= 2)
cv.imshow("dilation", dilationlow)

#Opening
kernel = numpy.ones((1,1),numpy.uint8)
openinglow=cv.morphologyEx(filtered_image,cv.MORPH_OPEN,kernel)
cv.imshow("opening",openinglow)

#Closing
kernel = numpy.ones((7,7),numpy.uint8)
Closinglow=cv.morphologyEx(filtered_image,cv.MORPH_CLOSE,kernel)
cv.imshow("closing",Closinglow)

#Gradient
kernel = numpy.ones((2,2),numpy.uint8)
Gradientlow=cv.morphologyEx(filtered_image,cv.MORPH_GRADIENT,kernel)
cv.imshow("Gradient ", Gradientlow)
 #################################################################################################

erosionlogic = cv.cvtColor(erosion,cv.COLOR_GRAY2BGR) 
andlogic=cv.bitwise_and(img,erosionlogic)
orlogic=cv.bitwise_or(img,erosionlogic)
xorlogic=cv.bitwise_xor(img,erosionlogic)
notlogic=cv.bitwise_not(erosionlogic)


closelogic1= cv.cvtColor(Closinglow,cv.COLOR_GRAY2BGR) 
and1logic=cv.bitwise_and(img,closelogic1)

closelogic= cv.cvtColor(Closing,cv.COLOR_GRAY2BGR) 
andlogicc=cv.bitwise_and(img,closelogic)

cv.imshow("AND",andlogic )
cv.imshow("OR",orlogic )
cv.imshow("NOT",notlogic )
cv.imshow("XOR",xorlogic )
cv.imshow("AND_",and1logic )
cv.imshow("ANDc",andlogicc )


cv.waitKey(0)
