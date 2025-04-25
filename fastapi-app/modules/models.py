
class FileModel:
    def __init__(
            self,
            file_name: str,
            file_content: str,
            file_updated_at: str = None
            ):
        self.file_name = file_name,
        self.file_content = file_content,
        self.file_updatad_at = file_updated_at
    def get_filename(self):
        return self.file_name.split('/')[-1]
    def get_filepath(self):
        return '/'.join(self.file_name.split('/')[:-1])
    def info(self):
        return (self.get_filename(), self.file_updatad_at)
