import subprocess as sp
import numpy as np
from PIL import ImageGrab as igrab


def search_window(classname="^Minecraft.*"):
    """ search window and return geometry

    currently can only get one window
    for stability reasons"""

    cmd = [
        'xdotool',
        'search',
        '--limit',
        '1',
        '--class',
        '{}'.format(classname)
    ]
    result = sp.run(cmd, stdout=sp.PIPE, shell=False)
    outputs = result.stdout

    # the below should contain one window id and an empty string if successful
    params = outputs.decode('utf-8').split('\n')

    return params[0]


def get_current_active_window():
    """ get current active window"""

    cmd = [
        'xdotool',
        'getactivewindow'
    ]
    result = sp.run(cmd, stdout=sp.PIPE, shell=False)
    outputs = result.stdout
    # the params below should contain one window id and an empty string if successful
    params = outputs.decode('utf-8').split('\n')
    return params[0]


def activate_window(wid=''):
    """ activate window"""
    cmd = [
        'xdotool',
        'windowactivate',
        str(wid)
    ]

    result = sp.run(cmd)

    # 0 for success
    return result.returncode


def get_window_geometry(wid=''):
    """ get window geometry

    example:
    WINDOW=71303174
    X=732
    Y=169
    WIDTH=800
    HEIGHT=600
    SCREEN=0
    """

    cmd = [
        'xdotool',
        'getwindowgeometry',
        '--shell',
        str(wid)
    ]
    result = sp.run(cmd, stdout=sp.PIPE, shell=False)
    outputs = result.stdout
    params = outputs.decode('utf-8').split('\n')

    data = dict()

    for p in params:
        if len(p) == 0:
            continue
        key, value = p.split('=')
        data[key] = int(value)
    
    return data


def shot_window(wid=''):
    """ take a screen shot at given window's position """

    data = get_window_geometry(wid=wid)
    
    bbox = (
        data['X'],
        data['Y'],
        data['X'] + data['WIDTH'],
        data['Y'] + data['HEIGHT']
    )

    im = igrab.grab()
    im = im.crop(bbox)
    return im

