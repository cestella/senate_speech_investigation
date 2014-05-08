import sys

def extract_politician(line):
    tokens = line.split(',')
    politician = tokens[0].replace("\"", "").split()[0].strip().upper()
    return politician

def to_color(ideal_pt, min_pt, max_pt):
    return (ideal_pt - min_pt) / (max_pt - min_pt)

def process_path(line):
    filename = line.split('/')[-1]
    politician = filename.split('_')[0].split('-')[1].upper()
    return politician

def write_colors(politician_to_color, topics_filename="topics"):
    with open(topics_filename) as f:
        contents = f.readlines()
        contents.pop(0)
        for color in [ politician_to_color[process_path(line.split()[1].strip())] for line in contents ]:
            print(str(color))

def read_labels(ideal_pts_filename="ideal_points.csv"):
    with open(ideal_pts_filename) as f:
        contents = f.readlines()
    contents.pop(0)
    ideal_pts = [ float(line.split(',')[1]) for line in contents ]
    politicians = [ extract_politician(line) for line in contents ]
    min_ideal_pt = min(ideal_pts)
    max_ideal_pt = max(ideal_pts)
    colors = [ to_color(pt, min_ideal_pt, max_ideal_pt) for pt in ideal_pts ]
    return dict( zip(politicians, colors) )

if __name__ == "__main__":
    ideal_pts_filename = sys.argv[1]
    topics_filename = sys.argv[2]

    politician_to_color = read_labels(ideal_pts_filename)
    write_colors(politician_to_color, topics_filename)
