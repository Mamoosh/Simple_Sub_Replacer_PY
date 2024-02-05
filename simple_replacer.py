import os

directory_path = 'path/to/your/directory'
target_substring = 'assaultrifle'
replacement_substring = 'breakingcolores'

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    # Check if the target substring is in the file name
    if target_substring in filename:
        # Create the new file name by replacing the target substring
        new_filename = filename.replace(target_substring, replacement_substring)
        
        # Construct the full old and new file paths
        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f'Renamed "{filename}" to "{new_filename}"')

print('All files have been renamed successfully!')
