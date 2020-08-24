try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Cooking with Chemistry website - source code',
    'author': 'NikZProjects',
    'url': 'https://github.com/NikZprojects/CWC',
    'download_url': 'https://github.com/NikZprojects/CWC/archive/master.zip',
    'author_email': 'NikZ.projects@gmail.com',
    'version': '0.2',
    'install_requires': ['flask', 'libsass'],
    'packages': ['CWC'],
    'scripts': [],
    'name': 'CWC-NikZProjects'
}

setup(**config)
