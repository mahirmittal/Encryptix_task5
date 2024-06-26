import cv2

camera=cv2.VideoCapture(1)

img_count=0

while True:
    retu, capture= camera.read()

    if not retu:
        print("some error occured")
        break

    cv2.imshow("mycam", capture)

    k=cv2.waitKey(1)

    if k%256==27:
        print("Esc key pressed, exit")
        break
    elif k%256==32:

        imagename="capture{}.png".format(img_count)
        cv2.imwrite(imagename,capture)
        print("image taken successfully")
        img_count+=1

camera.release()

# camera.destroyAllWindows()