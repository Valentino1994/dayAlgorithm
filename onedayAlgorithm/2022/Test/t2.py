import spacy

nlp = spacy.load('en_core_web_sm')

def anonymize_text(sentences):
    answer = []
    dic = nlp(sentences, disable=['parser'])
    removed_chr = []

    for token in dic:
        # token = dic[i]
        print(token.text)

        if str(token.pos_) == "PROPN":
            
            if len(answer) > 1 and answer[-1] == " " and answer[-2][-1] == "X":
                answer[-1] = "X"

            if token.text not in removed_chr:
                answer.append("X" * len(token.text))
                removed_chr.append(token.text)

            else:
                answer.append(token.text)
                
            if str(token.pos_) == "PUNCT" and len(answer) > 1 and answer[i-1] == ' ':
                answer.pop()
            
        else:
            answer.append(str(token.text))

        answer.append(" ")
    print(answer)
    answer.pop()

    return "".join(answer)

text = 'Yuh-jung Youn won the Oscar for best supporting actress for her performance in "Minari" on Sunday and made history by becoming the first Korean actor to win an Academy Award.'
text1 = 'John is old'
text2 = 'Mark Oldham ate an apple'
text3 = 'John eats an...did something U.K.'
# doc = nlp(text)

# str_format = "{:>10}"*8
# print(str_format.format('Text', 'Lemma', 'POS', 'Tag', 'Dep', 'Shape', 'is alpha', 'is stop'))
# print("=="*40)

# for token in doc:
#     print(str_format.format(token.text, token.lemma_, token.pos_, token.tag_, 
#                             token.dep_, token.shape_, str(token.is_alpha), str(token.is_stop)))

# print(anonymize_text(text))
# print(anonymize_text(text1))
# print(anonymize_text(text2))
print(anonymize_text(text3))

