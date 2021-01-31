def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count if count != "" else "1")
            count = ''
    return decode


def parse(pattern):
    pattern = rle_decode(pattern)
    output = []
    for item in pattern.split("$"):
        row = []
        for i in range(len(item)):
            if item[i] == "o":
                row.append(i)
        output.append(row)
    return output
