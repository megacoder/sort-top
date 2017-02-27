#!/usr/bin/python

import  os
import  sys

def keyfunc( line ):
    v = None
    tokens = line.split()
    if len(tokens) >= 5:
        v = tokens[4]
        if v.endswith( 'k' ):
            v = '%f' % (float(v[:-1]) * 1024)
        elif v.endswith( 'm' ):
            v = '%f' % (float(v[:-1]) * 1024 * 1024)
        elif v.endswith( 'g' ):
            v = '%f' % (float(v[:-1]) * (1024 * 1024 * 1024))
    if v:
        v = float( v )
    return v

def process( fyle ):
    while True:
        line = fyle.readline().rstrip()
        tokens = line.split()
        if len( tokens ) > 0 and tokens[0].isdigit(): break
        print line
    lines = fyle.readlines()
    lines.sort( key=keyfunc, reverse=True )
    for line in lines:
        print line.rstrip()

if __name__ == '__main__':
    if len( sys.argv ) < 2:
        process( sys.stdin )
    else:
        sys.argv.pop( 0 )
        for fn in sys.argv:
            try:
                fyle = open( fn )
            except:
                print >>sys.stderr, 'No such file "%s".' % fn
                continue
            try:
                process( fyle )
            except:
                print >>sys.stderr, 'Error reading "%s"' % fn
            fyle.close()
