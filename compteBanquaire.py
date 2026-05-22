
import sqlite3
class CompteBancaire(object):
    def __init__(self,Numcompte,proprio,solde):
        self.__Numcompte=Numcompte
        self.__proprio=proprio
        self.__solde=solde
    def versemment(self,sommeV):
        self.__solde=self.__solde+sommeV
        return self.__solde
    def retrait(self,sommeR):
        if self.__solde-sommeR<0:
            print('votre solde est insufisant pour effectuer cette opération\n')
        else:
            self.__solde=self.__solde-sommeR
            return self.__solde
    def agrio(self):
        self.__solde=self.__solde-(self.__solde*0.05)
        return self.__solde
    def afficher(self):
        print("les detailles du compte\n")
        print("\tLe numéro du compte: ",self.__Numcompte)
        print("\tLe propriétaire du compte: ",self.__proprio)
        print("\tLe solde courant du compte: ",self.__solde)

def creerLogfile():
    conn=sqlite3.connect('BaseDonnéesBank.db')
    cur=conn.cursor()
    cur.execute('create table logfile( ID integer primary key autoincrement,operation text not null,valeur number(5,2) not null,EtaCmpt number(5,2) not null)')
    conn.close()
def main():
    compte=CompteBancaire("C172","Zenab",1000000.0)
    conn=sqlite3.connect('BaseDonnéesBank.db')
    cur=conn.cursor()
    while(1):
        print("Taper 1 pour faire un versement\n")
        print("Taper 2 pour faire un retrait\n")
        print("Taper 3 pour appliqué l'agrio\n")
        print("Taper 4 pour afficher les detailles de compte\n")
        i=int(input("==>>"))
        if i==1:
            depot=float(input("Entrer le montant du dépot: "))
            compte.versemment(depot)
            print("L'opération éffectuer avec succès\nVotre nouveau solde est de ",compte._CompteBancaire__solde,"XOF")
            file=open("fichierTrace.txt","a")
            file.write("Depot#<"+str(depot)+"><"+str(compte._CompteBancaire__solde)+">\n")
            file.close()
            cur.execute('insert into logfile("operation","valeur","EtaCmpt") values("versement",?,?)',(depot,compte._CompteBancaire__solde))
            conn.commit
            conn.close()
        elif i==2:
            retrait=float(input("Entrer le montant à retirer: "))
            compte.retrait(retrait)
            print("L'opération éffectuer avec succès\nVotre restant solde est de ",compte._CompteBancaire__solde,"XOF")
            file=open("fichierTrace.txt","a")
            file.write("Retrait#<"+str(retrait)+"><"+str(compte._CompteBancaire__solde)+">\n")
            file.close()
            cur.execute('insert into logfile("operation","valeur","EtaCmpt") values("retrait",?,?)',(retrait,compte._CompteBancaire__solde))
            conn.commit
            conn.close()
        elif i==3:
            tmp=compte._CompteBancaire__solde
            compte.agrio()
            print("L'opération éffectuer avec succès\nLe nouveau solde du client est de",compte._CompteBancaire__solde,"XOF")
            file=open("fichierTrace.txt","a")
            file.write("Agrio#<"+str(tmp-compte._CompteBancaire__solde)+"><"+str(compte._CompteBancaire__solde)+">\n")
            file.close()
            cur.execute('insert into logfile("operation","valeur","EtaCmpt") values ("agrio",?,?)',(tmp-compte._CompteBancaire__solde,compte._CompteBancaire__solde))
            conn.commit
            conn.close()
        elif i==4:
            compte.afficher()
            file=open("fichierTrace.txt","a")
            file.write("<Info#>")
            file.close()
            cur.execute('insert into logfile("operation","valeur","EtaCmpt") values ("consultation","-",?)',compte._CompteBancaire__solde)
            conn.commit
            conn.close()
        else:
            print("Choix incorrect\n")
         
main()
                  
        
              
        
