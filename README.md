# Radar-Boxplot

This package provides the implementation of the radar-boxplot, a chart created and developed by the author.

## Installation

The package is available for Python 3 only and can be installed via pip.

`python -m pip install radarboxplot`


## Usage

Basically the arguments are a two-dimensional array of `x` numerical attributes (either continuous and ordinal will make sense), array of `y` classes (better the class name, because it will be the title of the subplots) and the `colNames` which are the column names to label the attributes accordingly. They must be in the same order os the columns of the `x` array.

Other parameters are:

- `plotMedian`: (boolean) if you want the median to be plotted
- `color`: list of colors to paint the chart. The first will be the 25-75% percentile, the second color the total range and the third color will be the median line.
- `nrows`: number of rows to arrange the subplots 
- `ncols`: number of columns to arrange the subplots

The function returns (`matplotlib figure`, [`matplotlib axes`]). The axes represent each of the subplots axes.


## Description

It merges the concepts of both radar chart and the boxplot chart, allowing to compare multivariate data for multiple classes/clusters at a time. It provides a intuitive understanding over the data by creating radar polygons which can be compared in terms of shape and thickness, giving a meaningful insight towards identifying high inner variation and similar classes/clusters.

By interpreting the radar-boxplot, it is possible to predict classification confusion over classes and understand why and what could be done to achieve better results.

The radar-boxplot draws two different regions colors representing the same a boxplot would, but for multiple attributes at once. The following example shows an example of the radar-boxplot over Iris Dataset. The inner red region represents the 25-75% percentiles of each attribute, while the blue area represents the total range, excluding the outliers as defined by [Tukey, 1977](https://amstat.tandfonline.com/doi/abs/10.1080/00031305.1978.10479236). Outlier appears as whiskers, just like the classic boxplot.

<p align="center">
IQR = Q3 - Q1 
 <br/>
LOWER_OUTLIER = Q1 - (1.5 x IQR)
<br/>
UPPER_OUTLIER = Q3 + (1.5 x IQR)
</p>


![Radar-boxplot example with iris](https://github.com/caiohamamura/radarboxplot-python/blob/master/tests/radarboxplot.png?raw=true)

Intuitively you can see that *Iris setosa* has a significant different distribution of its attributes. Although the radar-boxplot is still useful for this dataset, because it has only 4 variables, this could also be visualized by pairs of two variables or either a 3D scatter plot with 3 variables.

The radar-boxplot is best suited when you have more than 4 relevant variables for your clustering/classification task, because it makes able to represent such dimensionality while still being readable.

## Example

Using the iris dataset from sklearn:

```python
from sklearn.datasets import load_iris
from radarboxplot import radarboxplot
import matplotlib.pyplot as plt

iris = load_iris()

x = iris['data']
y = iris["target_names"][iris['target']]
colNames = iris["feature_names"]

# Basic default plot
radarboxplot(x, y, colNames)
plt.show()

# Use orange and green colors, plot median line, all in the same row
radarboxplot(x, y, colNames, plotMedian=True, color=["orange", "green"], nrows=1, ncols=3)
plt.show()
```
