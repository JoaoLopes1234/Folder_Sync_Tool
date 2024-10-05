import os
import hashlib
import shutil

def calculate_md5(filename):
    hash_object = hashlib.md5()
    with open(filename, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def sync_folder(source_folder, replica_folder, log_file):
    if not os.path.exists(source_folder):
        os.makedirs(replica_folder)
    
    for foldername, subfolders, filenames in os.walk(source_folder):
        relative_path = os.path.relpath(foldername,source_folder)
        replica_subfolder = os.path.join(replica_folder, relative_path)
        
        if not os.path.exists(replica_subfolder):
            os.makedirs(replica_subfolder)
        
        for filename in filenames:
            source_file = os.path.join(foldername, filename)
            replica_file = os.path.join(replica_subfolder, filename)
            
            if not os.path.exists(replica_file) or calculate_md5(source_file) != calculate_md5(replica_file):
                shutil.copy2(source_file, replica_file)
                print(log_file, f"Copied/Updated: {source_file} -> {replica_file}")