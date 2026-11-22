import unittest

from scripts.check_comments import comment_lines, gitignore_comment_lines


class CommentLintTest(unittest.TestCase):
    def test_python_shebang_and_string(self):
        self.assertEqual(comment_lines('#!/usr/bin/env python3\nx = "https://x/#part"\n# old', '.py'), [3])

    def test_python_inline_comment(self):
        self.assertEqual(comment_lines('x = 1  # old\n', '.py'), [1])

    def test_yaml_string_and_comment(self):
        self.assertEqual(comment_lines('name: "# literal"\nvalue: yes # old\n', '.yaml'), [2])

    def test_shell_shebang_string_and_comment(self):
        self.assertEqual(comment_lines('#!/bin/sh\nprintf "%s" "# literal"\n# old\n', '.sh'), [3])

    def test_shell_inline_comment(self):
        self.assertEqual(comment_lines('echo ready # old\n', '.sh'), [1])

    def test_gitignore_comment_and_literal(self):
        self.assertEqual(gitignore_comment_lines('\\#literal\n# old\n.qlaude/\n'), [2])


if __name__ == "__main__":
    unittest.main()
