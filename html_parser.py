import re

class Parser:
    def get_class(self, class_name: str, html: str) -> str:
        pattern = f'(?<=class="{class_name}")(.*)(?=>)'
        result = re.search(pattern, html)

        if result is None:
            return ''

        return result.group()
    
    def get_elements(self, element_name: str, html: str) -> list:
        pattern = f'<{element_name}(.*?)<\/{element_name}>'
        results = re.findall(pattern, html, flags=re.DOTALL)

        if len(results) == 0:
            pattern = f'{element_name}(.*\n)*<\/{element_name}>'
            results = re.findall(pattern, html)

        return results
    
    
    def get_number(self, html: str) -> int:
        pattern = '[^\D](\d*)'
        result = re.search(pattern, html)

        if result is None:
            return 0

        return int(result.group())
    
    def get_chapter(self, html: str) -> int:
        pattern = '(?<=c)\d*[^\D]'
        result = re.search(pattern, html)
        
        return int(result.group())