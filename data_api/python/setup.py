# -*- coding: utf-8 -*-


import os
from setuptools import setup, find_packages

def read(*rnames):
    text = open(os.path.join(os.path.dirname(__file__), *rnames)).read()
    return unicode(text, 'utf-8').encode('ascii', 'xmlcharrefreplace')

setup(
    name='kooaba.data_api',
    version='0.2.1',
    author="Peter Čech",
    description="Python API for kooaba",
    long_description=read('README.md'),
    keywords="kooaba api",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url='https://github.com/kooaba/kooaba-api',
    packages=('kooaba', 'kooaba.data_api',),
    install_requires=['distribute'],
    include_package_data=True,
    namespace_packages=['kooaba'],
    zip_safe=False,
    )
