from setuptools import setup, find_packages

VERSION = '0.1.4'
DESCRIPTION = 'Colemen Logging Library'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="colemenLogger",
    version=VERSION,
    author="Colemen Atwood",
    author_email="<atwoodcolemen@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    # py_modules=['ColemenLogger'],
    py_modules=['ColemenLogger', 'Colors', 'SingleLine', 'LoadingBar'],
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
# R146Racomplex3!5171Novaturient!
