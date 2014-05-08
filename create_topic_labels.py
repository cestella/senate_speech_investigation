import sys

if __name__ == "__main__":
    topics_filename= sys.argv[1]
    with open(topics_filename) as f:
        contents = f.readlines()
    for line in contents:
        tokens = line.split()
        tokens.pop(0)
        tokens.pop(0)
        topics_str= ",".join( tokens[:5] )
        print(topics_str )
