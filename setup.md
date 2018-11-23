---
layout: default
---

# Course setup

To get started, you should have the following three elements setup:

1. Install Python and the required Python packages
2. Download the course material to your computer
3. Start Jupyter notebook

In the following sections, more details are provided for each of these steps. When all three are done, you are ready to start coding!


## Create a Python environment

Advice on Python environment...

### I do not have anaconda or miniconda installed

installeer anaconda...

### I have a working anaconda or miniconda environment...

When you have a working conda setup, you can create a new environment using the provided `environment.yml` file using the command line (or anaconda shell):

```
conda env create -f environment.yml
```

This will create a new conda environment with the name `DS-python-data-analysis`. To switch to the environment, use the following conda command:

- Linux/Mac-users: `source activate DS-python-data-analysis`
- Windows-users: `activate DS-python-data-analysis`. 

Windows users working with the *Anaconda navigator* can also import the `environment.yml` file as explained in [this tutorial](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/#importing-an-environment). 

### Test your installation

to adapt: https://github.com/glemaitre/pyparis-2018-sklearn/blob/master/check_environment.py

## Getting the course materials

### You are a git user?

As the course has been setup as a [git](https://git-scm.com/) repository managed on [Github](https://github.com/jorisvandenbossche/DS-python-data-analysis), you can clone the entire course to your local machine:

Using the command line to clone the repository and go into the course folder:

```
> git clone https://github.com/jorisvandenbossche/DS-python-data-analysis.git
> cd DS-python-data-analysis
```

In case you would prefer using Github Desktop, see [this tutorial](https://help.github.com/desktop/guides/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop/).

### You are not a git user?

To download the repository to your local machine as a zip-file, clicj the  `download ZIP` on the repository page https://github.com/jorisvandenbossche/DS-python-data-analysis (green button "Clone or download")

After the download, unzip on the location you prefer. navigate into the folder `DS-python-data-analysis`

## Starting Jupyter Notebook

Each of the course modules is setup as a [Jupyter notebook](http://jupyter.org/), an interactive  environment to write and run code. It it no problem if you never used jupyter notebooks before as an introduction to notebooks is part of the course. 

### Using the command line

* In the terminal, navigate to the `DS-python-data-analysis` directory if not there already

* Ensure that the correct environment is activated.

* Start a jupyter notebook server with

```
$ jupyter notebook
```

### Using anaconda navigator

TODO...

## next?

This will open a browser window automatically. Use the `notebooks` folder to access the notebooks containing the course material. If you require some rehearsel of python itself (and numpy), check the [python_recap](https://github.com/jorisvandenbossche/DS-python-data-analysis/tree/master/notebooks/python_recap) folder first, otherwise you can directly jump into the `pandas_0x_` notebooks.



---------

#### Create an environment with Anaconda (for [2])

(*make sure you have a working internet connection*)

Use our [environment.yml](https://github.com/jorisvandenbossche/DS-python-data-analysis/blob/master/environment.yml) file inside the course folder to set up your Python working environment

In a terminal or cmd, navigate to the `DS-python-data-analysis` folder and use the following command:

```
$ conda env create -f environment.yml
```

When the environment is installed, activate the environment inside the terminal/cmd:

* Windows-users
  ```
  $ activate DS-python-data-analysis
  ```

* Linux/Mac-users
  ```
  $ source activate DS-python-data-analysis
  ```






Authors: Joris Van den Bossche, Stijn Van Hoey

<img src="img/logo_flanders+richtingmorgen.png" width="79%"> 
<img src="img/doctoralschoolsprofiel_hq_rgb_web.png" width="20%"> 