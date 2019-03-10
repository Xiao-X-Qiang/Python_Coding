
from sklearn.datasets import load_iris

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split

data = load_iris()

x_train,x_test,y_train,y_test = train_test_split(data.data,data.target,test_size=0.25)


