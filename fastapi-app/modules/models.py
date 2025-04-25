
class FileModel:
    def __init__(
            self,
            file_path: str,
            file_name: str,
            file_content: str,
            file_updated_at: str = None
            ):
        self.file_path = file_path,
        self.file_name = file_name,
        self.file_content = file_content,
        self.file_updatad_at = file_updated_at
    def info(self):
        return (self.file_name, self.file_updatad_at)
