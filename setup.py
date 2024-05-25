from setuptools import setup
from setuptools import find_namespace_packages

__version__ = "3.0.0"

setup(
    name="unike",
    version=__version__,
    author="LuYF-Lemon-love",
    author_email="3555028709@qq.com",
    url="https://github.com/CPU-DS/UniKE",
    description="基于 OpenKE-PyTorch 开发的知识图谱嵌入工具包",
    long_description="基于 OpenKE-PyTorch 开发的知识图谱嵌入工具包，底层数据处理利用 Python 实现。",
    extras_require={"test": "pytest"},
    zip_safe=False,
    python_requires=">=3.7",
    packages=find_namespace_packages(include=['unike*']),
    install_requires=[
        "torch",
        "pandas",
        "numpy",
        "tqdm",
        "wandb",
        "accelerate",
        "packaging",
    ],
)