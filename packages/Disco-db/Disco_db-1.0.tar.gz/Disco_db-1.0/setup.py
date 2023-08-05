from distutils.core import setup

setup(
  name = 'Disco_db',
  packages = ['Disco_db'],
  version = '1.0',
  license='gpl-3.0',     
  description = 'Disco is minimalist password encoded database system made in python, that emphasizes simplicity and efficiency',
  author = 'argvsc47',
  author_email = '',
  url = 'https://github.com/argvsc47/Disco_db',
  download_url = 'https://github.com/argvsc47/Disco_db/archive/refs/tags/v1.0.tar.gz',
  keywords = ['Disco', 'Database', 'light', 'secure'],
  install_requires=[
          'cryptography',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Database',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
