import re
import os
import sublime
import sublime_plugin

from Default.paragraph import expand_to_paragraph


#------------------------------------------------------------------------------
#
# Plugin
#
#------------------------------------------------------------------------------


#
# Returns the valid prefix of 's'
#
def match_token(s):
    s = s.lstrip()
    l = len(s)
    for i in range(l):
        # Only check the first two characters
        if i >= 2:
            break
        c = s[i]
        if c == "-":
            return c
        if c == "*":
            return c
        if c == ">":
            if i + 1 < l and c == s[i + 1]:
                return ">>"
            return c
        if c == "#":
            return c
        if c == "/":
            if i + 1 < l and c == s[i + 1]:
                return "//"
        if c == "~":
            return c
    return ""


#
# Escapes 't'
#
def escape(t):
    if t == "*":
        return "\*"
    return t


#
# Returns the number of leading spaces in 's'
#
def lspace(s):
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1
    return i


#
# Wraps 'stream' at 'cutoff' (including)
#
def wrap_stream(stream, indent=None, newlines=0, cutoff=80):
    if not indent:
        indent = lspace(stream)

    prefix = match_token(stream)
    prefix_indent = indent

    stream = re.sub('(\n)+', ' ', stream)
    stream = re.sub('( )+', ' ', stream)
    stream = re.sub('({})'.format(escape(prefix)), '', stream, 1)
    stream = stream.strip()

    if (len(prefix) > 0):
        prefix_indent += len(prefix) + 1
        prefix += " "

    if len(stream) + prefix_indent < cutoff:
        return " " * indent + prefix + stream + "\n"

    leader = 1
    block = ""
    line = ""
    linelen = 0
    for word in stream.split():
        if linelen + prefix_indent + len(word) >= cutoff:
            if not leader:
                block += " " * prefix_indent + line.rstrip() + "\n"
            else:
                leader = 0
                block += " " * indent + prefix + line.rstrip() + "\n"
            line = ""
            linelen = 0
        line += word + " "
        linelen += len(word) + 1
    block += " " * prefix_indent + line.rstrip()

    return block + "\n"


#------------------------------------------------------------------------------
#
# Sublime
#
#------------------------------------------------------------------------------


def get_file_ext(view):
    filepath = view.file_name()
    if filepath != None:
        ext = os.path.splitext(view.file_name())[1]
        if len(ext) != 0:
            return ext
    return None


def get_wrap_width(view):
    wrap_width = view.settings().get("wrap_width")
    if not wrap_width or wrap_width < 10:
        return 80
    return wrap_width


class WrapBlock(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        wrap_width = get_wrap_width(view)
        region = view.sel()[0]
        region = expand_to_paragraph(view, region.begin())
        string = wrap_stream(view.substr(region), cutoff=wrap_width)
        view.replace(edit, sublime.Region(region.begin(), region.end()), string)
