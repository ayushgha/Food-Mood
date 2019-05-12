
import time
import requests
from random import randint

flag = 0
import sys

import sqlite3

conn = sqlite3.connect('food.sqlite')
cur = conn.cursor()


if __name__=="__main__":
    emotion = "surprised"
    query = 'SELECT * FROM ' + str(emotion)

    list1 = []
    for i in cur.execute(query):
        list1.append(i[1])

    print(list1)
    count = 0
    for i in list1:
        if count == 5:
            count = 0
            time.sleep(60)
        count += 1

        randn = randint(0, 9)
        urlfood = 'https://api.edamam.com/search?q=' + str(i) + '&app_id=cdafc366&app_key=127a56f222287bfdf081bacc2e262d44&from=' + str(randn) + '&to=' + str(randn + 1)

        response = requests.get(urlfood)
        if response:
            print("Response", response)
            print("Word", i)
            print("URL=", urlfood)
            print(count)
            print(str(response.json()['hits'][0]['recipe']['label']))

            print((response.json()['hits'][0]['recipe']['totalNutrients']['FAT']['label']))
            print((response.json()['hits'][0]['recipe']['totalNutrients']['FAT']['quantity']))

            print((response.json()['hits'][0]['recipe']['totalNutrients']['CHOCDF']['label']))
            print((response.json()['hits'][0]['recipe']['totalNutrients']['CHOCDF']['quantity']))

            print((response.json()['hits'][0]['recipe']['totalNutrients']['FIBTG']['label']))
            print((response.json()['hits'][0]['recipe']['totalNutrients']['FIBTG']['quantity']))

            print((response.json()['hits'][0]['recipe']['totalNutrients']['PROCNT']['label']))
            print((response.json()['hits'][0]['recipe']['totalNutrients']['PROCNT']['quantity']))

            print((response.json()['hits'][0]['recipe']['totalNutrients']['NA']['label']))
            print((response.json()['hits'][0]['recipe']['totalNutrients']['NA']['quantity']))


            print((response.json()['hits'][0]['recipe']['totalNutrients']['CA']['label']))
            print((response.json()['hits'][0]['recipe']['totalNutrients']['CA']['quantity']))

            print((response.json()['hits'][0]['recipe']['totalNutrients']['MG']['label']))
            print((response.json()['hits'][0]['recipe']['totalNutrients']['MG']['quantity']))

            print((response.json()['hits'][0]['recipe']['totalNutrients']['K']['label']))
            print((response.json()['hits'][0]['recipe']['totalNutrients']['K']['quantity']))

            print((response.json()['hits'][0]['recipe']['totalNutrients']['P']['label']))
            print((response.json()['hits'][0]['recipe']['totalNutrients']['P']['quantity']))

            print((response.json()['hits'][0]['recipe']['totalNutrients']['VITC']['label']))
            print((response.json()['hits'][0]['recipe']['totalNutrients']['VITC']['quantity']))

            print((response.json()['hits'][0]['recipe']['totalNutrients']['FE']['label']))
            print((response.json()['hits'][0]['recipe']['totalNutrients']['FE']['quantity']))




            try:
                with open("nutrients_surprised.txt", "a") as f:

                    f.write('[')
                    f.write(str(response.json()['hits'][0]['recipe']['label']))
                    f.write(', ')

                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['FAT']['label']))
                    f.write(" : ")
                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['FAT']['quantity']))
                    f.write(', ')

                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['CHOCDF']['label']))
                    f.write(" : ")
                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['CHOCDF']['quantity']))
                    f.write(', ')

                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['FIBTG']['label']))
                    f.write(" : ")
                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['FIBTG']['quantity']))
                    f.write(', ')

                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['PROCNT']['label']))
                    f.write(" : ")
                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['PROCNT']['quantity']))
                    f.write(', ')

                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['NA']['label']))
                    f.write(" : ")
                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['NA']['quantity']))
                    f.write(', ')

                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['CA']['label']))
                    f.write(" : ")
                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['CA']['quantity']))
                    f.write(', ')

                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['MG']['label']))
                    f.write(" : ")
                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['MG']['quantity']))
                    f.write(', ')

                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['K']['label']))
                    f.write(" : ")
                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['K']['quantity']))
                    f.write(', ')

                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['P']['label']))
                    f.write(" : ")
                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['P']['quantity']))
                    f.write(', ')

                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['VITC']['label']))
                    f.write(" : ")
                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['VITC']['quantity']))
                    f.write(', ')

                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['FE']['label']))
                    f.write(" : ")
                    f.write(str(response.json()['hits'][0]['recipe']['totalNutrients']['FE']['quantity']))
                    f.write(']')

                    f.write('\n\n')

            except:
                pass

            print("_________________________________________________")

exit(0)