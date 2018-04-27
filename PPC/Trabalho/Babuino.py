# -*- coding: utf-8 -*-

from threading import Thread, Semaphore
import Rop, time, Vetores, sys


smf_direcao = Semaphore()                                                                                   # semaforo para alterar a direcao entre leste e oeste
# smf = Semaphore(value=4)
# smf_fluxo = Semaphore(value=4)
smf_rop = Semaphore(4)

smf_east = Semaphore()                                                                                      # semaforos para colocar os babuinos nos vetores leste ou Oeste
smf_west = Semaphore()

smf_count_east = Semaphore()                                                                                # semaforo para contagem de babuinos
smf_count_west = Semaphore()

smf_cainon = Semaphore()                                                                                    # semaforo para saida do canion

smf_sair_leste = Semaphore()                                                                                # semaforo para retirar os babuinos dos vetoers leste e oeste
smf_sair_oeste = Semaphore()

rop = Rop.Rop(None)
countEast = 0                                                                                               # contadores para ver quantos babuinos de leste e oeste estao na corda
countWest = 0

inicio_corda = 0
fim_corda_leste = 0                                                                                         # medir tempo que os babuinos passam na corda
fim_corda_oeste = 0


class Babuino(Thread) :

    def __init__(self, position, time):

        Thread.__init__(self)
        self.position = position                            # posicao inicial do babuino
        self.time = time                                    # tempo

    def atravessar(self):

        global countEast, countWest, inicio_corda, fim_corda_leste, fim_corda_oeste
        smf_cainon.acquire()                                                                                # quando chama essa funcao, ele ja toma o controle da corda

        if rop.direcao is None:                                                                             # essa condicao so será executada uma vez, que é quando o primeiro babuino chegar na corda

            smf_cainon.release()                                                                            # libera o canion para que outros possam entrar tbm

            smf_direcao.acquire()                                                                           # toma o controle da direcao para que não haja conflito e só possam entrar os que sao da msm direcao
            rop.direcao = self.position                                                                     # altera a direcao

            time.sleep(1)                                                                                   # espera 1 segundo pra subir na corda

            # smf_direcao.release()

            sys.stdout.write("DIRECAO DA CORDA ALTERADA PARA: " + rop.direcao + "\n")
            sys.stdout.flush()



            smf_rop.acquire()                                                                               # adquire semaforo da corda

            sys.stdout.write(str(self.name) + " entrou na corda pela " + str(rop.direcao) + "\n")
            sys.stdout.flush()

            rop.rop.append(self)                                                                            # babuino sobe na corda


            inicio_corda = time.time()                                                                      # comeca acontar o tempo q o babuino passa na corda


            if self in Vetores.East:
                smf_sair_leste.acquire()
                Vetores.East.remove(self)
                smf_sair_leste.release()
            elif self in Vetores.West:
                smf_sair_oeste.acquire()
                Vetores.West.remove(self)
                smf_sair_oeste.release()


            if self.position == "East":
                smf_count_east.acquire()
                countEast += 1                                                                              #
                smf_count_east.release()
            else:
                smf_count_west.acquire()
                countWest += 1
                smf_count_west.release()


            # if self.position == "East":
            #     Vetores.East.remove(self)
            # else:
            #     Vetores.West.remove(self)

            time.sleep(4)                                                                                   # 4 segundos para atravessar
            rop.rop.popleft()                                                                               # sai da corda

            sys.stdout.write(str(self.name) + " saiu da corda" + "\n")
            sys.stdout.flush()

            smf_rop.release()                                                                               # libera semaforo da corda



            if self.position == "East":                                                                     #
                smf_count_east.acquire()
                countEast -= 1
                smf_count_east.release()
            else:
                smf_count_west.acquire()
                countWest -= 1
                smf_count_west.release()




            if rop.direcao == "East" and countEast == 0:
                fim_corda_leste = time.time()
                print(fim_corda_leste-inicio_corda)
                Vetores.rop_time.append(fim_corda_leste - inicio_corda)
                smf_direcao.release()
            elif rop.direcao == "West" and countWest == 0:
                fim_corda_oeste = time.time()
                print(fim_corda_oeste - inicio_corda)
                Vetores.rop_time.append(fim_corda_oeste - inicio_corda)
                smf_direcao.release()


        # if len(rop.rop) is 0:
        #
        #     smf.acquire()
        #     time.sleep(1)
        #     rop.rop.append(self)
        #     rop.direcao = self.position
        #     for i in rop.rop:
        #         sys.stdout.write(str(i.name) + " entrou na corda pela " + str(rop.direcao) + "\n")
        #         sys.stdout.flush()
        #     time.sleep(4)
        #     rop.rop.popleft()
        #
        #     sys.stdout.write(str(self.name) + " saiu da corda" + "\n")
        #     sys.stdout.flush()
        #
        #     # print(str(self.name) + " saiu da corda")
        #     smf.release()

        elif rop.direcao is self.position:                                                                  # condicao se a direcao do babuino for a mesma da corda

            time.sleep(1)                                                                                   # um segundo para subir na corda

            smf_cainon.release()                                                                            # libera o canion para que outros possam entrar tbm

            # smf.acquire()

            smf_rop.acquire()                                                                               # bloqueia a corda para nenhum outro acessar

            sys.stdout.write(str(self.name) + " entrou na corda pela " + str(rop.direcao) + "\n")
            sys.stdout.flush()

            rop.rop.append(self)                                                                            # sobe na corda


            if self in Vetores.East:
                smf_sair_leste.acquire()
                Vetores.East.remove(self)
                smf_sair_leste.release()
            elif self in Vetores.West:
                smf_sair_oeste.acquire()
                Vetores.West.remove(self)
                smf_sair_oeste.release()

            # inicio_corda = time.time()

            if self.position == "East":
                smf_count_east.acquire()
                countEast += 1
                smf_count_east.release()
            else:
                smf_count_west.acquire()
                countWest += 1
                smf_count_west.release()


            # if self.position == "East":
            #     Vetores.East.remove(self)
            # else:
            #     Vetores.West.remove(self)
            # if self.position == "East":
            #     Direcao.East.popleft()
            # else:
            #     Direcao.West.popleft()


            # rop.maximo += 1
            # sys.stdout.write("count = " + str(rop.maximo) + "\n")
            # sys.stdout.flush()

            time.sleep(4)
            rop.rop.popleft()

            sys.stdout.write(str(self.name) + " saiu da corda" + "\n")
            sys.stdout.flush()

            smf_rop.release()


            if self.position == "East":
                smf_count_east.acquire()
                countEast -= 1
                smf_count_east.release()
            else:
                smf_count_west.acquire()
                countWest -= 1
                smf_count_west.release()




            if rop.direcao == "East" and countEast == 0:
                fim_corda_leste = time.time()
                print(fim_corda_leste - inicio_corda)
                Vetores.rop_time.append(fim_corda_leste- inicio_corda)
                smf_direcao.release()
            elif rop.direcao == "West" and countWest == 0:
                fim_corda_oeste = time.time()
                print(fim_corda_oeste - inicio_corda)
                Vetores.rop_time.append(fim_corda_oeste - inicio_corda)
                smf_direcao.release()

            # smf.release()

            # if (rop.maximo == 4) or (rop.maximo > 0 and (len(Direcao.East)==0 or len(Direcao.West)==0)):
            #     smf_fluxo.acquire()
            #     sys.stdout.write("Entrou no if" + "\n")
            #     sys.stdout.flush()
            #     # print("Entrou no if")
            #     rop.maximo = 0
            #     # while len(rop.rop) != 0:
            #     #     pass
            #     if rop.direcao == "East":
            #         rop.direcao = "West"
            #         sys.stdout.write("DIRECAO DA CORDA ALTERADA PARA: " + rop.direcao + "\n")
            #         sys.stdout.flush()
            #
            #     else:
            #         rop.direcao = "East"
            #         sys.stdout.write("DIRECAO DA CORDA ALTERADA PARA: " + rop.direcao + "\n")
            #         sys.stdout.flush()
            #
            #     smf_fluxo.release()
            #     self.atravessar()
            # sys.stdout.write(rop.direcao)
            # sys.stdout.flush()
        else:                                                                                               # caso a direcao do babuino seja diferente da corda

            time.sleep(1)


            smf_direcao.acquire()
            rop.direcao = self.position                                                                     # altera a direcao da corda para que possa subir

            sys.stdout.write("DIRECAO DA CORDA ALTERADA PARA: " + rop.direcao + "\n")
            sys.stdout.flush()

            smf_cainon.release()
            smf_rop.acquire()

            sys.stdout.write(str(self.name) + " entrou na corda pela " + str(rop.direcao) + "\n")
            sys.stdout.flush()

            rop.rop.append(self)

            inicio_corda = time.time()

            if self in Vetores.East:
                smf_sair_leste.acquire()
                Vetores.East.remove(self)
                smf_sair_leste.release()
            elif self in Vetores.West:
                smf_sair_oeste.acquire()
                Vetores.West.remove(self)
                smf_sair_oeste.release()

            if self.position == "East":
                smf_count_east.acquire()
                countEast += 1
                smf_count_east.release()
            else:
                smf_count_west.acquire()
                countWest += 1
                smf_count_west.release()



            # if self.position == "East":
            #     Vetores.East.remove(self)
            # else:
            #     Vetores.West.remove(self)

            time.sleep(4)
            rop.rop.popleft()

            sys.stdout.write(str(self.name) + " saiu da corda" + "\n")
            sys.stdout.flush()

            smf_rop.release()


            if self.position == "East":
                smf_count_east.acquire()
                countEast -= 1
                smf_count_east.release()
            else:
                smf_count_west.acquire()
                countWest -= 1
                smf_count_west.release()

            if rop.direcao == "East" and countEast == 0:
                fim_corda_leste = time.time()
                print(fim_corda_leste - inicio_corda)
                Vetores.rop_time.append(fim_corda_leste - inicio_corda)
                smf_direcao.release()
            elif rop.direcao == "West" and countWest == 0:
                fim_corda_oeste = time.time()
                print(fim_corda_oeste - inicio_corda)
                Vetores.rop_time.append(fim_corda_oeste - inicio_corda)
                smf_direcao.release()

        # Vetores.East.clear()
        # Vetores.West.clear()                                                    # Esvaziar os vetores Leste e Oete

    def run(self):

        if self.position == "East":                                             # Semaforo para inserir babuinos no lado East ou West
            smf_east.acquire()
        else:
            smf_west.acquire()

        inicio = time.time()

        time.sleep(self.time)

        if self.position == "East":
            Vetores.East.append(self)
            sys.stdout.write("adicionou" + str(self) + "em East" + "\n")
            sys.stdout.flush()
        else:
            Vetores.West.append(self)
            sys.stdout.write("adicionou" + str(self) + "em West" + "\n")
            sys.stdout.flush()

        if self.position == "East":
            smf_east.release()
        else:
            smf_west.release()
        self.atravessar()

        fim = time.time()

        Vetores.crossing_time.append(int(fim-inicio))