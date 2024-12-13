#!/usr/bin/env python3

import scipy.io
import numpy as np
from matplotlib import pyplot as plt
import os

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


# # Data for example plots
# dataset1 = scipy.io.loadmat(f".\P01_B02_Idef_Ndef")
# # print(list_indexes(dataset1))

# Te_0_ex = np.array(get_variable('te0', dataset1))
# tite_ex = np.array(get_variable('tite', dataset1))
# taue_ex = np.array(get_variable('taue', dataset1))
# ni_0_ex = np.array(get_variable('ni0', dataset1))

# T_i0_ex = Te_0_ex * tite_ex
# TP_ex = T_i0_ex * taue_ex * ni_0_ex

TP_means = []
TP_err = []

Te0_means = []
Te0_err = []

Ti0_means = []
Ti0_err = []

tite_means = []

taue_means = []
taue_err = []

ni0_means = []
ni0_err = []

beta_means = []
beta_err = []

indexes1 = ["01", "03", "05", "07", "09","11", "13", "15", "17", "19", "21", "23", "25", "27", 
            "29", "31", "33", "35", "37", "39"]
indexes2 = ["1", "2", "3", "4", "5","6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
indexes3 = ["0.5", "1", "1.5", "2", "2.5", "3","3.5", "4", "4.5", "5", "5.5", "6.5", "7",
             "9", "11", "13", "15", "17", "19", "21", "23", "25", "27", 
            "29", "31", "33", "35", "37", "39"]

data = 'matt runs 2'  # Replace this with the actual folder name
# Loop over your indexes and load the .mat files
for i in indexes2:
    # Create the full file path using os.path.join()
    file_path = os.path.join(data, f"P{i}")
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

    Te0_means.append(np.mean(Te0[50:100]))
    Te0_err.append(np.std(Te0[50:100]))

    tite_means.append(np.mean(tite[50:100]))

    taue_means.append(np.mean(taue[50:100]))
    taue_err.append(np.std(taue[50:100]))

    ni0_means.append(np.mean(ni0[50:100]))
    ni0_err.append(np.std(ni0[50:100]))

    Ti0_means.append(np.mean(Ti0[50:100]))
    Ti0_err.append(np.std(Te0[50:100]))

    beta_means.append(np.mean(beta[50:100]))
    beta_err.append(np.std(beta[50:100]))

    TP_means.append(np.mean(TP[50:100]))
    # TP_err.append(np.mean(TP[50:100])*np.sqrt((np.std(Ti0[50:100])/np.mean(Ti0[50:100]))**2 + 
    #                       np.std(taue[50:100])/np.mean(taue[50:100]))**2 +
    #                       np.std(ni0[50:100])/np.mean(ni0[50:100])**2)
    TP_err.append(np.std(TP[50:100]))

TP_means =  np.array(TP_means)
TP_err = np.array(TP_err)

Te0_means = np.array(Te0_means)
Te0_err = np.array(Te0_err)
Ti0_means = np.array(Ti0_means)
Ti0_err = np.array(Ti0_err)
tite_means = np.array(tite_means)
taue_means = np.array(taue_means)
taue_err = np.array(taue_err)
ni0_means = np.array(ni0_means)
ni0_err = np.array(ni0_err)
beta_means = np.array(beta_means)
beta_err = np.array(beta_err)