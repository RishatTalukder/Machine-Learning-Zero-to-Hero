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