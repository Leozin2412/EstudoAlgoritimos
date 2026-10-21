# dicionario=dict()
#
# dicionario["maçã"]=0.69
#
#
# print(dicionario["maçã"])

votaram={}

def verifica_eleitor(nome):
    if votaram.get(nome):
        print( "Mande embora!")
    else:
        votaram[nome]=True
        print("Deixe votar!")

verifica_eleitor("tom")
verifica_eleitor("tom")
verifica_eleitor("mike")