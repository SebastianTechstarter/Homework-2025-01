# 1.1 UML Klassendiagramm

class Zutat():
    def __init__(self, name, kalorien_pro_100g, zubereitungszeit):
        self.name = name
        self.kalorien_pro_100g = int(kalorien_pro_100g)
        self.zubereitungszeit = int(zubereitungszeit)

# 1.2 Overkill UML Klassendiagramm mit Methoden

class Rezept():
    def __init__(self, name, beschreibung, zubereitungszeit):
        self.name = name
        self.beschreibung = beschreibung
        self.zutatenliste = {}
        self.zubereitungszeit = zubereitungszeit

    def zutat_hinzufügen(self, Zutat, Menge):
        self.zutatenliste[Zutat] = Menge
 #   def kalorien(self, ):
    
 #   def kochzeit(self, ):
    
  #  def rezept_anzeigen(self, ):

test = Rezept("Pfannkuchen", "Superlecker")
print (test.beschreibung)
# 1.3 Beispielrezept