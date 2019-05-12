import pandas as pd
import statistics
import matplotlib.pyplot as plt



col = ['Fat','Carbs','Fiber','Protein','Sodium','Calcium','Magnesium','Potassium','Phosphorous','Vitamin C','Iron']
df = pd.read_csv('nutrient_cal_disgust1.csv', header=None, names=col)
print(df.head())

fat = round(statistics.mean(list(df['Fat'])),2)
Carbs = round(statistics.mean(list(df['Carbs'])),2)
Fiber = round(statistics.mean(list(df['Fiber'])),2)
Protein = round(statistics.mean(list(df['Protein'])),2)
Sodium = round(statistics.mean(list(df['Sodium'])),2)
Calcium = round(statistics.mean(list(df['Calcium'])),2)
Magnesium = round(statistics.mean(list(df['Magnesium'])),2)
Potassium = round(statistics.mean(list(df['Potassium'])),2)
Phosphorous = round(statistics.mean(list(df['Phosphorous'])),2)
VitaminC = round(statistics.mean(list(df['Vitamin C'])),2)
Iron = round(statistics.mean(list(df['Iron'])),2)

print(fat)
print(Carbs)
print(Fiber)



total = [fat,Carbs,Fiber,Protein,Sodium/10,Calcium,Magnesium,Potassium/10,Phosphorous/10,VitaminC,Iron]
sum_total = sum(total)
print(sum_total)


pie_chart = []
for i in total:
    pie_chart.append((i/sum_total)*100)

plt.bar(col,pie_chart, color="green")
plt.xticks(col, rotation=25)
plt.xlabel('Nutrient')
plt.ylabel('Percentage of the nutrient')
plt.title('Nutrient Need in case of Happy emotions')
plt.show()


print(len(pie_chart),len(col))


