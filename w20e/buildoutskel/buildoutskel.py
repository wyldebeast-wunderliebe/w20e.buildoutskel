from paste.script.templates import Template, var

vars = [
    var("varnish", "Varnish support?", default=False), 
    var("haproxy", "HAProxy support?", default=False),     
    ]

class BuildoutSkel(Template):
    
    _template_dir = './skel'
    summary = 'Buildout config files'
    vars = vars

    def write_files(self, command, output_dir, vars):    

        """ Override so as to put the files in '.' """

        # First write generic stuff, then specific
        #
        #Template.write_files(self, command, ".", vars)
        pass
