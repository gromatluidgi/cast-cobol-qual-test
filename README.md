# Study COBOL Code Quality Analysis

## Introduction

The purpose of this repository is to centralize information gathered about **COBOL code quality analysis**. It will also provides usefull tips and examples for create custom plugins that integrate custom rules detection for SAST tool likes:
- Cast AIP
- Sonar

## Definitions

- SAST: Static Application Security Testing

## Analysis Targets

SAST tools are based on a parsing engine, which **reads and traverse** software code. Their ability to detect bad practices or potential issues using a set of rules makes them indispensable.

- Performance
- Styles
- Security
- Reliability

## Analysis Scopes

According to the target of the used analyzer, we can defines primary aims for obtain various metrics.

### Code Quality
https://www.perforce.com/blog/sca/what-code-quality-overview-how-improve-code-quality

Talking about code quality generaly refer to a set of practices to follow for produces **high quality code** and **identify potential smells** during development. What's "good code" or "bad code", is subjective and may differ in organizations.

The code quality is important, as it impacts the overall software quality. And quality impacts how safe, secure, and reliable your codebase is. High quality is critical for many development teams today. And it's especially important for those developing safety-critical systems.

The subcategories below shows an unhexaustive list of rule areas for gather **quality infractions**:
- Design rules
- Documentation rules
- Globalization rules
- Portability and interoperability rules
- Maintainability rules
- Naming rules

### Coding Style

Coding style analysis aim to maintain consistent code style into a codebase. Thus, a set of rules thats focus on style infractions, can be organized into the following areas:

- Language rules
  - Rules that pertain to the COBOL language. For example, you can specify rules that regard the use of an **unsupported syntax**.
- Unnecessary code rules
  - Rules that pertain to unnecessary code that indicates a potential readability, maintainability, performance, or functional problem. For example, a paragraph that is never called with of "GO TO" or "PERFORM" is unnecessary code.
- Formatting rules
  - Rules that pertain to the layout and structure of your code.
- Naming rules
  - Rules that pertain to the naming of code elements. For example, you can specify that paragraphs should **follow a naming convention**.
- Miscellaneous rules
  - Rules that do not belong in other areas.