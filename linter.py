import os
from html.parser import HTMLParser


REQUIRED_ATTRS_FOR_VIDEO = ['playsinline','muted']
class DisallowedAttributeException(BaseException):
    def __init__(self, attr, tag, filename):
        message = f"We don't allow {attr[0]} in {tag} round these parts. Check {filename} for more info"
        super().__init__(message)

class MissingAttributeException(BaseException):
    def __init__(self, attrs, tag, filename):
        message = f"{tag} requires the following attributes: {attrs}. Check {filename} for more info"
        super().__init__(message)

class MissingDescriptionException(BaseException):
    def __init__(self,filename):
        message = f"{filename} is missing a description in front matter."
        super().__init__(message)

class MyParser(HTMLParser):

    def __init__(self, doc):
        self.doc = doc
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag=='iframe':
            for attr in attrs:
                if attr[0]=="width" or attr[0]=="height":
                    raise DisallowedAttributeException(attr, tag, self.doc)
        elif tag=='video':
            required_attrs = set([attr[0] for attr in attrs]) & set(REQUIRED_ATTRS_FOR_VIDEO)
            if (len(required_attrs)!=len(REQUIRED_ATTRS_FOR_VIDEO)):
                raise MissingAttributeException(REQUIRED_ATTRS_FOR_VIDEO, tag, self.doc)


def find_frontmatter(posttext):
    end = posttext[3:].find("---")
    return posttext[2:end+2]


def validate_front_matter(posttext, filename):
    text = find_frontmatter(posttext)
    if "description:" not in text and "micropost" not in text:
        raise MissingDescriptionException(filename)


BASE_PATH = "/home/rachel/rkaufman13-mysite"
list_of_files = os.listdir(f"{BASE_PATH}/_posts")

files_processed =0
for filename in list_of_files:
    try:
        with open(f"{BASE_PATH}/_posts/{filename}",'r') as content:
            text = content.read()
            parser = MyParser(filename)
            parser.feed(text)
            parser.close()
            validate_front_matter(text,filename)
            files_processed+=1
    except (DisallowedAttributeException,MissingAttributeException,MissingDescriptionException) as e:
        print(e)
        exit(1)
print(f"{files_processed} files out of {len(list_of_files)} processed.")
exit(0)