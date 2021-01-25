d = {"apple": '2', "ball": '1'}

print(sorted(d.items(), key = 
             lambda kv:(kv[1], kv[0]))) 