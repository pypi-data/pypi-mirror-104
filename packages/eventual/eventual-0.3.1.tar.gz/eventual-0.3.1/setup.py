# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eventual',
 'eventual.dispatch',
 'eventual.infra',
 'eventual.infra.exchange',
 'eventual.infra.repo',
 'eventual.infra.uow',
 'eventual.model',
 'eventual.util']

package_data = \
{'': ['*']}

install_requires = \
['aio-pika>=6.8.0,<7.0.0',
 'orjson>=3.5.2,<4.0.0',
 'tortoise-orm[asyncpg]>=0.17.2,<0.18.0']

extras_require = \
{'rmq': ['eventual-rmq>=0,<1']}

setup_kwargs = {
    'name': 'eventual',
    'version': '0.3.1',
    'description': '',
    'long_description': None,
    'author': 'Ivan Dmitriesvkii',
    'author_email': 'ivan.dmitrievsky@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
