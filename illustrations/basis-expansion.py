""" DSFM Illustration: Basis expansion
    -------------------------------------------------------------------------------------------------
    
    Creator: Data Science for Managers - EPFL Program - https://www.dsfm.ch
    Source:  https://github.com/dsfm-org/code-bank.git
    License: MIT License (https://opensource.org/licenses/MIT) - see LICENSE in Code Bank repository. 
    
    OVERVIEW:
    
    The following module executes the same illustration as the basis-expansion notebook, 
    but allows for interactive rotation of the graphs.

"""

# Import all packages 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
from mpl_toolkits.mplot3d import axes3d

# Special code to ignore un-important warnings 
import warnings
warnings.filterwarnings('ignore')


# In[2]:


# define all constant
STD            = 0.30
N              = 100
FIGSIZE        = (10, 10)
FONTSIZE       = 16
PLOT_X1_LABEL  = '\nNo A                              Yes A'
PLOT_X2_LABEL  = '\nNo B                              Yes B'
LOCATION       = 1
PLOT_MIN       = -2.0
PLOT_MAX       = 2.0
PLOT_ALPHA     = 0.3
PLOT_CMAP      = cm.winter
PLOT_LINES     = 0
PLOT_HIDE_GRID = False


# ## **Part 1**: Basis function expansion and SVM to solve XOR problem
# 
# This demo shows how a Support Vector Machine (SVM) can use a non-linear basis function expansion to warp the feature space in order to get it into a better shape for cutting it with a hyper-plane.
# 
# This demo does NOT show how a SVM actually uses it's optimization procedure to find the maximal cutting hyperplane (because the data is already evenly and symmetrically separated around the orgin, we can simply put the plane at the origin.
# 
# Note: 3D-rendering only works in Python scripts.

# In[3]:


# Generate data -------------------------------------------------------------------------------
x1_Yes_A = np.random.normal(loc=      LOCATION, scale=STD, size=N)
x2_Yes_A = np.random.normal(loc= -1 * LOCATION, scale=STD, size=N)
x1_Yes_B = np.random.normal(loc= -1 * LOCATION, scale=STD, size=N)
x2_Yes_B = np.random.normal(loc=      LOCATION, scale=STD, size=N)
x1_No_A  = np.random.normal(loc= -1 * LOCATION, scale=STD, size=N)
x2_No_A  = np.random.normal(loc= -1 * LOCATION, scale=STD, size=N)
x1_No_B  = np.random.normal(loc= -1 * LOCATION, scale=STD, size=N)
x2_No_B  = np.random.normal(loc= -1 * LOCATION, scale=STD, size=N)


# Plot the data in 2-D  ------------------------------------------------------------------------
fig = plt.figure(1, figsize=FIGSIZE)
ax = fig.add_subplot(111)

ax.set_title('Fuzzy XOR Data in 2 Dimensions\n', fontsize = FONTSIZE)
ax.tick_params(axis='both', which='major', labelsize=FONTSIZE)
ax.set_xlabel(PLOT_X1_LABEL, fontsize = FONTSIZE)
ax.set_ylabel(PLOT_X2_LABEL, fontsize = FONTSIZE)
plt.hlines(0, xmin = min(x1_No_A), xmax = max(x1_Yes_A), colors='black', linewidth=1)
plt.vlines(0, ymin = min(x2_No_B), ymax = max(x2_Yes_B), colors='black', linewidth=1)
plt.plot(x1_No_A,  x2_No_A,  c='red',   marker='x', linestyle='None', markersize=10)
plt.plot(x1_Yes_A, x2_Yes_B, c='red',   marker='x', linestyle='None', markersize=10)
plt.plot(x1_Yes_A, x2_Yes_A, c='green', marker='o', linestyle='None', markersize=10)
plt.plot(x1_Yes_B, x2_Yes_B, c='green', marker='o', linestyle='None', markersize=10)
plt.show()


# In[4]:


# Plot a hyperbolic surface to show a workable transformation  ---------------------------------

x                   = np.arange(PLOT_MIN, PLOT_MAX, 0.05)
y                   = np.arange(PLOT_MIN, PLOT_MAX, 0.05)
x, y                = np.meshgrid(x, y)
surface_hyperbolic  = -(x * y)
fig = plt.figure(2, figsize=FIGSIZE)
ax = fig.add_subplot(111, projection='3d')
ax.tick_params(axis='both', which='major', labelsize=FONTSIZE)
ax.set_title('Hyperbolic Transformation\n', fontsize=FONTSIZE)
ax.plot_surface(x, y, surface_hyperbolic, cmap=PLOT_CMAP, alpha=PLOT_ALPHA, linewidth=PLOT_LINES, antialiased=PLOT_HIDE_GRID)
ax.contour(x, y, surface_hyperbolic, cmap=PLOT_CMAP, )
plt.show()


# In[5]:


# Plot other surfaces (that do NOT work but are interesting) ------------------------------------

# /////// Quadratic surface
surface_quadratic = x ** 2 * y ** 2
fig = plt.figure(3, figsize=FIGSIZE)
ax = fig.add_subplot(111, projection='3d')
ax.tick_params(axis='both', which='major', labelsize=FONTSIZE)
ax.set_title('Quadratic Transformation\n', fontsize=FONTSIZE)
ax.plot_surface(x, y, surface_quadratic, cmap=PLOT_CMAP, alpha=PLOT_ALPHA, linewidth=PLOT_LINES, antialiased=PLOT_HIDE_GRID)
ax.contour(x, y, surface_quadratic, cmap=PLOT_CMAP)
ax.axis([PLOT_MIN, PLOT_MAX, PLOT_MIN, PLOT_MAX])
ax.set_zlim([0.0, 4.0 * LOCATION])
plt.show()


