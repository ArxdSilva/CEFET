text = 'segundo<em><strong> paragrafo</em></strong>'

tags = [
{'length': 8, 'tag': '<strong>', 'offset': 11},
{'length': 9, 'tag': '</strong>', 'offset': 34},
{'length': 4, 'tag': '<em>', 'offset': 7},
{'length': 5, 'tag': '</em>', 'offset': 29}
]

def modify(text, tags):
    for tag in tags:
        off = tag['offset']
        name = tag['tag']
        length = tag['length']

        if (name[1] = '/'):
            for tag2 in tags:
                tag_dif = off - off2
                off2 = tag2['offset']
                name2 = tag2['tag']
                length2 = tag2['length']

                if (name2[1] = '/') & (length2 != length) & (off > off2):
                    if (tag_dif = off2):
                        # cut before tag_dif
                        # add selected tag before tag_dif
                        # add tag_dif to the text
                        # cut original text after selected tag
                    else:
                    #     keep tag infos
                    #     close tag before tag_dif
                    #     reunite text
                    #     open tag after tag_dif
                    # reunite text
                    # update tags array

                else:
                    continue
        else:
            continue
    print tags
    print text

modify(text, tags)
