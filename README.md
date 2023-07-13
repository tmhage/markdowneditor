# Markdown Editor

## Objective

Implement a separate function for each of the formatters. It will keep your code structured. With functions, you will also be able to find and fix a bug with ease if something is wrong.

The program should work in the following way:

1. Ask a user to input a formatter.
2. If the formatter doesn't exist, print the following error message: `Unknown formatting type or command`.
3. Ask a user to input a text that will be applied to the formatter: `Text: <user's input>`.
4. Save the text with the chosen formatter applied to it and print the markdown. Each time you should print out the whole text in markdown accumulated so far.

Based on the [Markdown Guide](https://www.markdownguide.org/basic-syntax/):

plain — a normal text without any formatting
bold/italic — self-explanatory
inline-code — for example, python editor.py
link — for example, google.com
header — look at the header of this stage.
unordered-list — this very list is an example of an unordered list
ordered-list — a list with enumerated elements
new-line — switches to the next line

- Headings require a level and a text to print. The level is a number from 1 to 6. If the input number is out of bounds, print the corresponding error: The level should be within the range of 1 to 6 and ask the user for input again. A heading should always be printed on a new line and automatically add a new line at the end:
```commandline
Choose a formatter: > header
Level: > 4
Text: Hello World!
#### Hello World!
```
- Plain, bold, italic, and inline-code formatters require only text input. They should not add an extra space or line break at the end and should add a new formatted text to the previously formatted one (you do not need to print the new formatted text on a new line).
- The new-line formatter does not require text input.
- Link requires a label and a URL. This formatter should not add an extra space or line break at the end.
```commandline
Choose a formatter: > link
Label: > Tutorial
URL: > https://www.markdownguide.org/basic-syntax/
[Tutorial](https://www.markdownguide.org/basic-syntax/)
```

## Examples

Example 1: printing a heading.

```commandline
Choose a formatter: > header
Level: > 10
The level should be within the range of 1 to 6
Level: > 4
Text: Hello World!
#### Hello World!
Choose a formatter: > 
```

Example 2: printing a heading after some other text; the heading is on a new line and another new line is added right after it.

```commandline
Choose a formatter: > bold
Text: > Hello
**Hello**
Choose a formatter: > header
Level: > 2
Text: > Hello World!
**Hello**
## Hello World!
Choose a formatter: >
``````
Example 3: working with the plaintext , inline-code, and new-line formatters; mind that the new-line formatter does not require text input.

```commandline
Choose a formatter: > plain
Text: > raw text
raw text
Choose a formatter: > inline-code
Text: > code.format()
raw text`code.format()`
Choose a formatter: > new-line
raw text`code.format()`

Choose a formatter: >
```

Example 4: working with the bold and link formatters.

```commandline
Choose a formatter: > bold
Text: > You can use the following link:
**You can use the following link:**
Choose a formatter: > link
Label: > Tutorial
URL: > https://www.markdownguide.org/basic-syntax/
**You can use the following link:**[Tutorial](https://www.markdownguide.org/basic-syntax/)
Choose a formatter: >
```
Example 5: working with the header formatter; it automatically adds a line break, that's why the next formatted text (the link) is printed on a new line.
```commandline
Choose a formatter: > non-existing-formatter
Unknown formatting type or command
Choose a formatter: > header
Level: > 4
Text: > Hello World!
#### Hello World!
Choose a formatter: > plain
Text: > Some plain text
#### Hello World!
Some plain text
Choose a formatter: > new-line
#### Hello World!
Some plain text

Choose a formatter: > link
Label: > Tutorial
URL: > https://www.markdownguide.org/basic-syntax/
#### Hello World!
Some plain text
[Tutorial](https://www.markdownguide.org/basic-syntax/)
Choose a formatter: > !done
```