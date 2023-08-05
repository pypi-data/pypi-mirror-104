# quizpy

This package allows you to create a Moodle Quiz in Python code, which then can be imported via the XML import.
**Stop fumbling around** with the horrible moodle web interface! **Start coding and use version control!**

So far many of the existing question types are supported:

* [X] Multiple Choice
* [X] Multiple True-False
* [x] Numerical 
* [x] ShortAnswer 
* [x] Matching 
* [X] Drag & Drop on Images
* [X] Cloze
* [X] Essay
* [X] Descriptions

## Installation
Quizpy is available on PyPi and can be installed via pip:
```
pip install quizpy
```

## Usage
A moodle quiz (more specifically a question catalogue) consists of multiple categories that need to be filled
with questions. Each `Question` has at least a title, a question text and some default points (which can be
scaled in the actual quiz on moodle). Further customizations depend on the question type.

A minimal 2-question example might look like this:
```python
from quizpy import Quiz, Category, MultipleChoice, Essay, Choice

mc = MultipleChoice("Question Title", 'Is this a question?', 1.0)
mc.choices.append(Choice('Yes', 100.00, 'Correct, horse!'))
mc.choices.append(Choice('No', -100.00, 'Na-ahh'))
mc.choices.append(Choice('Maybe?', 0.0, 'Na-ahh'))

blabber = Essay("Psychology Question", "How does coding an exam make you feel?", 1.0, 
                response_template="Great!")

example_questions = Category("Example questions")
example_questions.questions.extend([mc, blabber])

example_quiz = Quiz(categories=[example_questions])

example_quiz.export('example_quiz.xml')

```

