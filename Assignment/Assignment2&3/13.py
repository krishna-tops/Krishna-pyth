#first to take a default dictionary
dic1 = {"take":1,"mix":2,"ready":3,"serve":4}
#we make acending and decending using lambda
ascendingorder = dict(sorted(dic1.items(), key=lambda x: x[1]))
decendingorder = dict(sorted(dic1.items(), key=lambda x: x[1], reverse=True))
#print the acending and decending
print("Ascending :", ascendingorder)
print("Descending :", decendingorder)
