# Qyrvunth, the Insane

Having a go at sentiment analysis, key phrase extraction, named entity recognition, language detection ...

Install python 3.8.x (at time of writing, x was 9)

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
    $ python3.8 -m venv qyrvunth

Activate virtual environment

    $ source qyrvunth/bin/activate

Within the virtual environment, you can use pip instead of pip3.8 and python instead of python3.8