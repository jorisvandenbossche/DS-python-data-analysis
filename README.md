# Data manipulation, analysis and visualisation in Python

## Specialist course Doctoral schools of Ghent University

For how to set up a working environment, fetch the course materials and start the notebooks, see the slides: https://jorisvandenbossche.github.io/DS-python-data-analysis/


### Requirements to run this tutorial

Look at the `environment.yml` file for all packages that need to be installed.

### Setting up a working environment

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

#### Starting a Jupyter Notebook

* In the terminal, navigate to the `DS-python-data-analysis` directory if not there already

* Ensure that the correct environment is activated.

* Start a jupyter notebook server with

  ```
  $ jupyter notebook
  ```

  This will open a browser window automatically. Use the `notebooks` folder to access the notebooks containing the course material. If you require some rehearsel of python itself (and numpy), check the [python_recap](https://github.com/jorisvandenbossche/DS-python-data-analysis/tree/master/notebooks/python_recap) folder first, otherwise you can directly jump into the `pandas_0x_` notebooks.

#### Getting the course materials

* With using git:

  First time (inside a terminal or cmd):

  ```
  $ git clone https://github.com/jorisvandenbossche/DS-python-data-analysis.git
  $ cd DS-python-data-analysis
  ```

  Updating (on second or third day):

  ```
  $ git pull
  ```

* Without git: download ZIP from https://github.com/jorisvandenbossche/DS-python-data-analysis (green button "Clone or download")


Authors: Joris Van den Bossche, Stijn Van Hoey

<img src="img/logo_flanders+richtingmorgen.png" width="79%"> 
<img src="img/doctoralschoolsprofiel_hq_rgb_web.png" width="20%"> 
