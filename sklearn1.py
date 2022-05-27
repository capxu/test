1.7 鸢尾花分类
1.71 初识数据
本例中我们用到了鸢尾花（Iris）数据集，这是机器学习和统计学中一个经典的数据集。它包含在 scikit-learn 的 datasets 模块中。我们可以调用 load_iris 函数来加载数据：
In[10]:
from sklearn.datasets import load_iris
iris_dataset = load_iris()
load_iris 返回的 iris 对象是一个 Bunch 对象，与字典非常相似，里面包含键和值：



