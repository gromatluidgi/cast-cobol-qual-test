from cast.analysers import log, mainframe

RULE_CATEGORY_NAME = "UC_COBOL_V6"
RULE_NAME = "jsonGenerateNotAllowed"
RULE_FULLNAME = str.join('.', [RULE_CATEGORY_NAME, RULE_NAME])

class JsonGenerateNotAllowed(mainframe.Extension):
    
    def __init__(self):
        self._program = None

    def start_program(self, program):
        log.info('Start of program')
        self._program = program

    def end_program(self, _):
        self._program = None
        
    def start_declaratives(self, declaratives):
        pass

    def end_declaratives(self, _):
        pass
