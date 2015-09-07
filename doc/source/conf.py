from sphinx.util.texescape import tex_replacements

extensions = ['sphinx.ext.extlinks']
source_suffix = ['.rst']
project = 'NTP'
copyright = '1992-2015 University of Delaware, 2011-2015 Network Time Foundation'
release = 'RELEASE'
version = release
master_doc = 'sitemap'
primary_domain = ''
highlight_language = 'text'
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
def setup(app):
  app.add_object_type('confval', 'confval',
    'pair: %s; configuration value')
  # Define LaTeX mathematical symbol replacements
  # To lookup see:
  # http://www.w3.org/Math/characters/html/symbol.html
  # https://en.wikibooks.org/wiki/LaTeX/Mathematics
  tex_replacements.extend((
    (u'\u2212', '$-$'),
    (u'\u2265', '$\ge$'),
  ))
