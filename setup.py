#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tableshift',
      version='0.1',
      url='https://tableshift.org',
      description='A tabular data benchmarking toolkit.',
      long_description='A benchmarking toolkit for tabular data under distirbution shift. '
                       'For more details, see the paper '
                       '"Benchmarking Distribution Shift in Tabular Data with TableShift", '
                       'Gardner, Popovic, and Schmidt, 2023.',
      author='Josh Gardner',
      author_email='jpgard@cs.washington.edu',
      packages=find_packages(),
      include_package_data=True,
      data_files=[('tableshift/datasets',
                   ['tableshift/datasets/nhanes_data_sources.json',
                    'tableshift/datasets/icd9-codes.json'])],
      install_requires=[
          'numpy>=1.24.0',
          'ray>=2.5.0',
          'torch>=2.0.0',
          'torchvision>=0.15.0',
          'scikit-learn>=1.3.0',
          'pandas>=2.0.0',
          'fairlearn>=0.9.0',
          'folktables',
          'frozendict',
          'rtdl_revisiting_models',
          'xport',
          'tqdm',
          'hyperopt',
          'h5py',
          'tables',
          'category_encoders',
          'einops',
          'tab-transformer-pytorch',
          'openpyxl',
          'optuna',
          'kaggle',
          'datasets',
          'torchinfo'
      ]
      )
