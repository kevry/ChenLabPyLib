import json
import os
import requests
import sys


def chenlab_filepaths(path: str) -> str:
    """ Convert file/directory path based on ChenLab paths depending on the current OS in use.
    
    :param path: Full path to either a directory or file
    (ex: Z:/Projects/Homecage/DeepLabCut/test.txt)
    
    :return: the converted full path
    (ex: /net/claustrum/mnt/data/Projects/Homecage/DeepLabcut/test.txt)
    """
    
    # hard-coded lookup-table for converting between network drive letters(on Windows) and mounted paths on SCC(Linux)
    map2scc = {'Z:': '/net/claustrum/mnt/data', 'Y:': '/net/claustrum/mnt/data1', 'X:': '/net/claustrum2/mnt/data', 
               'W:': '/net/clasutrum3/mnt/data', 'V:': '/net/claustrum4/mnt/storage/data'}
    map2win = {v: k for k, v in map2scc.items()}
    
    if sys.platform == 'linux':
        # running on linux
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



def send_slack_notification(message: str, channel: str ="#e_pipeline_log", 
                            slack_url_path: str ="Z:\Dropbox\Chen Lab Dropbox\Chen Lab Team Folder\Projects\Home_Cage_Training\DeepLabCut\SlackPython\slack_url_chenlab.txt"
                            ) -> None:
    """ Send Slack notifications to Chen Lab channel
    
    :param message: Message to send to Slack
    :param channel: (Optional) Channel to send message (default channel is #e_pipeline_log
    :param slack_url_path: (Optional) Full path to the text file with the ChenLab Slack url. Note this Slack url should never be posted publicly

    :return: None
    """

    # update path based on OS
    slack_url_path = chenlab_filepaths(path = slack_url_path)
    
    if not os.path.exists(slack_url_path): # check if file exists
        raise ValueError("{} does not exist.".format(slack_url_path))
    
    with open(slack_url_path) as f:
        url = f.readline()
        
    payload = {}
    payload["text"] = message
    payload["channel"] = channel

    # create payload json
    myobj = json.dumps(payload)

    # error-check sending post-request
    try:
        # post request to slack
        # TODO: better improve ... check for response code
        response = requests.post(url, data = myobj)
    except:
        # print warning to command window
        print("Unable to communicate with ChenLab Slack")
        
    return None
