def main(file_name: str):
    # First we open up the file
    file = open(file_name, 'r')
    line_count = file.readline()
    result = []

    # Now, we iterate through all the lines. We know how many lines
    # there are because the first line told us how many there would be
    for i in range(0, int(line_count)):
        line = file.readline()
        output = ""
        should_flip = True  # We'll flip the first lowercase letter
        for c in line:
            # If the letter is lowercase, we'll flip every other one.
            # Every time we see a lowercase letter, we make should_flip True
            # if it's False, and False if it's true. Therfore, we will
            # end up flipping every other lowercase letter.
            if c.islower():
                if should_flip:
                    output += c.upper()
                else:
                    output += c
                should_flip = not should_flip
            # If it's uppercase, punctuation, numbers, etc., we put it
            # back in the output.
            else:
                output += c
        result.append(output)

    for line in result:
        print(line)


if __name__ == '__main__':
    main("test_files/not_the_caps_youre_looking_for.txt")
