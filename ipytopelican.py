import json
import sys

f = open(sys.argv[1], 'r')
o = open(sys.argv[2], 'w')
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

