# Fastreport

Get report of different metrices  for classification and regression problem for many popular algorithms with single line of code. You have to pass only features(dataframe) and target(series) as arguments


Link to [PyPI](https://pypi.org/project/easyreport/)

Link to [detailed example](https://github.com/kishore-s-gowda/fastreport)


## Installation

Run the following to install:

```python
pip install fastreport
```

## Usage

```python
import report

# get report_classification
report.report_classification(df_features,df_target,test_size=0.3,scaling=False,large_data=False,average='binary')

```

```python
import report

# get report_regression
report.report_regression(df_features,df_target,test_size=0.3,scaling=False,large_data=False)

```



## Future works
1. Optimization
2. Add more functionality

## Drawbacks
1. Not suitable for very large datasets
2. Limited to existing users only
