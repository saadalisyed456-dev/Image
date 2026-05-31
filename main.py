mport cv2
img = cv2.imread("car.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("oriignal image", img)
cv2.imshow("Grayscale image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()