import os
uzantı=input("Hangisine bakmak istiyorsun?")
for i in os.listdir("C:/Users/ogr2/Desktop"): #listenin elemanlarına tek tek ulaşmak için.
    if i.endswith(uzantı):
        print(i)

