from pathlib import Path
# pathlib provides an Object-oriented filesystem path
# 2 Options to use pathlibs Absolute Path or Relative Path
# Example Absolute path would look like c:\Program file\Microsoft

# This will check if there's a file called ecommerce
path = Path("ecommerce")
print(path.exists())

# This will make a new Directory on our project
path = Path("email")
print(path.mkdir())

# This will remove a Directory from our project
path = Path("email")
print(path.rmdir())

# This checks all files ('*'), current project ('*.*') or the files py, xls, html, etc
path = Path()
print(path.glob('*.py'))
for file in path.glob('*.py'):
    print(file)

