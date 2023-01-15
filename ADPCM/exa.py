import encoder
import decoder
import xlrd
import matplotlib.pyplot as plt

xl = xlrd.open_workbook(r'A1.xlsx')
table = xl.sheets()[0]
Y = table.col_values(0)  # 按列读取数据
# print(Y)
# print(len(Y))

y = encoder.adpcm_encoder(Y)
YY = decoder.adpcm_decoder(y)
# print(Y, end='\n')
print(len(Y), end='\n')
# print(y, end='\n')
# print(YY, end='\n')
print(len(YY), end='\n')
plt.plot(range(len(Y)), Y, color='r', linestyle='-', label='')
plt.plot(range(len(YY)), YY, color='g', linestyle='-', label='')
plt.show()
wucha = []
for i in range(len(Y)):
    wucha.append(YY[i]-Y[i])
plt.plot(range(len(wucha)), wucha, color='r', linestyle='-', label='')
plt.show()
rate = []
for i in range(len(Y)):
    if Y[i] != 0:
        rate.append(wucha[i]/Y[i])
plt.plot(range(len(rate)), rate, color='r', linestyle='-', label='')
plt.show()


