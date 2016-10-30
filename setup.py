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
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    keywords='web zope plone theme diazo',
    author='Andrew Mleczko',
    author_email='amleczko@redturtle.it',
    url='http://pypi.python.org/pypi/plonetheme.earthlingtwo',
    license='GPL',
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
