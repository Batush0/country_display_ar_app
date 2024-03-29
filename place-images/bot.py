import os

# def dosya_isimleri_al(klasor_yolu):
#     dosya_isimleri = ""
#     for dosya in os.listdir(klasor_yolu):
#             ayristirma = dosya.split(".");
#             dosya_ad = ayristirma[0].split("_")[0];
#             if(dosya_ad not in dosya_isimleri): 
#                 dosya_isimleri +=f"----- {dosya_ad}\n"
#             dosya_isimleri += "{\"image_format\":\"" + ayristirma[1] + "\"},\n"
#     return dosya_isimleri

# klasor_yolu = "./"
# dosya_isimleri = dosya_isimleri_al(klasor_yolu)
# print(dosya_isimleri)

for dosya in os.listdir("./"):
    if(dosya == "bot.py"):
        continue
    ayrik = dosya.split(".");
    ayrik[0] = ayrik[0] + ".preview."
    os.rename(dosya,"".join(ayrik))