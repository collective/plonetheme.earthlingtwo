plonetheme.earthlingtwo
=======================


Introduction
------------

The ``plonetheme.earthlingtwo`` package uses the **theming** and **packaging** features
available in `plone.app.theming`_ to make the `TEMPLATED (CSS Templates)`_ theme `earthlingtwo`_ easily
available in Plone 4.x version.

.. image:: https://raw.github.com/collective/plonetheme.earthlingtwo/master/screenshot01.png
   :alt: A plonetheme.earthlingtwo product theme screenshot

*Earthlingtwo*: is a remake of an older template (Earthling). Bigger, better, and way more nature. Posted on September 16, 2009 in CSS Templates.


Examples
--------

This `Earthlingtwo` theme distribute in this add-on can be seen in action at the following site:

* https://templated.co/earthlingtwo


Installation
------------

Add Plone site
~~~~~~~~~~~~~~

Install Plone 4.x with `plone.app.theming`_ and create a Plone site (if you have not already)
with Diazo theming configured.

Zip file
~~~~~~~~

If you are an end user, you might enjoy installation via zip file import.

1. Download the zip file: https://raw.githubusercontent.com/collective/plonetheme.earthlingtwo/master/earthlingtwo.zip
2. Import the theme from the Diazo theme control panel.


Buildout
~~~~~~~~

If you are a developer, you might enjoy installation via buildout.

Add ``plonetheme.earthlingtwo`` to your ``plone.recipe.zope2instance`` section's *eggs* parameter e.g.::

    [instance]
    eggs =
        Plone
        …
        plonetheme.earthlingtwo

and then running "bin/buildout"


Select theme
~~~~~~~~~~~~

Select and enable the theme from the Diazo control panel. That's it!


Help
----

Obviously there is more work to be done. If you want to help, pull requests accepted! Some ideas:

* Add a diazo rule to import Plone editing styles
* Configure styles to use portal_css
* Add quick installer support
* Improve styles 


Contribute
----------

* Issue Tracker: https://github.com/collective/plonetheme.earthlingtwo/issues

* Source Code: https://github.com/collective/plonetheme.earthlingtwo

* Wiki: https://github.com/collective/plonetheme.earthlingtwo/wiki


Authors
-------

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.net/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/


Collaborations
~~~~~~~~~~~~~~

* Leonardo J. Caballero G. aka macagua

* Full Name aka nickname

For an updated list of all the contributors visit: https://github.com/collective/plonetheme.earthlingtwo/graphs/contributors


Support
-------

If you are having issues, please let us know via `our Issue Tracker`_.


License
-------

The author is not a "license guy", but the earthlingtwo theme is distributed via CC 3.0 license [1]_ and this package is GPL version 2 (assuming that makes sense).

.. _`earthlingtwo`: https://templated.co/earthlingtwo
.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`TEMPLATED (CSS Templates)`: https://templated.co/
.. _`our Issue Tracker`: https://github.com/collective/plonetheme.earthlingtwo/issues

.. [1] https://templated.co/license
