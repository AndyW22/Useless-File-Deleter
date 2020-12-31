import os
from send2trash import send2trash
print("This program currently deletes .txt, .html, .srt, .url, and .vtt files")


while True:
    count = 0
    try:
        filepath = input("Enter folder to traverse: ")
    except FileNotFoundError or OSError:
        print("not a valid directory")
    if filepath.lower() == 'c' or filepath.lower() == 'c:' or filepath.lower() == r'c\'':
        print("Cannot type c")
    else:
        answer = input("Press y to confirm file path is: " + filepath + " \n")
        if answer.lower().startswith('y'):
            for root,subs,files in os.walk(filepath):
                try:
                    for item in files:
                        if item.endswith('.txt') or item.endswith('.vtt') or item.endswith('.html') or item.endswith('.url') or item.endswith('.srt'):
                            print("Sending " + item + " to recycle bin")
                            send2trash(os.path.join(root, item))
                except OSError:
                    continue
                

        print("\n" + "Items deleted successfully" + "\n")