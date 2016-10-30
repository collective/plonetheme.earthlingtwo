from setuptools import setup, find_packages
import os

setup(
    name='plonetheme.earthlingtwo',
    version='0.3',
    description='An installable Diazo theme for earthlingtwo Theme at Plone 4.x',
    long_description=open("README.rst", "rb").read() +
                     open(os.path.join("docs", "HISTORY.txt"), "rb").read(),
    # Get more strings from
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='web zope plone theme diazo',
    author='Andrew Mleczko',
    author_email='amleczko@redturtle.it',
    url='http://pypi.python.org/pypi/plonetheme.earthlingtwo',
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
