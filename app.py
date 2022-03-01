from common import constants
from service.imageProcessingService import processImage
from common.exceptions.exception import CustomExcetionImage
import json

def handler(event, context):
    try:
        body = json.loads(event['body'])
        urlResizedImage = processImage(body['path'], body['height'], body['width']) 
        return {
                "statusCode": constants.CREATED_STATUS_CODE,
                "body": json.dumps({"urlPresigned": urlResizedImage}),
                "headers": {
                    "Content-Type": "application/json"
                }
            }
    except CustomExcetionImage as custEx:
        return {
            "statusCode": constants.NOT_ACCEPTABLE_STATUS_CODE["status"],
            "errorMessage": str(custEx),
            "errorType": constants.NOT_ACCEPTABLE_STATUS_CODE["message"]
        }
    except Exception as ex:
        return {
            "statusCode": constants.INTERNAL_SERVER_ERROR_STATUS_CODE["status"],
            "errorMessage": str(ex),
            "errorType": constants.NOT_ACCEPTABLE_STATUS_CODE["message"]
        }