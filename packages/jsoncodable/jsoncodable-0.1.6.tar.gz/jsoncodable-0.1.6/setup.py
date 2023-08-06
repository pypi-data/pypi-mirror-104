import setuptools, os

readme_path = os.path.join(os.getcwd(), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r") as f:
        long_description = f.read()
else:
    long_description = 'jsoncodable'

setuptools.setup(
    name="jsoncodable",
    version="0.1.6",
    author="Kristof",
    description="to_dict",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/py_jsoncodable",
    packages=setuptools.find_packages(),
    install_requires=[
        'jsonpickle>=2.0.0',
        'noraise>=0.0.16'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)