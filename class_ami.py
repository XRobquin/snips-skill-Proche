import datetime
import pickle

class ami:
    def __init__(self,
                 nnom = "Dupont",
                 pprenom = "Rémy",
                 jjnaissance = 1,
                 mmnaissance = 1,
                 aanaissance = 1900,
                 vville = "Paris",
                 llien = "Ami"):

        self.nom = nnom
        self.prenom = pprenom
        self.jnaissance = jjnaissance
        self.mnaissance = mmnaissance
        self.anaissance = aanaissance
        self.ville = vville
        self.lien = llien

    def calcul_age(self):
        date = datetime.datetime.now()
        if (date.month > self.mnaissance or (date.month == self.mnaissance and date.day >= self.jnaissance)):
            aage = date.year - self.anaissance
        else:
            aage = date.year - self.anaissance - 1
        self.age = aage
        print(self.prenom + " a " + str(self.age) + " ans ")

    def calcul_nb_jours_avant_anniv(self):
        date = datetime.datetime.now()
        year = date.year
        today = datetime.date.today()
        anniv = datetime.date(year+1, self.mnaissance, self.jnaissance)
        diff = anniv - today
        print("Il reste " + str(diff.days%365-1) + " jours avant l'anniversaire de " + self.prenom)
