from simplenote import Simplenote
import simplejson as json
import sys

"""
backup.py <username> <password> [outfile]

Dumps the full contents of a Simplenote account to JSON. Outputs to stdout if 
outfile is not specified.
"""

def fetch_all( api ):
    index = api.index()
    notes = []
    
    for i in index:
        n = api.get_note( i['key'] )
        for k in ('created', 'modified'):
            n[k] = n[k].strftime("%Y-%m-%d %H:%M:%S")
        notes.append( n )
    
    return notes

def main(args):
    if len( args ) == 2:
        outfile = sys.stdout
    else:
        assert( len( args ) == 3 )
        outfile = open( args[-1], 'w' )
    
    json.dump( fetch_all( Simplenote( args[0], args[1] ) ), outfile )

if __name__ == '__main__':
    main( sys.argv[1:] )