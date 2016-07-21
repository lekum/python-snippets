import shutil

shutil.make_archive('files_compressed', 'zip', 'files')
shutil.unpack_archive('files_compressed.zip')
