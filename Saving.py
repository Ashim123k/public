import datetime
import pickle
import os
filename = "example.txt"
current_directory = os.getcwd()
filepath = os.path.join(current_directory, filename)
d={}

def insert(order, order_value,charge):
    global d
    global order_id
    order_id=0
    key=counting()
    if key ==None:
        order_id=1
    else:
        order_id=1+key
    order_date= datetime.date.today()
    di = {order_id: (order,order_value,order_date,charge)}
    if not os.path.exists(filepath):
        with open('example.txt', 'wb+') as f:
            while True:
                try:
                    d=pickle.load(f)
                except EOFError:
                    break
            d.update(di)
            pickle.dump(d, f)
            print('Congratulation', 'Data saved succesfully')
    elif os.stat(filename).st_size==0:
        with open('example.txt', 'wb+') as f:
            while True:
                try:
                    d = pickle.load(f)
                except EOFError:
                    break

            d.update(di)
            pickle.dump(d, f)
            print('Congratulation', 'Data saved succesfully')

    else:
        with open('example.txt', 'rb+') as f:
            while True:
                try:
                    d=pickle.load(f)
                except EOFError:
                    break
            d.update(di)
            pickle.dump(d, f)
            print('instruction', 'data saved successfully')
def counting():
    try:
        if not os.path.getsize(filepath):
            print("None ")
        else:
            with open('example.txt', "rb+") as f:
                keys_count = 0
                # unpickler = pickle.Unpickler(f)
                while True:
                    try:
                        data = pickle.load(f)
                    except EOFError:
                        break
                    # Count the number of keys in the unpickled dictionary
                    keys_count = len(data.keys())
                return keys_count


    except FileNotFoundError:
        return
def load(option):
    totals=0
    global datz
    if os.path.getsize(filepath) == 0:
        print("Nothing")
    else:
        f = open('example.txt', 'rb')
        # unpickler = pickle.Unpickler(f)
        # print(unpickler)
        print("Order ID\t\tDate\tTotal Amount Paid(AUD)\tType of Order")
        de={}
        while True:
            try:
                datz = pickle.load(f)
                de.update(datz)
            except EOFError:
                break
        key_list = list(de.keys())
        for key in key_list:
            mixed_data = de[key]
            value_ord = mixed_data[1]
            dates = mixed_data[2]
            total = mixed_data[3]
            if mixed_data[1]==option:
                print('S00' + str(key), '\t\t\t', dates, '\t\t', total, '\t\t\t\t', value_ord)


            # Count the number of keys in the unpickled dictionary

        f.close()
def kalls(option):
    totals = 0
    global dats
    if os.path.getsize(filepath) == 0:
        print("Nothing")
    else:
        f = open('example.txt', 'rb')
        # unpickler = pickle.Unpickler(f)
        print("Order ID\t\tDate\tTotal Amount Paid(AUD)\tType of Order")
        db={}
        while True:
            try:
                dats = pickle.load(f)
                db.update(dats)
            except EOFError:
                break
        key_list = list(db.keys())
        for key in key_list:
            mixed_data = db[key]
            sid = mixed_data[1]
            dates = mixed_data[2]
            total = mixed_data[3]
            print('S00' + str(key), '\t\t\t', dates, '\t\t', total, '\t\t\t\t', sid)




def whole(option):
    totals = 0
    global datx
    if os.path.getsize(filepath) == 0:
        print("Nothing")
    else:
        f = open('example.txt', 'rb')
        # unpickler = pickle.Unpickler(f)
        dx={}
        while True:
            try:
                datx = pickle.load(f)
                dx.update(datx)
            except EOFError:
                break
        key_list = list(dx.keys())
        for key in key_list:
            mixed_data = datx[key]
            total = mixed_data[3]
            totals += total
            # Count the number of keys in the unpickled dictionary
        print('Total amount spend on all orders:',totals)
        f.close()
