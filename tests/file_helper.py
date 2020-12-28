import os

class FileHelper:

    def __init__(self, api):
        self.api = api
    def remove_file(self, filepath):
        if os.path.isfile(filepath):
            print(f"removing file{filepath}")
            os.unlink(filepath)

    def prepare_file(self, filepath):
        print(f"Preparing file {filepath} for upload")
        return bytes()

    def upload_file(self, filepath):
        data = self.prepare_file(filepath)
        self.api.request("POST", data)