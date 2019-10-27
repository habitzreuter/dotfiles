# qutebrowser config file based on
# https://git.sr.ht/~sircmpwn/dotfiles/tree/master/.config/qutebrowser/config.py

c.spellcheck.languages = ["en-US", "pt-BR", "de-DE"]

config.bind("xjt", "set content.javascript.enabled true")
config.bind("xjf", "set content.javascript.enabled false")

# qute-pass shortcuts
config.bind('<z><l>', 'spawn --userscript qute-pass -d dmenu')

# download settings
c.downloads.remove_finished = 1
c.downloads.location.directory = '~/Downloads/'

c.content.cookies.accept = 'no-3rdparty'

c.content.javascript.enabled = False
whitelist = [
    "*://localhost/*",
    "*://127.0.0.1/*",
    "*://duckduckgo.com/*",
    "*://translate.google.com/*",
    "*://ufrgs.br/*",
    "*://*.ufrgs.br/*",
    "*://*.stackexchange.com/*",
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
