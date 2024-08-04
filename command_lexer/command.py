import re

from pygments.lexer import RegexLexer, bygroups, include, using, words
from pygments.token import (Comment, Generic, Keyword, Literal, Name, Number,
                            Operator, String, Text, Whitespace, Punctuation)

__all__ = ("CommandLexer",)

class CommandLexer(RegexLexer):
    name = "Command Mkdocs"
    aliases = ["cmd"]
    flags = re.MULTILINE | re.IGNORECASE

    tokens = {
        "root": [
            include('basic'),
            (r"(?:[^\n\w]+#.*$)|(?:^\s*#.*$)", Comment),
            (r'"', String, 'doublequote'),
            (r"'", String, 'singlequote'),
            (r'\s\d+\s', Name.Constant),
            (r'\\$', String.Escape),
            (r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\/\d{1,3})?\s", Name.Constant),
            (r"-\b\w+\b", Keyword.Reserved),
            (r"--\b(\w*[-]?)+\b", Keyword.Reserved),
            (r"<.+>", String.Escape),
            include('interp'),
        ],
        'doublequote': [
            ('[^"<]+', String),
            ('<', String.Escape, 'param'),
            ('"', String, '#pop'),
        ],
        'singlequote': [
            ("[^'<]+", String),
            ('<', String.Escape, 'param'),
            ("'", String, '#pop'),
        ],
        'param': [
            ('[^>]+', String.Escape),
            ('>', String.Escape, '#pop')
        ],
        'interp': [
            (r'\$\(\(', Keyword, 'math'),
            (r'\$\(', Keyword, 'paren'),
            (r'\$\{#?', String.Interpol, 'curly'),
            (r'\$[a-zA-Z_]\w*', Name.Variable),  # user variable
            (r'\$(?:\d+|[#$?!_*@-])', Name.Variable),      # builtin
            (r'\$', Text),
        ],
        'basic': [
            (r'\b(if|fi|else|while|in|do|done|for|then|return|function|case|'
             r'select|break|continue|until|esac|elif)(\s*)\b',
             bygroups(Keyword, Whitespace)),
            (r'\b(alias|bg|bind|builtin|caller|cd|command|compgen|'
             r'complete|declare|dirs|disown|echo|enable|eval|exec|exit|'
             r'export|false|fc|fg|getopts|hash|help|history|jobs|kill|let|'
             r'local|logout|popd|printf|pushd|pwd|read|readonly|set|shift|'
             r'shopt|source|suspend|test|time|times|trap|true|type|typeset|'
             r'ulimit|umask|unalias|unset|wait)(?=[\s)`])',
             Name.Builtin),
        ],
        'curly': [
            (r'\}', String.Interpol, '#pop'),
            (r':-', Keyword),
            (r'\w+', Name.Variable),
            (r'[^}:"\'`$\\]+', Punctuation),
            (r':', Punctuation),
            include('root'),
        ],
        'paren': [
            (r'\)', Keyword, '#pop'),
            include('root'),
        ],
        'math': [
            (r'\)\)', Keyword, '#pop'),
            (r'\*\*|\|\||<<|>>|[-+*/%^|&<>]', Operator),
            (r'\d+#[\da-zA-Z]+', Number),
            (r'\d+#(?! )', Number),
            (r'0[xX][\da-fA-F]+', Number),
            (r'\d+', Number),
            (r'[a-zA-Z_]\w*', Name.Variable),  # user variable
            include('root'),
        ],
    }
