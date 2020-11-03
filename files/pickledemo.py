import pickle 

def writedata():
    students={}
    students['student1']={'sno':1,'name':'Rahul','city':"Chennai"}
    students['student2']={'sno':2,'name':'Pramodh','city':"Mumbai"}
    students['student3']={'sno':3,'name':'Mani','city':"Mumbai"}

    dbfile = open('examplePickle', 'wb') 
      
    # source, destination 
    pickle.dump(students, dbfile)                      
    dbfile.close() 

def readdata():
    dbfile = open('examplePickle', 'rb')      
    db = pickle.load(dbfile) 
    for keys in db: 
        print(keys, '=>', db[keys]) 
    dbfile.close() 

writedata()
readdata()
    