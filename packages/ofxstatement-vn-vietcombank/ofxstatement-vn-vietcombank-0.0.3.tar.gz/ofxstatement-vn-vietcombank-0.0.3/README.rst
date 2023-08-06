~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Vietcombank plugin for ofxstatement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TL;DR to convert Vietcombank Excel to OFX:

1. Install plugin
  $ pip install ofxstatement-vn-vietcombank

2. Open ofxstatement config:
  $ ofxstatement edit-config

3. Add the following block:
::

  [vietcombank:vnd]
  plugin = vietcombank_excel
  currency = VND
  account = vnd_account_number

4. Save & close the file

5. Now you can run:
  $ ofxstatement convert -t vietcombank:vnd Vietcombank_Account_Statement.xlsx Vietcombank_Account_Statement-converted.ofx

Notes:

* If above results in encoding error, try adding encoding to the config explicitly:
::

  encoding = utf-8

* Unfortunately, Vietcombank doesn't provide much details regarding the payee in their statement, in most cases it would only contain ID of POS where transaction happened; if you find a way to match those, please let me know via PR or an issue explaining 'how' :)

About
==================================

`ofxstatement`_ is a tool to convert proprietary bank statement to OFX format,
suitable for importing to GnuCash. Plugin for ofxstatement parses a
particular proprietary bank statement format and produces common data
structure, that is then formatted into an OFX file.

.. _ofxstatement: https://github.com/kedder/ofxstatement

This plugin was tested to work with KMyMoney 5.1.1 with the following settings:

* Payee from Memo
* Dedup by OFX FITID

For contributors/developers
==================================

It is recommended to use ``pipenv`` to make a clean development environment.::

  $ git clone https://github.com/darkms/ofxstatement-vn-vietcombank
  $ cd ofxstatement-vn-vietcombank
  $ pipenv sync --dev
  $ pipenv shell
  $ python setup.py install
  $ ofxstatement list-plugins

list-plugins should now return you `vietcombank_excel` plugin

Testing
=======

You can run tests using:

  $ pytest
