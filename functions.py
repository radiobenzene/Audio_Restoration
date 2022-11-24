#Author - Uditangshu Aurangabadkar
import wave
import matplotlib.pyplot as plt
from tqdm import tqdm
import time
from scipy.io import loadmat
import pandas as pd
import numpy as np
import scipy.io.wavfile as wav
from scipy.io import wavfile
import soundfile as sf
from playsound import playsound
import pandas as pd
from pymatreader import read_mat
from time import gmtime, strftime
from functions import *
import sys



'''
    The current file contains all the functions
    used in the main() function for median filtering
'''
#Defining error code for window with even length
WINDOW_LEN_EVEN = -1

#Function to read an audio track
'''
    Params - track_name - specifies the name of the track to be read
    Return - track that has been read as an object type
'''
def readTrack(track_name):
    fs, signal = wavfile.read(track_name)
    #data, samplerate = sf.read(track_name)
    return fs, signal

#Function to read matlab file where index is a 1
'''
    Params - file_name - matlab file
    Return - A dictionary
'''
def getMatlabFile(file_name):
    matlab_file = loadmat(file_name)
    return matlab_file

#Function to convert dictionary to array
'''
    Params - dict_name - dictionary type variable
    Return - Converted dictionary as an array
'''
def getArrayFromDict(dict_name):
    ret_val = dict_name['thress']
    return ret_val

#Function to get the detection index
'''
    Params - arr - input array
           - item - 1 or 0
    Return - index where the item is present in array
'''
def getIndex(arr, item):
    indices = np.where(arr == item)
    indices = indices[1]
    indices = indices[1:661500]
    return indices

#Function to set window length for the median filter
def setWindowLength(val):
    return val

# Function to check if the filter length is odd
'''
    Params - filter_len - length of the filter
    Return - odd_flag - boolean variable if filter length is odd = true, else false
'''
def isOddLength(filter_len):

    if (filter_len % 2 == 1):
        is_odd_flag = True

    else:
        is_odd_flag = False
        print("Window size is even")
        
    return is_odd_flag

# Function for zero padding of the list
'''
    Params - data_list - input list
           - window_len - window length
    Return - A padded list with 0s determined by the window length and input list
'''
def zeroPadding(data_list, window_len):
    padded_list = data_list

    N_filter = window_len
    N_new = int((N_filter - 1) / 2)

    is_odd_flag = isOddLength(window_len)

    if (is_odd_flag == True):
        padded_list = np.pad(padded_list, (N_new, N_new),
                             'constant', constant_values=(0, 0))

    else:
        padded_list = data_list


    return padded_list

# Function for Median filtering
'''
    Params - data_list - input list
           - window_len - window length
    Return - A new filter after being median filtered
'''
def medianFilter(data_list, window_len):
    new_array = []

    #Case when the length of list is less than window length
    if (isOddLength(window_len) == False):
        return WINDOW_LEN_EVEN

    if len(data_list) < window_len:
        return data_list

    for i in range(len(data_list) - window_len + 1):
        #Sorting the windowed elements
        sorted_list = np.sort(data_list[i: i + window_len])

        #Getting the middle element
        middle_index = int((window_len - 1) / 2)

        #Getting elements from the sorted list
        middle_elem = sorted_list[middle_index]

        #Creating a new array of only middle elements
        new_array.append(middle_elem)

    return np.array(new_array)

#Function to modify median filter such that window size and list are same
def modifyList(data_list, window_len):
    ret_list = data_list
    pass

#Function to plot the graph
'''
    Params - track - audio track
           - fs - sampling rate
    Return - a plotted graph
'''
def plotGraph(track, fs):
    length = track.shape[0] / fs
    time = np.linspace(0., length, track.shape[0])
    plt.plot(time, track)
    plt.show()

#Function to show help
def showHelp():
    print("This is an audio restoration project which uses Median Filtering to restore a track\n")
    print("python3 <file_name> -h displays the Help Menu")
    print("python3 <file_name> -r runs the program")
    print("python3 <file_name> -mse gives the MSE error between the audio tracks")