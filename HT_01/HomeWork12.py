'''
12. Write a script to concatenate following dictionaries to create a new one.
        Sample Dictionary:
        dic1 = {1: 10, 2: 20}
        dic2 = {3: 30, 4: 40}
        dic3 = {5: 50, 6: 60}
        Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
# look exercise number 10
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic2.update(dic3)
dic1.update(dic2)
print(dic1)
