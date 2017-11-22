class FileManager:
    def open_file(file_name):
        try:
            lines = []
            file = open(file=file_name, mode='r', encoding='utf-8')
            lines = file.readlines()
            file.close()
            return Response(True, lines)
        except FileNotFoundError:
            return Response(False, exception="FileNotFound")

    def save_file(file_name, lines):
        file = open(file=file_name, mode='w', encoding='utf-8')
        file.writelines(lines)
        file.close()


class Response:
    def __init__(self, success, lines=None, exception = None):
        self.success = success
        self.lines = lines
        self.exception = exception

    def was_successful(self):
        return self.success, self.exception

    def get_lines(self):
        return self.lines
