import os, sass

scss_input = str(open('custom.scss', 'r').read())
css_output = open(os.path.abspath('../../static/scripts/custom_bootstrap.css'), 'w')

css_output.write(sass.compile(filename='custom.scss'))
