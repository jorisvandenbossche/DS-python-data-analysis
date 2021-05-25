---
layout: default
---

# Course setup

To get started, you should have the following three elements setup:

1. Install Python and the required Python packages
1. Download the course material to your computer
1. Test your configuration and installation
1. Start Jupyter lab

In the following sections, more details are provided for each of these steps. When all three are done, you are ready to start coding!


## 1. Install Python and the required Python packages

For scientific and data analysis, we recommend to use Anaconda (or Miniconda) (<https://www.anaconda.com/download/>), which provides a Python distribution that includes the scientific libraries (this recommendation applies to all platforms, so for both Windows, Linux and Mac), instead of installing Python as such. After installation, proceed with the setup.

### Install Anaconda

#### Option 1: I do not have Anaconda  installed

For first time users and people not fully confident with using the command line, we advise to install Anaconda, by downloading and installing the Python 3.x version from <https://www.anaconda.com/download/>. Recent computers will require the 64-Bit installer.

For more detailed instructions to install Anaconda, check the [Windows](https://docs.anaconda.com/anaconda/install/windows/), [Mac](https://docs.anaconda.com/anaconda/install/mac-os/) or [linux](https://docs.anaconda.com/anaconda/install/linux/) installation tutorial.

**Note:** When you are already familiar to the command line and Python environments you could opt to use Miniconda instead of Anaconda and download it from <https://conda.io/miniconda.html>. The main difference is that Anaconda provides a graphical user interface (Anaconda navigator) and a whole lot of scientific packages (e.g <https://docs.anaconda.com/anaconda/packages/py3.6_win-64/>) when installing, whereas for Miniconda the user needs to install all packages using the command line. On the other hand, Miniconda requires less disk space.

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

As not all packages we will use in the course are provided by default as part of Anaconda, we have to add the package to Anaconda to get started. As a good practice, we will create a new _conda environment_ to work with. This environment will contain the required packages on which this course depends.

The packages used in the course are enlisted in an [`environment.yml` file](https://raw.githubusercontent.com/jorisvandenbossche/DS-python-data-analysis/master/environment.yml). The file looks as follows:

```
name: DS-python-data-analysis
channels:
- defaults
- conda-forge
dependencies:
- python=3.8
- pandas=1.2
- matplotlib>3
- ipython
...
```

The file contains information on:
- `name` is the name used for the environment
- `channels` to define where to download the packages from
- `dependencies` contains each of the packages

To download the environment file, click to go to the [environment.yml](https://raw.githubusercontent.com/jorisvandenbossche/FLAMES-python-data-wrangling/master/environment.yml) online. Once opened in the browser, right-click and save the file/page on your computer. The specific text depends on your browser (`Save page as...`, `Save as...`).

__WARNING !__ Make sure you save the file as `environment.yml` instead of `environment.yml.txt` which, specifically on Windows operating system, might be the default option. To do so, choose for 'save as type' _All Files_ instead of 'Text Document'.

![](./img/environment_save.png)

You will need the folder/directory containing the `environment.yml` file in the next step. Make sure you know where you stored the file on your computer, e.g. when stored in the folder `C:/Users/yourusername/Documents` you should see the file `environment.yml` in File Explorer in that directory.

Next, start the Anaconda Navigator program (for windows users: Start > Anaconda Navigator) and go to the Environments tab. You should see the *base (root) environment*, click the arrow next to it and click `Open terminal`, as shown in the following figure:

![Navigator terminal](./img/navigator_terminal.png)

Type following commands line by line + ENTER-button (make sure you have an internet connection):

```
conda config --add channels conda-forge
conda config --set channel_priority strict
cd FOLDER_PATH_TO_ENVIRONMENT_FILE
conda env create -f environment.yml
```

__!__ `FOLDER_PATH_TO_ENVIRONMENT_FILE` should be replaced by the path to the folder containing the downloaded environment file. In the example earlier, this was `C:/Users/yourusername/Documents`, but make sure you use your specific folder (as seen in File Explorer).

Respond with *Yes* by typing `y` when asked. Output will be printed and if no error occurs, you should have the environment configured with all packages installed.

**Note:** If you did use Miniconda instead, create the environment using the same commands/instructions in the terminal (make sure to do the `conda config ...` steps.).

When finished, keep the terminal window open (or reopen it). Execute the following commands to check your installation:

```
conda activate DS-python-data-analysis
ipython
```

Within the terminal, a Python session will be started in which you can start writing Python! Type the following command:

```
import pandas
import matplotlib
```

If no message is returned, you're all set! If a message (probably an error) returned, contact the instructors. Copy paste the message returned.


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

To download the repository to your local machine as a zip-file, click the  `download ZIP` on the repository page <https://github.com/jorisvandenbossche/DS-python-data-analysis> (green button "Code"):

![Download button](./img/download-button.png)

After the download, unzip on the location you prefer within your user account (e.g. `My Documents`, not `C:\`).

__Note:__ Make sure you know where you stored the course material, e.g. `C:/Users/yourusername/Documents/DS-python-data-analysis`

## 3. Test your configuration

To check if your packages are properly installed, open the Conda Terminal again (see above) and navigate to the course directory:

```
cd FOLDER_PATH_TO_COURSE_MATERIAL
```

With `FOLDER_PATH_TO_COURSE_MATERIAL` replaced by the path to the folder with the downloaded course material (e.g. in the example it is `C:/Users/yourusername/Documents/DS-python-data-analysis`).

Activate the newly created conda environment:

```
conda activate DS-python-data-analysis
```

Run the `check_environment.py` script:

```
python check_environment.py
```

When all checkmarks are ok, you're ready to go!

## 4. Starting Jupyter Notebook with Jupyter Lab

Each of the course modules is set up as a [Jupyter notebook](http://jupyter.org/), an interactive  environment to write and run code. It it no problem if you never used jupyter notebooks before as an introduction to notebooks is part of the course.

### Option 1: Using the command line

* In the terminal, navigate to the `DS-python-data-analysis` directory (downloaded or cloned in the previous section)

* Ensure that the correct environment is activated.

  ```
  conda activate DS-python-data-analysis
  ```

* Start a jupyter notebook server by typing

  ```
  $ jupyter lab
  ```

### Option 2: Using Anaconda Navigator

In the Anaconda Navigator *Home* tab, first switch to the course environment, called `DS-python-data-analysis` in the selection bar. Next, select the Launch button under the Jupyter Lab icon:

![Navigator terminal](./img/navigator_notebook.png)

## Next?

This will open a browser window automatically. Navigate to the course directory (if not already there) and choose the `notebooks` folder to access the individual notebooks containing the course material.

If you require some rehearsal of python itself (and numpy), check the [python_recap](https://github.com/jorisvandenbossche/DS-python-data-analysis/tree/master/notebooks/python_recap) folder first, otherwise you can directly jump into the `pandas_0x_` notebooks.
