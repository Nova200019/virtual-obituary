from django.core.files.storage import Storage
from azure.storage.blob import BlobServiceClient, BlobClient
from tempfile import SpooledTemporaryFile
import os

class CustomS3Boto3Storage(Storage):
    def __init__(self, option=None):
        if not option:
            option = {}
        self.account_name = option.get('account_name')
        self.account_key = option.get('account_key')
        self.container_name = option.get('container_name')
        self.blob_service_client = BlobServiceClient(
            f"https://{self.account_name}.blob.core.windows.net/",
            credential=self.account_key
        )
        self.container_client = self.blob_service_client.get_container_client(self.container_name)

    def _open(self, name, mode='rb'):
        # Assuming we're opening in binary read mode
        blob_client = self.container_client.get_blob_client(name)
        downloader = blob_client.download_blob()
        return downloader.readall()

    def _save(self, name, content):
        content.seek(0, os.SEEK_SET)
        with SpooledTemporaryFile() as content_autoclose:
            content_autoclose.write(content.read())
            content_autoclose.seek(0)
            blob_client = self.container_client.get_blob_client(name)
            blob_client.upload_blob(content_autoclose, overwrite=True)
        return name

    def exists(self, name):
        blob_client = self.container_client.get_blob_client(name)
        return blob_client.exists()

    def url(self, name):
        # Generates a URL accessible publicly. Adjust as needed for permissions.
        return f"https://{self.account_name}.blob.core.windows.net/{self.container_name}/{name}"
