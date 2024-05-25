安装
==================================

Pip
----------------------------------

1. 安装：

.. prompt:: bash

    pip install dgl
    pip install git+https://github.com/CPU-DS/UniKE.git

2. 验证:

::

    >>> import unike
    >>> unike.__version__
    '3.0.0'
    >>>

Linux
----------------------------------

1. 克隆 main 分支。

.. prompt:: bash

    git clone -b main git@github.com:CPU-DS/UniKE.git --depth 1
    cd UniKE/
    python -m venv env
    source env/bin/activate
    which python
    pip install --upgrade pip
    pip install dgl
    pip install . -i https://pypi.tuna.tsinghua.edu.cn/simple

2. 快速开始。

.. prompt:: bash

    cd examples/TransE/
    python single_gpu_transe_FB15K.py

Windows
----------------------------------

1. 克隆 main 分支。

.. prompt:: bash

    git clone -b main git@github.com:CPU-DS/UniKE.git --depth 1
    cd UniKE/
    py -m venv env
    .\env\Scripts\activate
    pip install --upgrade pip
    pip install dgl
    pip install . -i https://pypi.tuna.tsinghua.edu.cn/simple

2. 快速开始。

.. prompt:: bash

    cd examples/TransE/
    python single_gpu_transe_FB15K.py