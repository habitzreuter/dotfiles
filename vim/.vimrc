syntax on			" syntax highlighting
filetype plugin indent on	" activates indenting

set nocompatible		" be iMproved
set autoindent			" auto indenting 
set ignorecase			" ignore case when searching
set autoread			" autoreload changed files
set incsearch			" incremental search
set backspace=indent,eol,start	" make backspace work as expected
set colorcolumn=81
set nowrap
set number
set relativenumber

" Show trailing spaces
:highlight ExtraWhitespace ctermbg=red guibg=red
:autocmd Syntax * syn match ExtraWhitespace /\s\+$\| \+\ze\t/

colorscheme ron
