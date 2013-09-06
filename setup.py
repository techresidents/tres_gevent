import os
import setuptools
from distutils.core import setup

def find_packages():
    packages = []
    for dir,subdirs,files in os.walk('tres_gevent'):
        package = dir.replace(os.path.sep, '.')
        if '__init__.py' not in files:
            # not a package
            continue
        packages.append(package)
    return packages

setup(
    name='tres_gevent',
    version = '0.5.0',
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
        'trpycore>=0.11.0',
        'trhttp>=0.5.0',
        'trhttp_gevent>=0.5.0',
        'tres>=0.5.0'
    ]
)
