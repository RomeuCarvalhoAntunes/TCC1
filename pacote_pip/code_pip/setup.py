import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="html-accessibility-tests-Romeu-Antunes", # Replace with your own username
    version="0.0.1",
    author="Romeu Carvalho Antunes",
    author_email="romeu.antunes@outlook.com",
    description="Automation of accessibility tests for html",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RomeuCarvalhoAntunes/TCC1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)