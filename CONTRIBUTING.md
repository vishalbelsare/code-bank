# DSFM Code Bank - Guidelines for Contributors

 

## Overview

The [Data Science for Managers Network](https://www.dsfm.org) open sources, under an [MIT License](LICENSE), all of code used in the demos, exercises, illustrations, projects, and workshops of DSFM. You may access, download, clone, and contribute to these materials at [https://github.com/dsfm-org/code-bank.git](https://github.com/dsfm-org/code-bank.git).

If you find the DSFM Code Bank useful, please contribute. If you do, please follow these guidelines:

## Configuration


### Anaconda Python 3.7+

All code in the Code Bank should be harmonized to Python version 3.7, or later. Examples in R, MatLab, Stata, etc. may be included, but please try to provide a Pythonic example of the same application and results. 

### Jupyter Lab Notebooks

We request that most code be written to execute, and then be presented in, a [Jupyter Lab](https://jupyter.org/) notebook. It is not required that **all** code run in a notebook, however - contibutions of code in stand-alone modules are welcome when a Jupyter notebook is not a suitable options. 

### Machine

We request that you fpcus on developing code that can be executed on a standard-sized computer. For example, most of the code developed internally by the The [Data Science for Managers Network](https://www.dsfm.org) will run on a standard instance in the Google Cloub Computing platform, with Anaconda Python installed. 

If a Code Bank item does require a more powerful platform to execute, then please be sure to document exactly what is required to run the code.   
  
### Environment

Try to use standard libraries with a proven track-record. Cutting-edge or interactive modules can look cool, but they can also have hidden dependencies and/or break down more often - and then frustrate students. 

If you do contribute code that is more interactive or unusual, please provde two versions: a simplified version in a jupyter notebook that should always run (as-is), and the more interactive / unusual version in a secondary file (perhaps as a raw pyton `.py` file).  

If a contribution requires a particularly unusual environment, then consider developing and providing access to a pre-configured __Docker Container__ to host it. Containers can then be hosted at DockerHub (or elsewhere) with instructions as to how to access it.

### Encapsulated Directories

All contributions to the Code Bank should be bundled together into one directory: 

  * Include a copy of the DSFM Code Bank License in the directory.
  
  * Include a subdirectory called data/ with all of your required data (or include code to fetch your data as needed from with your notebook).   
  
  * Include a `requirements.txt` file with all of the Python modules required by your program. Requirements should auto-install with `pip install` - or otherwise prepare detailed instructions at the top of your notebook to explain how to setup the environment. We will merge your requirements into a global `REQUIREMENTS.txt` file for the Code Bank overall.


## Collaboration by Git

All contributions to the Code Bank must be made by `git` through GitHub.com:

  * The DSFM Network adminsitrator will maintain the MASTER repo for the Code Bank. No one else can push to the master.   
  
  * Contributors should fork the [Code Bank](https://github.com/dsfm-org/code-bank.git), make changes or additions to their copy, and then submit a Pull Request to the master repo.  
  
  * Please start a __new__ contribution by adding a new directory underneath the appropriate subdirectory of  _beta_testing/ .  For example, you might suggest adding a new illustration by developing it and adding it to:  _beta/illustrations/cool-example/ 
  
    * The main distribution directories ( demos/ ,  exercises/ ,  illustrations/  ,  projects/ , workshops/ ,  etc...) are for materials that are fully tested and ready for instruction.  
    
    * Please do not try to add new files directly into a primary distribution directory (  demos/ ,   exercises/ ,  illustrations/  ,  projects/ ,  workshops/ ,  etc...) 

    * An accepted contribution will appear in the appropriate  _beta_testing/  subdirectory until it is fully tested by the DSFM community.  

  * You may also make suggested changes to existing notebooks and files in the released
  
  * __Please clean your notebook before submitting a pull request__: Submissions of a pull request should strip out all Jupyter Notebook output and other metadata. MetaData makes it difficult to use git `diff` to compare submissions. You can clear output by running `Edit >> Clear All Outputs` in Jupyter Lab. 
 
