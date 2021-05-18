import sys

import manage_files as mf
import hash_utils as hu
import generic_utils as gu

sys.path.append('/cron-job/elasticsearch')
import write_db as wd


def write_cities_in_db(file_csv):
    list_cities = mf.read_csv(file_csv)
    resp = wd.write_doc_to_elasticsearch(list_cities)
    print("Bulk Response: " + str(resp))
    print("Bulk Done")

def download_list_of_files(files_info, download_dir):

    file_path_list = []
    for file in files_info:
        file_item_info = {}
        file_item_info["file_path"] = mf.download_zip_file(file["url_file"],download_dir,file["dest_file_name"])
        file_item_info["file_name"] = file["dest_file_name"]
        file_path_list.append(file_item_info)
    
    return file_path_list


def init_cities_files(file_info_list,resource_folder):

    hash_value_map = {}
    for file_info in file_info_list:
        
        #Unzip the files
        file_csv = mf.unzip_file_csv(file_info["file_path"], resource_folder)

        #Create the hash of the files for checking new version
        hash_file_csv = hu.create_hash_file(file_csv)

        #Create hash value map
        hash_value_map[file_info["file_name"]] = hash_file_csv

        #Write cities files in db elasticsearch
        write_cities_in_db(file_csv)

    #Create csv file with hash map value
    hu.write_hash_value_map("/cron-job/hash_file.csv",hash_value_map)

    return hash_value_map


def update_cities_files(file_info_list,hash_value_map,resource_folder):

    for file_info in file_info_list:

        #Unzip the files in tmp folder
        file_csv = mf.unzip_file_csv(file_info["file_path"], "tmp")

        #Create the hash of the files for checking new version
        hash_file_csv = hu.create_hash_file(file_csv)

        #Check if the files are changed
        file_is_changed = hu.check_hash_value(file_info["file_name"], hash_file_csv, hash_value_map)

        #If the files are changed we have to update the DB
        if file_is_changed:
            write_cities_in_db(file_csv)
            #Unzip the files
            file_csv = mf.unzip_file_csv(file_info["file_path"], resource_folder)
            #Update the hash value map
            hash_value_map[file_info["file_name"]] = hash_file_csv

    #update the hash value map file
    hu.write_hash_value_map("/cron-job/hash_file.csv",hash_value_map)
    #Remove tmp folder and its content
    gu.remove_temp_folder("tmp")
    

