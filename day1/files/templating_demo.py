'Introduction to the Bottle templating system'
# Documentation at:
#    https://bottlepy.org/docs/dev/stpl.html
# Not part of the standard library:
#    python -m pip install bottle

# There are many templating tools:
#    bottle cheetah mako jinja2 django

# Anything inside double curly braces in evaluated and printed.
# By default, HTML special characters are escaped:  < > &
# To turn this off, put a ! at the beginning of the expression.
# Python statements are on lines where the first non-whitespace character is a %
# Those lines don't print.  They execute.
# To end a block, you need a % end entry.
# Anything not after % or inside double curly braces is a literal.  It is just printed normally.

# include(subtemplate, arguments) will fill-out the sub-template and substitute it inside the current template.
# rebase(subtemplate, arguments) will fill-out the current template and substitutes it an an outer template.
# \% escapes the percent.

from notes2.bottle import template, view

lastname = 'lannister'
first_names = 'tywin cersei&jamie tyrion jeoffrey tommin mycella'.split()

family_plain_text = '''\
The {{ lastname.capitalize() }} Family
{{ "=" * (11 + len(lastname)) }}
% for i, name in enumerate(first_names, start=1):
{{i}}. {{! name.title() }}
%   if i == 1:
    ^-- Very important person
%   end
% end
'''

family_html_text = '''\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> {{ lastname.capitalize() }} Family </title>
</head>
<body>
<h1> The <em> {{ lastname.capitalize() }} </em> Family </h1>
<hr>
<ol>
% for name in first_names:
  <li> {{ name.title() }} </li>
% end
</ol>
</body>
</html>
'''

#print template(family_html_text, lastname=lastname, first_names=first_names)

@view(family_html_text)
def show_family(line):
    fields = line.split()
    return dict(lastname=fields[0], first_names=fields[1:])

families = '''\
stark eddard catelyn robb jonsnow sansa arya bran rickon
targaryen aegon danyeres ameon vasayres
simpsons homer marge bart lisa maggie
'''.splitlines()

for line in families:
    print show_family(line)
