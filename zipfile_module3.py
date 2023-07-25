import shutil

# folder_we_want_to_zip = "C:\\Users\\andy12_lin\Desktop\\python\\Employee"
# output_name = "C:\\Users\\andy12_lin\Desktop\\python\\output"

# shutil.make_archive(output_name, "zip", folder_we_want_to_zip)


something_we_want_to_unzip = "C:\\Users\\andy12_lin\Desktop\\python\\output.zip"
unzipped_folder_name = "C:\\Users\\andy12_lin\Desktop\\python\\shutil_result"

shutil.unpack_archive(something_we_want_to_unzip, unzipped_folder_name, "zip")
