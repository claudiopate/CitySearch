import shutil


def remove_temp_folder(folder):
    try:
        shutil.rmtree(folder)
    except OSError as e:
        print("Error: %s : %s" % (folder, e.strerror))