# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:50:41 2018

@author: caioh

It generates the radar-boxplot
"""
import matplotlib.pyplot as plt
from math import pi
import numpy as np
import pandas as pd


def radoxPlot(data, varFactor):
    data2 = data.loc[:,data.columns!=varFactor]
    N = data2.shape[1]
    colNames=data2.columns
    minVal = data2.apply(np.min)
    maxVal = data2.apply(np.max)
    padronizado=0.1+0.9*(data2-minVal)/(maxVal-minVal)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]


    spp = np.unique(data[varFactor])
    for i in range(len(spp)):
        sp = spp[i]
        values=padronizado[data[varFactor]==sp]
        q25=values.apply(np.quantile, 0, q=0.25)
        q50=values.apply(np.quantile, 0, q=0.5)
        q75=values.apply(np.quantile, 0, q=0.75)
        qDiff = q75-q25
        outTop = values>(q75+qDiff*1.5)
        outBot = values<(q25-qDiff*1.5)
        tops=pd.DataFrame.mask(values, np.logical_not(outTop))
        bots=pd.DataFrame.mask(values, np.logical_not(outBot))
        maxVals=pd.DataFrame.mask(values, outTop).apply(np.max)
        minVals=pd.DataFrame.mask(values, outBot).apply(np.min)
        maxVals=np.append(maxVals, maxVals[0])
        minVals=np.append(minVals, minVals[0])
        q25=np.append(q25, q25[0])
        q50=np.append(q50, q50[0])
        q75=np.append(q75, q75[0])
        bots=bots.values[outBot]
        botsAlpha=(np.array(angles[:-1])*outBot).values[outBot]
        tops=tops.values[outTop]
        topsAlpha=(np.array(angles[:-1])*outTop).values[outTop]
        generatePlot(angles, q25, q50, q75, minVals, maxVals, topsAlpha, tops, 
                 botsAlpha, bots, i+1, sp, colNames)
    


def generatePlot(angles, q25, q50, q75, minVals, maxVals, topsAlpha, tops, botsAlpha, bots, row, title, categories):
    ax = plt.subplot(4, 4, row, polar=True)
    plt.title(title, y=1.16)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=7)
    plt.subplots_adjust(hspace=0.6, wspace=0.6)
    
    # Draw ylabels
    ax.set_rlabel_position(0)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    
    plt.yticks([0.25, 0.5, 0.75], ["", "", ""], color="grey", size=7)
    plt.ylim(0,1)
    
    # Fill area
    plt.fill_between(angles, q25, q75, color='r', lw=0, alpha=0.7)
    plt.fill_between(angles, q75, maxVals, color='b', lw=0, alpha=0.4)
    plt.fill_between(angles, q25, minVals, color='b', lw=0, alpha=0.4)
    
    plt.polar(angles, q50, lw=.5, color='black')
    plt.polar(angles, q25, lw=1, color='r')
    plt.polar(angles, q75, lw=1, color='r')
    plt.polar(topsAlpha, tops, markeredgecolor="black", marker="o", 
              markerfacecolor="none", linewidth=0, markersize=3)
    plt.polar(botsAlpha, bots, markeredgecolor="black", marker="o", 
              markerfacecolor="none", linewidth=0, markersize=3)



    
    
