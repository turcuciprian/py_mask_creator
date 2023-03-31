import os

def rename_files_with_suffix(folder_path):
    """
    Renames all files in a folder with files with the same name but the suffix "_mask"
    """
    # get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # iterate over the file list
    for file_name in file_list:
        # get the file extension
        file_extension = os.path.splitext(file_name)[1]

        # create the new file name with the suffix "_mask"
        new_file_name = file_name.replace(file_extension, '') + '_mask' + file_extension

        # create the full file paths for the old and new file names
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)

        # rename the file
        os.rename(old_file_path, new_file_path)

    print("All files in the folder have been renamed with the suffix '_mask'.")

rename_files_with_suffix('renameImages')