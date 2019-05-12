import re
with open("nutrients_happy.txt", "r+") as f:

    print("Output of Read function is ")
    r = (list(f))

y1= []
# Carbs : ([0-9].*), Fiber : ([0-9].*), Protein : ([0-9].*), Sodium : ([0-9].*), Calcium : ([0-9].*), Magnesium : ([0-9].*), Potassium : ([0-9]*), Phosphorus : ([0-9].*), Vitamin C : ([0-9].*), Iron : ([0-9].*)'
for i in r:
    #print((i))
    y1.append(re.findall('Fat : ([0-9].*).*, Carbs : ([0-9].*).*, Fiber : ([0-9].*).*, Protein : ([0-9].*).*, Sodium : ([0-9].*).*, Calcium : ([0-9].*).*, Magnesium : ([0-9].*).*, Potassium : ([0-9]*).*, Phosphorus : ([0-9].*).*, Vitamin C : ([0-9].*).*, Iron : ([0-9].*)]',i))


print("y=",y1[0])

# ans = []
# for i in y1:
#     dict1 = {}
#     dict1['Fat'] = i[0][0]
#     dict1['Carbs'] = i[0][1]
#     dict1['Fiber'] = i[0][2]
#     dict1['Protein'] = i[0][3]
#     dict1['Sodium'] = i[0][4]
#     dict1['Calcium'] = i[0][5]
#     dict1['Magnesium'] = i[0][6]
#     dict1['Potassium'] = i[0][7]
#     dict1['Phosphorous'] = i[0][8]
#     dict1['Vitamin C'] = i[0][9]
#     dict1['Iron'] = i[0][10]
#     ans.append(dict1)

with open('nutrient_cal_happy.txt', 'a') as f:
    for i in y1:
        if len(i)==0:
            continue
        for j in (i[0]):
                f.write(j)
                f.write(',')
        f.write('\n')





    print("------------------")