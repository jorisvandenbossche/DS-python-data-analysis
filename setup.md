---
layout: default
---

# Course setup

To get started, you should have the following three elements setup:

1. Install Python and the required Python packages
2. Download the course material to your computer
3. Start Jupyter notebook

In the following sections, more details are provided for each of these steps. When all three are done, you are ready to start coding!


## 1. Install Python and the required Python packages

For scientific and data analysis, we recommend to use Anaconda (or Miniconda) (<https://www.anaconda.com/download/>), which provide a Python distribution that includes the scientific libraries (this recommendation applies to all platforms, so for both Window, Linux and Mac), instead of installing Python as such. After installation, proceed with the setup.

### Install Anaconda

#### Option 1: I do not have Anaconda  installed

For first time users and people not fully confident with using the command line, we advice to install Anaconda, by downloading and installing the Python 3.x version from <https://www.anaconda.com/download/>. Recent computers will require the 64-Bit installer.

For more detailed instructions to install Anaconda, check the [Windows](https://docs.anaconda.com/anaconda/install/windows/), [Mac](https://docs.anaconda.com/anaconda/install/mac-os/) or [linux](https://docs.anaconda.com/anaconda/install/linux/) installation tutorial.

**Note:** When you are already familiar to the command line and Python environments you could opt to use Miniconda instead of Anaconda and download it  from <https://conda.io/miniconda.html>. The main difference is that Anaconda provides a graphical user interface (Anaconda navigator) and a whole lot of scientific packages (e.g <https://docs.anaconda.com/anaconda/packages/py3.6_win-64/>) when installing, whereas for Miniconda the user needs to install all packages using the command line. On the other hand, Miniconda requires less disc space. By choosing Miniconda, create the lesson environment using the [environment file](https://github.com/jorisvandenbossche/DS-python-data-analysis/blob/master/environment.yml): `conda env create -f environment.yml`

#### Option 2: I have installed Anaconda  earlier

When you already have an installation of Anaconda, you have to make sure you are working with the most recent versions. As the course is developed for Python 3, make sure you have Anaconda3 (on Windows, check Start > Programs > Anaconda3). If not, reinstall Anaconda according to the previous section.

Start the Anaconda Navigator program (for Windows users: Start > Anaconda Navigator) and go to the Environments tab. You should see the *base (root) environment*, click the arrow next to it and click `Open terminal`, as shown in the following figure:

![Navigator terminal](./img/navigator_terminal.png)

Type following command + ENTER-button (make sure you have an internet connection):

```
conda update -n root conda
```

when finished, type (+ ENTER-button):

```
conda update --all
```

and respond with *Yes* by typing `y`. Packages should be updated after the completion of the command.

### Setup after installation

As the `plotnine` package we will use in the course is not provided by default as part of Anaconda, we have to add the package to Anaconda to get started. Start the Anaconda Navigator program (for windows users: Start > Anaconda Navigator) and go to the Environments tab. You should see the *base (root) environment*, click the arrow next to it and click `Open terminal`, as shown in the following figure:

![Navigator terminal](./img/navigator_terminal.png)

Type following command + ENTER-button (make sure you have an internet connection):

```
conda install -c conda-forge plotnine
```

and respond with *Yes* by typing `y`. Output will be printed and if no error occurs, you should have the plotnine package installed.

**Note:** This can be done as well using the interface of Anaconda Navigator, adding `conda-forge` as channel according to [this tutorial](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-channels/#adding-a-channel) and adding the `plotnine` package using [this tutorial](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-packages/#installing-a-package).


## 2. Getting the course materials

### Option 1: You are a git user?

As the course has been setup as a [git](https://git-scm.com/) repository managed on [Github](https://github.com/jorisvandenbossche/DS-python-data-analysis), you can clone the entire course to your local machine:

Use the command line to clone the repository and go into the course folder:

```
> git clone https://github.com/jorisvandenbossche/DS-python-data-analysis.git
> cd DS-python-data-analysis
```

In case you would prefer using Github Desktop, see [this tutorial](https://help.github.com/desktop/guides/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop/).

### Option 2: You are not a git user?

To download the repository to your local machine as a zip-file, click the  `download ZIP` on the repository page <https://github.com/jorisvandenbossche/DS-python-data-analysis> (green button "Clone or download"):

![Download button](./img/download-button.png)

After the download, unzip on the location you prefer within your user account (e.g. `My Documents`, not `C:\`).

### Test your installation

To check if your packages are properly installed, open the Terminal again and navigate to the course directory (see above). Run the `check_environment.py` script:

```
python check_environment.py
```

When all is green, you're ready to go!


## 3. Starting Jupyter Notebook

Each of the course modules is setup as a [Jupyter notebook](http://jupyter.org/), an interactive  environment to write and run code. It it no problem if you never used jupyter notebooks before as an introduction to notebooks is part of the course.

### Option 1: Using the command line

* In the terminal, navigate to the `DS-python-data-analysis` directory (downloaded or cloned in the previous section)

* Ensure that the correct environment is activated.

* Start a jupyter notebook server by typing

  ```
  $ jupyter notebook
  ```

### Option 2: Using Anaconda Navigator

In the Anaconda Navigator *Home* tab, select the Launch button under the Jupyter notebook icon:

![Navigator terminal](./img/navigator_notebook.png)

## Next?

This will open a browser window automatically. Navigate to the course directory (if not already there) and choose the `notebooks` folder to access the individual notebooks containing the course material. If you require some rehearsel of python itself (and numpy), check the [python_recap](https://github.com/jorisvandenbossche/DS-python-data-analysis/tree/master/notebooks/python_recap) folder first, otherwise you can directly jump into the `pandas_0x_` notebooks.