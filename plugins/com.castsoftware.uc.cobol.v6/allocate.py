from cast.analysers import log, mainframe

RULE_CATEGORY_NAME = "UC_COBOL_V6"
RULE_NAME = "allocateNotAllowed"
RULE_FULLNAME = str.join('.', [RULE_CATEGORY_NAME, RULE_NAME])

class AllocateNotAllowed(mainframe.Extension):
    
    def __init__(self):
        self.program = None

    def start_program(self, program):
        self.program = program

    def end_program(self, _):
        self.program = None
