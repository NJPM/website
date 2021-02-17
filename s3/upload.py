
## Access keys for S3
from decouple import config
ACCESS_KEY = config("ACCESS_KEY")
SECRET_ACCESS_KEY = config("SECRET_ACCESS_KEY")

## Imports
from boto3 import client
from botocore.exceptions import ClientError

## Connect to client with keys
def connect_client():
    """
    Create connection to client with keys pre-filled.
    Requires ACCESS_KEY and SECRET_ACCESS_KEY env
    :return: s3_client
    """
    s3_client = client("s3", aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_ACCESS_KEY)
    return s3_client

## Upload a file
def upload_file(file_name, bucket="hroar.uk", object_name=None, content_type='text/html'):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to, by default the hroar.uk bucket
    :param object_name: S3 object name. If not specified then file_name is used
    :param content_type: Content type, default to text/html
    :return: True if file was uploaded, else False
    """

    ## If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    ## Upload the file
    s3_client = connect_client()
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs = {'ContentType': content_type})
    except ClientError as e:
        print(e)
        return False
    return True

## Run the upload for index.html
upload_file("/home/nathanminter1992/website/hroar.uk/index.html", object_name = "index.html")
