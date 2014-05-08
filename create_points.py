import sys
import re
import numpy as Math

def convert(topics_filename = "topics", dim=350):
    with open(topics_filename) as topics_f:
        contents = topics_f.readlines()
    with open(out_filename, "w") as out:
        contents.pop(0)
        for line in contents:
            splits = re.split('\s+', line)
            pairs = zip(splits[::2], splits[1::2])
            pairs.pop(0)
            d = dict(pairs)
            vals = [ d[str(i)] if str(i) in d else '0' for i in xrange(0, dim) ]
            print(",".join(vals))

if __name__ == "__main__":
    topics_filename=sys.argv[1]
    dim = int(sys.argv[2])
    convert(topics_filename, dim)

