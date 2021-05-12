import requests
import os
import zipfile
import csv

def download_zip_file(cities_file_name,dir_name,file_name):
    r = requests.get(cities_file_name)

    filename_suffix_zip = "zip"

    path_file_compressed = os.path.join(dir_name, file_name + "." + filename_suffix_zip)

    with open(path_file_compressed,"wb") as f:
        f.write(r.content)

    return path_file_compressed

def unzip_file_csv(path_file_compressed,destination_folder):
    unzipped_folder = zipfile.ZipFile(path_file_compressed)
    for file_name in unzipped_folder.namelist():
        if file_name.endswith(".csv"):
            file_extracted = unzipped_folder.extract(file_name, destination_folder)
            return file_extracted

def read_csv(file_name):
    list_cities = []
    with open(file_name, 'r', encoding='ISO-8859-1') as data:      
        for line in csv.DictReader(data, delimiter=";"):
            list_cities.append(line)
    return list_cities