# 2D data encoding
def adpcm_encoder(raw_y):
    IndexTable = [-1, -1, -1, -1, 2, 4, 6, 8, -1, -1, -1, -1, 2, 4, 6, 8]

    StepSizeTable = [7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 19, 21, 23, 25, 28, 31, 34, 37, 41, 45, 50, 55, 60, 66, 73,
                     80, 88, 97, 107, 118, 130, 143, 157, 173, 190, 209, 230, 253, 279, 307, 337, 371, 408, 449, 494,
                     544, 598, 658, 724, 796, 876, 963, 1060, 1166, 1282, 1411, 1552, 1707, 1878, 2066, 2272, 2499,
                     2749, 3024, 3327, 3660, 4026, 4428, 4871, 5358, 5894, 6484, 7132, 7845, 8630, 9493, 10442, 11487,
                     12635, 13899, 15289, 16818, 18500, 20350, 22385, 24623, 27086, 29794, 32767]

    prevsample = 0
    previndex = 0

    Ns_1 = len(raw_y)
    Ns_2 = len(raw_y[0])

    raw_y_2 = []
    # raw_y = 32767 * raw_y  # 16 - bit operation
    for i in range(len(raw_y)):
        raw_y_1 = []
        for j in range(len(raw_y[0])):
            raw_y_1.append(32767*raw_y[i][j])
        raw_y_2.append(raw_y_1)

    adpcm_y_2 = []
    n_1 = 0
    while n_1 < Ns_1:
        adpcm_y_1 = []
        n_2 = 0
        while n_2 < Ns_2:
            predsample = prevsample
            index = previndex
            step = StepSizeTable[index]  # MATLAB indexing starts at 1, python indexing starts at 0

            diff = raw_y_2[n_1][n_2] - predsample
            if diff >= 0:
                code = 0
            else:
                code = 8
                diff = -diff

            tempstep = step
            if diff >= tempstep:
                code = code | 4  # bitwise or
                diff = diff - tempstep
            tempstep = tempstep >> 1  # Move the specified position bit by bit
            if diff >= tempstep:
                code = code | 2
                diff = diff - tempstep
            tempstep = tempstep >> 1
            if diff >= tempstep:
                code = code | 1

            diffq = step >> 3
            if code & 4:  # bitwise and
                diffq = diffq + step
            if code & 2:
                diffq = diffq + (step >> 1)
            if code & 1:
                diffq = diffq + (step >> 2)

            if code & 8:
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

            a = code & 15
            adpcm_y_1.append(a)
            n_2 = n_2 + 1
        adpcm_y_2.append(adpcm_y_1)
        n_1 = n_1 + 1
    return adpcm_y_2



# if __name__ == '__main__':
    # raw_y = [[1, 1, 0.5], [1, 1, 0.5]]
    # raw_y_2 = []
    # for i in range(len(raw_y)):
    #     raw_y_1 = []
    #     for j in range(len(raw_y[0])):
    #         raw_y_1.append(32767*raw_y[i][j])
    #     raw_y_2.append(raw_y_1)
    # print(raw_y_2)









