# Qyrvunth, the Insane

Having a go at sentiment analysis, key phrase extraction, named entity recognition, language detection ...

## Installation

Debian 10 includes Python version 3.7. Python 3.8, the latest major release, is not available in the standard Debian 10 repositories yet.

[Download python 3.8.x](https://www.python.org/downloads/source/) (at time of writing, x was 9)

    $ curl -O https://www.python.org/ftp/python/3.8.9/Python-3.8.9.tar.xz

Unpack

    $ tar -xf Python-3.8.9.tar.xz

Configure

    $ cd Python-3.8.2
    $ ./configure --enable-optimizations

Make altinstall (to not overwrite the default system python3 binary) 

    $ nproc
    4
    $ make -j 4
    $ sudo make altinstall

Verify

    $ python3.8 --version
    Python 3.8.9

Set up virtual environment

    $ cd qyrvunth/
    $ virtualenv -p /usr/local/bin/python3.8 venv

Activate virtual environment

    $ source venv/bin/activate

Install pip in venv

    $ pip install requests
    $ python -m pip install --upgrade pip


Install nltk and numpy

    $ pip install nltk
    $ pip install numpy

Test by downloading the nltk [datasets](http://www.nltk.org/data.html)

    $ python -m nltk.downloader all