import numpy as np
import datetime
import os
import csv
import typing
import numpy as np
import matplotlib.pyplot as plt

#variable pour compter les sources 
a = int
a=0
b = int
b=0
c = int
c=0
d = int
d=0
e = int
e=0
f = int
f=0
g = int
g=0
h = int
h=0
i = int
i=0
k=int
k=0
l=int
l=0

m=int
m=0

n=int
n=0
p=int
p=0





try:
    with open("DumpFile.txt", encoding="utf8") as fh:
        res=fh.read()
except:
        print("Le fichier n'existe pas %s", os.path.abspath('fichieratraiter.txt'))
ress=res.split('\n')

tableau_evenements=np.array([])
fichier=open("graphique.csv", "w")#test est le fichier d'arrivée des extractions
evenement = "DATE ; SOURCE ; PORT ; DESTINATION ; FLAG ; SEQ ; ACK ; WIN ; OPTIONS ; LENGTH" #intitulé de mes colonnes
fichier.write(evenement + "\n") #écriture de mes titres dans le tableur
characters = ":" #définir une variable avec le caractère ":" (qui nous sera utile pour la suite)
for event in ress:
        if event.startswith('11:42'): #évenement qui commence par "11:42" (ils commencent tous par 11:42)
            #déclaration variables et remise à zéro
            sequence = ""
            heure1 = ""
            nomip = ""
            port = ""
            flag = ""
            ack = ""
            win = ""
            options = ""
            length = ""
            #Pour la date de l'évenement (première colonne)
            texte=event.split(" ")
            heure1=texte[0]
            #Pour la source (2ème colonne) 
            texte=event.split(" ")
            AdrIP1=texte[2].split(".")
            if len(AdrIP1) == 2:
                nomip=AdrIP1[0]
            if len(AdrIP1) == 3:
                nomip=AdrIP1[0]+ "." +AdrIP1[1]
            if len(AdrIP1) == 4:
                nomip=AdrIP1[0]+ "." +AdrIP1[1]+ "." +AdrIP1[2] 
            if len(AdrIP1) == 5:
                nomip=AdrIP1[0]+ "." +AdrIP1[1]+ "." +AdrIP1[2]+ "." +AdrIP1[3]
            if len(AdrIP1) == 6:
                nomip=AdrIP1[0]+ "." +AdrIP1[1]+ "." +AdrIP1[2]+ "."+AdrIP1[3]+"."+ AdrIP1[4]
            
            #port
            if len(texte) > 1: 
                port1=texte[2].split(".")
                port=port1[-1]
            #Pour la destination (3ème colonne)
            texte=event.split(" ")
            nomip2=texte[4]
            # Flag
            texte=event.split("[") #On coupe à partir du crochet
            if len(texte) > 1: #s'il y a plus de une partie à partir du crochet
                flag1=texte[1].split("]") #on prend après le premier crochet et on coupe au deuxième crochet
                flag=flag1[0]#pourquoi 0 ? Car on prend la partie de gauche du deuxième crochet (ce qu'on recherche)
            #seq
            texte=event.split(",")#on coupe à la virgule
            if len(texte) > 1: #s'il y a plus de 1 partie à partir du crochet
                if texte[1].startswith(" seq"): #Si le texte [1] commence par " seq"
                    seq1=texte[1].split(" ") #on coupe à l'espace et on prend le texte juste après
                    sequence=seq1[2] #On a 2 parties entre le split ',' et ce que je recherche
            #ack
            if len(texte) > 2: #
                if texte[2].startswith(" ack"): #Si le texte [2] commence par "ack"
                    ack1=texte[2].split(" ") #on coupe à l'espace et on prend le texte juste après
                    ack=ack1[2] #On a 2 parties entre le split ',' et ce que je recherche
                #si la partie "seq" est absente :
                if texte[1].startswith(" ack"): #Si le texte [1] commence par " ack"
                    ack1=texte[1].split(" ") #on coupe à l'espace et on prend le texte juste après
                    ack=ack1[2] #On a 2 parties entre le split ',' et ce que je recherche
            #win
            if len(texte) > 3: #si le nombre de partie est supérieur à 3
                #si "ack" est présent 
                if texte[3].startswith(" win"): #Si le texte [3] commence par " win"
                    win1=texte[3].split(" ") #on coupe à l'espace et on prend le texte juste après
                    win=win1[2] #On prend le texte après l'espace (la partie qu'on retrouvera dans le tableau)
                #si "ack" n'est pas présent
                if texte[2].startswith(" win"): #Si le texte [2] commence par " win"
                    win1=texte[2].split(" ") #on coupe à l'espace et on prend le texte juste après
                    win=win1[2]#On prend le texte après l'espace (la partie qu'on retrouvera dans le tableau
            #options
            texte=event.split("[") #On coupe à partir du crochet
            if len(texte) > 2: #
                options1=texte[2].split("]") #On part du premier "[" et on a texte [2] pour arriver à ce qu'on souhaite récupérer 
                options=options1[0]#pourquoi 0 ? Car on prend la partie à gauche du deuxième crochet "]"
            
            #length (avec option)
            texte=event.split("]") 
            if len(texte) > 2: #vérifier le nombre de partie (split au crochet)
                    length1=texte[2].split(" ") #on part du premier "[" et ce qu'on recherche est bien dans texte [2]. On split à l'espace pour avoir que le nombre
                    length=length1[2] #On veut bien le "2" pour avoir que le nombre (il y a une partie avant l'espace + une autre après).
            #length (sans option)
            texte=event.split(",")
            if len(texte) > 3:
                if texte[3].startswith(" length"): #Si ça commence par " length" et on recherche dans le texte [3]
                    length1=texte[3].split(" ") #on coupe à l'espace
                    length=length1[2] ##On veut bien le "2" pour avoir que le nombre (texte [1] avant l'espace c'est le mot "length").
                    length = length.replace(characters,"")#remplacement du "characters" en " " (pour éviter que le tableur écrit sous forme de date)
            if event.startswith("11:42:55.536521") : #dès que le programme arrive à la dernière ligne du fichier texte
                prog=0 #il ne fait plus de tour, il s'arrete
            evenement=heure1+";"+nomip+ ";" +port+ ";" + nomip2+ ";"+flag+ ";" +sequence+ ";" +ack+ ";" +win+ ";" +options+ ";" +length
            fichier.write(evenement + "\n") #on écrire "evenement" dans le csv et \n pour revenir à la ligne (pour ne pas écrire sur la même ligne)

            #avoir le nombre de fois que chaque source reviens 

            if nomip=="BP-Linux8":
                a = a + 1
                
            if nomip=="ns1.lan.rt":
                b=b+1
            
            if nomip=="190-0-175-100.gba.solunet.com.ar":
                c=c+1
            
            if nomip=="par21s04-in-f4.1e100.net":
                d=d+1

            if nomip=="www.aggloroanne.fr":
                e=e+1
                
            if nomip=="mauves.univ-st-etienne.fr":
                f=f+1
                
            if nomip=="par10s38-in-f3.1e100.net":
                g=g+1
                
            if nomip=="par21s23-in-f10.1e100.net":
                h=h+1
            
            if nomip=="par21s23-in-f2.1e100.net":
                i=i+1
             
             # Avoir le nombre de voir qu'apparait les différents flag   
             
            if flag=="P.":
                k = k+1
            if flag=="S":
                l = l+1
            if flag==".":
                m = m+1
            if flag=="":
                n = n+1
            if flag=="F.":
                p = p+1
                
            
                
