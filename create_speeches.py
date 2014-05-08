import sys

if __name__ == "__main__":
    topics_filename= sys.argv[1]
    with open(topics_filename) as f:
        contents = f.readlines()
    contents.pop(0)
    for line in contents:
        long_file = line.split()[1]
        print long_file.split('/')[-1]
