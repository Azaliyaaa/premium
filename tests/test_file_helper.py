from file_helper import FileHelper


class TestFileHelper:
    def test_init(self):
        api = object()
        fh = FileHelper(api)
        assert fh.api is api