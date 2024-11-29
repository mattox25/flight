#!/usr/bin/env python3

import scipy.io
import numpy as np
from matplotlib import pyplot as plt

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


# Data for example plots
dataset1 = scipy.io.loadmat(f".\P01_B02_Idef_Ndef")
# print(list_indexes(dataset1))

Te_0_ex = np.array(get_variable('te0', dataset1))
tite_ex = np.array(get_variable('tite', dataset1))
taue_ex = np.array(get_variable('taue', dataset1))
ni_0_ex = np.array(get_variable('ni0', dataset1))

T_i0_ex = Te_0_ex * tite_ex
TP_ex = T_i0_ex * taue_ex * ni_0_ex

TP_means = []
TP_vars = []
Te_0_means = []
tite_means = []
taue_means = []
ni_0_means = []

indexes = ["01", "03", "05", "07", "09","11", "13", "15", "17", "19", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39"]
for i in indexes:
    full_dataset = scipy.io.loadmat(f".\P{i}_B02_Idef_Ndef")

# To get T_i0 we want T_e0*tite
    Te_0 = np.array(get_variable('te0',full_dataset))
    tite = np.array(get_variable('tite', full_dataset))
    taue = np.array(get_variable('taue', full_dataset))
    ni_0 = np.array(get_variable('ni0', full_dataset))
    T_i0 = Te_0 * tite
    TP = T_i0 * taue * ni_0
    TP_means.append(np.mean(TP[50:100]))
    TP_vars.append(np.std(TP[50:100]))
    Te_0_means.append(np.mean(Te_0[50:100]))
    tite_means.append(np.mean(tite[50:100]))
    taue_means.append(np.mean(taue[50:100]))
    ni_0_means.append(np.mean(ni_0[50:100]))
