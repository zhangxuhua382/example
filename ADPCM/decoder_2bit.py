# 2bit data is decoded into 32bit data
def adpcm_decoder(adpcm_y):
    raw_y = []

    IndexTable = [-1, -1, -1, -1, 2, 4, 6, 8, -1, -1, -1, -1, 2, 4, 6, 8]

    StepSizeTable = [7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 19, 21, 23, 25, 28, 31, 34, 37, 41, 45, 50, 55, 60, 66, 73,
                     80, 88, 97, 107, 118, 130, 143, 157, 173, 190, 209, 230, 253, 279, 307, 337, 371, 408, 449, 494,
                     544, 598, 658, 724, 796, 876, 963, 1060, 1166, 1282, 1411, 1552, 1707, 1878, 2066, 2272, 2499,
                     2749, 3024, 3327, 3660, 4026, 4428, 4871, 5358, 5894, 6484, 7132, 7845, 8630, 9493, 10442, 11487,
                     12635, 13899, 15289, 16818, 18500, 20350, 22385, 24623, 27086, 29794, 32767]

    prevsample = 0
    previndex = 0

    Ns = len(adpcm_y)
    n = 0

    while n < Ns:
        predsample = prevsample
        index = previndex
        step = StepSizeTable[index]
        code = adpcm_y[n]

        diffq = step >> 1
        if code & 1:
            diffq = diffq + step

        if code & 2:
            predsample = predsample - diffq
        else:
            predsample = predsample + diffq

        if predsample > 32767:
            predsample = 32767
        elif predsample < -32768:
            predsample = -32768

        index = index + IndexTable[code]

        if index < 1:
            index = 1
        if index > 89:
            index = 89

        prevsample = predsample
        previndex = index

        a = predsample / 32767
        raw_y.append(a)
        n = n + 1
    return raw_y
