#! /usr/bin/python3.8

print("Ievadiet skaitli")
# a=2**200000
#pildot int(input()) "bez izmēģinājuma" programma var vienkārši izlidot...
#tāpēc lai neizlidot  mēs izmantosim try...except...finally konstrukciju
paziime = False
while not paziime:
    try:
        a=int(input())
        paziime = True
    except:
        print("Diemzēl, cienijamais lietotāj, to kas ievadīts nevar pārveidot ",\
              "par vesela tipa skaitli")
        print("Lūdzu, ievadi s_k_a_i_t_l_i velreiz" )
#if (a == int): print("a**100")
if (a == 5):
    print(a**100)
    print("Aprēkins ir gatavs")
print ("Šis teksts atrodās ārpus darbibu bloka - pierakstīts bez",\
" atstarpēm priekšā, tāpēc tas paradisies jebkura gadijuma")

#print ("Ievadāmai vērtībai jābūt skaitlim")
#b=a**100
