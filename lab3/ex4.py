# The build_xml_element function receives the following parameters: tag, content, and key-value elements
# given as name-parameters. Build and return a string that represents the corresponding XML element. 

def build_xml_element(tag, content, **kwargs):
    result = "<" + tag
    for key, value in kwargs.items():
        result += " " + key + "=\"" + value + "\""
    result += ">" + content + "</" + tag + ">"
    return result

def main():
    print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))

main()