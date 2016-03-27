import sys

from HotkeyLexer import HotkeyLexer
from HotkeyParser import HotkeyParser
from HotkeyListener import HotkeyListener

#The data classes that the parser is populating!
from data.configuration import Configuration
from data.projectinfo import ProjectInfo
from data.osconfig import OsConfig
from data.externaltoolhotkey import ExternalToolHotkey
from data.customscripthotkey import CustomScriptHotkey

class HotkeyEmitter(HotkeyListener):
    def __init__(self):
        self.configuration  = Configuration()
        self.dictionaries   = {}
        self.values         = {}
        self.current_os     = None
        
    def enterString(self, ctx:HotkeyParser.StringContext):
        """
        Denotes the entry of a value context of type string.
        """
        self.values[ctx] = ctx.getText().strip('"')

    def enterAtom(self, ctx:HotkeyParser.AtomContext):
        """
        Denotes the entry of a value context of any type other than the string type.
        """
        self.values[ctx] = ctx.getText().strip('"')

    def enterAnObject(self, ctx:HotkeyParser.AnObjectContext):
        """
        Denotes the entry of a non-empty dictionary context.
        """
        dict = {}
        for pair_ctx in ctx.pair():
            key         = pair_ctx.STRING().getText()
            value       = self.values.get(pair_ctx.value(), None)
            dict[key]   = value

        self.dictionaries[ctx] = dict
        
    def enterConfig(self, ctx:HotkeyParser.ConfigContext):
        self.current_os = ctx.OPERATING_SYSTEM().getText().strip(":")
    
    def enterEmptyObject(self, ctx:HotkeyParser.EmptyObjectContext):
        """
        Denotes the entry of an empty dictionary context.
        """
        self.dictionaries[ctx] = {}
        
    def exitProject(self, ctx : HotkeyParser.ProjectContext):
        # First we need to populate the ProjectInfo class with the header information of the project.
        project_info        = ProjectInfo()

        proj_info_ctx       = ctx.project_info()
        
        proj_name           = proj_info_ctx.NAME().getText()
        project_info.name   = proj_name
        
        info_ctx            = proj_info_ctx.dictionary()
        project_info.info   = self.dictionaries[info_ctx]
        
        self.configuration.project_info = project_info

        # Then we need to loop through all of the os_config contexts and create all of those objects.
        for config_ctx in ctx.config():
            os_config = OsConfig(self.current_os)

            for namespace_ctx in config_ctx.namespace():
                namespace_name                          = namespace_ctx.NAME().getText()
                os_config.namespaces[namespace_name]    = self.dictionaries.get(namespace_ctx, {})

            for hotkey_ctx in config_ctx.external_tool_hotkey():
                hotkey              = ExternalToolHotkey()

                hotkey.name         = hotkey_ctx.NAME().getText()

                env_vars_ctx        = hotkey_ctx.environment_vars()
                hotkey.env_vars     = self.dictionaries[env_vars_ctx.dictionary()]

                conditions_ctx      = hotkey_ctx.simultaneous_condition()
                conditions          = []

                for condition_ctx in conditions_ctx.NAME():
                    conditions.append(condition_ctx.getText())

                hotkey.condition    = conditions

                working_dir_ctx     = hotkey_ctx.working_dir()
                hotkey.working_dir  = working_dir_ctx.STRING()

                hotkey.executable   = hotkey_ctx.NAME().getText()

                os_config.hotkeys[hotkey.name] = hotkey

            for hotkey_ctx in config_ctx.custom_script_hotkey():
                hotkey              = CustomScriptHotkey()

                hotkey.name = hotkey_ctx.NAME().getText()

                conditions_ctx = hotkey_ctx.simultaneous_condition()
                conditions = []

                for condition_ctx in conditions_ctx.NAME():
                    conditions.append(condition_ctx.NAME().getText())

                hotkey.condition = conditions

                hotkey.executable = hotkey_ctx.COMMAND().strip("$")

                os_config.hotkeys[hotkey.name] = hotkey

            self.configuration.os_configs[self.current_os] = os_config


def parse(file_path):
    input   = FileStream(file_path)
    lexer   = HotkeyLexer(input)
    stream  = CommonTokenStream(lexer)
    parser  = HotkeyParser(stream)
    tree    = parser.project()
    
    
    listener = HotkeyEmitter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.configuration