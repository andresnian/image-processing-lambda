from adapter.s3Adapter import getFileFromS3, saveNewImage, getPresignedUrl
from common.exceptions.exception import CustomExcetionImage
from common import constants
import cv2 as cv
import numpy as np
import hashlib

def processImage(path, height, width):
  try:
    print('ImageProcessingService - processImage('+ path +', '+ str(height) +', '+ str(width)+')')
    nameImage = path.rsplit('/', 1)[1].split('.', 1)[0]
    image = getFileFromS3(path)
    nparray = cv.imdecode(np.asarray(bytearray(image)), cv.IMREAD_COLOR)
    dsize = (width, height)
    resizedImage = cv.resize(nparray, dsize)
    hashMd5 = hashlib.md5(path.encode()).hexdigest()
    pathResizedImage = constants.IMAGES_BUCKET_DIR+constants.SLASH+constants.OUTPUT_BUCKET_DIR+constants.SLASH+nameImage+constants.SLASH+str(width)+constants.SLASH+hashMd5+constants.JPG
    saveNewImage(pathResizedImage, bytes(resizedImage))
    return getPresignedUrl(pathResizedImage)
  except CustomExcetionImage as custEx:
    raise CustomExcetionImage(str(custEx))
  

