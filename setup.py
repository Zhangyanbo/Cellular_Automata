import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CA",
    version="1.0.0",
    author="Yanbo Zhang",
    author_email="Zhang.Yanbo@asu.edu",
    description="A package for implementing cellular automata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zhangyanbo/Cellular_Automata",
    project_urls={
        "Bug Tracker": "https://github.com/Zhangyanbo/Cellular_Automata/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['CA'],
    python_requires=">=3.6",
)