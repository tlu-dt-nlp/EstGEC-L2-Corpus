import re

def detokenize_quotmarks(sentence):
    chars = []
    closing_mark = False
    no_space_after = False
    for char in sentence:
        if char == '"':
            if not closing_mark:
                no_space_after = True
                closing_mark = True
            else:
                if len(chars) > 0 and chars[-1] == ' ':
                    chars.pop()
                closing_mark = False
        if not (no_space_after and char == ' '):
            chars.append(char)
        if not char == '"':
            no_space_after = False
    return ''.join(chars)


detokenized_sentences = []

with open('source_sentences.txt', 'r', encoding='utf-8') as f_tokenized,\
    open('source_sentences_detokenized.txt', 'w', encoding='utf-8') as f_detokenized:
    sentences = f_tokenized.read().splitlines()
    for sent in sentences:
        sent = re.sub(r'\s([.,?!:;)])', r'\1', sent)
        sent = re.sub(r'([(])\s', r'\1', sent)
        sent = detokenize_quotmarks(sent)
        detokenized_sentences.append(sent)
    f_detokenized.write('\n'.join(detokenized_sentences))