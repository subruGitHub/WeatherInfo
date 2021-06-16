# Press Shift+F10 to execute it or replace it with your code.
import matplotlib.pyplot as plt
import numpy as np
import pymongo

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Weather in Chennai: 30')
    x = np.random.normal(170,10,250)
    plt.hist(x)
    plt.show()


# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  # print(x)

print("All over")
