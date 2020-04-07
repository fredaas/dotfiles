#
# gdb -tui --args <program> <args> // Pass args to program
#
# x/20x $sp // Print 20 words bellow SP
#
# info fram // Print current stack frame info
#
# backtrace // Show line responsible for program crash
#

set ui border-mode normal
set tui active-border-mode normal
set tui border-kind ascii

set prompt gdb$

define ln
    layout next
end

define lp
    layout prev
end

define rn
    tui reg next
end

define rp
    tui reg prev
end
