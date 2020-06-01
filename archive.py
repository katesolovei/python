import os
import zipfile
import stat

base_dir = os.getcwd()

for folder, subfolders, files in os.walk(base_dir):
    os.chdir(folder)
    for file in files:
        if file.endswith('.fb2'):
            books_zip = zipfile.ZipFile(file+'.zip', 'w')
            books_zip.write(os.path.join(folder, file), os.path.relpath(file), compress_type = zipfile.ZIP_DEFLATED)
            path = os.path.join(folder, file)
            os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            os.remove(os.path.join(folder, file))
            books_zip.close()
