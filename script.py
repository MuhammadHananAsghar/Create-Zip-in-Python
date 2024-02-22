import os
import zipfile

def zip_subdirectories(directory_path):
    try:
        # Get a list of all subdirectories
        subdirectories = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]

        for subdirectory in subdirectories:
            # Check if zip file already exists
            zip_filename = f'{subdirectory}.zip'
            if os.path.exists(zip_filename):
                print(f'Zip file already exists for {subdirectory}. Skipping...')
                continue

            # Create a zip file for writing for each subdirectory
            with zipfile.ZipFile(zip_filename, 'w') as zip_file:
                # Walk through the subdirectory and add its contents to the zip file
                subdirectory_path = os.path.join(directory_path, subdirectory)
                for root, dirs, files in os.walk(subdirectory_path):
                    for item in dirs + files:
                        item_path = os.path.join(root, item)
                        arcname = os.path.relpath(item_path, subdirectory_path)
                        zip_file.write(item_path, arcname=arcname)

            print(f'Successfully created zip file: {zip_filename}')

    except Exception as e:
        print(f'Error: {e}')

# Example usage:
directory_to_zip = 'dir_name'
zip_subdirectories(directory_to_zip)
