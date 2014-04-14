"""
IPython Notebook to Pelican Converter
-----

Converts IPython Notebooks code and markdown to Pelican code snippets and markdown.

"""

from setuptools import find_packages, setup


setup(
        name='ipytopelican',
        version='0.1a',
        url='http://github.com/alexbyrnes/',
        license='MIT',
        author='Alex Byrnes',
        author_email='alexbyrnes@gmail.com',
        description='Converter for IPython notebooks to Pelican markdown.',
        long_description=__doc__,
        packages=find_packages(exclude=['tests*']),
        include_package_data=True,
        zip_safe=False,
        platforms='any',
        install_requires=['argparse>=1.2.1'],
        classifiers=[
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: OS Independent',
                    'Programming Language :: Python',
                ],
)


