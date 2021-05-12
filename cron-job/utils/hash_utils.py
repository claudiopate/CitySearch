import csv
import hashlib
import os

def create_hash_file(file_name):

    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(file_name, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

def check_hash_value(file_name, new_hash, hash_value_map):
    
    old_hash = hash_value_map[file_name]

    if new_hash == old_hash:
        print("The file in memory is the last version")
        return False
    else:
        print("The file will be downloaded")
        return True


def load_hash_value_map(hash_value_file):

    hash_value_map = {}
    if hash_file_exists(hash_value_file):
        with open(hash_value_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    hash_value_map[row[0]] = row[1]
                    line_count += 1
        return hash_value_map

def write_hash_value_map(path_hash_file,hash_value_map):
    with open(path_hash_file, 'w') as f:
        f.write("files,hash_value\n")
        for key in hash_value_map.keys():
            f.write("%s,%s\n"%(key,hash_value_map[key]))

def hash_file_exists(path_hash_file):
    if os.path.exists(path_hash_file):
        return True
    else:
        return False