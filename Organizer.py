import os
import datetime
import shutil



extension_mappings = {
    '.jpg': 'Image',
    '.jpeg': 'Image',
    '.png': 'Image',
    '.gif': 'Image',
    '.bmp': 'Image',
    '.tiff': 'Image',
    '.webp': 'Image',
    '.svg': 'Image',
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.flac': 'Audio',
    '.aac': 'Audio',
    '.ogg': 'Audio',
    '.wma': 'Audio',
    '.m4a': 'Audio',
    '.aiff': 'Audio',
    '.opus': 'Audio',
    '.mid': 'Audio',
    '.midi': 'Audio',
    '.amr': 'Audio',
    '.ac3': 'Audio',
    '.mp4': 'Video',
    '.avi': 'Video',
    '.mkv': 'Video',
    '.mov': 'Video',
    '.wmv': 'Video',
    '.flv': 'Video',
    '.webm': 'Video',
    '.3gp': 'Video',
    '.m4v': 'Video',
    '.mpeg': 'Video',
    '.mpg': 'Video',
    '.rmvb': 'Video',
    '.ts': 'Video',
    '.pdf': 'Document',
    '.doc': 'Document',
    '.docx': 'Document',
    '.ppt': 'Document',
    '.pptx': 'Document',
    '.xls': 'Document',
    '.xlsx': 'Document',
    '.odt': 'Document',
    '.odp': 'Document',
    '.ods': 'Document',
    '.rtf': 'Document',
    '.zip': 'Compressed',
    '.rar': 'Compressed',
    '.7z': 'Compressed',
    '.tar.gz': 'Compressed',
    '.tar.bz2': 'Compressed'
}

def get_file_extension(filename):
    return os.path.splitext(filename)[1]

def list_directory_with_info(directory_path):
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        item_stat = os.stat(item_path)
        creation_time = datetime.datetime.fromtimestamp(item_stat.st_ctime)
        creation_time = creation_time.strftime("%d/%m/%Y %H:%M:%S")
        add_file_to_directory(item)

def add_file_to_directory(file):
    ext = get_file_extension(file) #get the extension of file
    file_path = os.path.join(directory, file) #get the path of the source file
    if not os.path.isdir(file_path) and ext in extension_mappings :
        dest_directory = os.path.join(directory ,extension_mappings[ext]) #get the path of the destination directory
    if ext in extension_mappings:
        if not os.path.exists(dest_directory):
            os.mkdir(f'{dest_directory}')
        shutil.move(file_path, dest_directory) # sort/move the file to the corresponding directory        


#Main Function:

while True:
    directory = input("Give The path Directory You want to sort:")
    if not os.path.isdir(directory) :
        print("Directory Does not exist!")
    else:
        break

list_directory_with_info(directory)        
print("Sorting Is Done.")