import pickle
import tensorflow as tf
import numpy as np
train_data = {}
test_data = {}

with open('/home/intern01/jhk/data.pickle','rb') as f :
    train_data = pickle.load(f)

train_data = train_data[:,:,30:,50:]
print(train_data.shape)
with open('/home/intern01/jhk/1820obsv.pickle','rb') as f :
    test_data = pickle.load(f)
    test_data = test_data.numpy()

## C, U, V 순서
train_tensor = tf.constant(train_data)
test_tensor = tf.constant(test_data)

train_data = np.delete(train_data,5103,axis=0)
train_data = np.delete(train_data,10359,axis=0)
train_data = np.delete(train_data,14872,axis=0)
train_data = np.delete(train_data,14870,axis=0)
train_data = np.delete(train_data,14363,axis=0)

print(np.where(train_data[:,0,:,:] == -8.834088819714962))

C_max = np.max(train_data[:, 0, :, :])
C_min = np.min(train_data[:, 0, :, :])
U_max = np.max(train_data[:, 1, :, :])
U_min = np.min(train_data[:, 1, :, :])
V_max = np.max(train_data[:, 2, :, :])
V_min = np.min(train_data[:, 2, :, :])
print(C_max, C_min)
print('**********')
print(U_max, U_min)
print('**********')
print(V_max, V_min)
print('*****new*****')

train_data[:, 0, :, :] = (train_data[:, 0, :, :] - C_min) / (C_max - C_min)
train_data[:, 1, :, :] = (train_data[:, 1, :, :] - U_min) / (U_max - U_min)
train_data[:, 2, :, :] = (train_data[:, 2, :, :] - V_min) / (V_max - V_min)

test_data[:, 0, :, :] = (test_data[:, 0, :, :] - C_min) / (C_max - C_min)
test_data[:, 1, :, :] = (test_data[:, 1, :, :] - U_min) / (U_max - U_min)
test_data[:, 2, :, :] = (test_data[:, 2, :, :] - V_min) / (V_max - V_min)

tcmax = np.nanmax(test_data[:, 0, :, :])
tcmin = np.nanmin(test_data[:, 0, :, :])
tumax = np.max(test_data[:, 1, :, :])
tumin = np.min(test_data[:, 1, :, :])
tvmax = np.max(test_data[:, 2, :, :])
tvmin = np.min(test_data[:, 2, :, :])
print(tcmax, tcmin)
print('**********')
print(tumax, tumin)
print('**********')
print(tvmax, tvmin)