
import numpy as np
from sklearn.metrics import roc_auc_score

def auc(n, label, pre):
    y = np.array(label)
    y_score = np.array(pre)
    roc_auc_score(y, y_score)
    return roc_auc_score(y,y_score)

n = int(input())
label = []
pre = []
for i in range(n):
    sen = input()
    label.append(float(sen.split(' ')[0]))
    pre.append(float(sen.split(' ')[1]))
print(auc(n, label, pre))

