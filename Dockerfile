# Docker file for Abalone age prediction project
# Every change in the dockerfile will automatically trigger the automated builds
# of the Docker image, and to tag it in the GitHub Action workflow.
# 
# Author: Chuang Wang, Huanhuan Li, Charles Suresh
# -------------------
# Date: Dec 11 2020
# -------------------

# use rocker/tidyverse as the base image
FROM rocker/tidyverse

# update existing packages
RUN apt-get update

# install `libpython3-dev` package 
RUN apt-get install -y libpython3-dev

# then install the `reticulate` package
RUN apt-get update -qq && apt-get -y --no-install-recommends install \
    && install2.r --error \
    --deps TRUE \
    reticulate

# install the anaconda distribution of python
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/conda update -n base -c defaults conda

# put anaconda python in path
ENV PATH="/opt/conda/bin:${PATH}"

# install docopt, matplotlib, scikit-learn, pandas, seaborn python package
RUN /opt/conda/bin/conda install -y -c anaconda docopt \
    matplotlib \
    pandas \
    scikit-learn>=0.23 \
    seaborn

# update all conda packages to make sure they are up-to-date
RUN /opt/conda/bin/conda update -y --all