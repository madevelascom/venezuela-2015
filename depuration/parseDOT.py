__author__ = 'madevelasco'

import re

def parse_file():
    words_file = open('../results/Venezuela_cleaned_hashtags.dot', 'r')
    save_nodes = open('../results/Venezuela_cleaned_hashtags_node.csv', 'w')
    save_edges = open('../results/Venezuela_cleaned_hashtags_edge.csv', 'w')


    header_node = 'word,weight\n'
    header_edge = 'word1,word2,weight\n'

    save_nodes.write(header_node)
    save_edges.write(header_edge)



    for line in words_file:
        if (is_node(line)):
            # "diem" ["weight"=1,"ui.label"="diem","cons"=4,"ui.size"=1.5];
            word = find_between(line,  "\"", "\"" )
            weight =  find_between(line, "weight\"=", "," )
            res = word +','+weight+'\n'
            save_nodes.write(res)
        else:
            # "anosdefraude" -- "venezuela" ["weight"=1];
            word1 = find_between(line, "\"", "\"" )
            word2 = find_between(line, "-- \"", "\"" )
            weight = find_between(line, "weight\"=", "]")
            res = word1+','+word2+','+weight+'\n'
            save_edges.write(res)

def is_node(line):
    searchObj = re.search(r'ui.label', line, re.M|re.I)
    if searchObj:
        return True
    else:
        return False

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

if __name__ == '__main__':
    parse_file()