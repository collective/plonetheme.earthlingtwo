from setuptools import setup, find_packages
import os

setup(
    name='plonetheme.earthlingtwo',
    version='0.3',
    description='Earthlingtwo, is an installable Diazo theme for Plone 4',
    long_description=open("README.rst", "rb").read() +
                     open(os.path.join("docs", "HISTORY.txt"), "rb").read(),
    # Get more strings from
    # https://pypi.org/pypi?:action=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: Theme',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='web zope plone theme diazo earthlingtwo',
    author='Andrew Mleczko',
    author_email='amleczko@redturtle.it',
    maintainer='Leonardo Caballero',
    maintainer_email='leonardocaballero@gmail.com',
    url='https://github.com/collective/plonetheme.earthlingtwo',
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
