=======================
plonetheme.earthlingtwo
=======================


Introduction
============

*plonetheme.earthlingtwo* package is an installable Plone_ Theme using the **theming** and **packaging** 
features available in `plone.app.theming`_  make the `TEMPLATED (CSS Templates)`_ theme `earthlingtwo`_ easily
available in `Plone`.

*Earthlingtwo*: is a remake of an older template (Earthling). Bigger, better, and way more nature. Posted on September 16, 2009 in CSS Templates.


Examples
========

This `Earthlingtwo` theme distribute in this add-on can be seen in action at the following site:

* https://templated.co/earthlingtwo


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Features
========

- It's an installable Plone_ Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- Also it's a simple Diazo_ package (Zip file).
- It's have support for clean uninstallation.


Installation
============


Add Plone site
--------------

Install Plone 4.x with `plone.app.theming`_ and create a Plone site (if you have not already)
with Diazo theming configured.

.. image:: https://github.com/collective/plonetheme.earthlingtwo/raw/master/screenshot0.png
  :width: 1024px
  :alt: Create a Plone site from ZMI
  :align: center


Zip file
--------

If you are an **end user**, you might enjoy installation via zip file import.

1. Download a `zip file <https://raw.github.com/collective/plonetheme.earthlingtwo/master/earthlingtwo.zip>`_.
2. Import the theme from the Diazo theme control panel.

.. image:: https://github.com/collective/plonetheme.earthlingtwo/raw/master/screenshot1.png
  :width: 1024px
  :alt: Import the Diazo theme zip file
  :align: center


Buildout
--------

If you are a **developer user**, you might enjoy installing it via buildout.

For install ``plonetheme.earthlingtwo`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.earthlingtwo


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.earthlingtwo',
    ],


Enabling the theme
^^^^^^^^^^^^^^^^^^

Browse to ``http://yoursite/Plone/@@theming-controlpanel`` click on ``Enable`` 
on ``Earthling2`` theme from the Diazo control panel.

.. image:: https://github.com/collective/plonetheme.earthlingtwo/raw/master/screenshot2.png
  :width: 1024px
  :alt: For select the Diazo theme just click on Activate button
  :align: center

That's it!

You should see the layout of the site when viewed in a computer resolution:

.. image:: https://raw.githubusercontent.com/collective/plonetheme.earthlingtwo/master/plonetheme/earthlingtwo/theme/earthlingtwo/preview.png
    :align: center


Help
====

Obviously there is more work to be done. If you want to help, pull requests accepted! Some ideas:

* Add a diazo rule to import Plone editing styles
* Configure styles to use portal_css
* Add quick installer support
* Improve styles 


Contribute
==========

* Issue Tracker: https://github.com/collective/plonetheme.earthlingtwo/issues

* Source Code: https://github.com/collective/plonetheme.earthlingtwo

* Wiki: https://github.com/collective/plonetheme.earthlingtwo/wiki


Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.net/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/


Collaborations
--------------

* Andrew Mleczko (amleczko at redturtle dot it).

* Leonardo J. Caballero G. (leonardocaballero at gmail dot com).

* Full Name aka nickname

For an updated list of all the contributors visit: https://github.com/collective/plonetheme.earthlingtwo/graphs/contributors


Support
=======

If you are having issues, please let us know via `our Issue Tracker`_.


License
=======

The author is not a "license guy", but the earthlingtwo theme is distributed via CC 3.0 license [1]_ and this package is GPL version 2 (assuming that makes sense).

.. [1] https://templated.co/license

.. _`TEMPLATED (CSS Templates)`: https://templated.co/
.. _`earthlingtwo`: https://templated.co/earthlingtwo
.. _`Plone`: http://plone.org
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`Diazo`: http://diazo.org
.. _`our Issue Tracker`: https://github.com/collective/plonetheme.earthlingtwo/issues
