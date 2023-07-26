import os
import sys

def convert_path(path):
	""" modify file path depending on the current OS in use.
	this code will sometimes run on Windows environment or SCC(linux) """

	print("testing")

	# create hash table of letter network drives and SCC mounted paths
	map2scc = {
		'Z:': '/net/claustrum/mnt/data', 
		'Y:': '/net/claustrum/mnt/data1',
		'X:': '/net/claustrum2/mnt/data',
		'W:': '/net/clasutrum3/mnt/data', 
		'V:': '/net/claustrum4/mnt/storage/data',
	}

	map2win = {v: k for k, v in map2scc.items()}

	# running on linux
	if sys.platform == 'linux':
		for key in map2scc:
			if key in path:
				path = path.replace(key, map2scc[key])
				break
		# reverse backslash		
		path = path.replace('\\', '/')
	else:
		# running on windows
		for key in map2win:
			if key in path:
				path = path.replace(key, map2win[key])
				break
		path = path.replace('/', '\\')

	return path