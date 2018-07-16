#!/usr/bin/python

##############################################################################################################################################################################
# Copyright (c) 2017, Miroslav Stoyanov
#
# This file is part of
# Toolkit for Adaptive Stochastic Modeling And Non-Intrusive ApproximatioN: TASMANIAN
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions
#    and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse
#    or promote products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
# OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# UT-BATTELLE, LLC AND THE UNITED STATES GOVERNMENT MAKE NO REPRESENTATIONS AND DISCLAIM ALL WARRANTIES, BOTH EXPRESSED AND IMPLIED.
# THERE ARE NO EXPRESS OR IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE, OR THAT THE USE OF THE SOFTWARE WILL NOT INFRINGE ANY PATENT,
# COPYRIGHT, TRADEMARK, OR OTHER PROPRIETARY RIGHTS, OR THAT THE SOFTWARE WILL ACCOMPLISH THE INTENDED RESULTS OR THAT THE SOFTWARE OR ITS USE WILL NOT RESULT IN INJURY OR DAMAGE.
# THE USER ASSUMES RESPONSIBILITY FOR ALL LIABILITIES, PENALTIES, FINES, CLAIMS, CAUSES OF ACTION, AND COSTS AND EXPENSES, CAUSED BY, RESULTING FROM OR ARISING OUT OF,
# IN WHOLE OR IN PART THE USE, STORAGE OR DISPOSAL OF THE SOFTWARE.
##############################################################################################################################################################################
#
#
#  The examples below were adjusted for the OSM 18 lab at BFI Chicago.
#  Simon Scheidegger, 07/18
#
##############################################################################################################################################################################

# necessary import for every use of TASMANIAN
#
import TasmanianSG
import numpy as np

# imports specifically needed by the examples
import math
from random import uniform
from datetime import datetime

print("TasmanianSG version: {0:s}".format(TasmanianSG.__version__))
print("TasmanianSG license: {0:s}".format(TasmanianSG.__license__))

grid1 = TasmanianSG.TasmanianSparseGrid()
grid2 = TasmanianSG.TasmanianSparseGrid()
grid3 = TasmanianSG.TasmanianSparseGrid()
grid4 = TasmanianSG.TasmanianSparseGrid()
grid5 = TasmanianSG.TasmanianSparseGrid()
grid6 = TasmanianSG.TasmanianSparseGrid()
grids = [grid1, grid2, grid3, grid4, grid5, grid6]
#############################################################################


c=np.array([0.3,0.5])
w=np.array([3,5])
aPnts = np.empty([1000, 2])
for iI in range(1000):
    for iJ in range(2):
        aPnts[iI][iJ] = uniform(-1.0, 1.0)
# aPnts=uniform(-1.0, 1.0,size=[1000, ])
# Result
aTres_1 = np.empty([1000, ])
aTres_2 = np.empty([1000, ])
aTres_3 = np.empty([1000, ])
aTres_4 = np.empty([1000, ])
aTres_5 = np.empty([1000, ])
aTres_6 = np.empty([1000, ])

for iI in range(1000):
    aTres_1[iI] = math.cos(2*math.pi*w[0]+c[0]*aPnts[iI,0]++c[1]*aPnts[iI,1])
    aTres_2[iI] = (c[0]**(-2)+(aPnts[iI][0]-w[0])**2)**(-1)*(c[1]**(-2)+(aPnts[iI][1]-w[1])**2)**(-1)
    aTres_3[iI] = (1+c[0]*aPnts[iI][0]+c[1]*aPnts[iI][1])**(-1)
    aTres_4[iI] = np.exp(-c[0]**2*(aPnts[iI][0]-w[0])**2-c[1]**2*(aPnts[iI][1]-w[1])**2)
    aTres_5[iI] = np.exp(-c[0]*np.absolute(aPnts[iI][0]-w[0])-c[1]*np.absolute(aPnts[iI][1]-w[1]))
    if aPnts[iI][0]>w[0] or aPnts[iI][1]>w[1]:
        aTres_6[iI] = 0
    else:
        aTres_6[iI] = np.exp(c[0]*aPnts[iI][0]+c[1]*aPnts[iI][1])

aTres_list = [aTres_1,aTres_2,aTres_3,aTres_4,aTres_5,aTres_6]
# Sparse Grid with dimension 2 and 1 output and refinement level 5
iDim = 2
iOut = 1
iDepth = 5
which_basis = 1  # 1= linear basis functions -> Check the manual for other options

print("\n-------------------------------------------------------------------------------------------------")
# print("Example 1 for OSM: interpolate f(x,y) = cos(0.5 * pi * x) * cos(0.5 * pi * y)")
# print("       using fixed sparse grid with depth {0:1d}".format(iDepth))
# print("       the error is estimated as the maximum from 1000 random points\n")

# construct sparse grid
aPoints_list = []
iNumP1_list = []
aVals_list = []
for grid in grids:
    grid.makeLocalPolynomialGrid(iDim, iOut, iDepth, which_basis, "localp")
    aPoints=grid.getPoints()
    aPoints_list.append(aPoints)
    iNumP1_list.append(aPoints.shape[0])
    aVals = np.empty([aPoints.shape[0], 1])
    aVals_list.append(aVals)


aTres_1[iI] = math.cos(2*math.pi*w[0]+c[0]*aPnts[iI][0]++c[1]*aPnts[iI][1])
aTres_2[iI] = (c[0]**(-2)+(aPnts[iI][0]-w[0])**2)**(-1)*(c[1]**(-2)+(aPnts[iI][1]-w[1])**2)**(-1)
aTres_3[iI] = (1+c[0]*aPnts[iI][0]+c[1]*aPnts[iI][1])**(-1)
aTres_4[iI] = np.exp(-c[0]**2*(aPnts[iI][0]-w[0])**2-c[1]**2*(aPnts[iI][1]-w[1])**2)
aTres_5[iI] = np.exp(-c[0]*np.absolute(aPnts[iI][0]-w[0])-c[1]*np.absolute(aPnts[iI][1]-w[1]))
if aPnts[iI][0]>w[0] or aPnts[iI][1]>w[1]:
    aTres_6[iI] = 0
