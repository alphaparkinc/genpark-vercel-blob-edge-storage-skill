class VercelBlobEdgeStorageClient:
    def upload_blob(self, file_data_base64: str, target_path: str) -> dict:
        import base64
        raw_len = len(base64.b64decode(file_data_base64.encode()))
        return {"blob_url": f"https://genpark.public.blob.vercel-storage.com/{target_path}", "bytes_written": raw_len}