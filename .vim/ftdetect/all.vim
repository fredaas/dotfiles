autocmd BufNewFile,BufRead * highlight clear texItalStyle
autocmd BufNewFile,BufRead * highlight clear texBoldStyle
autocmd BufNewFile,BufRead * highlight Error NONE
autocmd BufWrite * call Trim()