else:
    aTres_6[iI] = np.exp(c[0]*aPnts[iI][0]+c[1]*aPnts[iI][1])

for iI in range(aPoints_list[0].shape[0]):
    aVals_list[0][iI] =  math.cos(2*math.pi*w[0]+c[0]*aPoints_list[0][iI][0]++c[1]*aPoints_list[0][iI][1])
    aVals_list[1][iI] =  (c[0]**(-2)+(aPoints_list[1][iI][0]-w[0])**2)**(-1)*(c[1]**(-2)+(aPoints_list[1][iI][1]-w[1])**2)**(-1)
    aVals_list[2][iI] = (1+c[0]*aPoints_list[2][iI][0]+c[1]*aPoints_list[2][iI][1])**(-1)
    aVals_list[3][iI] = np.exp(-c[0]**2*(aPoints_list[3][iI][0]-w[0])**2-c[1]**2*(aPoints_list[3][iI][1]-w[1])**2)
    aVals_list[4][iI] = np.exp(-c[0]*np.absolute(aPoints_list[4][iI][0]-w[0])-c[1]*np.absolute(aPoints_list[4][iI][1]-w[1]))
    if  aPoints_list[5][iI][0] > w[0] or  aPoints_list[5][iI][1] > w[1]:
        aVals_list[5][iI] = 0
    else:
        aVals_list[5][iI] = np.exp(c[0] * aPoints_list[5][iI][0] + c[1] * aPoints_list[5][iI][1])

aRes_list=[]
fError_list=[]
for i,grid in enumerate(grids):
    grid.loadNeededPoints(aVals_list[i])
    aRes = grid.evaluateBatch(aPnts)
    aRes_list.append(aRes)
    fError1 = max(np.fabs(aRes[:, 0] - aTres_list[i]))
    fError_list.append(fError1)
    # compute the error
    print ("/n ------------------------")
    print("for {}th function, here's the error:".format(i))
    print(" For localp  Number of points: {0:1d}   Max. Error: {1:1.16e}".format(iNumP1_list[i], fError1))

    # write coordinates of grid to a text file
    f = open("fix_sparse_grid_f{}.txt".format(i), 'a')
    np.savetxt(f, aPoints_list[i], fmt='% 2.16f')
    f.close()

# #############################################################################
#
# ## EXAMPLE 2 for OSM:
# ## interpolate: f(x,y) = exp(-x) / (1 + 100 * exp(-10 * y))
# ## using refinement
#
# aTres = np.empty([1000, ])
# for iI in range(1000):
#     aTres[iI] = math.cos(0.5 * math.pi * aPnts[iI][0]) * math.cos(0.5 * math.pi * aPnts[iI][1])
#
# # Adaptive Sparse Grid with dimension 2 and 1 output and maximum refinement level 5, refinement criterion.
# iDim = 2
# iOut = 1
# iDepth = 1
# fTol = 1.E-5
# which_basis = 1
# refinement_level = 5
#
# # level of grid before refinement
# grid1.makeLocalPolynomialGrid(iDim, iOut, iDepth, which_basis, "localp")
#
# aPoints = grid1.getPoints()
# aVals = np.empty([aPoints.shape[0], 1])
# for iI in range(aPoints.shape[0]):
#     aVals[iI] = math.cos(0.5 * math.pi * aPoints[iI][0]) * math.cos(0.5 * math.pi * aPoints[iI][1])
# grid1.loadNeededPoints(aVals)
#
# print("\n-------------------------------------------------------------------------------------------------")
# print("Example 2: interpolate f(x,y) = cos(0.5 * pi * x) * cos(0.5 * pi * y)")
# print("   the error is estimated as the maximum from 1000 random points")
# print("   tolerance is set at 1.E-5 and piecewise linear basis functions are used\n")
#
# print("               Classic refinement ")
# print(" refinement level         points     error   ")
#
# # refinement level
# for iK in range(refinement_level):
#     grid1.setSurplusRefinement(fTol, 1, "fds")  # also use fds, or other rules
#     aPoints = grid1.getNeededPoints()
#     aVals = np.empty([aPoints.shape[0], 1])
#     for iI in range(aPoints.shape[0]):
#         aVals[iI] = math.cos(0.5 * math.pi * aPoints[iI][0]) * math.cos(0.5 * math.pi * aPoints[iI][1])
#     grid1.loadNeededPoints(aVals)
#
#     aRes = grid1.evaluateBatch(aPnts)
#     fError1 = max(np.fabs(aRes[:, 0] - aTres))
#
#     print(" {0:9d} {1:9d}  {2:1.2e}".format(iK + 1, grid1.getNumPoints(), fError1))
#
# # write coordinates of grid to a text file
# f2 = open("Adaptive_sparse_grid.txt", 'a')
# np.savetxt(f2, aPoints, fmt='% 2.16f')
# f2.close()
#
# grid2 = TasmanianSG.TasmanianSparseGrid()
# grid2.makeLocalPolynomialGrid(iDim, iOut, refinement_level + iDepth, which_basis, "localp")
# a = grid2.getNumPoints()
#
# print("\n-------------------------------------------------------------------------------------------------")
# print("   a fix sparse grid of level ", refinement_level + iDepth, " would consist of ", a, " points")
# print("\n-------------------------------------------------------------------------------------------------\n")
#


