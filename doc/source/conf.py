from sphinx.util.texescape import tex_replacements

extensions = ['sphinx.ext.extlinks']
source_suffix = ['.rst']
project = 'NTP'
copyright = '1992-2015 University of Delaware, 2011-2015 Network Time Foundation'
release = 'RELEASE'
version = release
master_doc = 'sitemap'
nitpicky = True
primary_domain = ''
highlight_language = 'text'
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'My tab %s', 'code-block': 'My code %s'}
needs_sphinx = '1.3'
templates_path = ['_templates']
html_theme = 'bizstyle'
html_short_title = 'NTP Documentation'
html_copy_source = False
html_show_sourcelink = False
html_sidebars = {
  '**': ['localtoc.html', 'sitetoc.html', 'sourcelink.html', 'searchbox.html']
}
extlinks = {
  'ntp_bug': ('https://bugs.ntp.org/%s', None),
  'ntp_home': ('http://www.ntp.org/%s', 'www.ntp.org'),
  'ntp_research': ('http://www.eecis.udel.edu/~mills/%s', None),
}

from sphinx import addnodes

def parse_confval(env, sig, signode):
	first, rest = sig.split(' ', 1)
	if rest.startswith('|'):
		signode += addnodes.desc_name(sig, sig)
		return sig
	signode += addnodes.desc_name(first, first)
	lastarg = None
	for arg in rest.split(' '):
		if lastarg and arg.strip(']') == lastarg:
			arg = '<' + lastarg + '>' + (']' if arg.endswith(']') else '')
		signode += addnodes.desc_addname(arg, ' ' + arg)
		lastarg = arg.strip("[ ")
	return first

def setup(app):
  app.add_object_type('confval', 'confval',
    'pair: %s; configuration value', parse_confval)
  # Define LaTeX mathematical symbol replacements
  # To lookup see:
  # http://www.w3.org/Math/characters/html/symbol.html
  # https://en.wikibooks.org/wiki/LaTeX/Mathematics
  tex_replacements.extend((
    (u'\u2212', '$-$'),
    (u'\u2265', '$\ge$'),
  ))
