# DSFM Code Bank - Contributors


## Overview

The [Data Science for Managers Network](https://www.dsfm.org) open sources, under an [MIT License](LICENSE), all of code used in DSFM demos, exercises, illustrations, projects, and workshops. You may access, download, clone, and potentially contribute to these materials from the [DSFM GitHub Code Bank repository](https://github.com/dsfm-org/code-bank.git).

## Guidelines for Contibutors


### Python 3.7+

All code in the Code Bank should be harmonized to Python version 3.7, or later. Examples in R, MatLab, Stata, etc. may be included, but please then also provide a Pythonic example of the same application/results. 

### Jupyter Lab

We request that most code be written to execute, and then be presented in, a [Jupyter Lab](https://jupyter.org/) notebook. It is not required that **all** code run in a notebook, however - contibutions of code in stand-alone modules are welcome when a Jupyter notebook is not a suitable options. 

### Clean Notebooks before committing

Submissions to the Code Bank (at least to the master repo on GitHub) should have all Jupyter Notebook output and other metadata stripped out of it before committing. MetaData makes it difficult to use git `diff` to compare submissions. You can clear output by running `Edit >> Clear All Outputs` in Jupyter Lab for each and every notbook file, before committing and pushing contributions to the master repo at GitHub. 
 
### Machine & Environment

We request that you fpcus on developing code that can be executed in a "typical" Anaconda environment on a standard-sized computer. For example, most of the code developed internally by the The [Data Science for Managers Network](https://www.dsfm.org) will run on a standard instance in the Google Cloub Computing platform, with Anaconda Python installed. 

  * Unusual code / unusal modules that are more interactive can look cool, but they can also break down more and frustrate students from learning the intended concepts. If you contribute code that is more interactive or unusual, please provde two versions: a simplified version in a jupyter notebook that should always run (as-is), and the more interactive / unusual version in a secondary file (perhaps as a raw pyton `.py` file).  
  

  * When a task requires a more powerful platform to run, then we request that you document exactly what is required to run that code, and when possible provide access to a Docker container with the appropriate environment.   
  
  * Please document all requirements and request that they be added to the `REQUIREMENTS.txt` file.
