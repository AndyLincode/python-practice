import zipfile

zipped_file = zipfile.ZipFile("researchpaper.zip", "w")
zipped_file.write("researchpaper.txt", compress_type=zipfile.ZIP_DEFLATED)
zipped_file.write("research2.txt", compress_type=zipfile.ZIP_DEFLATED)
zipped_file.close()
