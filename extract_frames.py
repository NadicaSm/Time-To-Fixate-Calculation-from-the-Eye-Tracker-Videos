#%%
import cv2

user_id = 'user_1'
cap = cv2.VideoCapture(user_id + '.mp4')

i = 0
 
while(cap.isOpened()):
    ret, frame = cap.read()
     
    # This condition prevents from infinite looping in case video ends.
    if ret == False:
        break
     
    # Save Frame by Frame into disk using imwrite method
    cv2.imwrite('video/' + user_id + '/' + user_id + 'Frame'+str(i)+'.jpg', frame)
    i += 1
 
cap.release()
cv2.destroyAllWindows()


