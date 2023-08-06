[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/mattkearns/mldatatools/blob/master/LICENSEs)
[![PyPi Version](https://img.shields.io/pypi/v/mldatatools.svg)](https://pypi.python.org/pypi/mldatatools/)

# mldatatools

This package provides several utility objects for automatically preprocessing machine learning datasets. Specifically, this package provides tools for automatically handling missing values, removing statistical outliers, encoding categorical (nominal & ordinal) features, scaling numerical features, and feature discretization (binning).

## Installation Guide

### Prerequisites

This package requires `numpy` `scipy` and `pandas` to be installed before it can be used.

`pip install numpy scipy pandas`

or

`pip install -r requirements.txt`

### Install from the Python Package Index (PyPi):

`pip install mldatatools`

### Install from Source (GitHub):

`git clone https://github.com/mattkearns/mldatatools.git`

`cd mldatatools/`

`pip install .`

## Usage Guide

### How to use the PandasDataProcessor to process a Pandas DataFrame:


```python
from mldatatools.preprocessing import PandasDataProcessor

df = ...

# tell the data processor exactly how to process your data
df = PandasDataProcessor(
    numerical_feats=['f1', 'f2', 'f3'],
    nominal_feats=['f4'],
    ordinal_feats=['f5'],
    missing_policy='mean',
    nominal_policy='dummy',
    scaling_policy='min-max',
    missing_values=[np.nan, '?', ''],
    outlier_zscore=2.5,
    ordinal_schema={'f5': {'low': 1, 'medium': 2, 'high': 3}}
).process(df)
```

### Alternatively, you can use the PandasMetadataExtractor helper class:


```python
from mldatatools.preprocessing import PandasMetadataExtractor

df = PandasDataProcessor(
    **PandasMetadataExtractor().extract(df)
).process(df)
```

## Contributors

Matt Kearns @mattkearns

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgements

Thanks to James Scott for his blog post on how to write a 'kick ass' README!

https://dev.to/scottydocs/how-to-write-a-kickass-readme-5af9