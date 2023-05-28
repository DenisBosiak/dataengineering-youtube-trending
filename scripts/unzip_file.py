import os


def unzip_file(folder: str, file_name: str) -> None :
    "Unzip dataset with raw data"
    bash = "cd {0} && tar -xf {1}.zip".format(folder, file_name)
    os.system(bash)


unzip_file('dataset', 'youtube-new')   