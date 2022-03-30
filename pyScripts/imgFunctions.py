import urllib
import cv2
import numpy as np

ip = '192.168.8.100'

url='http://' + ip + '/cam-hi.jpg'

def getImage():
    # @param : none
    # @return : an image
    imgResp = urllib.request.urlopen(url) # get respone from server
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8) # convert to NP array
    img = cv2.imdecode(impNp, -1)
    return img # give out the image format data

def showImage(window,img):
    # @param : window: str; img : an img
    # @return : none
    cv2.imshow(window, img)

def close(window):
    if window is not None:
        cv2.destroyWindow(window)
    else:
        cv2.destroyAllWindows()

# while True:
#     imgResp=urllib.request.urlopen(url)
#     imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
#     img=cv2.imdecode(imgNp,-1)

#     # all the opencv processing is done here
#     cv2.imshow('test',img)
#     if ord('q')==cv2.waitKey(10):
#         exit(0)