# In[6]:


# /////// Mexican-hat surface
surface_mexican = np.cos((x ** 2 + y ** 2) ** .5) ** 2
fig = plt.figure(4, figsize=FIGSIZE)
ax = fig.add_subplot(111, projection='3d')
ax.tick_params(axis='both', which='major', labelsize=FONTSIZE)
ax.set_title('Mexican-Hat Transformation\n', fontsize=FONTSIZE)
ax.plot_surface(x, y, surface_mexican, cmap=PLOT_CMAP, alpha=PLOT_ALPHA, linewidth=PLOT_LINES, antialiased=PLOT_HIDE_GRID)
ax.contour(x, y, surface_mexican, cmap=PLOT_CMAP)
ax.axis([PLOT_MIN, PLOT_MAX, PLOT_MIN, PLOT_MAX])
ax.set_zlim([0.0, 1.0 * LOCATION])
plt.show()


# In[7]:


# /////// Egg-carton surface
surface_eggs = np.cos(2 * x) * np.sin(3 * y)
fig = plt.figure(5, figsize=FIGSIZE)
ax = fig.add_subplot(111, projection='3d')
ax.tick_params(axis='both', which='major', labelsize=FONTSIZE)
ax.set_title('Peak Transformation\n', fontsize=FONTSIZE)
ax.plot_surface(x, y, surface_eggs, cmap=PLOT_CMAP, alpha=PLOT_ALPHA, linewidth=PLOT_LINES, antialiased=PLOT_HIDE_GRID)
ax.contour(x, y, surface_eggs, cmap=PLOT_CMAP)
ax.axis([PLOT_MIN, PLOT_MAX, PLOT_MIN, PLOT_MAX])
ax.set_zlim([-LOCATION, LOCATION])
plt.show()


# In[8]:


# Project data onto hyperbolic surface  -------------------------------------------------------
y_success_by_a        =  -(x1_Yes_A * x2_No_B)
y_success_by_b        =  -(x1_No_A * x2_Yes_B)
y_failure_by_inaction =  -(x1_No_A * x2_No_A)
y_failure_by_conflict =  -(x1_Yes_A * x2_Yes_B)


# Plot projected data in 3-D  -----------------------------------------------------------------
fig = plt.figure(6, figsize=FIGSIZE)
ax = fig.add_subplot(111, projection='3d')
ax.tick_params(axis='both', which='major', labelsize=FONTSIZE)
ax.set_xlabel(PLOT_X1_LABEL, fontsize = FONTSIZE)
ax.set_ylabel(PLOT_X2_LABEL, fontsize = FONTSIZE)
ax.axis([PLOT_MIN, PLOT_MAX, PLOT_MIN, PLOT_MAX])
ax.set_zlim([PLOT_MIN, PLOT_MAX])
ax.plot_surface(x, y, surface_hyperbolic, cmap=PLOT_CMAP, alpha=PLOT_ALPHA, linewidth=PLOT_LINES, antialiased=PLOT_HIDE_GRID)
ax.contour(x, y, surface_hyperbolic, cmap=PLOT_CMAP, )
ax.scatter(x1_No_A, x2_No_B, y_failure_by_inaction, c='red', marker='x', linestyle='None')
ax.scatter(x1_Yes_A, x2_Yes_B, y_failure_by_conflict, c='red', marker='x', linestyle='None')
ax.scatter(x1_Yes_A, x2_No_B, y_success_by_a, c='green', marker='o', linestyle='None')
ax.scatter(x1_No_A, x2_Yes_B, y_success_by_b, c='green', marker='o', linestyle='None')
plt.show()


# In[9]:


# Plot 3-D solution (data + a splitting plane) ------------------------------------------------
cutting_plane = 0.0 * x
fig = plt.figure(7, figsize=FIGSIZE)
ax = fig.add_subplot(111, projection='3d')
ax.tick_params(axis='both', which='major', labelsize=FONTSIZE)
ax.set_xlabel(PLOT_X1_LABEL, fontsize = FONTSIZE)
ax.set_ylabel(PLOT_X2_LABEL, fontsize = FONTSIZE)
ax.axis([PLOT_MIN, PLOT_MAX, PLOT_MIN, PLOT_MAX])
ax.set_zlim([PLOT_MIN, PLOT_MAX])
ax.plot_surface(x, y, surface_hyperbolic, cmap=PLOT_CMAP, alpha=PLOT_ALPHA, linewidth=PLOT_LINES, antialiased=PLOT_HIDE_GRID)
ax.contour(x, y, surface_hyperbolic, cmap=PLOT_CMAP, )
ax.scatter(x1_No_A, x2_No_A, -(x1_No_A * x2_No_A), c='red', marker='x', linestyle='None')
ax.scatter(x1_Yes_A, x2_Yes_B, -(x1_Yes_A * x2_Yes_B), c='red', marker='x', linestyle='None')
ax.scatter(x1_Yes_A, x2_No_B, -(x1_Yes_A * x2_No_B), c='green', marker='o', linestyle='None')
ax.scatter(x1_No_A, x2_Yes_B, -(x1_No_A * x2_Yes_B), c='green', marker='o', linestyle='None')
ax.plot_surface(x, y, cutting_plane, alpha=PLOT_ALPHA, linewidth=PLOT_LINES, antialiased=PLOT_HIDE_GRID)
plt.show()


# In[ ]:




