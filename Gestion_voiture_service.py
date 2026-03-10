class Employe:
    def __init__(self, numero_permis, nom, prenom,):
        self.numero_permis = numero_permis
        self.nom = nom
        self.prenom = prenom
        self.voiture_service=None

    def afficher_infos(self):
        print(f" numero_permis: {self.numero_permis}, nom: {self.nom}, prenom: {self.prenom}")
        if self.voiture_service is not None:
            print("la voiture de service est assignée")
        else:
            print("aucune voiture de service n'est assignée")

    def affecter_voiture(self, voiture):
        if self.voiture_service is not None:
            print("cet employé possède deja une voiture")
            return
        self.voiture_service=voiture

    def retirer_voiture(self):
        if self.voiture_service is None:
            print("cet employé n'a pas de voiture de service")
            return
        self.voiture_service=None

class Voiture:
    def __init__(self, matricule, annee, marque, killometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.killometrage = killometrage
        self.chauffeur = None



