# Machine Learning-Zero-to-Hero
This repository is for the youtube series on machine learning.

# Installation Guide

## Installing Conda

`Conda` is a package manager that simplifies the installation of Python packages and their dependencies. To install `Conda` we can use the `Anaconda` or `Miniconda` distribution.

`Anaconda` is a large distribution that includes many packages and tools from the scientific Python ecosystem. It is a good choice if you want to have a lot of packages available out of the box. But it is also quite large and can take a long time to download and install.

`Miniconda` is a smaller distribution that includes only `Conda` and its dependencies. It is a good choice if you want to have a minimal installation and install only the packages you need.

I will install `Miniconda` because it is smaller and faster to install and it gives us a lot of flexibility to install only the packages we need.

### Installing Miniconda

We can install `Miniconda` for both Windows and Linux. The installation process is similar for both operating systems.
1. Go to the [Miniconda download page](https://www.anaconda.com/docs/getting-started/miniconda/install).
2. Follow the instructions for your operating system.

For `windows`:

```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
start /wait "" .\miniconda.exe /S
del .\miniconda.exe
```
3. Follow the instructions to install `Miniconda`.
4. After the installation is complete, open the `Anaconda Prompt` and run the following command to update `Conda`:

```bash
conda init --all
```
5. Now open a new `command prompt` and run the following command to update `Conda`:

```bash
conda --version
```
6. If you see the version of `Conda`, it means that `Conda` is installed correctly.


Or you can use the `Anaconda` installer. It has a gui interface and is easier to use for beginners. You can download it from the [Anaconda download page](https://www.anaconda.com/products/distribution). Don't forget to check the box that says "Add Anaconda to my PATH environment variable" during installation.

For `Linux(Debian/Ubuntu)`:

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

3. Follow the instructions to install `Miniconda`.
4. After the installation is complete, run the following command to update `Conda`:

```bash
conda --version
```
5. After installing `Miniconda` and opening a new terminal you might see a minor change in the prompt like this:

```bash
(base) user@hostname:~$
```
This means that the `base` environment is activated by default. You can deactivate it by running the following command:

```bash
conda config --set auto_activate_base false
```
6. this will prevent the `base` environment from being activated by default. You can activate it manually by running the following command:

```bash
conda activate
```

7. To deactivate the `base` environment, you can run the following command:

```bash
conda deactivate
```

## Making a Python environment & Ready for ML

After Installation of `Conda` is complete, we can create a new Python environment. Oh! did I not mention that when you install `Conda`, it also installs Python? Yes, it does! So, activate the `base` environment and run the following command to see the default Python version:

```bash
# activate the base environment
conda activate
# check the Python version
python --version
```

It should be the latest version of `Python`. But we won't use the `base` environment for our projects. 

In conda we can install different `Python` versions and create isolated environments for that version with different packages. This is very useful for managing dependencies and avoiding conflicts between packages.

So, It's best to create a new environment where we can have all the tools and packages we need for our projects.

Let's make a new environment with the `python` version 3.11 and name it `ML_ENV`:

```bash
# create a new environment with python 3.11
conda create -n ML_ENV python=3.11
# activate the new environment
conda activate ML_ENV
```

> The syntax is `conda create -n <env_name> python=<version>` where `<env_name>` is the name of the environment and `<version>` is the version of Python you want to install and -n flag is used to specify the name of the environment.

This will make a new environment with the name `ML_ENV` and install the latest version of `Python` 3.11 in it. And we can just activate it with the command `conda activate ML_ENV` whenever we want to use it.

## setting up Jupyter Notebook

`Jupyter Notebook` is a `web-based interactive development environment` that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. It is a very popular tool for data science and machine learning.

To install `Jupyter Notebook` in our new environment, we can run the following command:

```bash
conda install jupyter
```

This will install `Jupyter Notebook` and all its dependencies in the `ML_ENV` environment. After the installation is complete, we can run the following command to start `Jupyter Notebook`:

```bash
jupyter notebook
```

This will open a new tab in your web browser with the `Jupyter Notebook` interface. You can create a new notebook by clicking on the `New` button and selecting `Python 3` from the dropdown menu.
You can also open an existing notebook by clicking on the notebook file in the file browser.

I will use jupyter notebook in `vscode` for this series. You can also use `Jupyter Notebook` in `vs code` by installing the `Jupyter` extension from the `vs code marketplace`.

And also to work with `Jupyter Notebooks` in `vscode`, also you need to have `ipykernel` installed in your environment.

```bash
conda install ipykernel
```

Now, make a file named `test.ipynb` in the root folder and open it in `vscode`. You should see the `Jupyter` interface in the editor. There will be a `kernel` selector in the top right corner of the editor. If you installed `ipykernel` in the `ML_ENV` environment, you should see the `Python 3 (ML_ENV)` kernel in the list. If you don't see it, you can select the `Python 3` kernel and then select the `ML_ENV` environment from the list of available kernels.

That's it! You are now ready to start coding in `Python` and `Jupyter Notebook` in `vscode` with the `ML_ENV` environment.

# Folder Structure of This Repository

Every topic has its own folder with the name of the topic. Inside each folder, there will be a `.ipynb` file with the code and description of the topic. If we are using external datasets, they will be in a folder named `resources` inside the topic folder.

```
.
├── README.md
├── requirements.txt
├── 1_Python_basics
│   ├── Python_basics.ipynb
│   └── resources
│       └── sample_data.csv
├── 2_Numpy
│   ├── Numpy.ipynb
│   └── resources
│       └── sample_data.csv
├── 2_Pandas
│   ├── Pandas.ipynb
│   └── resources
│       └── sample_data.csv
....

```

> requirements.txt file is used to install the required packages for the project. You can install the packages using the command `pip install -r requirements.txt` or `conda install --file requirements.txt` in the activated environment.

and done!

You can start from the `Python_basics` folder and Follow on from there. The topics are arranged in a way that you can follow along easily.

# Happy Coding!