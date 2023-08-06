from setuptools import setup, find_packages

setup(
    name='Pforests-dtw',
    version='1.3',
    author='Moradisten',
    author_email='moradabaz@gmail.com',
    url='https://github.com/moradisten/ProximityForests-python',
    description="Proximity Forest Classifier using DTW distance measure",
    keywords ='time series classification',
    python_requires='>=3.6',
    install_requires=['numpy', 'dtaidistance', 'pytest', 'scipy'],
    packages=find_packages()
)
