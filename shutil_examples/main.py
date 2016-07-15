import shutil

shutil.copytree("original", "copy")
print("Copied to 'copy'")
input("Press any key to remove 'copy'")
shutil.rmtree("copy")
