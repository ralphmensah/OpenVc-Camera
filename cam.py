import cv2, time

video= cv2.VideoCapture(0)


a=0

while True:
    a = a + 1

    check, frame = video.read()
    
    #outputs in matrix

    #print(check)
    #print(frame) #rep image

    #grascale
    #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #show frame // for grayscale"gray = frame"
    cv2.imshow("Capturing",frame)

    #make window wait
    #cv2.waitKey(0)

    #for video(every milisecond)
    key = cv2.waitKey(1)

#'q' to end streaming
    if key ==ord("q"):
        break
    elif key == ord("c"):
        cv2.waitKey(0) & 0xFF
        cv2.imwrite('img.png')
        cv2.destroyAllWindows()

    #outputs value of a in terminal
    #print(a)



#shut camera
video.release()  
cv2.destroyAllWindows()