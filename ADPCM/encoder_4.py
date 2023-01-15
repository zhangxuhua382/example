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
    Ns_3 = len(raw_y[0][0])
    Ns_4 = len(raw_y[0][0][0])


    raw_y_4 = []
    for i in range(len(raw_y)):
        raw_y_3 = []
        for j in range(len(raw_y[0])):
            raw_y_2 = []
            for k in range(len(raw_y[0][0])):
                raw_y_1 = []
                for m in range(len(raw_y[0][0][0])):
                    raw_y_1.append(32767*raw_y[i][j][k][m])
                raw_y_2.append(raw_y_1)
            raw_y_3.append(raw_y_2)
        raw_y_4.append(raw_y_3)


    adpcm_y_4 = []
    n_1 = 0
    while n_1 < Ns_1:
        adpcm_y_3 = []
        n_2 = 0
        while n_2 < Ns_2:
            adpcm_y_2 = []
            n_3 = 0
            while n_3 < Ns_3:
                adpcm_y_1 = []
                n_4 = 0
                while n_4 < Ns_4:
                    predsample = prevsample
                    index = previndex
                    step = StepSizeTable[index]  # MATLAB索引从1开始，python索引从0开始

                    diff = raw_y_4[n_1][n_2][n_3][n_4] - predsample
                    if diff >= 0:
                        code = 0
                    else:
                        code = 8
                        diff = -diff

                    tempstep = step
                    if diff >= tempstep:
                        code = code | 4  # 按位或
                        diff = diff - tempstep
                    tempstep = tempstep >> 1  # 按位移动指定位置
                    if diff >= tempstep:
                        code = code | 2
                        diff = diff - tempstep
                    tempstep = tempstep >> 1
                    if diff >= tempstep:
                        code = code | 1

                    diffq = step >> 3
                    if code & 4:  # 按位与
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
                    n_4 = n_4 + 1
                adpcm_y_2.append(adpcm_y_1)
                n_3 = n_3 + 1
            adpcm_y_3.append(adpcm_y_2)
            n_2 = n_2 + 1
        adpcm_y_4.append(adpcm_y_3)
        n_1 = n_1 + 1
    return adpcm_y_4



# if __name__ == '__main__':
#     raw_y = [[[[0.1214, -0.0445, 0.0061],
#                [0.1092, -0.1432, 0.1516],
#                [-0.0278, 0.1210, 0.0510]],
#               [[0.0006, 0.0971, 0.0557],
#                [0.0828, -0.0429, 0.0162],
#                [-0.0052, 0.0493, 0.0208]],
#               [[0.1918, 0.1038, -0.0256],
#                [-0.1064, -0.0040, -0.0572],
#                [-0.0488, 0.0295, 0.1348]]],
#              [[[-0.0228, 0.1648, -0.0724],
#                [-0.1267, 0.0514, 0.1671],
#                [-0.0200, -0.0108, 0.0891]],
#               [[0.0250, 0.0364, 0.1011],
#                [0.0880, -0.1373, -0.0756],
#                [0.1329, 0.0309, 0.0450]],
#               [[0.1861, 0.1192, 0.0768],
#                [0.1852, -0.1679, 0.0314],
#                [0.0518, -0.0318, -0.0897]]]]
#     y = adpcm_encoder(raw_y)
#     print(y)










