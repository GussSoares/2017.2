from Baboon import Babuino
#import Baboon
import threading

def inicio():
    threadsL = []   # Babuino que iniciam do lado Leste
    threadsO = []   # Babuino que iniciam do lado Oeste
    campo = []
    qnt = 0


    #for i in range(50):
    while not qnt == 50:
        if len(threadsL) == 27:
            nome_thread = 'threadino' + str(qnt)
            babuino = Babuino("Oeste", None)
            babuino.sorteio_tempo_chegada()
            t = threading.Thread(name=nome_thread, target=babuino)
            # threadsO.append(t)
            campo.append(t)
            print("if 1")

            qnt += 1
            continue
        if len(threadsO) == 27:
            nome_thread = 'threadino' + str(qnt)
            babuino = Babuino("Leste", None)
            babuino.sorteio_tempo_chegada()
            t = threading.Thread(name=nome_thread, target=babuino)
            # threadsL.append(t)
            campo.append(t)
            print("if 2")
            qnt += 1
            continue
        else:
            nome_thread = 'threadino' + str(qnt)
            babuino = Babuino(None, None)
            babuino.sorteio_sentido()
            babuino.sorteio_tempo_chegada()
            t = threading.Thread(name=nome_thread, target=babuino)
            if str(babuino.sentido_da_movimentacao) == "Leste":
                # threadsL.append(t)
                campo.append(t)
                print("if 3")
                qnt += 1
                continue
            else:
                # threadsO.append(t)
                campo.append(t)
                print("if 4")
                qnt += 1
                continue

    print(len(threadsL))
    print(len(threadsO))
    print("campo: "+str(len(campo)))
    for i in range(len(threadsL)):
        print(threadsL[i])


#Iniciar Treads
    # for i in range(len(threadsL)):
    #     threadsL[i].start()
    #     threadsL[i].join()
    #    # print("Iniciando thread Leste")
    # for i in range(len(threadsO)):
    #     threadsO[i].start()
    #     threadsO[i].join()
    #    # print("Iniciando thread Oeste")

if __name__ == "__main__":
    inicio()