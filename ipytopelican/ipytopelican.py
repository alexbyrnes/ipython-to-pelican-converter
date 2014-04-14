import json
import sys
import argparse
import os

def convert(infile, outfile=None):


    if outfile is None:
        fname, ext = os.path.splitext(infile)
        outfile = fname + '.md'

    f = open(infile, 'r')
    o = open(outfile, 'w')
    d = json.loads(f.read())

    for x in d['worksheets'][0]['cells']:

        if x['cell_type'] == 'code':
            o.write('```python\n%s\n```\n\n' % ''.join(x['input']))
            for opts in x['outputs']:
                if opts['output_type'] == 'pyout':
                    o.write('    '.join(opts['text']))
        elif x['cell_type'] == 'markdown':
            o.write(''.join(x['source']))
        o.write('\n\n')

    f.close()
    o.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Convert an IPython Notebook (.ipynb) file to Pelican.  Works on Markdown, python input, and python output.')
    parser.add_argument('filename', help='Input file (.ipynb)')
    parser.add_argument('--outputfile', '-o',  help='Output markdown file.', default=None)
    args = parser.parse_args()

    convert(args.filename, args.outputfile)
