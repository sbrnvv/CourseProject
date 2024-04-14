import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from matplotlib import pyplot as plt

zp1 = pd.read_csv("https://raw.githubusercontent.com/sbrnvv/CourseProject/main/2000-2016(1).csv", delimiter=';', on_bad_lines='skip')
zp2 = pd.read_csv("https://raw.githubusercontent.com/sbrnvv/CourseProject/main/2017-2023(1).csv", delimiter=';', on_bad_lines='skip')
years1 = zp1.columns[1:].astype(int)
zp1o = zp1[zp1['Отрасли'] == 'Образование'].values[0][1:]
years2 = zp2.columns[1:-1].astype(int)
zp2o = zp2[zp2['Отрасль'] == 'образование'].values[0][1:-1]
zp2o[0] = int(zp2o[0])
zpo = np.concatenate((zp1o, zp2o))
years = np.concatenate((years1, years2))
fig1, pl1 = plt.subplots()
pl1.set_title('Изменение среднемесячной номинальной заработной платы в сфере образования с 2000 года')
pl1.set_xlabel('Год')
pl1.set_ylabel('Среднемесячная номинальная зара ботная плата')
pl1.plot(years, zpo, '-')


#график по сфере финансовой деятельности
zp1f = zp1[zp1['Отрасли'] == 'Финансовая деятельность'].values[0][1:]
zp2f = zp2[zp2['Отрасль'] == 'деятельность финансовая и страховая'].values[0][1:-1]
zp2f[0] = int(zp2f[0])
zpf = np.concatenate((zp1f, zp2f))
fig2, pl2 = plt.subplots()
pl2.set_title('Изменение среднемесячной номинальной заработной платы в сфере финансовой деятельности с 2000 года')
pl2.set_xlabel('Год')
pl2.set_ylabel('Среднемесячная номинальная заработная плата')
pl2.plot(years, zpf, '-')

#сравнение прироста зарплаты и процента инфляции
realzpo = []
for i in range((len(zpo)-2)):
    real = ((zpo[i+1] - zpo[i])/ zpo[i])*100
    realzpo.append(real)
i = pd.read_csv("https://raw.githubusercontent.com/sbrnvv/CourseProject/main/infl%202000-2023(1).csv", delimiter=';', on_bad_lines='skip')
yearsinfl = i.columns[1:].astype(int)
infl = i[i['Год'] == 'Всего'].values[0][1:]
fig3, plt1 = plt.subplots()
plt2 = plt1.twinx()
plt1.set_title("График изменения средней заработной платы в сфере образования по отношению к предыдущему году в сравнении с уровнем инфляции в этот год")
plt1.set_xlabel('Год')
plt1.set_ylabel('Процент')
plt1.plot(years[1:-1], realzpo, "-", color = 'b', label = 'Изменение средней зп                                ' )
plt2.plot(years[1:-1], infl[1:-1], "-", color = 'r', label = 'Инфляция' )
plt1.legend()
plt2.legend()

#сравнение прироста зарплаты и процента инфляции
realzpf = []
for i in range((len(zpf)-2)):
    real = ((zpf[i+1] - zpf[i])/ zpf[i])*100
    realzpf.append(real)
i = pd.read_csv("https://raw.githubusercontent.com/sbrnvv/CourseProject/main/infl%202000-2023(1).csv", delimiter=';', on_bad_lines='skip')
yearsinfl = i.columns[1:].astype(int)
infl = i[i['Год'] == 'Всего'].values[0][1:]
fig4, plt1 = plt.subplots()
plt2 = plt1.twinx()
plt1.set_title("График изменения средней заработной платы в сфере финансовой деятельности по отношению к предыдущему году в сравнении с уровнем инфляции в этот год")
plt1.set_xlabel('Год')
plt1.set_ylabel('Процент')
plt1.plot(years[1:-1], realzpf, "-", color = 'b', label = 'Изменение средней зп                                ' )
plt2.plot(years[1:-1], infl[1:-1], "-", color = 'r', label = 'Инфляция' )
plt1.legend()
plt2.legend()

#график по реальным и номинальным зп
i = pd.read_csv("https://raw.githubusercontent.com/sbrnvv/CourseProject/main/infl%202000-2023(1).csv", delimiter=';', on_bad_lines='skip')
infl = i[i['Год'] == 'Всего'].values[0][1:]
urinfl = []
for i in range(len(infl)):
    infl[i] = (infl[i]+100)/100
    urinfl.append(infl[i])
zporeal = []
for a in range(len(zpo)):
    zporeal.append(zpo[a]/urinfl[a])
