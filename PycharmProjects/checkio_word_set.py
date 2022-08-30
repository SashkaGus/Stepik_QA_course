def checkio(words_set):
    while words_set:
        val = max(words_set, key=len)
        words_set.remove(val)
        if words_set:
            for i in words_set:
                if val.endswith(i):
                    return True
    return False                

print(checkio({"hello", "lo", "he"}))            # == True
print(checkio({"hello", "la", "hellow", "cow"})) # == False
print(checkio({"walk", "duckwalk"})            ) # == True
print(checkio({"one"})                         ) # == False
print(checkio({"helicopter", "li", "he"})      ) # == False
print(checkio(["hello", "lo", "he"])      )      # == True
   