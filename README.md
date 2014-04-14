IPython to Pelican Converter
============================

##### Usage as standalone

    $ ipytopelican.py infile.ipynb

or

    $ ipytopelican.py infile.ipynb -o outfile.md


##### Usage as library

```python
from ipytopelican import convert

convert('infile.ipynb')
```


You can set up your notebook with Pelican metadata by putting it in the first cell:

    Title: My Notebook, Automatically Published
    Date: 2014-04-11 5:30
    Category: Experiments
    Tags: data science


