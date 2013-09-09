import os
from setuptools import setup, find_packages, Extension

import ez_setup
ez_setup.use_setuptools()

setup(
    name='tres_gevent',
    version = '0.6-SNAPSHOT',
    author = 'Tech Residents, Inc.',
    packages = find_packages(),
    license = open('LICENSE').read(),
    description = 'Tech Residents Elastic Search Library (Gevent)',
    long_description = open('README').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        ],
    install_requires=[
        'greenlet>=0.4.0',
        'gevent>=0.13.7',
        'trpycore>=0.12.0',
        'trhttp_gevent>=0.6.0',
        'tres>=0.6.0'
    ],
    dependency_links=[
        'git+ssh://dev.techresidents.com/tr/repos/techresidents/lib/python/trpycore.git@0.12.0#egg=trpycore-0.12.0',
        'git+ssh://dev.techresidents.com/tr/repos/techresidents/lib/python/trhttp_gevent.git@0.6.0#egg=trhttp_gevent-0.6.0',
        'git+ssh://dev.techresidents.com/tr/repos/techresidents/lib/python/tres.git@0.6.0#egg=tres-0.6.0'
    ],
)
