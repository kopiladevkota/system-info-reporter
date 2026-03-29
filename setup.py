from setuptools import setup, find_packages

setup(
    name="system-info-reporter",       
    version="0.1.0",                   
    packages=find_packages(),          
    install_requires=[],               
    python_requires='>=3.8',           
    author="Kopila Devkota",
    author_email="kopiladevkota7@gmail.com",
    description="A tool to report system info",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kopiladevkota/system-info-reporter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)