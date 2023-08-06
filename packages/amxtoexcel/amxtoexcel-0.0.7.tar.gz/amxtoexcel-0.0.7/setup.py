import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amxtoexcel", # Replace with your own username
    version="0.0.7",
    author="Logan Vaughn",
    # author_email="logantv@gmail.com",
    description="amx dict list to xlsx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/logantv/amxtoexcel",
    project_urls={
        "Bug Tracker": "https://github.com/logantv/amxtoexcel/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'openpyxl',
        'pandas'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
