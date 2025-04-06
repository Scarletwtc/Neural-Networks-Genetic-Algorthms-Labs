import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

#we have dataframe and time series
df = pd.read_csv('iris.data',header= None)

# matrix with 150 lines adn 4 cols
X= df.iloc[:, :4]

# we need taeget bt target is string and also 3 classes not 2 
# we will put 3 binary out pt A is 100 B 010 C 001
# so we map it wiht numbers

classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
T= df[4].replace(classes, [0,1,2])

plt.close('all')
'''
df.columns = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Class']
sns.pairplot(df, hue='Class')
'''


X_train, X_test, t_train, t_test = train_test_split(X, T, test_size=0.2, random_state=2)
#radom-state =2 e split bin de date , bune la atreanare proaste la test

#0.2 test is 20% train is 80%
#stohastic gradient descend = sgd, adam is better tahn sgd, sgd is standard 
#radient to mnimise loss, by sequential or by batch. 
# stohastc u compute gradient u dnt make resultant, 
#alpha is learning rate
# verbose = show changes ephoch whatever
# max_iten srtop
#hidden layer sized 4 inputs , 3 neurons in first hidden layer 
# 2 neurons on last hidden lay and 3 on output 
#random state =1 to have same result to not make random w and biases

#ctrl i to see stuff ab this
net = MLPClassifier(solver='sgd', alpha=1e-5, verbose=1, max_iter=1000, 
                    hidden_layer_sizes=(3, 3), random_state=1)

net.fit(X_train,t_train)

''''
4 
4 0   0
4 0 0 0
4 0 0 0

4s is input , then 3 neurons ,then 2 , then 3 outputs

'''
b = net.intercepts_
w= net.coefs_

#we need results close to T things train or test not sure

yTest = net.predict(X_test)


print('The accuracy is ' , accuracy_score(t_test, yTest))
print('Condusion matrix')
print(confusion_matrix(t_test, yTest))


# we have 6 verginica ,  6/30 20% classified correctly as verginica
# 0.33 e pt 3 grupe 



