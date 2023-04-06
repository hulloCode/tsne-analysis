import matplotlib as mpl
import pandas as pd
import numpy as np

# mpl.use('TkAgg')

NORM_FREQ = 37.28941975

df = pd.read_csv('/home/ngmonteiro/RPDBCS/features_all.csv', delimiter=';')
df2 = pd.read_csv('/home/ngmonteiro/RPDBCS/labels.csv', delimiter=';', comment='#')

with np.load('/home/ngmonteiro/RPDBCS/spectrum.npz') as f:
    mat = [f[str(i.id)][100:6200] for _, i in df.iterrows()]

def get_axis(index):
    Y_index = df[df['id'] == index].index.values[0]
    Y = mat[Y_index]

    entry = df2.iloc[Y_index]
    factor = min(NORM_FREQ / entry.real_rotation_hz, 1.0)
    X = np.arange(Y.size + 100) * (entry.xhz_step / factor) + (entry.xhz_0 / factor)
    X = X[100:] / entry.real_rotation_hz

    return X, Y