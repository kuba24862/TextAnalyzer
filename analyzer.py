import sys
# Importování knihovny pro vytváření "progress" baru (s printem by to bylo těžší)



class TextAnalyzer:
    """Analizuje text
    text - který je analyzován
    maximum - počet slov který na konci vypíše
    procenta - Chce aby vypsalo nakonci prenctuální podíl slova
    """

    def __init__(self, text, maximum=10, procenta=True):
        # Metoda který se spouští při vytvoření instance
        self.__text = self.getTextWithnoutInterpuntion(text).lower().split()
        # Odstraní z textu interpunkci
        # převede vše na malá písmena
        # rozdělí do array (mezery)

        self.__analyze = self.analyze()
        # Uloží do proměné vysledek metody - hodnoty několik krát volám čas, paměť

        self.__maximum = maximum
        self.__procenta = procenta
         # ukládám oláklní promění do třídy

    def __str__(self):
        # output vrací str

        pocetslov = self.getPocetslov()
        procentcelkem = self.soucetprocent()
        slova = self.getTop()

        vypis = "\nSlovo | počet vyskutu | Procent z celku"
        for i, y in slova.items():
            vypis += "\n"
            vypis += "{0} | {1} | {2}% ".format(i, y[0], y[1])

        vypis += "\nprvních " + str(self.__maximum) + " slov tvoří " + \
            str(procentcelkem) + "%"
        vypis += "\nPočet slov který byl zanalyzován: " + str(self.__pocetslov)
        vypis += "\nPočet typu slov: " + str(self.getDictLen())
        return vypis

    def getTextWithnoutInterpuntion(self, text):
        # Vrací text bez interpinkce
        for i in [",", ".", "?", "!", "-", ":", ";"]:
            # Postupně projde všechny znaky a odstraní jez textu
            text = text.strip(i)
        return text

    def progress(self, count, total, suffix=''):
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))

        percents = round(100.0 * count / float(total), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)

        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
        sys.stdout.flush()  # As suggested by Rom Ruben

    def analyze(self):
        slovoKUpocetvyskytu = {}
        # dictinary, saving word : count

        progress = 0
        # var used to progress bar

        self.__pocetslov = self.getPocetslov()
        # how many word i have

        for i in self.__text:
            # browse all word and if no exist add him to dict. If exist +1
            if i in slovoKUpocetvyskytu:
                slovoKUpocetvyskytu[i] += 1
            else:
                slovoKUpocetvyskytu[i] = 1
            progress += 1
            self.progress(progress, self.__pocetslov)
        #self.__analyze = slovoKUpocetvyskytu
        return slovoKUpocetvyskytu

    def getTop(self):
        # returns list of top word par:
        slovnik = self.__analyze
        maximalni_key = list(slovnik.keys())
        maximalni_values = list(slovnik.values())
        pocetslov = self.getPocetslov()
        # nejpouzivanjsislovo = ""
        top = {}
        for i in range(self.__maximum):
            indexslova = maximalni_values.index(int(max(maximalni_values)))
            maximalni = maximalni_key[indexslova]
            # nejpouzivanjsislovo += maximalni + ", "
            if self.__procenta:
                top[maximalni] = [maximalni_values[indexslova],
                                  round(maximalni_values[indexslova]*100/pocetslov, 2)]
            else:
                top[maximalni] = maximalni_values[indexslova]
            del maximalni_key[indexslova]
            del maximalni_values[indexslova]
        return top

    def getPocetslov(self):
        # Vrací počet slov ve slovníku
        return len(self.__text)

    def soucetprocent(self):
        procenta = list(self.getTop().values())
        vysledek = 0
        for i in procenta:
            vysledek += i[1]
        return round(vysledek, 2)

    def getDictLen(self):
        # Vrací počet slov ve slovníku
        return len(self.__analyze)
