from common import constants
from common.exceptions.exception import CustomExcetionImage
import boto3

def getFileFromS3(path):
  print('s3Adapter - getFileFromS3('+ path+')')
  try:
    s3 = boto3.resource('s3', region_name=constants.REGION_NAME)
    image = s3.Object(constants.BUCKET_NAME, path).get().get("Body").read()
    return image
  except Exception:
    raise CustomExcetionImage("Error getting file from S3 bucket "+constants.BUCKET_NAME+" and File: "+ path)

def saveNewImage(path, image):
  print('s3Adapter - saveNewImage('+ path+')')
  try:
    s3 = boto3.resource('s3', region_name=constants.REGION_NAME)
    newImage = s3.Object(constants.BUCKET_NAME, path)
    result = newImage.put(Body=image, ContentType= 'image/jpeg')
    res = result.get('ResponseMetadata')
    if res.get('HTTPStatusCode') == 200:
      return 'File Uploaded Successfully'
    else:
      raise CustomExcetionImage("Error saving file to S3 bucket "+constants.BUCKET_NAME+" and File: "+ path)
  except Exception:
    raise CustomExcetionImage("Error saving file to S3 bucket "+constants.BUCKET_NAME+" and File: "+ path)
  
def getPresignedUrl(path):
  print('s3Adapter - getPresignedUrl('+ path+')')
  try:
    s3 = boto3.client('s3', region_name=constants.REGION_NAME)
    
    response = s3.generate_presigned_url(
      ClientMethod='get_object',
      Params={
        'Bucket': constants.BUCKET_NAME,
        'Key': path
        },
      ExpiresIn=constants.ONE_HOUR_SECONDS)
    print(response)
    return response
  except Exception as ex:
    print(ex)
    raise CustomExcetionImage("Error getting pressigned URL from S3 bucket "+constants.BUCKET_NAME+" and File: "+ path)