#Graphique Source
   
x=["www.aggloroanne.fr","ns1.lan.rt","BP-Linux8","190-0-175-100.gba.solunet.com.ar","par21s04-in-f4.1e100.net","mauves.univ-st-etienne.fr","par10s38-in-f3.1e100.net","par21s23-in-f10.1e100.net","par21s23-in-f2.1e100.net"]               
y=[e,b,a,c,d,f,g,h,i]
fig, ax = plt.subplots(figsize=(20,10))   
ax.set_yticks(np.arange(0,4000,400))
ax.set_title ("Source", color="#000000", y=1.05)
fig.autofmt_xdate(rotation=90)
ax.bar(x, y)


#Graphique Flag

fig.savefig("longueur.png", dpi=300 , bbox_inches="tight")

x=[".","F.","P.","S","Vide"]
y=[m,p,k,l,n]
fig, ax = plt.subplots(figsize=(20,10))   
ax.set_yticks(np.arange(0,7500,500))
ax.set_title ("FLAG", color="#000000", y=1.05)

ax.bar(x, y)


fig.savefig("flag.png", dpi=300 , bbox_inches="tight")

#Graphique destination

x=["184.107.43.74","BP-Linux8.34862","mauves.univ-st-etienne.fr","www.aggloroanne.fr","BP-Linux8.40678","BP-Linux8.53324","BP-Linux8.53325","BP-Linux8.53328","BP-Linux8.53329","BP-Linux8.40682"]               
y=[2000,827,251,1022,383,499,385,352,324,400]
fig, ax = plt.subplots(figsize=(20,10))   
ax.set_yticks(np.arange(0,4000,400))
ax.set_title ("DDOS", color="#000000", y=1.05)
fig.autofmt_xdate(rotation=90)
ax.bar(x, y)


fig.autofmt_xdate(rotation=65)





fig.savefig("longueurr.png", dpi=300 , bbox_inches="tight")


plt.show()




fichier.close()



