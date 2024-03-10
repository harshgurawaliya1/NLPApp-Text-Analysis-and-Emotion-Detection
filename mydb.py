import json

class Database:

    def add_data(self,name,email,password):

        with open('db.json','r') as rf:
            d1 = json.load(rf)

        if email in d1:
            return 0
        else:
            d1[email] = [name,password]
            with open('db.json','w') as wf:
                json.dump(d1,wf)
            return 1


    def search(self,email,password):

        with open('db.json','r') as df:
            d2 = json.load(df)

            if email in d2:
                if d2[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0