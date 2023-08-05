#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['pyimporters_skos_rf']

package_data = \
{'': ['*']}

install_requires = \
['pyimporters_plugins', 'rdflib']

entry_points = \
{'pyimporters.plugins': ['skos-rf = '
                         'pyimporters_skos_rf.skos_rf:SKOSRFKnowledgeParser']}

setup(name='pyimporters-skos-rf',
      version='0.1.27',
      description='Sherpa knowledge import plugins',
      author='Olivier Terrier',
      author_email='olivier.terrier@kairntech.com',
      url='https://kairntech.com/',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      entry_points=entry_points,
      python_requires='>=3.8',
     )
