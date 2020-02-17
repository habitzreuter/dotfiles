# qutebrowser config file based on
# https://git.sr.ht/~sircmpwn/dotfiles/tree/master/.config/qutebrowser/config.py

import os

c.spellcheck.languages = ["en-US", "pt-BR", "de-DE"]

config.bind("xjt", "set content.javascript.enabled true")
config.bind("xjf", "set content.javascript.enabled false")

# userscripts shortcuts
config.bind('<z><l>', 'spawn --userscript qute-pass -d dmenu')
config.bind('<z><b>', 'spawn --userscript getbib')

# view videos in mpv
config.bind(',m', 'spawn mpv {url}')
config.bind(',M', 'hint links spawn mpv {hint-url}')

# download settings
c.downloads.remove_finished = 1
c.downloads.location.directory = '~/Downloads/'

c.content.cookies.accept = 'no-3rdparty'
c.content.cookies.store = False

c.content.javascript.enabled = False
whitelist = [
    "*://localhost/*",
    "*://127.0.0.1/*",
    "*://duckduckgo.com/*",
    "*://translate.google.com/*",
    "*://dictionary.cambridge.org/*",
    "*://*.latex.codecogs.com/*",
]

js_whitelist = os.path.expanduser("~/.config/qutebrowser/js_whitelist")
if os.path.exists(js_whitelist):
    with open(js_whitelist) as f:
        whitelist += filter(lambda l: bool(l), f.read().split("\n"))

for site in whitelist:
    with config.pattern(site) as pat:
        pat.content.javascript.enabled = True

c.colors.statusbar.normal.bg = "#333"
c.colors.statusbar.url.success.https.fg = "white"
c.colors.tabs.even.fg = "#888"
c.colors.tabs.even.bg = "#333"
c.colors.tabs.odd.fg = "#888"
c.colors.tabs.odd.bg = "#333"
c.colors.tabs.selected.odd.bg = "#285577"
c.colors.tabs.selected.even.bg = "#285577"
c.colors.messages.error.fg = c.colors.statusbar.normal.fg
c.colors.messages.warning.fg = c.colors.statusbar.normal.fg
c.colors.prompts.fg = c.colors.statusbar.normal.fg
