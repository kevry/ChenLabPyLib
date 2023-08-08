import chenlabpylib
import sys

def test_chenlabpaths1():
  # testing chenlab_filepaths function still follows functionality
  test_path = "/net/claustrum/mnt/data/Projects/Homecage/TestFile.txt"
  converted_path = chenlabpylib.chenlab_filepaths(test_path)
  
  if sys.platform == 'linux': # on linux/SCC
    assert converted_path == test_path
  else: # on Windows
    assert converted_path == 'Z:\\Projects\\Homecage\\TestFile.txt'

def test_chenlabpaths2():
  # testing chenlab_filepaths function still follows functionality
  test_path = "/net/claustrum4/mnt/storage/data/Projects/ARG"
  converted_path = chenlabpylib.chenlab_filepaths(test_path)
  
  if sys.platform == 'linux': # on linux/SCC
    assert converted_path == test_path
  else: # on Windows
    assert converted_path == 'V:\\Projects\\ARG'
    
  
