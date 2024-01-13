def countSeniors(details):
    count= 0
    for item in details:
        print(item[11:13])
        print(int(item[11:13]))
        if int(item[11:13]) > 6:
            count+=1
    # count = [count+=1 for item in details if int(item[11:13]) > 65]
     
    return count

print(countSeniors(["5612624052M0130","5378802576M6424","5447619845F0171","2941701174O9078"]))
