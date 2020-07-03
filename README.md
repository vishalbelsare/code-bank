# The Data Science For Managers (DSFM) Code Bank

Source:  [https://github.com/dsfm-org/code-bank.git](https://github.com/dsfm-org/code-bank.git)  
License: [MIT License](https://opensource.org/licenses/MIT).  

The __Data Science for Managers Network__ partners with leading universities and organizations around the world to provide high-quality __boot camps__, __seminars__, and __workshops__ in Data Science. We open source our demos, exercises, illustrations, projects, and workshops for use by all parties.

![DSFM Participants](images/participants.jpg)

DSFM is currently offered at two locations:

  * __Swiss Institute of Technology - EPFL__  

    Join DSFM at the École Polytechnique Fédérale de Lausanne (EPFL), part of the Swiss Federal Institute of Technology and one of the leading technical centers in Europe. EPFL is home to over 350 laboratories and research groups, each working at the forefront of science and technology.  


  * __University of Washington - GIX__

    Join DSFM at the Global Innovation Exchange (GIX) in the Seattle, Washington area. Founded by the University of Washington, Tsinghua University, and Microsoft, GIX is a global collaboration between leading academic and cross-sector partners. Courses will be presented at the state-of-the-art Steve Ballmer building in Bellevue, WA.  



## The DSFM Open Source Initiative

The [Data Science for Managers Network](https://www.dsfm.org) open sources for the creative commons, all of code used in the demos, exercises, illustrations, projects, and workshops of a participating DSFM program. Subject to the [MIT License](LICENSE), you may freely access, download, clone, reuse, and potentially collaborate on the materialsin [this repoasitory](https://github.com/dsfm-org/code-bank.git). Please see the [contributing](CONTRIBUTING.md) page for more information on how to contribute to this open source initiative.  

![Open Source Initiative](images/open-source.png)  ![Creative Commons](images/creative-commons.png)</center>


The Code Bank is organized into the following types of content:


  * __Illustrations__  

    Illustrations are short portions of programming code to demonstrate a concept covered in a lecture. Each illustration may take 5 to 10 minutes to complete. The emphasis when showing an illustrations is not on the code, syntax, or libraries used - but rather on the concepts that are being taught. When showing an illustration, the idea is to jump over the code and show the result(s) of what the code does.

  * __Demos__  

    Demonstrations cover a topic in more depth than an illustration; here, there is more emphasis on the code, syntax, and libraries that are being used. Each demo generally takes 45 to 90 minutes to complete. The emphasis in a demo is to walk the students through an extended example, going step-by-step, so they see a complete example of solving a particular problem.  

  * __Exercises__  

    Exercises require students to solve short problems on their own. Exercises do not require long logical chains to complete. The emphasis of an exercise is to push students to look through other code that they have covered elsewhere in DSFM (say in Demos and Illustrations) in order to find snippets of code that they can re-purpose to solve a new problem.

 * __Projects__  

    Projects asks students to work through an entire Data Science application. Projects do not require students to program all of it (doing so would not be feasible during the available time in boot camp courses); rather, projects focus attention on discrete portions of code to be completed, while the missing piece is embedded within a longer chain/logical progression of code. 

  * __Workshops__  

    Whereas code from the Illustrations, Demos, Exercises and Projects can be used 'a la carte' following the needs of a particular course of instruction, the coding examples and notebooks for each workshop are intended to be used in concert to cover a particular topic or application in depth.


Code appearing in the directories above are complete and ready for instruction. Code in raw development may appear in the **_alpha/** directory, and code in beta testing will appear in the **_beta/** directory.


## Installation

1. Install Python 3.7.

    Download and install [Anaconda Python 3.7](https://www.anaconda.com/download/).

2. Clone the Code Bank.

    `git clone https://github.com/dsfm-org/code-bank.git`
    
3. Install the Python [requirements](REQUIREMENTS.txt).

    `cd code-bank`
    
    `pip install -r REQUIREMENTS.txt`  


## Code Execution  

Most of the code is included in [Jupyter Lab](https://jupyter.org/) notebooks that will run (locally or remotely) through a standard web-browser. Therefore, most any kind of computer will work (even a Chromebook) provded that the back-end Jupyter Server is setup and configured with Python 3.x and [the requirements](REQUIREMENTS.txt). Some advanced examples may require a computer with additional memory, processors, GPUs/TCUs, a Spark cluster, or other resources to run - as indicated in each file. For that reason, we recommend students to use a virtual machine (VM) to run their code. We provide instructions below as to how to do so on the [Google Compute Platform](https://cloud.google.com/).


### Google Cloud

You can use the DSFM Code Bank on any computer with the requirements installed, as described above. Many students, however, prefer to use a virtual machine to run the code on a remote computer that is more powerful than their local computer. Virtual Machines may also be started, stopped, and backed-up remotely - as needed. You can use any virtual machine that can host a Jupyter Server interface; however, we typically use a VM on the Google Cloud Platform.

Follow the instructions below to setup your own virtual machine at Google. Google now also offers ready-to-go VMs for data science projects - you can use a preconfigured machine if it meets your needs. The follow instructions are helpful if you want to set up a particular type of machine for your project.

#### Step 1: Create an account.  

Start a [Google Cloud Platform](https://cloud.google.com/) (GCP) account and log into your console.

![optional caption text](images/console.png)

#### Step 2: Create a project.  

From the main dashboard, create a new GCP project.

![optional caption text](images/newproject.png)

#### Step 3: Start a virtual machine.

Create a new virtual machine (VM) by clicking on **Main Menu -> Compute Engine -> VM instances** and Create a new instance. Configure the location, hardware specifications (CPU / GPU, RAM, Hard Disk), Operating System, and other settings of the machine when you create it. The price of the machine per month is displayed on the right panel.

![optional caption text](images/vmconfig.png)

#### Step 4: Create a static IP address.

You will want to set an static external IP address for your VM so that you can always access it at that address (reserving a static IP, however, does cost more). To do so, click on the **VPC network -> External IP addresses** from the main console menu. Once you have reserved a static address, you will then need to connect it to the virtual machine "instance" that you created earlier by selecting the VM under "Attach to." 

![optional caption text](images/staticip.png)

#### Step 5: Configure the firewall.

By default, external traffic to your virtual machine will be blocked, so you will need to enable external access to your instance through port 5000 and the TCP protocol.

To enable such access, click on the **VPC network -> Firewall rules** from the main console menu, click on **Create** a firewall rule, and fill out the red parts as shown.
 
![optional caption text](images/firewallrule.png)
 
#### Step 6: Start your VM and login with SSH.

Select your machine from **Main Menu -> Compute Engine -> VM instances** and start it. Once it is up and running, you can then access the VM through an SSH terminal by clicking on the SSH option listed with the machine.

![optional caption text](images/ssh.png)

#### Step 7: Install Anaconda Python 3.7.

As your VM is probably running Linux, you may need to install Anaconda Python manually. The following instructions worked for us 
	
	apt-get update
	apt-get upgrade
	apt-get install git
	
	sudo su
	wget https://repo.continuum.io/archive/Anaconda3-5.2.0-Linux-x86_64.sh
	apt-get install bzip2
	bash Anaconda3-5.2.0-Linux-x86_64.sh
	source /root/.bashrc
	
	pip install -r requirements.txt
	
	pip install google-compute-engine --ignore-installed      # required for proper installation of gensim
	conda install -c conda-forge gensim 
	conda install -c conda-forge tensorflow                   # install before keras as default backend
	conda install -c conda-forge keras
	apt-get install graphviz                                  # needed for keras model visualization
	conda install -c conda-forge xgboost 
	conda install -c conda-forge plotly 
	conda install -c conda-forge networkx
	conda install -c conda-forge lightgbm
	conda install -c conda-forge textblob
	conda install -c conda-forge scikit-optimize
	conda install -c conda-forge scrapy
	conda install -c conda-forge nodejs
	conda install -c conda-forge pydot 
	conda install -c conda-forge basemap
	conda install -c conda-forge folium  
	conda install -c conda-forge spacy 
	conda install -c conda-forge scikit-image
	conda install -c conda-forge wordcloud
	apt-get install enchant
	pip install pyenchant
	apt-get install unzip  


### Step 8: Setup Jupyter Lab server

Convert your virtual machine to a Jupyter Lab server to access it remotely. First generate a configuration file using:

**`jupyter notebook --generate-config`**
 
Next open the configuration file with your favourite editor (e.g. *vim*):

**`vim /root/.jupyter/jupyter_notebook_config.py`**

Add the following four lines in the jupyter_notebook_config.py file:

	c = get_config()
	c.NotebookApp.ip = '*'
	c.NotebookApp.open_browser = False
	c.NotebookApp.port = 5000

![optional caption text](images/jupyterconfig.png)

Install any of the Jupyter Lab extensions that you think you will use. For example:

**`jupyter labextension install jupyterlab_bokeh`** 

Run the Jupyter Lab server using the following command:

**`jupyter lab`**

This will run a Jupyter Lab server on the earlier specified port (e.g. 5000) so you can access it remotely.

![optional caption text](images/jupyterlabserver.png)

### Step 9: Connect to your Jupyter Lab server

Copy the link printed by the console after starting the Jupyter Lab server (where it says "Login with a token:") and past it into the URL Address box on your web browser. 

![optional caption text](images/jupyterlabweb.png)

### Step 10: Clone the DSFM Code Bank

In Jupyter Lab, open a new Linux Terminal: **File -> New -> Terminal**

Then clone the repository by executing the following command into the terminal:

`git clone https://github.com/dsfm-org/code-bank.git`

------

# You are Ready to Go!
