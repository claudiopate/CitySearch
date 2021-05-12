import sys
sys.path.append('/cron-job/utils/')
import os
from os import path
import handler as ha
import hash_utils as hu


if __name__ == '__main__':

    download_dir = "/cron-job/download"
    resource_dir = "/cron-job/resources"
    hash_file_csv = "/cron-job/hash_file.csv"

    if os.path.exists() == False:
        os.mkdir(download_dir)

    files_info = [
        {       
            "url_file" : "https://www.istat.it/storage/codici-unita-amministrative/Elenco-codici-statistici-e-denominazioni-delle-unita-territoriali.zip",
            "dest_file_name": "actual_cities"
        },
        {
            "url_file" : "https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-soppressi.zip",
            "dest_file_name": "deleted_cities"
        }
        
    ]

    #Download files of cities
    file_info_list = ha.download_list_of_files(files_info,download_dir)

    #Load the current hashes for the files
    hash_value_map = hu.load_hash_value_map(hash_file_csv)

    #Check if it is the first time
    if not hu.hash_file_exists(hash_file_csv):
        hash_value_map = ha.init_cities_files(file_info_list, resource_dir)
    else:
        ha.update_cities_files(file_info_list,hash_value_map,resource_dir)