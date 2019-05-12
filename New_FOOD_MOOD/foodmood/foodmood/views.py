from django.http import HttpResponse
from django.shortcuts import render
#from . import finalise_emotion
import re
#emo = finalise_emotion.my_final_emotion
emo = 'Happy'


def home(request):
    return render(request,'home.html')

def recipe(request):

    label = []
    image = []
    healthlabels = []
    ingredients = []
    calories = []
    drive = 'C:/Users/user/PycharmProjects/Ayush_FoodMood/foodmood/foodmood/recipe_suggestion/'+str(emo)+'.txt'
    f = open(drive, 'r')
    file_content = f.read()
    file_content = (file_content.split('\n'))
    for line in file_content:
        print(line)
        my_line = list(line)
        count = 0
        word = ''
        flag = 0
        for i in range(0, len(my_line)):
            if count == 2:
                word += my_line[i]
                if my_line[i] == ']':
                    count += 1
                    healthlabels.append(word)
                    word = ''
                continue
            if count == 3:
                if my_line[i] == ',' and flag == 0:
                    flag = 1
                    continue
                else:
                    word += my_line[i]
                    if my_line[i] == ']':
                        count += 1
                        ingredients.append(word)
                        word = ''
                    continue
            if count == 4:
                if my_line[i] == ',':
                    continue
                else:
                    if my_line[i] == ']':
                        calories.append(word)
                        break;
                    word += my_line[i]
                    continue

            if my_line[i] != ',':
                word += my_line[i]

            else:
                if count == 0:
                    y = re.findall('.(.*)',word)
                    label.append(y[0])
                    print(label)
                    count += 1
                    word = ''
                    continue
                if count == 1:
                    image.append(word)
                    print(image)
                    count += 1
                    word = ''

    print(label)
    print()
    print(image)
    print()
    print(healthlabels)
    print()
    print(ingredients)
    print()
    print(calories)
    print()

    all_items = []
    for i in range(0, len(label)):
        all_items.append(
            {'label': label[i], 'image': image[i], 'healthlabels': healthlabels[i], 'ingredients': ingredients[i],
             'calories': calories[i]})
    display = [label, image, healthlabels, ingredients, calories]
    # print(all_items)

    for i in all_items:
        print(i)
        print()
    f.close()
    # context = {'file_content': file_content}
    context = {'display': all_items,'emo':emo}
    return render(request, 'recipe.html', context)


def food(request,x):
    return render(request,'food.html')