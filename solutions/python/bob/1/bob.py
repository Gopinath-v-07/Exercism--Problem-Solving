def response(hey):
    # Remove whitespace at beginning and end
    msg = hey.strip()

    # 1. Silence
    if msg == "":
        return "Fine. Be that way!"

    # Check if message contains letters
    has_letter = False
    for c in msg:
        if c.isalpha():
            has_letter = True
            break

    # 2. Yelling question
    if msg.endswith("?") and has_letter and msg.upper() == msg:
        return "Calm down, I know what I'm doing!"

    # 3. Question
    if msg.endswith("?"):
        return "Sure."

    # 4. Yelling
    if has_letter and msg.upper() == msg:
        return "Whoa, chill out!"

    # 5. Anything else
    return "Whatever."