import os  # Library for file and directory manipulation
import shutil  # Library for copying files and folders
import hashlib  # Library for generating MD5 hash of files
import time  # Library for time control and creating synchronization intervals
import argparse  # Library to handle command-line arguments

# Main function that handles command-line arguments and runs the synchronization
def main():
    parser = argparse.ArgumentParser(description='Folder synchronization tool')
    parser.add_argument('source_folder', help='Source folder path')
    parser.add_argument('replica_folder', help='Replica folder path')
    parser.add_argument('interval', type=int,
                        help='Synchronization interval in seconds.')
    parser.add_argument('--log_file', help='Log file path', default=None)

    args = parser.parse_args()

    while True:
        sync_folder(args.source_folder, args.replica_folder, args.log_file)
        time.sleep(args.interval)

# Function to calculate the MD5 hash of a file
# Used to check if a file has been modified
def calculate_md5(filename):
    hash_object = hashlib.md5()
    with open(filename, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_object.update(chunk)
    return hash_object.hexdigest()

# Function to synchronize the source folder with the replica folder
def sync_folder(source_folder, replica_folder, log_file):
    # Check if the replica folder exists, if not, create it
    if not os.path.exists(source_folder):
        os.makedirs(replica_folder)

    # Synchronize files and folders from the source to the replica
    for foldername, subfolders, filenames in os.walk(source_folder):
        relative_path = os.path.relpath(foldername, source_folder)
        replica_subfolder = os.path.join(replica_folder, relative_path)

        if not os.path.exists(replica_subfolder):
            os.makedirs(replica_subfolder)

        for filename in filenames:
            source_file = os.path.join(foldername, filename)
            replica_file = os.path.join(replica_subfolder, filename)

            if not os.path.exists(replica_file) or calculate_md5(source_file) != calculate_md5(replica_file):
                shutil.copy2(source_file, replica_file)
                print(
                    log_file, f"Copied/Updated: {source_file} -> {replica_file}")
    # Remove files that exist in the replica but not in the source
    for foldername, subfolders, filenames in os.walk(replica_folder, topdown=False):
        relative_path = os.path.relpath(foldername, replica_folder)
        source_subfolder = os.path.join(source_folder, relative_path)

        for filename in filenames:
            replica_file = os.path.join(foldername, filename)
            source_file = os.path.join(source_subfolder, filename)

            if not os.path.exists(source_file):
                os.remove(replica_file)
                print(log_file, f"Removed: {replica_file}")
        # Remove empty folders in the replica that don't exist in the source
        if not os.path.exists(source_subfolder) and not os.listdir(foldername):
            os.rmdir(foldername)
            print(log_file, f"Removed empty folder: {foldername}")


if __name__ == '__main__':
    main()
