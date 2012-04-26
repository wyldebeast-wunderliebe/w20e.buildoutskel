w20e.buildoutskel
=================

Paster template for buildout config. The command creates a full set of
config files for several environments. Using these, you should be able
to quickly set up a working buildout for your specific project.

Please note that this template only provides a __skeleton__ for your
project, so you'll still need to edit the buildout files. However, this
template is supposed to be better that the old copy 'n paste...

Installation
------------

Use easy_install to install this egg, and you should have an extra
template in your Paster listing:

    paster create --list-templates
    ...
    buildout
    ...

Usage
-----

It couldn't be easier to use:

    paster create -t buildout
