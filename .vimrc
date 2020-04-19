"
" :windo diffthis // Show difference between windows (:diffoff to disable)
"
" :set iskeyword+=:,- // Add symbols to word definition (comma separated)
"
" :%bd | e# // Delete all buffers except current one
"
" :%!xxd // Convert binary file to hex
"

set nocompatible

colorscheme gruvbox

let g:netrw_banner = 0
let g:netrw_liststyle = 0
let g:gruvbox_italic = 0
let g:gruvbox_bold = 0
let g:gruvbox_contrast_dark = 'hard'

set wildmenu
set path+=**

set ttyfast
set t_Co=256
set background=dark

set nobackup
set noswapfile
set nowritebackup
set clipboard=unnamedplus
set noreadonly

set textwidth=80
set nowrap
set expandtab
set autoindent
set nojoinspaces

set shiftwidth=4
set softtabstop=4
set tabstop=4

set hlsearch
set ruler
set showcmd
set showmode
set laststatus=2
set tabpagemax=5
set scrolloff=10

set nospell
set spelllang=en_us

noremap d "_dd
noremap x "_x
nnoremap o o<ESC><ESC>
nnoremap O O<ESC><ESC>
nnoremap ( :bp<CR>
nnoremap ) :bn<CR>
nnoremap <C-x> :bp\|bd #<CR>
nnoremap <C-h> <C-w><C-h>
nnoremap <C-j> <C-w><C-j>
nnoremap <C-k> <C-w><C-k>
nnoremap <C-l> <C-w><C-l>

highlight clear SpellBad
highlight SpellBad cterm=underline

command! -nargs=1 Search call Search(<f-args>) | normal! n
command! -nargs=1 Indent call Indent(<f-args>)
command! Goto execute 'cd %:p:h'
command! Trim call Trim()

fun! Search(string)
  let @/='\V'.escape(a:string, '\\')
endfun

fun! Indent(width)
  let &shiftwidth=a:width
  let &softtabstop=a:width
  let &tabstop=a:width
endfun

fun! Trim()
  let l:view=winsaveview()
  execute '%s/\s\+$//e'
  call winrestview(l:view)
endfun
