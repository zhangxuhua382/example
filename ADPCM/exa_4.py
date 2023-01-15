import encoder_4
import decoder_4
import math
import matplotlib.pyplot as plt


Y = [[[[0.1214, -0.0445, 0.0061],
       [0.1092, -0.1432, 0.1516],
       [-0.0278, 0.1210, 0.0510]],
      [[0.0006, 0.0971, 0.0557],
       [0.0828, -0.0429, 0.0162],
       [-0.0052, 0.0493, 0.0208]],
      [[0.1918, 0.1038, -0.0256],
       [-0.1064, -0.0040, -0.0572],
       [-0.0488, 0.0295, 0.1348]]],
     [[[-0.0228, 0.1648, -0.0724],
       [-0.1267, 0.0514, 0.1671],
       [-0.0200, -0.0108, 0.0891]],
      [[0.0250, 0.0364, 0.1011],
       [0.0880, -0.1373, -0.0756],
       [0.1329, 0.0309, 0.0450]],
      [[0.1861, 0.1192, 0.0768],
       [0.1852, -0.1679, 0.0314],
       [0.0518, -0.0318, -0.0897]]]]
y = encoder_4.adpcm_encoder(Y)
YY = decoder_4.adpcm_decoder(y)
print(Y, end='\n')
print(y, end='\n')
print(YY, end='\n')
# plt.plot(range(len(Y)), Y, color='r', linestyle='-', label='')
# plt.plot(range(len(YY)), YY, color='g', linestyle='-', label='')
# plt.show()

def ListTransform(list):
    try:
        for sublist in list:
            for element in ListTransform(sublist):
                yield element
    except TypeError:
        yield list
Y_原 = []
for num in ListTransform(Y):
    Y_原.append(num)
print(Y_原, '222')

wucha = []
for i in range(len(Y)):
     for j in range(len(Y[0])):
         for k in range(len(Y[0][0])):
             for m in range(len(Y[0][0][0])):
                wucha.append(math.fabs(YY[i][j][k][m]-Y[i][j][k][m]))
plt.plot(range(len(wucha)), wucha, color='g', linestyle='-', label='')
plt.plot(range(len(Y_原)), Y_原, color='r', linestyle='-', label='')
plt.show()
# rate = []
# for i in range(len(Y)):
#     if Y[i] != 0:
#         rate.append(wucha[i]/Y[i])
# plt.plot(range(len(rate)), rate, color='r', linestyle='-', label='')
# plt.show()





