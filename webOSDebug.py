import os

import sublime
import sublime_plugin

from .webOS import WebosCommand


class WebosDebugCommand(sublime_plugin.WindowCommand, WebosCommand):
    def run(self):
        settings = sublime.load_settings('webOS.sublime-settings')

        appinfo_path = self.get_appinfo_path()
        if not appinfo_path:
            sublime.active_window().run_command('webos_view_output', {'output': 'ERROR: "appinfo.json" could not be found.'})
            return

        appinfo_data = self.get_appinfo_data(appinfo_path=appinfo_path)
        ares_command = os.path.join(self.get_cli_path(), 'ares-launch')
        # command = ['ares-launch', '-d', settings.get('target'), '-i', appinfo_data['id']]
        command = [ares_command, '-d', settings.get('target'), '-i', '-o', appinfo_data['id']]
        self.run_command(command, show_status=False)
