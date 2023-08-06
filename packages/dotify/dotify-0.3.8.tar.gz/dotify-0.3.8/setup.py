# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dotify', 'dotify.models']

package_data = \
{'': ['*'], 'dotify.models': ['schema/*']}

install_requires = \
['moviepy',
 'mutagen',
 'python-jsonschema-objects',
 'pytube',
 'requests',
 'spotipy',
 'youtube-search-python']

setup_kwargs = {
    'name': 'dotify',
    'version': '0.3.8',
    'description': '🐍🎶 Yet another Spotify Web API Python library',
    'long_description': '# Dotify\n\n> **Because OOP is the light**\n\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dotify)](https://www.python.org/)\n[![PyPI](https://img.shields.io/pypi/v/dotify)](https://pypi.org/project/dotify/)\n[![CI](https://github.com/billsioros/dotify/actions/workflows/ci.yml/badge.svg)](https://github.com/billsioros/dotify/actions/workflows/ci.yml)\n[![Maintainability](https://api.codeclimate.com/v1/badges/573685a448c6422d49de/maintainability)](https://codeclimate.com/github/billsioros/dotify/maintainability)\n[![codecov](https://codecov.io/gh/billsioros/dotify/branch/master/graph/badge.svg?token=3F4OYLDW7P)](https://codecov.io/gh/billsioros/dotify)\n[![BCH compliance](https://bettercodehub.com/edge/badge/billsioros/dotify?branch=master)](https://bettercodehub.com/)\n[![PyPI - License](https://img.shields.io/pypi/l/dotify)](https://opensource.org/licenses/MIT)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n[![docs](https://github.com/billsioros/dotify/actions/workflows/docs.yml/badge.svg)](https://billsioros.github.io/dotify/)\n\n*🚧 The project is under development 🚧*\n\n## Example\n\n```python\n>>> from dotify import Dotify, Track\n>>> with Dotify(SPOTIFY_CLIENT, SPOTIFY_SECRET):\n>>>     result = next(Track.search("SAINt JHN 5 Thousand Singles", limit=1))\n>>> result\n<Track "SAINt JHN - 5 Thousand Singles">\n>>> result.url\n\'https://open.spotify.com/track/0fFWxRZGKR7HDW2xBMOZgW\'\n>>> result.download("SAINt JHN - 5 Thousand Singles.mp3")\nPosixPath(\'SAINt JHN - 5 Thousand Singles.mp3\')\n```\n\n## Documentation\n\nThe project\'s documentation can be found [here](https://billsioros.github.io/dotify/).\n\n## Installation\n\n```bash\npip install dotify\n```\n\n## License\n\n<img align="right" src="http://opensource.org/trademarks/opensource/OSI-Approved-License-100x137.png">\n\nThe project is licensed under the [MIT License](http://opensource.org/licenses/MIT):\n\nCopyright &copy; 2021 [Vasileios Sioros](https://github.com/billsioros)\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n',
    'author': 'billsioros',
    'author_email': 'billsioros97@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://billsioros.github.io/dotify/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
