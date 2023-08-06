~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
NewB plugin for ofxstatement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This project provides a newB (Belgian cooperative bank) plugin for ofxstatement.
https://www.newb.coop

`ofxstatement`_ is a tool to convert proprietary bank statement to OFX format,
suitable for importing to GnuCash or Tryton. Plugin for ofxstatement parses a
particular proprietary bank statement format and produces common data
structure, that is then formatted into an OFX file.

.. _ofxstatement: https://github.com/kedder/ofxstatement


Users of ofxstatement have developed several plugins for their banks. They are
listed on main `ofxstatement`_ site. If your bank is missing, you can develop
your own plugin.

This pluggin has been created with https://github.com/kedder/ofxstatement-sample

Setting up development environment
==================================

It is recommended to use ``pipenv`` to make a clean development environment.
Setting up dev environment for writing a plugin is easy::

  $ git clone https://github.com/SDaron/ofxstatement-be-newb.git
  $ cd ofxstatement-be-newb
  $ pipenv sync --dev
  $ pipenv shell

This will download all the dependencies and install them into your virtual
environment. After this, you should be able to do::

  $ ofxstatement list-plugins
  The following plugins are available:

    newb             NewB (Belgian Cooperative Bank) plugin



