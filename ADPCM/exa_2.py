import encoder_2
import decoder_2
import math
import xlrd
import matplotlib.pyplot as plt


Y = [[6.1035e-03, 1.5259e-03, 2.1362e-03, 3.0518e-03, 3.6621e-03],
     [6.4035e-03, 1.5423e-03, 2.8712e-03, 3.8743e-03, 3.2999e-03]]
y = encoder_2.adpcm_encoder(Y)
YY = decoder_2.adpcm_decoder(y)
print(Y, end='\n')
print(y, end='\n')
print(YY, end='\n')
# plt.plot(range(len(Y)), Y, color='r', linestyle='-', label='')
# plt.plot(range(len(YY)), YY, color='g', linestyle='-', label='')
# plt.show()
wucha = []
for i in range(len(Y)):
     for j in range(len(Y[0])):
          wucha.append(math.fabs(YY[i][j]-Y[i][j]))
plt.plot(range(len(wucha)), wucha, color='r', linestyle='-', label='')
plt.show()
# rate = []
# for i in range(len(Y)):
#     if Y[i] != 0:
#         rate.append(wucha[i]/Y[i])
# plt.plot(range(len(rate)), rate, color='r', linestyle='-', label='')
# plt.show()





