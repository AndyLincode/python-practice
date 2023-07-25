import zipfile

zipped_obj = zipfile.ZipFile("researchpaper.zip", "r")
zipped_obj.extractall("result")
zipped_obj.close()
