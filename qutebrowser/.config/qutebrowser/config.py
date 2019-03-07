# qutebrowser config file based on
# https://git.sr.ht/~sircmpwn/dotfiles/tree/master/.config/qutebrowser/config.py

c.downloads.location.directory = '~/tmp/'

config.bind("xjt", "set content.javascript.enabled true")
config.bind("xjf", "set content.javascript.enabled false")

# qute-pass shortcuts
config.bind('<z><l>', 'spawn --userscript qute-pass -d dmenu')

c.content.javascript.enabled = False
c.content.cookies.accept = 'no-3rdparty'
whitelist = [
    "*://localhost/*",
    "*://127.0.0.1/*",
    "*://duckduckgo.com/*",
    "*://translate.google.com/*",
    "*://gitlab.com/*",
    "*://*.gitlab.com/*",
    "*://github.com/*",
    "*://*.github.com/*",
    "*://ufrgs.br/*",
    "*://*.ufrgs.br/*",
]
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
