"""Setup file"""

import pathlib

from setuptools import find_packages, setup

from deepchain.version import VERSION

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


req = [
    "numpy>=1.16",
    "requests>=2.23.0",
    "torch==1.5.0",
    "tensorflow==2.3.0",
    "fair-esm==0.3.1",
    "scikit-learn>=0.22.0",
    "pandas>=1.2.3",
    "tqdm>=4.60.0",
    "pytorch_lightning>=1.2.6",
    "transformers>=4.5.1",
    "bio-transformers>=0.0.1",
]


def make_install():
    """main install function"""
    setup_fn = setup(
        name="deepchain-apps",
        license="Apache-2.0",
        version=VERSION,
        description="Define a personnal app for the user of DeepChain.bio",
        author="Instadeep",
        long_description=README,
        long_description_content_type="text/markdown",
        author_email="a.delfosse@instadeep.com",
        packages=find_packages(exclude=["test"]),
        entry_points={
            "console_scripts": ["deepchain=deepchain.cli.deepchain_cli:main"],
        },
        classifiers=[
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.7",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Scientific/Engineering :: Bio-Informatics",
            "Topic :: Software Development",
        ],
        install_requires=req,
        include_package_data=True,
        zip_safe=False,
        python_requires=">=3.7",
    )

    return setup_fn


if __name__ == "__main__":
    make_install()
