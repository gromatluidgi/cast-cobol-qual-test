# Rule Coding Convention

**Last update:** May 2022

**Applicable for:** AIP v8.X

## Requirements

- Eclipse
- CAST AIP Pyhton 3.4 Interpreter

## References

- Starting kit for quality rules writing: http://cast-projects.github.io/Extension-SDK/doc/writing_quality_rule.html#starter-kit
- CAST AIP Mainframe Extension Documentation: https://doc.castsoftware.com/display/TECHNOS/Mainframe+-+Qualification
- Mainframe: http://cast-projects.github.io/Extension-SDK/doc/mainframe.html
- AIP Core COBOL rules: https://technologies.castsoftware.com/rules?sec=t_-4&ref=||
- SDK Documentation: http://cast-projects.github.io/Extension-SDK/doc/overview.html
- Github SDK: https://github.com/CAST-projects/Extension-SDK

## Implementation

### Rule Class Definition for COBOL

```python
from cast.analyzers import mainframe
class RuleName(mainframe.Extension):
    def __init__(self):
        self.program = None
    
    def start_program(self, program):
        self.program = program

    def end_program(self, _):
        self.program = None

    # See: 
    def on_cast_visitor_event(self, **):
        pass
```

#### Mandatory

Any test class MUST extends "mainframe.Extension".

## Testing

### Test Rule Class Definition for COBOL

```python
from cast.analyzers import mainframe
class TestRuleName(mainframe.Extension):
    def __init__(self):
        self.program = None
    
    def start_program(self, program):
        self.program = program

    def end_program(self, _):
        self.program = None

    # See: http://cast-projects.github.io/Extension-SDK/doc/mainframe.html#events
    def on_cast_visitor_event(self, **):
        pass
```

## Events

AIP rules detection engine use a kind of visitor mecanism which trigger various events according to the current parsed line of code.

**See:** http://cast-projects.github.io/Extension-SDK/doc/mainframe.html#events

## Integration

### MasterFiles

