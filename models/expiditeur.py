from odoo import api,fields,models,tools

class SelectExpiditeur(models.Model):
    _name ='expiditeur.select'
    _description = "Folder managment for puerto transit"
    def get_dum(self):
      query = "SELECT dum_list FROM dum_number_table"
      self.env.cr.execute(query)
      records = self.env.cr.fetchall()
      l = [] 
      for recs in records :
       for rec in recs :
        l.append((rec,rec))
      return l 


    test_ids = fields.Selection(lambda self:self.get_dum())
    test_apend = fields.Char(string="append to dum list test") 
    dummy = fields.Char(compute=lambda self:self._add_new_dum(self.test_apend))
    def _add_new_dum(self,values):
     print(values)
     query = "INSERT INTO dum_number_table(dum_list) VALUES('"+values+"')"    
     self.env.cr.execute(query)
     for rec in self :
      print(self.test_apend)
      rec.dummy = 10
     """
     query = "INSERT INTO dum_number_table(dum_list) VALUES('"+values+"')"    
     print("APPENDEDDD")
     self.env.cr.execute(query)
     for rec in self :
      rec.test_apend = '10'
     """
    expiditeur_ids = fields.Selection(
        [
            ('DANOSA MAROC', 'DANOSA MAROC'),
            ('11 RUE IBN HAYTAM TANGER', '11 RUE IBN HAYTAM TANGER'),
            ('2N-SUD MAROC S.A.R.L.', '2N-SUD MAROC S.A.R.L.'),
            ('4 AC SARL', '4 AC SARL'),
            ('A TOUT LOCATION', 'A TOUT LOCATION'),
            ('A.C. MODE', 'A.C. MODE'),
            ('A.C.X ( advanced cargo express)', 'A.C.X ( advanced cargo express)'),
            ('A.E.T SARL', 'A.E.T SARL'),
            ('A.M.M.Z TRANSPORT', 'A.M.M.Z TRANSPORT'),
            ('A.P.A TEXTIL', 'A.P.A TEXTIL'),
            ('AB INTERNATIONAM SARL AU', 'AB INTERNATIONAM SARL AU'),
            ('ABRATEX', 'ABRATEX'),
            ('AC MODE', 'AC MODE'),
            ('ACBELC MODE', '   ACBELC MODE'),
            ('ACCES INDUSTRIE', 'ACCES INDUSTRIE'),
            ('ACCIONA AGUA', 'ACCIONA AGUA'),
            ('ACOME MAROC', 'ACOME MAROC'),
            ('ACT ANDALUS MAROC', 'ACT ANDALUS MAROC'),
            ('ACTION VISUELLE', 'ACTION VISUELLE'),
            ('ACTIV DISTRIBUTION', 'ACTIV DISTRIBUTION'),
            ('ACX (Advanced Cargo Express)', 'ACX (Advanced Cargo Express)'),
            ('AGRO 3', 'AGRO 3'),
            ('AGRO GAILLES SARL', 'AGRO GAILLES SARL'),
            ('AGRO NIVELACION B E SARL', 'AGRO NIVELACION B E SARL'),
            ('AGROBIOTEC', 'AGROBIOTEC'),
            ('AGRU-ESMA S.A.R.L', 'AGRU-ESMA S.A.R.L'),
            ('AHABIA SARL', 'AHABIA SARL'),
            ('AIDA MAROC', 'AIDA MAROC'),
            ('AIR SEA MAROC SARL', 'AIR SEA MAROC SARL'),
            ('AKZO NOBEL PERFORMANCE COATINGS MOROCC', 'AKZO NOBEL PERFORMANCE COATINGS MOROCC'),
            ('AKZONOBEL COATINGS S.A', 'AKZONOBEL COATINGS S.A'),
            ('ALABRA INDUSTRIE', 'ALABRA INDUSTRIE'),
            ('ALAE URBAN', 'ALAE URBAN'),
            ('ALAE WELTMARK SARL', 'ALAE WELTMARK SARL'),
            ('ALARWOOL', 'ALARWOOL'),
            ('ALE EQUIPEMENTS ELECTRIQUE ET MECANIOUE1', 'ALE EQUIPEMENTS ELECTRIQUE ET MECANIOUE1'),
            ('ALF MABROUK', 'ALF MABROUK'),
            ('ALGINIA SARL', 'ALGINIA SARL'),
            ('ALLOPC', 'ALLOPC'),
            ('ALPHEN MODA', 'ALPHEN MODA'),
            ('ALTO SERVICES', 'ALTO SERVICES'),
            ('ALUMINIUM DE MAROC', 'ALUMINIUM DE MAROC'),
            ('ALUPRAL SARL', 'ALUPRAL SARL'),
            ('ALUSISTEM EMPRESA ESPANOLA', 'ALUSISTEM EMPRESA ESPANOLA'),
            ('ALVILEX SARL', 'ALVILEX SARL'),
            ('AMALIO PAPER', 'AMALIO PAPER'),
            ('AMBITIOUS NEGOCE', 'AMBITIOUS NEGOCE'),
            ('AMERNIS CONFECTION SARL', 'AMERNIS CONFECTION SARL'),
            ('AMG PRODUCTIONS AFRIQUE DU NORD', 'AMG PRODUCTIONS AFRIQUE DU NORD'),
            ('AN FASHION', 'AN FASHION'),
            ('ANAOUJI TRANS', 'ANAOUJI TRANS'),
            ('ANGUS SOFT FRUITS MAROC', 'ANGUS SOFT FRUITS MAROC'),
            ('ANMOU CONFECTION', 'ANMOU CONFECTION'),
            ('ANTA BARA', 'ANTA BARA'),
            ('ANTAMETA MEA', 'ANTAMETA MEA'),
            ('ANTIPASTI-MED', 'ANTIPASTI-MED'),
            ('ANTIPASTI-MED SARL', 'ANTIPASTI-MED SARL'),
            ('ANTOLIN', 'ANTOLIN'),
            ('APTIV SERVICES CONNECTION SYSTEMS', 'APTIV SERVICES CONNECTION SYSTEMS'),
            ('APTIV SERVICES ELECTRICAL', 'APTIV SERVICES ELECTRICAL'),
            ('APTIV SERVICES FRANCE', 'APTIV SERVICES FRANCE'),
            ('APTIV SERVICES KENITRA SA(X Delphi Kenitra)', 'APTIV SERVICES KENITRA SA(X Delphi Kenitra)'),
            ('APTIV SERVICES MAROC SA(X Delphi Maroc)', 'APTIV SERVICES MAROC SA(X Delphi Maroc)'),
            ('APTIV SERVICES MEKNES SA(X Delphi Meknes)', 'APTIV SERVICES MEKNES SA(X Delphi Meknes)'),
            ('APTIV SERVICES PACKARD AUSTRIA GMBH 8 COK', 'APTIV SERVICES PACKARD AUSTRIA GMBH 8 COK'),
            ('APTIV SERVICES TANGER SA(X Delphi Tanger)', 'APTIV SERVICES TANGER SA(X Delphi Tanger)'),
            ('APTIV SERVICES TUNISIE', 'APTIV SERVICES TUNISIE'),
            ('ARABTEX', 'ARABTEX'),
            ('AR8AGRI SRLAU AGADIR', 'AR8AGRI SRLAU AGADIR'),
            ('ATAGRI SARL', 'ATAGRI SARL'),
            ('ATELIER TURGUE DE TOUR SARL', 'ATELIER TURGUE DE TOUR SARL'),
            ('ATG MAROC', 'ATG MAROC'),
            ('ATLANTA SERVICES', 'ATLANTA SERVICES'),
            ('ATOUTLOC', 'ATOUTLOC'),
            ('ATS GLOBAL', 'ATS GLOBAL'),
            ('AUTO WORLDLINE', 'AUTO WORLDLINE'),
            ('AUTO WORLDLINE SARL', 'AUTO WORLDLINE SARL'),
            ('AUTOMATIC ID', 'AUTOMATIC ID'),
            ('AUTOMOTIVE CABLAGE CONTROL', 'AUTOMOTIVE CABLAGE CONTROL'),
            ('AUTRANSA MAROC SARL', 'AUTRANSA MAROC SARL'),
            ('AVANTEX SARL', 'AVANTEX SARL'),
            ('AVANZIT TECHNOLOGIE MAROC', 'AVANZIT TECHNOLOGIE MAROC'),
            ('AYAZINTEX', 'AYAZINTEX'),
            ('AYRA MODE S.A.R.L', 'AYRA MODE S.A.R.L'),
            ('BADDENDUM', 'BADDENDUM'),
            ('UM Trans Mahusz Wiechetek', 'UM Trans Mahusz Wiechetek'),
            ('B4 CREATION SARL', 'B4 CREATION SARL'),
            ('BA CONFECCIONES', 'BA CONFECCIONES'),
            ('BABYSHIRT', 'BABYSHIRT'),
            ('BANI MODE SARL', 'BANI MODE SARL'),
            ('BATEOUI TEXTILE', 'BATEOUI TEXTILE'),
            ('BCR TRADE SARL', 'BCR TRADE SARL'),
            ('BDP', 'BDP'),
            ('BDP INTERNATIONAL', 'BDP INTERNATIONAL'),
            ('BIOMIP MAROC SARL', 'BIOMIP MAROC SARL'),
            ('BOHANEG', 'BOHANEG'),
            ('BOLLORE TRANSPORT & LOGISTICS MAROC', 'BOLLORE TRANSPORT & LOGISTICS MAROC'),
            ('BONITRANS. SAU (GRUPO SESE)', 'BONITRANS. SAU (GRUPO SESE)'),
            ('BORDADOS CARMEN', 'BORDADOS CARMEN'),
            ('BOUFELL', 'BOUFELL'),
            ('BOUJDOUR WIND FARM', 'BOUJDOUR WIND FARM'),
            ('BOUZI FASHION', 'BOUZI FASHION'),
            ('BSH Bectrodomosticos Espana S.A', 'BSH Bectrodomosticos Espana S.A'),
            ('BSH ELECTROMENAGERS SA', 'BSH ELECTROMENAGERS SA'),
            ('BSL', 'BSL'),
            ('BUSBY MAROC', 'BUSBY MAROC'),
            ('C.E.I.T S.A.', 'C.E.I.T S.A.'),
            ('C.M.F', 'C.M.F'),
            ('C.T ELEVATION', 'C.T ELEVATION'),
            ('CABAEXPO', 'CABAEXPO'),
            ('CADIZ CONFECTION SARL', 'CADIZ CONFECTION SARL'),
            ('CALSINA CARRE AFRIGUE', 'CALSINA CARRE AFRIGUE'),
            ('CAMARA DE COMERCIO E INDUSTRIA', 'CAMARA DE COMERCIO E INDUSTRIA'),
            ('CANC TRANS', 'CANC TRANS'),
            ('CANPACK MOROCCO SARL', 'CANPACK MOROCCO SARL'),
            ('CAP INTER SARL', 'CAP INTER SARL'),
            ('CAP MODE', 'CAP MODE'),
            ('CAP SECURITE', 'CAP SECURITE'),
            ('CAPERSMED', 'CAPERSMED'),
            ('CARACOLE JAOUI', 'CARACOLE JAOUI'),
            ('CARACOL-EX SARL', 'CARACOL-EX SARL'),
            ('CARRE R MAROC', 'CARRE R MAROC'),
            ('CARREAUXCHOME SARL', 'CARREAUXCHOME SARL'),
            ('CARROSSERIE MONTAGE FATH SARL', 'CARROSSERIE MONTAGE FATH SARL'),
            ('CARS CEE MAROC SARL', 'CARS CEE MAROC SARL'),
            ('CART-ECO SARL', 'CART-ECO SARL'),
            ('CASA VIGILANGE', 'CASA VIGILANGE'),
            ('CASABLANCA TRANSPORTS EN SITE AMENA', 'CASABLANCA TRANSPORTS EN SITE AMENA'),
            ('CASUAL CONFECCIONES', 'CASUAL CONFECCIONES'),
            ('ASUAL PANT', 'ASUAL PANT'),
            ('CAT MAROC SARL', 'CAT MAROC SARL'),
            ('CCCM SA', 'CCCM SA'),
            ('CENTRAL EXPERT INDUSTRIE', 'CENTRAL EXPERT INDUSTRIE'),
            ('CENTRALE EXPERT INDUSTRIE', 'CENTRALE EXPERT INDUSTRIE'),
            ('CF TANGIER', 'CF TANGIER'),
            ('CHAFEHTEX', 'CHAFEHTEX'),
            ('CHAMPINTERMA SARL', 'CHAMPINTERMA SARL'),
            ('CHANGCHUN SHIFA AUTO TECHNOLOGY CO. LTD', 'CHANGCHUN SHIFA AUTO TECHNOLOGY CO. LTD'),
            ('CHHIOUAT CHAMAL', 'CHHIOUAT CHAMAL'),
            ('CHIFAE FASHION', 'CHIFAE FASHION'),
            ('CHIKAS DESIGN', 'CHIKAS DESIGN'),
            ('CHIN POON INDUSTRIAL CO', 'CHIN POON INDUSTRIAL CO'),
            ('CIDON Y PLUTO SL', 'CIDON Y PLUTO SL'),
            ('CIE AUTOMOTIVE MAROC', 'CIE AUTOMOTIVE MAROC'),
            ('CIETEC EX LEROY SOMER MAROC', 'CIETEC EX LEROY SOMER MAROC'),
            ('CIM SPA MAROCCO', 'CIM SPA MAROCCO'),
            ('CIMOLAITECH', 'CIMOLAITECH'),
            ('CLARION HORN', 'CLARION HORN'),
            ('CLARION HORN MAROC', 'CLARION HORN MAROC'),
            ('CLEAR VIEW FASHION', 'CLEAR VIEW FASHION'),
            ('ri ril inrprr', 'ri ril inrprr'),
            ('CART-EDO SARL', 'CART-EDO SARL'),
            ('CASUAL PANT', 'CASUAL PANT')
        ], string="éxpiditeur"
    )
