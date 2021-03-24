import sublime
import sublime_plugin

from Default.paragraph import expand_to_paragraph

class SelectBlock(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        region = view.sel()[0]
        region = expand_to_paragraph(view, region.begin())
        sublime.Selection.add(view, sublime.Region(region.end(), region.begin()))

class SelectLine(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        region = view.sel()[0]
        region = view.line(region)
        sublime.Selection.add(view, sublime.Region(region.begin(), region.end()))
