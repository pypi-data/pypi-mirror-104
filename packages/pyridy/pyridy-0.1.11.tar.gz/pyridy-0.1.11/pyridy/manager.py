import os
from typing import List, Union

from .file import RDYFile


class CampaignManager:
    def __init__(self, name="", folder: Union[list, str] = None, recursive=True, exclude: Union[list, str] = None):
        """
        The Manager manages loading, processing etc of RDY files
        :param name: Name of the Campaign
        :param folder: Path(s) to folder(s) where to search for measurement files
        :param recursive: If True also searches in subfolders
        :param exclude: List or str of folder(s) to exclude
        """
        self.folder = folder
        self.name = name
        self.files: List[RDYFile] = []

        if folder:
            self.import_folder(self.folder, recursive, exclude)

        pass

    def import_folder(self, folder: Union[list, str] = None, recursive: bool = False, exclude: Union[list, str]=None):
        """

        :param exclude:
        :param recursive: If True, recursively opens subfolder and tries to load files
        :param folder: Path(s) to folder(s) that should be imported
        :return:
        """
        if exclude is None:
            exclude = []

        if type(folder) == list:
            for fdr in folder:
                self.import_folder(fdr, recursive, exclude)

        elif type(folder) == str:
            _, sub_folders, files = next(os.walk(folder))

            if recursive:
                for sub_folder in sub_folders:
                    if sub_folder not in exclude:
                        sub_folder_path = os.path.join(folder, sub_folder)
                        self.import_folder(sub_folder_path, recursive, exclude)

            for file in files:
                file_path = os.path.join(folder, file)
                _, ext = os.path.splitext(file_path)

                if ext not in [".rdy", ".sqlite"]:
                    continue
                else:
                    self.files.append(RDYFile(file_path))

        else:
            raise TypeError("folder argument must be list or str")

        pass
