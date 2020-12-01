

"""
Change the class CustomParser so that the pipe_parse() runs.

restrictions:
1)  you are not allowed to change anything in the classes PosTagger and DependencyParser. You are neither allowed
    to change CustomParser.pipe_parse()

"""

class PosTagger:

    def tag_pos(self):
        return "tagging POS"
    

class DependencyParser:

    def parse_dep(self):
        return "parsing dependencies"


class CustomParser(PosTagger, DependencyParser):
    def pipe_parse(self):
        return self.tag_pos(), self.parse_dep()


if __name__ == "__main__":
    c = CustomParser()
    print(c.pipe_parse())