try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Cooking with Chemistry website',
    'author': 'NikZProjects',
    # Github link
    'url': 'URL where to get it',
    # Githib download file (tar/zip)
    'download_url': 'URL where to download it',
    'author_email': 'NikZ.projects@gmail.com',
    'version': '0.1',
    'install_requires': ['flask', 'libsass'],
    'packages': ['CWC'],
    'scripts': [],
    'name': 'CWC-NikZProjects'
}

setup(**config)
