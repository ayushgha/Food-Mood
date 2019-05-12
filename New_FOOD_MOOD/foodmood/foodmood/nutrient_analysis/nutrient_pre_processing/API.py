#angry(Stressed)= Calming food, Magnesium, pumpkin seeds, brown rice, avocado, black beans, nuts

#fear(Anxious)= Calming food like nuts, seeds, tofu, cheese, red meat, chicken, fish, turkey, oats, beans, lentils and eggs

#happy(cheerful)= Vitamin B6 like potatoes, chicken, eggs

#Sadness(Fed up)= Vitamin D like diary products, eggs, oily fish

#Surprised(Excited)= Whole grains, fish, chicken, low-fat diary, lentils,beans

#disgust = Omega3s
from random import randint

import time
import requests
flag = 0
import sys

import sqlite3

conn = sqlite3.connect('food.sqlite')
cur = conn.cursor()

#response = requests.get('https://api.edamam.com/search?q=potato&app_id=cdafc366&app_key=127a56f222287bfdf081bacc2e262d44&from=0&to=10').json()

#json_data = json.loads(response.text)
#print(response['hits'])

if __name__=="__main__":

    emotion = "disgust"
    query = 'SELECT * FROM '+str(emotion)

    list1 = []
    for i in  cur.execute(query):
        list1.append(i[1])

    print(list1)
    count = 0
    for i in list1:
        if count==5:
            count = 0
            time.sleep(60)
        count+=1

        randn = randint(0, 9)
        urlfood = 'https://api.edamam.com/search?q=' + str(i) + '&app_id=cdafc366&app_key=127a56f222287bfdf081bacc2e262d44&from=' + str(randn) + '&to=' + str(randn + 1)

        response = requests.get(urlfood)
        if response:
            print("Response",response)
            print("Word", i)
            print("URL=", urlfood)
            print(count)
            print(str(response.json()['hits'][0]['recipe']['label']))
            print((response.json()['hits'][0]['recipe']['ingredientLines']))
            with open("Disgust.txt", "a") as write_file:
                write_file.write('[')
                write_file.write(str(response.json()['hits'][0]['recipe']['label']))
                write_file.write(",")
                write_file.write(str(response.json()['hits'][0]['recipe']['image']))
                write_file.write(",")
                write_file.write(str(response.json()['hits'][0]['recipe']['healthLabels']))
                write_file.write(",")
                write_file.write(str((response.json()['hits'][0]['recipe']['ingredientLines'])))
                write_file.write(",")
                write_file.write(str(response.json()['hits'][0]['recipe']['calories']))
                write_file.write("]")
                write_file.write("\n\n")

            print("_________________________________________________")

exit(0)