import os
# list folders
# move folder up
# move folder down
# display text content of file


cwd = os.getcwd()


# os.chdir(downloadDir)


for filename in os.listdir(cwd):
    absPath = (os.path.join(os.getcwd(), filename))
    extension = os.path.splitext(filename)[1].lstrip('.').lower()
    print(filename)


while True:
    print(cwd)
    choice = input('If you want to move up enter u if down press d')
    print(choice)
    if choice not in ['u', 'd']:
        raise Exception('u or d silly')
    # os.chdir()
# https://2.bp.blogspot.com/-PvgHh2ndj3U/WjbPr28XAnI/AAAAAAAAVOc/phMNmZDiUioUbkTN9zLmEg_YVwHBv3IogCLcBGAs/s1600/100%2Bpomys%25C5%2582%25C3%25B3w%2Bpython.png
