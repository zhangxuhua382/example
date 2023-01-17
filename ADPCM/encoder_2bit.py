# 32bit data encoded as 2bit data
def adpcm_encoder(raw_y):
    adpcm_y = []
    raw_y_1 = []

    IndexTable = [-1, -1, 2, 4]

    StepSizeTable = [7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 19, 21, 23, 25, 28, 31, 34, 37, 41, 45, 50, 55, 60, 66, 73,
                     80, 88, 97, 107, 118, 130, 143, 157, 173, 190, 209, 230, 253, 279, 307, 337, 371, 408, 449, 494,
                     544, 598, 658, 724, 796, 876, 963, 1060, 1166, 1282, 1411, 1552, 1707, 1878, 2066, 2272, 2499,
                     2749, 3024, 3327, 3660, 4026, 4428, 4871, 5358, 5894, 6484, 7132, 7845, 8630, 9493, 10442, 11487,
                     12635, 13899, 15289, 16818, 18500, 20350, 22385, 24623, 27086, 29794, 32767]

    prevsample = 0
    previndex = 0

    Ns = len(raw_y)
    n = 0

    # raw_y = 32767 * raw_y  # 16 - bit operation
    for i in range(len(raw_y)):
        raw_y_1.append(32767*raw_y[i])

    while n < Ns:
        predsample = prevsample
        index = previndex
        step = StepSizeTable[index]  # MATLAB indexing starts at 1, python indexing starts at 0

        diff = raw_y_1[n] - predsample
        if diff >= 0:
            code = 0
        else:
            code = 2
            diff = -diff

        tempstep = step
        if diff >= tempstep:
            code = code | 1  # bitwise or

        diffq = step >> 1
        if code & 1:  # bitwise and
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

        if index < 0:
            index = 0
        if index > 88:
            index = 88

        prevsample = predsample
        previndex = index

        a = code & 3
        adpcm_y.append(a)
        n = n + 1
    return adpcm_y


# if __name__ == '__main__':
#     # a = [0.0012, 0.0015, 0.0078, 0.0056, 0.0045, 0.0023]
#     a = [6.1035e-05, 1.5259e-04, 2.1362e-04, 3.0518e-04, 3.6621e-04]
#     m = adpcm_encoder(a)
#     print(m)




