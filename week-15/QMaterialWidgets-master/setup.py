import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="PyQt-Material-Widgets",
    version="0.9.10",
    keywords="pyqt5 material widgets",
    author="zhiyiYo",
    author_email="shokokawaii@outlook.com",
    description="A material design widgets library based on PyQt5",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="GPLv3",
    url="https://github.com/zhiyiYo/QMaterialWidgets/tree/master",
    packages=setuptools.find_packages(),
    install_requires=[
        "PyQt5>=5.15.0",
        "PyQt5-Frameless-Window>=0.2.7",
        "darkdetect",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    project_urls={
        'Documentation': 'https://qmaterialwidgets.readthedocs.io/',
        'Source Code': 'https://github.com/zhiyiYo/QMaterialWidgets/tree/master',
        'Bug Tracker': 'https://github.com/zhiyiYo/QMaterialWidgets/issues',
    }
)
