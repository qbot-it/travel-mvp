import re
from ...dto.destination import Destination


class Parser:
    def parse(self, input_txt: str) -> list[Destination]:
        rows = re.findall('(?<=\\d.).*?\\(.+?\\)', input_txt)
        destinations = []

        for row in rows:
            code_with_parentheses = re.findall('\\(.*\\)', row)[0]
            code = re.findall('(?<=\\().*(?=\\))', code_with_parentheses)[0]
            row = row.replace(code_with_parentheses, '')

            if isinstance(code, str):
                code = code.strip()
                if len(code) == 3:
                    destinations.append(Destination(name=row.strip(), airport_code=code))

        return destinations

