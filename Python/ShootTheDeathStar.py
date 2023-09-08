def main(file_name: str):
    # First we open up the file
    file = open(file_name, 'r')
    line_count = file.readline()
    output = []

    # Now, we iterate through all the lines. We know how many lines
    # there are because the first line told us how many there would be
    for i in range(0, int(line_count)):
        line = file.readline().split(" ")

        # We'll calculate the result according to the formula in the instructions
        result = ((int(line[0]) * 3) - int(line[1])) / int(line[2])

        # And then we'll respond with a message according to the instructions
        if 100 < result < 300:
            output.append("You have hit the Death Star!")
        else:
            output.append("You have missed the death star.")

    for line in output:
        print(line)


if __name__ == '__main__':
    main("test_files/shoot_the_death_star.txt")
