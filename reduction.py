
'''
Written by JT Fuchs, UNC, September 2016.

This program mimics ReduceSpec.py, but allows the user to select which functions to perform on which images.

Outline:
prompt user for task (subtract, divide, combine, trim, apply wavelength solution)
complete task

'''

import numpy as np
import pyfits as pf
import ReduceSpec_tools as rt
import spectools as st
import warnings

task = raw_input('What would you like to do? (bias, flat, normalize, combine, trim, wavelength) ')

if task == 'combine':
    files = raw_input('Name of file containing images to combine: ')
    filelist = rt.Read_List(files)
    output_file = raw_input('Output file name: ')
    method = raw_input('Method to combine (median,average,sum): ')
    low_sig = float(raw_input('Low sigma clipping threshold: '))
    low_sig = np.abs(low_sig) #Ensure that this value is positive
    high_sig = float(raw_input('High sigma clipping threshold: '))

    rt.imcombine(filelist,output_file,method,lo_sig = low_sig, hi_sig = high_sig)

if task == 'trim':
    files = raw_input('Name of file to trim: ')
    rt.Trim_Spec(files)

if task == 'wavelength':
    Wavefile = raw_input('Name of file with wavelength solution: ')
    files = raw_input('Name of file to apply wavelength solution to: ')
    outputfile = raw_input('Output name of file: ')

    st.applywavelengths(Wavefile,files,outputfile)

if task == 'normalize':
    files = raw_input('Name of flat file to normalize: ')
    rt.Norm_Flat_Poly(files)

if task == 'bias':
    files = raw_input('Name of file containing images to bias-subtract: ')
    filelist = rt.Read_List(files)
    zerofile = raw_input('Name of Master Zero: ')
    
    rt.Bias_Subtract(filelist,zerofile)

if task == 'flat':
    files = raw_input('Name of file containing images to flat-field: ')
    filelist = rt.Read_List(files)
    flatfile = raw_input('Name of Normalized Flat: ')

    rt.Flat_Field(filelist,flatfile)

    