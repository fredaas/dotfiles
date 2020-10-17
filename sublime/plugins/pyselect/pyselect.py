import sublime
import sublime_plugin


class SelectLine(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        regions = view.sel()
        if len(regions) > 1:
            return
        region = view.line(regions[0])
        sublime.Selection.add(view, sublime.Region(region.begin(), region.end()))
