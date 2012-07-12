from paste.script.templates import Template, var
import os

vars = [
    var("type", "What type of project do you want? [plone|pyramid|django|pycms]"),
    ]

class BuildoutSkel(Template):
    
    _template_dir = './skel/common'
    summary = 'Buildout config files'
    vars = vars

    def write_files(self, command, output_dir, vars):    

        """ Override so as to put the files in '.' """

        type_dir = os.path.join(self.module_dir(), "./skel/%s" % vars['type'])

        assert os.path.isdir(type_dir)
        
        # First write generic stuff, then specific
        #
        Template.write_files(self, command, ".", vars)

        self._template_dir = type_dir

        Template.write_files(self, command, ".", vars)
