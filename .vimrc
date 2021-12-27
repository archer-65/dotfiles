call plug#begin('~/.vim/plugged')
	Plug 'vim-airline/vim-airline'
	Plug 'vim-airline/vim-airline-themes'
	Plug 'preservim/nerdtree'
	Plug 'arcticicestudio/nord-vim'
	Plug 'SirVer/ultisnips'
	Plug 'honza/vim-snippets'
	Plug 'dracula/vim', { 'as': 'dracula' }  
	Plug 'iandwelker/rose-pine-vim'
call plug#end()

syntax on
set number
colorscheme rose-pine-dark 
set tabstop=2
set showcmd
set cursorline
filetype indent on
set wildmenu
set showmatch
set foldenable
let g:airline_theme='dracula'
let g:airline_powerline_fonts=1
highlight Normal ctermbg=None

noremap <up> <Nop>
noremap <down> <Nop>
noremap <left> <Nop>
noremap <right> <Nop>

vnoremap <up> <Nop>
vnoremap <down> <Nop>
vnoremap <left> <Nop>
vnoremap <right> <Nop>

inoremap <up> <Nop>
inoremap <down> <Nop>
inoremap <left> <Nop>
inoremap <right> <Nop>
