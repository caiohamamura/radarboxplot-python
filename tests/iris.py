from sklearn.datasets import load_iris
from radarboxplot import radarboxplot
import matplotlib.pyplot as plt

iris = load_iris()

x = iris['data']
y = iris["target_names"][iris['target']]
colNames = iris["feature_names"]

radarboxplot(x, y, colNames, color=["orange", "green"], nrows=1, ncols=3)
plt.show()
