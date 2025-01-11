def tanga_lis(lis1,lis2):
    miqdor=[3,3]

    for i in range(len(lis1)):
        birinchi = lis1[i].lower()
        ikkinchi = lis2[i].lower()

        if birinchi not in ["share", "steal"] or ikkinchi not in["share", "steal"]:
            return "Faqat share va steal sozlarini"
        
        if birinchi == "share" and ikkinchi == "share":
            miqdor[0] += 2
            miqdor[1] += 2
        elif birinchi == "share" and ikkinchi == "steal":
            miqdor[0] -= 1
            miqdor[1] += 3
        elif birinchi == "steal" and ikkinchi == "share":
            miqdor[0] += 3
            miqdor[1] -= 1
        elif birinchi == "steal" and ikkinchi == "steal":
            miqdor[0] += 0 
            miqdor[1] += 0
    return miqdor
    
lis1 = ["share", "share", "share"]
lis2 = ["steal", "share", "steal"]

natija = tanga_lis(lis1, lis2)
print(natija)
        
        
