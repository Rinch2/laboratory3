list1 = []
stop = "stop"

for i in range(100):
    list1 += list(map(str, input("Слово: ").split()))
    if stop in list1:
        list1.remove("stop")
        break
end = ""
for word in list1:
    end = end + " " + word
print(end)