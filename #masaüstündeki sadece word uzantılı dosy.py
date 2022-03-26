#masaüstündeki sadece word uzantılı dosyaları ekrana yazdırınız

import os
for i in os.listdir("C:/Users/ogr2/Desktop"): #listenin elemanlarına tek tek ulaşmak için.
    if i.endswith(".docx"):
        print(i)