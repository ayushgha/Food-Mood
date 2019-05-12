import sqlite3

conn = sqlite3.connect('food.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS angry
    (SrNo TEXT, fooditem TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS fear
    (SrNo TEXT, fooditem TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS happy
    (SrNo TEXT, fooditem TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS sad
    (SrNo TEXT, fooditem TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS surprised
    (SrNo TEXT, fooditem TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS disgust
    (SrNo TEXT, fooditem TEXT)''')

angry = ['seeds','carrots','milk','yogurt','beans','blueberries','pistachios','nuts','whole%20grain','dark%20chocolates','green%20tea','Avocado','Banana','Green%20leafy%20vegetables','fish']

fear = ['seeds', 'oats', 'beans', 'lentils', 'eggs', 'whole grain food', 'blueberries', 'seaweed', 'chocolate', 'spinach', 'orange', 'nuts', 'Tea', 'coconut', 'tofu', 'cheese', 'red meat', 'chicken', 'fish', 'turkey']

happy = ['potato', 'cheese', 'red pepper', 'coconut', 'chocolate', 'seeds', 'beef', 'yogurt', 'asparagus', 'honey', 'tomato', 'chicken', 'Olive oil', 'spinach', 'flaxseed', 'salmon', 'crab', 'Banana', 'peas', 'sprouts', 'raisins', 'avocado', 'eggs', 'apricots', 'brocoli', 'lemons', 'tuna', 'nuts', 'mushroom', 'coffee', 'lentils', 'brown rice', 'oranges', 'beans', 'butter', 'whole%20grain%20food', 'seaweed', 'tea', 'blueberries', 'red%20wine']

sad = ['diary', 'flaxseeds', 'nuts', 'salmon', 'tea', 'olive%20oil', 'avocado', 'leafy%20vegetables', 'oranges', 'dark%20chocolates', 'chicken', 'eggs', 'chickpeas', 'rice', 'fish', 'sweet%20potato', 'oats', 'beans', 'peas', 'lentils', 'banana']

surprised = ['whole%20grain%20food', 'fish', 'chicken', 'diary', 'beans', 'lentils']

disgust = ['flaxseeds', 'salmon', 'fish', 'tuna']

for every in range(0,len(angry)):
    cur.execute('insert into angry (SrNo, fooditem) values (?,?)',(str(every),str(angry[every]),))

for every in range(0,len(fear)):
    cur.execute('insert into fear (SrNo, fooditem) values (?,?)',(str(every),str(fear[every]),))

for every in range(0,len(happy)):
    cur.execute('insert into happy (SrNo, fooditem) values (?,?)',(str(every),str(happy[every]),))

for every in range(0,len(sad)):
    cur.execute('insert into sad (SrNo, fooditem) values (?,?)',(str(every),str(sad[every]),))

for every in range(0,len(surprised)):
    cur.execute('insert into surprised (SrNo, fooditem) values (?,?)',(str(every),str(surprised[every]),))

for every in range(0,len(disgust)):
    cur.execute('insert into disgust (SrNo, fooditem) values (?,?)',(str(every),str(disgust[every]),))


conn.commit()
cur.close()


