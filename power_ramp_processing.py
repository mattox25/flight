#!/usr/bin/env python3

import scipy.io
from scipy.signal import find_peaks
import numpy as np
from matplotlib import pyplot as plt
import os

import scipy.optimize

def list_subsections():
    print("subsections (I'm using zerod by default):")
    print(full_dataset['post'].dtype)


def list_indexes(dataset, subsection='zerod'):
    print("indexes in subsection " + subsection + ":")
    print(dataset['post']['zerod'][0][0].dtype)


def get_variable(index, dataset, subsection='zerod'):
    a = dataset['post'][subsection][0][0][index][0][0]
    a = [float(x[0]) for x in a]
    return a


def get_average(start, end, index, subsection='zerod'):
    a = get_variable(index, subsection=subsection)
    return (np.mean(a[start:end]), np.std(a[start:end]))

data = 'power_ramp_data'  # Replace this with the actual folder name

file_path = os.path.join(data, f"run2")
full_dataset = scipy.io.loadmat(file_path)

# # Define the folder where the files are located
# folder_path = 'best data'  # Replace with the actual path of your folder

# To get T_i0 we want T_e0*tite
Te0 = np.array(get_variable('te0',full_dataset))
tite = np.array(get_variable('tite', full_dataset))
taue = np.array(get_variable('taue', full_dataset))
ni0 = np.array(get_variable('ni0', full_dataset))
beta = np.array(get_variable('betan', full_dataset))
Ti0 = Te0 * tite
TP = Ti0 * taue * ni0

# We also need the power at different times!
pnbi = np.array(get_variable('pnbi', full_dataset))
mask = np.where(pnbi != 0)[0]

peaks = find_peaks(taue[mask])[0]