import shelve
shelf_file = shelve.open('mydata')

shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']
shelf_file.close()