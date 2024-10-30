class Volume:
    def __init__(self, value=0):
        if value > 11:
            self.value = 11
        elif value < 0:
            self.value = 0
        else:
            self.value = value

    def set(self, new_value):
        if new_value > 11:
            self.value = 11
        elif new_value < 0:
            self.value = 0
        else:
            self.value = new_value

    def get(self):
        return self.value

    def __repr__(self):
        return f"Volume({self.value})"

    def up(self, up_value):
        if self.value + up_value > 11:
            self.value = 11
        else:
            self.value += up_value

    def down(self, down_value):
        if self.value - down_value < 0:
            self.value = 0
        else:
            self.value -= down_value

    def __eq__(self, other):
        if isinstance(other, Volume):
            return self.value == other.value
        else:
            return False


# v = Volume(5)
# v.up(1.1)
# # v.down(2)
# print(v == Volume(6.1) )


def partyVolume(filename):
    with open(filename, "r") as file:
        initial_volume = eval(file.readline().replace("\n", ""))
        rest_volumes = file.readlines()

        v = Volume(initial_volume)

        for i in range(len(rest_volumes)):
            volume = rest_volumes[i].split(" ")
            # print(volume)

            if volume[0] == "U":
                v.up(eval(volume[1].replace("\n", "")))
            else:
                v.down(float(volume[1].replace("\n", "")))

        return v


# print(partyVolume("party1.txt"))
# print(partyVolume("party2.txt"))
# print(partyVolume("party3.txt"))

# print(partyVolume("party1.txt") == Volume(6.35))
# print(partyVolume("party2.txt") == Volume(3.75))
# print(partyVolume("party3.txt") == Volume(0.75))


if __name__ == "__main__":
    import doctest

    print(doctest.testfile("hw7TEST.py"))
