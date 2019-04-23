# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:50:41 2018

@author: Caio Hamamura

It generates the radar-boxplot
"""
import matplotlib.pyplot as plt
import math
import numpy as np


def radarboxplot(x, y, colNames, plotMedian=False, **kwargs):
    nrows = kwargs.get("nrows")
    ncols = kwargs.get("ncols")

    # Standardize between [0.1, 1]
    N = x.shape[1]
    minVal = np.min(x, 0)
    maxVal = np.max(x, 0)
    standardized = 0.1+0.9*(x-minVal)/(maxVal-minVal)
    
    # Calculate angles for each variable and 
    # repeat to close polygons
    angles = [n / float(N) * 2 * math.pi for n in range(N)]
    angles += angles[:1]

    classes = np.unique(y)
    if not(nrows and ncols):
        nClasses = len(classes)
        nrows = ncols = math.ceil(math.sqrt(nClasses))
    axs = []
    fig = plt.figure()
    for i in range(len(classes)):
        class_i = classes[i]
        values = standardized[y == class_i]
        quantiles = np.quantile(values, axis=0, q=[0.25, 0.5, 0.75])
        q25 = quantiles[0]
        q50 = quantiles[1]
        q75 = quantiles[2]
        qDiff = q75-q25
        outTop = values > (q75+qDiff*1.5)
        outBot = values < (q25-qDiff*1.5)
        tops = np.ma.array(values, mask=outTop)
        bots = np.ma.array(values, mask=outBot)
        q100 = np.max(tops, 0)
        q0 = np.min(bots, 0)
        q100 = np.append(q100, q100[0])
        q0 = np.append(q0, q0[0])
        q25 = np.append(q25, q25[0])
        q50 = np.append(q50, q50[0])
        q75 = np.append(q75, q75[0])
        bots = values[outBot]
        botsAlpha = (np.array(angles[:-1])*outBot)[outBot]
        tops = values[outTop]
        topsAlpha = (np.array(angles[:-1])*outTop)[outTop]
        axs.append(__generate_plot__(angles, q25, q50, q75, q0, q100, topsAlpha,
                                tops, botsAlpha, bots, i+1, class_i, colNames,
                                plotMedian, fig, nrows, ncols, kwargs))
    return (fig, axs)


def __generate_plot__(angles, q25, q50, q75, q0, q100, topsAlpha, tops,
                 botsAlpha, bots, row, title, categories, plotMedian, fig,
                 nrows, ncols, kwargs):
    # Check if there is color kwargs:
    color = kwargs.get("color")
    if not color:
        color = ['r', 'b', 'black']

    col1 = color[0]
    col2 = color[1]
    col3 = "black"
    if len(color) > 2:
        col3 = color[2]

    # Initialize polar subplot
    ax = plt.subplot(nrows, ncols, row, polar=True)
    plt.title(title, y=1.16)
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axis per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=7)
    plt.subplots_adjust(hspace=0.6, wspace=0.6)

    # Draw ylabels
    ax.set_rlabel_position(0)
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)

    plt.yticks([0.25, 0.5, 0.75], ["", "", ""], color="grey", size=7)
    plt.ylim(0, 1)

    # Fill area
    plt.fill_between(angles, q25, q75, color=col1, lw=0, alpha=0.7)
    plt.fill_between(angles, q75, q100, color=col2, lw=0, alpha=0.4)
    plt.fill_between(angles, q25, q0, color=col2, lw=0, alpha=0.4)

    if plotMedian:
        plt.polar(angles, q50, lw=.5, color=col3)
    plt.polar(angles, q25, lw=1, color=col1)
    plt.polar(angles, q75, lw=1, color=col1)
    plt.polar(topsAlpha, tops, markeredgecolor="black", marker="o", 
              markerfacecolor="none", linewidth=0, markersize=3)
    plt.polar(botsAlpha, bots, markeredgecolor="black", marker="o", 
              markerfacecolor="none", linewidth=0, markersize=3)
    return ax
