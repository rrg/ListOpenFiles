import sublime,sublime_plugin,os

class ListOpenFilesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        window = sublime.active_window()
        views = window.views()

        fileNames = ''
        for view in views:
            if view and view.file_name():
                fileNames += os.path.abspath(view.file_name())+'\n'

        window.new_file().insert(edit, 0, "List of open files:\n\n"+fileNames)
