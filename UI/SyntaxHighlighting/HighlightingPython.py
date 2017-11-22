from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont
from PyQt5.QtCore import Qt, QRegExp

import keyword


class HighlightingPython(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(HighlightingPython, self).__init__(parent)

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(Qt.darkBlue)
        keywordFormat.setFontWeight(QFont.Bold)

        keywordPatterns = []
        for keyword_ in keyword.kwlist:
            keywordPatterns.append("\\b{}\\b".format(keyword_))

        self.highlightingRules = [(QRegExp(pattern), keywordFormat) for pattern in keywordPatterns]

        builtinFormat = QTextCharFormat()
        builtinFormat.setForeground(Qt.darkMagenta)
        self.highlightingRules.append((QRegExp("__[^\\n ]*__"), builtinFormat))
        self.highlightingRules.append((QRegExp("\*\*[^\\n\(\) ]*"), builtinFormat))

        commentFormat = QTextCharFormat()
        commentFormat.setForeground(Qt.gray)
        self.highlightingRules.append((QRegExp("\#[^\n]*"), commentFormat))

        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(Qt.darkGreen)
        self.highlightingRules.append((QRegExp("\".*\""),
                                       quotationFormat))

        # functionFormat = QTextCharFormat()
        # functionFormat.setFontItalic(True)
        # functionFormat.setForeground(Qt.blue)
        # self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
        #                                functionFormat))

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)