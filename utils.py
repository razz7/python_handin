import os


def filepathtofolder(folder, output):
    with open(output, 'w') as File:
        for folders in os.listdir(folder):
            File.write(folder + folders + "\n")


def filepathWritenames(folder, output):
    with open(output, 'w') as File:
        for path, directories, files in os.walk(folder):
            for filenames in files:
                File.write(os.path.join(path, filenames) + "\n")

def print_first_file_line(filename):
    for l in filename:
            with open(l, 'r') as File:
                print(File.readline())

                
def print_emails(filenames):
    for l in filenames:
        if os.path.isfile(l):
            with open(l, 'r') as File:
                for lines in File:
                    if '@' in lines:
                        print(lines)
                        
                        
def print_headers_md(filenames):
    for l in filenames:
        if os.path.isfile(l):
            with open(l, 'r') as File:
                for lines in File:
                    if lines.startswith("#"):
                        print(lines)
                    