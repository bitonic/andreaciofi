import re

class BBCode:
    re_flags = re.IGNORECASE | re.DOTALL
    
    def __init__(self, text):
        self.text = text

    def generate_html(self):
        result = self.text
        
        rules = [
            # Bold text
            (r'\[b\](.*?)\[\/b\]', '<b>\g<1></b>'),
            # Italics
            (r'\[b\](.*?)\[\/b\]', '<i>\g<1></i>'),
            # Un-named urls
            (r'\[url\](.*?)\[\/url\]', '<a href="\g<1>">\g<1></a>'),
            # Named urls
            (r'\[url=(.*?)\](.*?)\[\/url\]', '<a href="\g<1>">\g<2></a>'),            
            ]

        for (rule, replace) in rules:
            result = re.sub(re.compile(rule, self.re_flags), replace, result)

        return result

        
