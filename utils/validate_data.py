class ValidateData:
    @staticmethod
    def validate_data(result):
        if not "title" in result:
            return False
        if not "image" in result:
            return False
        if not "url" in result["image"]:
            return False
        return True
