
## Imports
import os
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

s3_client = connect_client()

## Upload a file
def upload_file(file_name, bucket="hroar.uk", object_name=None, content_type=None):
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
    try:
        if content_type is None:
            response = s3_client.upload_file(file_name, bucket, object_name)
        else:
            response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs = {'ContentType': content_type})
        print("{} uploaded.".format(object_name))
    except ClientError as e:
        print(e)
        return False
    return True

"""
## Run the upload for each file
upload_file("/home/nathanminter1992/website/hroar.uk/dark/index.html", object_name="dark/index.html", content_type = "text/html")
upload_file("/home/nathanminter1992/website/hroar.uk/dog/index.html", object_name="dog/index.html", content_type = "text/html")
upload_file("/home/nathanminter1992/website/hroar.uk/images/jacato.png", object_name="images/jacato.png")
upload_file("/home/nathanminter1992/website/hroar.uk/styles/dark.css", object_name="styles/dark.css")
upload_file("/home/nathanminter1992/website/hroar.uk/styles/main.css", object_name="styles/main.css")
upload_file("/home/nathanminter1992/website/hroar.uk/index.html", object_name = "index.html", content_type = "text/html")
"""

def upload_website():
    path = "/home/nathanminter1992/website/hroar.uk/"
    for root, dirs, files in os.walk(path):
        for f in files:
            file_name = os.path.join(root, f)
            object_name = os.path.relpath(file_name, path)
            if f.endswith(".html"):
                s3_client.upload_file(file_name, "hroar.uk", object_name, ExtraArgs = {'ContentType': 'text/html'})
            else:
                s3_client.upload_file(file_name, "hroar.uk", object_name)
            print("{} uploaded.".format(object_name))

if __name__ == "__main__":
    upload_website()
