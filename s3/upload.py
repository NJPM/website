
## Imports
import os
import posixpath
from boto3 import client
from botocore.exceptions import ClientError

## Access keys for S3
from decouple import config
ACCESS_KEY = config("ACCESS_KEY")
SECRET_ACCESS_KEY = config("SECRET_ACCESS_KEY")

## Connect to client with keys
def connect_client():
    """
    Create connection to client with keys pre-filled.
    Requires ACCESS_KEY and SECRET_ACCESS_KEY env
    :return: s3_client
    """
    s3_client = client("s3", aws_access_key_id = ACCESS_KEY, aws_secret_access_key = SECRET_ACCESS_KEY)
    return s3_client

## Upload all files in hroar.uk folder
def upload_website():
    """
    Upload all files in hroar.uk folder to hroar.uk bucket.
    Objects will be named based on relative path to hroar.uk folder.
    """
    path = "C:/Users/natha/Documents/Code/website/hroar.uk/"
    for root, dirs, files in os.walk(path):
        for f in files:
            file_name = os.path.join(root, f)
            object_name = os.path.relpath(file_name, path).replace(os.sep, posixpath.sep)
            if f.endswith(".html"):
                s3_client.upload_file(file_name, "hroar.uk", object_name, ExtraArgs = {'ContentType': 'text/html'})
            else:
                s3_client.upload_file(file_name, "hroar.uk", object_name)
            print("{} uploaded.".format(object_name))

if __name__ == "__main__":
    s3_client = connect_client()
    upload_website()
