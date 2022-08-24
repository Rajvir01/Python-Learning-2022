def rev_name(name, idx):
    if idx == len(name) - 1:
        print(name[idx])
        return
    else:
        idx +=1
        rev_name(name, idx)
        print(name[idx])


print(rev_name("raj", 0))