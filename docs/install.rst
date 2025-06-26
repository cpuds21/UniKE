安装
==================================

Pip
----------------------------------

1. 安装：

.. prompt:: bash

    pip install git+https://github.com/CPU-DS/UniKE.git
    uv pip install dgl
    uv sync

1. 验证:

::

    >>> import unike
    >>> unike.__version__
    '3.0.1'
    >>>

Linux
----------------------------------

1. 克隆 main 分支。

.. prompt:: bash

    git clone -b main git@github.com:CPU-DS/UniKE.git --depth 1
    cd UniKE/
    uv pip install dgl
    uv sync

1. 快速开始。

.. prompt:: bash

    cd examples/TransE/
    python single_gpu_transe_FB15K.py

Windows
----------------------------------

1. 克隆 main 分支。

.. prompt:: bash

    git clone -b main git@github.com:CPU-DS/UniKE.git --depth 1
    cd UniKE/
    uv pip install dgl
    uv sync

1. 快速开始。

.. prompt:: bash

    cd examples/TransE/
    python single_gpu_transe_FB15K.py