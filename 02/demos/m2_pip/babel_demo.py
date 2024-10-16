"""
This script demonstrates the usage of the Babel library to format numbers
according to different locale conventions.

The script imports the `format_number` function from the `babel.numbers` module
and uses it to format a given number in both US English and Dutch formats.

The number 12345678 is formatted and printed in the following locales:
- en_US (US English)
- nl_NL (Dutch)

Output:
The script prints the formatted number in both locales, showing the difference
in number formatting conventions between the US and the Netherlands.
"""

from babel.numbers import format_number

NUMBER = 12345678
print(
    "In the Netherlands we write",
    format_number(NUMBER, locale="en_US"),
    "as",
    format_number(NUMBER, locale="nl_NL"),
)
