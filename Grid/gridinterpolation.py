import pickle

data = {}

with open('/home/intern01/jhk/data.pickle','rb') as f :
    data = pickle.load(f)

## Conc, u, v 순서
print(data.shape)