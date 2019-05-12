import pandas as pd
from collections import Counter

col = ['Emotion', 'Percentage']
emotion = pd.read_csv('C:/Users/user/PycharmProjects/Ayush_FoodMood/foodmood/foodmood/emotion_recorded.csv',header=None, names=col )

#print(emotion.head())
my_emotion = (list(emotion['Emotion'].values))
my_values = (list(emotion['Percentage'].values))

c = dict(Counter(my_emotion))
#print(c)

e = []
for i,j in c.items():
    e.append([i,j])

#print(e)

e.sort(key=lambda x:x[1], reverse=True)
print(e)

my_final_emotion = e[0][0]

if my_final_emotion =='Neutral':
    my_final_emotion = e[1][0]


print(my_final_emotion)


