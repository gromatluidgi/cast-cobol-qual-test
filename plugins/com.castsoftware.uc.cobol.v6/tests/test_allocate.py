import unittest
from cast.analysers.test import MainframeTestAnalysis

VIOLATION_NAME = "UC_COBOL_V6.allocateNotAllowed"

class TestAllocateNotAllowed(unittest.TestCase):

    def test_rule_returns(self):
        """
        Test thats no violation is raised on a valid 
        source code sample.
        """
        # Arrange
        analysis = MainframeTestAnalysis()
        analysis.add_dependency(r'C:\ProgramData\CAST\CAST\Extensions\com.castsoftware.mainframe.1.0.0-alpha1')
        analysis.add_selection('allocate/allocate_ok.cbl')
        analysis.run()
        
        # Act
        program = analysis.get_object_by_name('PGM1', 'CAST_COBOL_SavedProgram')

        # Assert
        self.assertTrue(program)
        self.assertFalse(analysis.get_violations(program, VIOLATION_NAME))

    def test_rule_raises_violation(self):
        """
        Test thats at least one violation is raised for
        an invalid source code sample.
        """
        pass