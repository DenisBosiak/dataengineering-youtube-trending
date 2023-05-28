import os


def kaggle_download (ds_name: str) -> None: 
    "Download dataset into local"
    bash = "cd dataset && kaggle datasets download -d {0}".format(ds_name)
    os.system(bash)


kaggle_download('datasnaek/youtube-new')