from copy import deepcopy
from sklearn.metrics import make_scorer, accuracy_score, f1_score, precision_score, recall_score
import torch


class Metrics():
    def __init__(self, num_classes):
        self.num_classes = num_classes

    def pearson(self, predictions, labels):
        x = deepcopy(predictions)
        y = deepcopy(labels)
        x = (x - x.mean()) / x.std()
        y = (y - y.mean()) / y.std()
        return torch.mean(torch.mul(x, y))

    def mse(self, predictions, labels):
        x = deepcopy(predictions)
        y = deepcopy(labels)
        return torch.mean((x - y) ** 2)

    def accuracy(self, predictions, labels):
        x = deepcopy(predictions)
        y = deepcopy(labels)
        count = 0
        for i,val in enumerate(predictions):
            if int(val) == int(labels[i]):
                count += 1
        return count/len(predictions)
    
    def recall(self, predictions, labels):
        x = deepcopy(predictions)
        y = deepcopy(labels)
        rec = recall_score(labels, predictions, average = 'macro')
        return rec
    
    def f1(self, predictions, labels):
        x = deepcopy(predictions)
        y = deepcopy(labels)
        f1s = f1_score(labels, predictions, average = 'weighted')
        return f1s
