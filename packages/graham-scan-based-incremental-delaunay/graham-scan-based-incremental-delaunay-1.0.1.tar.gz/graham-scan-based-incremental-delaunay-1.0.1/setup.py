from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()
    
setup(
    version='1.0.1',
    name='graham-scan-based-incremental-delaunay',
    author="Carl Klier, Jimmy Zheng, Zhikai Gao",
    url='https://github.com/carlklier/graham-scan-based-incremental-delaunay',
    description="Graham-scan based incremental Delaunay triangulation algorithm with visualization.",
    long_description_content_type="text/markdown",
    install_requires=['numpy >= 1.19.0','pyglet >= 1.5.0'],
    license="MIT license",
    long_description=readme,
    packages=find_packages(),
)
