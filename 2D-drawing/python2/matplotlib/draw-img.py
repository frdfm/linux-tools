from __future__ import division

import matplotlib
matplotlib.use('GTKAgg') 

import sys
import csv


import pickle
import scipy
import pylab
import sys
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import copy
import numpy as np
#import log1
import math


from random import randint
from time import time
import copy
import random

def sgn(x):
    return (np.sign(x)+1)/2

def drawimg(o_x,o_y,o_w,o_h,img001):
    global c_x,c_y,c_w,c_h
    op_x=(o_x-c_x)/c_w
    op_y=(o_y-c_y)/c_h
    op_w=o_w/c_w
    op_h=o_h/c_h
    op_x=op_x-op_w/2
    op_y=op_y-op_h/2
    axicon = fig.add_axes([op_x,op_y,op_w,op_h])
    axicon.imshow(img001, aspect='auto')
    axicon.set_xticks([])
    axicon.set_yticks([])
    axicon.axis('off')

   
    

def drawtxt(o_x,o_y,txt,sz,cl,prop):
    global c_x,c_y,c_w,c_h,pic_shrink
    op_x=(o_x-c_x)/c_w
    op_y=(o_y-c_y)/c_h
    eps1 = sys.float_info.epsilon
    plt = fig.add_axes([op_x,op_y,.1,.1])
    #prop = fm.FontProperties(fname='eric.ttf')
    pylab.text(0,0,txt,fontsize=sz*pic_shrink,color=cl,fontproperties=prop)
    plt.set_xticks([])
    plt.set_yticks([])
    plt.axis('off')






def init():
    global fig,c_x,c_y,c_w,c_h,pic_shrink,script_list,pw,ph,screen,sprites
    c_x=-1
    c_y=-.5
    c_w=2
    c_h=1
    
    pic_shrink=1
    eps1 = sys.float_info.epsilon
    fig = pylab.figure()
    fig.set_size_inches(20*pic_shrink,10*pic_shrink)
    fig.set_dpi(100)
    axplot = fig.add_axes([0+eps1,0,1,1])
    axplot.set_xticks([])
    axplot.set_yticks([])
    axplot.axis('off')
    
    [pw, ph] = [2000,1000]
    

init()

drawimg(0,0,2,1,mpimg.imread('test.jpg'));

fig.savefig('frame%s.png'%(str(int(0*1000000)).rjust(20,'0')));






