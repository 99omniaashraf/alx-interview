def validUTF8(data):
    def check_following_bytes(start, count):
        for i in range(start + 1, start + count + 1):
            if i >= len(data) or data[i] >> 6 != 0b10:
                return False
        return True

    i = 0
    while i < len(data):
        byte = data[i]
        if byte >> 7 == 0:  # 1-byte character
            i += 1
            continue
        elif byte >> 5 == 0b110:  # 2-byte character
            if not check_following_bytes(i, 1):
                return False
            i += 2
        elif byte >> 4 == 0b1110:  # 3-byte character
            if not check_following_bytes(i, 2):
                return False
            i += 3
        elif byte >> 3 == 0b11110:  # 4-byte character
            if not check_following_bytes(i, 3):
                return False
            i += 4
        else:
            return False
    return True
