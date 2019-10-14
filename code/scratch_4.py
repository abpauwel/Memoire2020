import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import train_test_split
from Machine_learning import worktbl,tbl,matching
def mgtbl(table,lisT,nameoflist):
    inTH = len(lisT)
    newtbl = pd.DataFrame({'Nb_run': np.tile(Nb_run, inTH), nameoflist: np.repeat(lisT, 10, axis=0)})
    return table.merge(newtbl, on='Nb_run')

for meta in range(51,len(matching)):
    curr = matching[meta]
    Nb_run = list(range(10))
    max_depth = [2,3,6,10,15,20]
    min_samples_split = [2,4,5,8,10,15,20]
    min_impurity_decrease = [0,0.01,0.03,0.05,0.07,0.1,0.15,0.2,0.3]
    t1 = pd.DataFrame({'Nb_run':np.repeat(Nb_run,1,axis=0),'criterion':np.repeat(['entropy'],10, axis=0)})
    t2 = pd.DataFrame({'Nb_run':np.repeat(Nb_run,1,axis=0),'criterion':np.repeat(['gini'],10, axis=0)})
    t3 = t1.append(t2)
    inT = len(max_depth)
    t4 = pd.DataFrame({'Nb_run':np.tile(Nb_run,inT),'max_depth':np.repeat(max_depth,10,axis=0)})
    t5 = t3.merge(t4, on ='Nb_run' )
    inT = len(min_samples_split)
    t6 = mgtbl(t5,min_samples_split,'min_samples_split')
    t8 = mgtbl(t6,min_impurity_decrease,'min_impurity_decrease')


    t8['Bcr_test'] = 0
    t8['Bcr_train'] = 0
    t8['iter'] = list(range(len(t8)))

    def fillinetree(table,Tbl,Worktbl):
        label = Tbl[curr].notnull().astype(int).to_frame()
        # Split the data and the label into test and train set
        train, test, label_train, label_test = train_test_split(Worktbl, label, test_size=0.2)

        # If this exercise was never used by the physio, don't run the algorithm
        if sum(label_train.values) != 0:

            # Train prediction
            clf = tree.DecisionTreeClassifier(max_depth=table['max_depth'],criterion=table['criterion'],min_samples_split=table['min_samples_split'],min_impurity_decrease=table['min_impurity_decrease'])
            clf = clf.fit(train, label_train)

            # Predict the label for train set
            train_pred = clf.predict(train)

            # Bcr calculationn
            table['Bcr_train'] = balanced_accuracy_score(label_train, train_pred)

            # Test prediction with the model build on the train set
            test_pred = clf.predict(test)

            table['Bcr_test'] = balanced_accuracy_score(label_test, test_pred)

            print(str(table['iter']) + ": "+str(matching[meta])+" :"+str(table['Bcr_test'] ))
        return table






    t9 = t8.copy()

    t9 = t9.apply(fillinetree,args = (tbl,worktbl), axis=1)
    t9.to_csv("C:\\Users\cocol\Desktop\memoire\Jéjé_work\metaparam\met"+str(curr)+".csv")