fig5, pl5 = plt.subplots()
pl5.plot(years, zporeal, '-', color = 'r',label = 'Реальная зп' )
pl5.plot(years, zpo, '-', color = 'b',label = 'Номинальная зп')
pl5.legend()
pl5.set_title('График номинальной и реальной заработной платы в сфере образования с 2000г')
pl5.set_xlabel('Год')
pl5.set_ylabel('Средняя заработная плата')

#график по реальным и номинальным зп
zpfreal = []
for a in range(len(zpf)):
    zpfreal.append(zpf[a]/urinfl[a])
fig6, pl6 = plt.subplots()
pl6.plot(years, zpfreal, '-', color = 'r',label = 'Реальная зп')
pl6.plot(years, zpf, '-', color = 'b', label = 'Номинальная зп')
pl6.legend()
pl6.set_title('График номинальной и реальной заработной платы в сфере финансовой деятельности с 2000г')
pl6.set_xlabel('Год')
pl6.set_ylabel('Средняя заработная плата')

#разница между реальными и номинальными зп в образовании
razno = []
raznf = []
for j in range(len(zpf)):
    raznf.append(zpf[j]-zpfreal[j])
for i in range(len(zpo)):
    razno.append(zpo[i]-zporeal[i])
n = len(zpo)
r = np.arange(n)
width = 0.25
fig7, pl7 = plt.subplots()
pl7.bar(r, razno, color = 'b', width = width, edgecolor = 'black', label='Сфера образования')
pl7.bar(r + width, raznf, color = 'g', width = width, edgecolor = 'black', label='Сфера финансовой деятельности')
pl7.set_xlabel("Год, начиная с 2000")
pl7.set_ylabel("Разница в рублях")
pl7.set_title("Разница между реальными и номинальными зарплатами в обеих сферах")
pl7.legend()

st.title('Ну что там с деньгами?:money_with_wings:')
st.subheader('Или как менялись заработные платы в России с 2000 по 2023 год')

st.info('Основываясь на данных Росстата о "Среднемесячной номинальной начисленной'
' заработной плате работников организаций по видам экономической деятельности в Российской Федерации '
'за 2000-2023 гг.", я провела анализ изменения оплаты труда в двух наиболее интересных для меня сферах: '
' образовательной и финансовой деятельности и получила интересные, но вовсе не неожиданные результаты.')

st.markdown('Перед вами графики изменения средней номинальной заработной платы в обеих сферах:')

st.pyplot(fig1)
st.pyplot(fig2)

st.info('Не сложно заметить, что в обеих сферах среднемесячные номинальные зарплаты стабильно возрастают,'
' мы не наблюдаем как резких скачков, так и спадов.')

image = Image.open('infliation.jpg')
st.image(image, caption='А что насчет инфляции?')

st.markdown('Если сравнить процент повышения среднемесячной номинальной зарплаты по отношению к '
'предыдущему году и уровень инфляции за этот год, мы увидим нечто инересное:')

st.pyplot(fig3)
st.pyplot(fig4)

st.info('Выходит, что процент повышения заработной платы лишь изредко превышает уровень инфляции. '
'В большинстве же случаев, инфляция "съедает" повышение или вовсе превышает его. Получается, зарплата не растет?')

st.markdown('Чтобы ответить на этот вопрос, я подсчитала реальную среднемесячную зарплату'
' и сравнила ее с номинальной, вот что вышло:')

st.pyplot(fig5)
st.pyplot(fig6)

st.info('Действительно, в сфере как образовательной, так и финансовой деятельности, реальная зароботная плата'
' ниже номинальной, что хорошо видно на графиках. Таким образом, работники получают меньше "реальных денег",'
' чем должны. Критично ли это?')

st.markdown('Давайте разберемся! Перед вами столбчатая диаграмма, которая отражает разницу между номинальной'
' и реальной заработной платой для сфер образования и финансовой деятельности:')

st.pyplot(fig7)

st.info('Обратите внимание на сферу финансовой деятельности: ее работникам не позавидуешь! Разница очевидно'
' велика. В сфере образования ситуация складывается лучше. Несмотря на то, что работники все же недополучают,'
' зарплаты, разница мала. Вероятно, это связано с тем, что большинство работников - бюджетники(их зарплаты выделяются'
'из государственного бюджета), а потому доход более стабилен и реален, чем у работников независимых организаций.'
'Тем не менее, невозможно отрицать существование весомой разницы между номинальными и реальными заработными платами. '
'Вероятно, это сказывается не только на уровне жизни граждан, но и на их эмоциональном состоянии.')

st.markdown('Вот такое получилось исследование! Спасибо за внимание)')
st.balloons()
