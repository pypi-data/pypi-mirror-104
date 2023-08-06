# borch

[![pipeline status](https://gitlab.com/desupervised/borch/badges/master/pipeline.svg)](https://gitlab.com/desupervised/borch/-/commits/master)
[![coverage report](https://gitlab.com/desupervised/borch/badges/master/coverage.svg)](https://gitlab.com/desupervised/borch/-/commits/master)
[![lifecycle](https://img.shields.io/badge/lifecycle-maturing-blue?style=flat&link=https://lifecycle.r-lib.org/articles/stages.html)](https://lifecycle.r-lib.org/articles/stages.html)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![docs](https://img.shields.io/badge/docs-latest-green?style=flat&link=https://borch.readthedocs.io/en/latest/)](https://borch.readthedocs.io/en/latest/)

borch is an artificial intelligence (AI) framework developed by Desupervised.
It's designed to be flexible and scalable framework that can solve problems
using artificial intelligence and machine learning. Doing so by utilizing a wide
ranging toolbox including Bayesian inference, ....

It consists of several sub packages:

- `infer`: An inference package with support for Bayesian inference methods such
  as Variational Inference (VI), Markov Chain Monte Carlo (MCMC) as well as
  tools for semi-supervised training and many others.
- `utils`: various utility functions

## Usage

Run `make help` to see available make targets.

## Installation

### Virtual environment

When installing borch we normally use virtual environment to manage the Python
version dependencies. Two good ones are https://virtualenv.pypa.io/en/stable/
and https://docs.conda.io/en/latest/miniconda.html, look at them and pick one to
use and follow their documentation to crate and activate an environment.

**NB** All installations of python packages should be placed in the correct
environment. Installing packages in the global python interpreter can result in
unexpected behavior, where global packages may be used in favor of local
packages.

### Install locally

Once an appropriate conda environment has been created, run

```
make install
```

to install a production version of borch with support for a GPU, or

```
ARCH=cpu make install
```

for a version that only supports a CPU.

To install in development mode on machine(with no gpu support) run, and all
development dependencies.

```
ARCH=cpu make install-dev
```

and for GPU support use

```
make install-dev
```

## Docker

Currently, all borch docker images are based on Ubuntu 16.04. The GPU image is
based on an Nvidia Cuda version. Both base images are specified as build
arguments which calling `docker build`.

The GPU image can be built using:

```
docker build --build-arg BASE="nvidia/cuda:9.1-cudnn7-runtime-ubuntu16.04" --build-arg ARCH=gpu  --pull -t borch-gpu .
```

And the CPU image using:

```
docker build --build-arg BASE="ubuntu:18.04" --build-arg ARCH=cpu  --pull -t borch-cpu .
```

## Contributing

Please read the contribution guidelines in `CONTRIBUTING.md`.

## Citation

If you use this software for your research or business please cite us and help
the package grow!

```text
@misc{borch,
  author = {Belcher, Lewis and Gudmundsson, Johan and Green, Michael},
  title = {Borch},
  howpublished = {https://gitlab.com/desupervised/borch},
  month        = "Apr",
  year         = "2021",
  note         = "v0.1.0",
  annote       = ""
}
```
