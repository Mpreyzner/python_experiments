import os
# list folders
# move folder up
# move folder down


def print_files(dir):
    for filename in os.listdir(cwd):
        abs_path = (os.path.join(os.getcwd(), filename))
        extension = os.path.splitext(filename)[1].lstrip('.').lower()
        print(filename)


while True:
    cwd = os.getcwd()
    relative_path = os.path.dirname(__file__)
    print(cwd)
    print(print_files(cwd))
    choice = input('If you want to move up enter .. if you want to move down enter folder name')
    print(choice)
    if choice == '..':
        os.chdir('..' + relative_path)
    elif choice.isprintable():
        os.chdir(cwd + '/' + choice)

