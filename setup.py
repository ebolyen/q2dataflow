# ----------------------------------------------------------------------------
# Copyright (c) 2018-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
from setuptools import setup, find_packages


setup(
    name='q2dataflow',
    version="0.1.0",
    license='BSD-3-Clause',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['q2dataflow=q2dataflow.__main__:root']})
