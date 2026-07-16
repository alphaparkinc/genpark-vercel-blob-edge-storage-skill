from client import VercelBlobEdgeStorageClient
client = VercelBlobEdgeStorageClient()
print(client.upload_blob("SGVsbG8gVmVyY2VsIEJsb2Ih", "documents/readme.txt"))