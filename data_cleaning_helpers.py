# -*- coding: utf-8 -*-
"""
Data Clearning Helper Functions

Created on Fri Oct 27 10:19:34 2017

@author: Tim McCormick


"""

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y