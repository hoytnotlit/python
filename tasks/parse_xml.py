"""
write a function called parse_xml() which loads and parses data/21728182.xml. The data contains NER labeled sentences.

The output of the parse_xml() should be a two dicts structured in the following way:

sentences = {
            sentence_id:"sentence",
            ...
            }

ners = {
            sentence_id:[
                         ((char_start, char_end),  NER_TYPE),
                        ...
                        
                        ]
            ...
        
        }

NOTE! NER_TYPE is the label not the drug text/name
"""

import xml.etree.ElementTree as ET


def parse_xml():
    tree = ET.parse('data/21728182.xml')
    root = tree.getroot()

    sentences = {}
    ners = {}
    for child in root:
        sentences[child.attrib['id']] = child.attrib['text']
        if len(list(child.iter('entity'))) > 0:
            ners[child.attrib['id']] = []
            for entity in child.iter('entity'):
                c = entity.attrib['charOffset']
                t = tuple(c.split(sep='-'))
                ners[child.attrib['id']].append((t, entity.attrib['type']))
    return(sentences, ners)


sentences, ners = parse_xml()
print(sentences, ners)


