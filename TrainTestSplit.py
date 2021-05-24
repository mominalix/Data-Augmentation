import pandas as pd
import numpy as np
import os
import pandas as pd
import shutil

directory=os.path.join(os.getcwd(), 'data/train_labels.csv')
df = pd.read_csv(directory)
df['split'] = np.random.randn(df.shape[0], 1)

msk = np.random.rand(len(df)) <= 0.8

train = df[msk]
test = df[~msk]

train.to_csv('data/split/train_labels.csv', index = None)
test.to_csv('data/split/test_labels.csv', index = None)

df = pd.read_csv('data/split/train_labels.csv')
matrix1 = df[df.columns[0]].to_numpy()
list1 = matrix1.tolist()
df2 = pd.read_csv('data/split/test_labels.csv')
matrix2 = df2[df2.columns[0]].to_numpy()
list2 = matrix2.tolist()

for file in list1:
    shutil.move("images/"+file, "images/train/"+file)
for file in list2:
    shutil.move("images/"+file, "images/test/"+file)