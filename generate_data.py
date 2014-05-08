import numpy as np
from numpy import nonzero
from numpy.random import rand
import sys

def load_labels(topic_labels_filename):
    with open(topic_labels_filename) as f:
        contents = f.readlines()
    return [content.strip() for content in contents]

def get_data_by_persuasion(persuasion, target):
    ret = []
    for i in xrange(0, len(xdata)):
        if persuasion[i] == target:
            ret.append(i)
    return ret

def persuasion_to_color(persuasion):
    if persuasion == 'd':
        return 'blue'
    elif persuasion == 'r':
        return 'red'
    else:
        return 'grey'

if __name__ == '__main__':
    points=sys.argv[1]
    
    data_pts = np.loadtxt(points, delimiter=",")
    speeches = load_labels(sys.argv[2])
    politicians= [ line.split(',')[0].replace('"', '').replace('(','').lower().split() for line in load_labels(sys.argv[3]) ]
    politician_names = [ line.split(',')[0].replace('"', '') for line in load_labels(sys.argv[3]) ]
    politician_names.pop(0)
    politicians_to_name = dict( [ (name.split()[0].lower(), name) for name in politician_names ])
    politicians.pop(0)
    politicians_to_persuasions = dict( [ (t[0], t[1]) for t in politicians ])
    persuasions = [ politicians_to_persuasions[line.split('_')[0].split('-')[1].lower()] for line in speeches ]
    politicians_by_doc= [ politicians_to_name[line.split('_')[0].split('-')[1].lower()] for line in speeches ]
    topic_vectors = [ line.split(',') for line in load_labels(sys.argv[4]) ] 
    topics_pts = load_labels(sys.argv[5]) 
    summaries = load_labels(sys.argv[6]) 
    colors = [ persuasion_to_color(persuasion) for persuasion in persuasions]
    
    pts = zip(data_pts[:,0]
             , data_pts[:,1]
             , speeches
             , colors
             , topics_pts
             , politicians_by_doc
             , summaries
             )
    print "topics = ["
    for topic in topic_vectors:
        print str(topic) + ","
    print "];"
    print "data = ["
    for pt in pts:
        print '{ "x":%f, "y":%f,"speech":"%s","party":"%s", "topics":[%s], "politician":"%s", "summary":"%s"},' % pt
    print "];"
