def abbreviate(words):
    phrase = words.replace("-", " ").replace("_"," ")
    result = ""

    for word in phrase.split():
        result += word[0].upper()

    return result