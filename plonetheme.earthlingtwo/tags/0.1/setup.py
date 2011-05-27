from setuptools import setup, find_packages
import os

setup(
    name='plonetheme.earthlingtwo',
    version='0.1',
    description='An installable Diazo theme for Plone 4.1',
    long_description=open("README.rst", "rb").read() +
                     open(os.path.join("docs", "HISTORY.txt"), "rb").read(),
    author='Andrew Mleczko',
    author_email='amleczko@redturtle.it',
    url='http://pypi.python.org/pypi/plone.earthlingtwo',
    classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python',
    ],
    keywords='web zope plone theme diazo',
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=[
        'plonetheme',
    ],
    install_requires=[
        'setuptools',
        'plone.app.theming',
    ],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
)
