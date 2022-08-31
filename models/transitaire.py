from odoo import api,fields,models,tools,_

class Transitaire(models.Model):
    _name = 'transitaire'
    _description = 'Transitaire selection list'
    transitaire = fields.Selection([
        ("A TRANS", "A TRANS"),
        ("A.G.T.T", "A.G.T.T"),
        ("ADATRA", "ADATRA"),
        ("AGECOMAR", "AGECOMAR"),
        ("AGENCE FUENTES", "AGENCE FUENTES"),
        ("AGRISOUSS", "AGRISOUSS"),
        ("ALIF TRANS INTERNATIONAL", "ALIF TRANS INTERNATIONAL"),
        ("ALMOU TRANS", "ALMOU TRANS"),
        ("AMRANI TRANSIT NOW SARL", "AMRANI TRANSIT NOW SARL"),
        ("AMTT", "AMTT"),
        ("ANJAD TRANSIT", "ANJAD TRANSIT"),
        ("Asmae forwarding express", "Asmae forwarding express"),
        ("ASNITRANS", "ASNITRANS"),
        ("BACHIR ET BENCHEKROUN SARL", "BACHIR ET BENCHEKROUN SARL"),
        ("BADRIMEXT", "BADRIMEXT"),
        ("BAYSIM SARL", "BAYSIM SARL"),
        ("CABINET DRISS KHALLADI", "CABINET DRISS KHALLADI"),
        ("CABINET HANIN DE TRANSIT", "CABINET HANIN DE TRANSIT"),
        ("CAP INTER", "CAP INTER"),
        ("CAPRICORNE TRANSTIR sad.", "CAPRICORNE TRANSTIR sad."),
        ("CIMTEX", "CIMTEX"),
        ("COGETRANS", "COGETRANS"),
        ("COMATTIR", "COMATTIR"),
        ("CONSERVERIES DES DEUX MERS", "CONSERVERIES DES DEUX MERS"),
        ("CUMAREX SA", "CUMAREX SA"),
        ("DACHSER Tanger", "DACHSER Tanger"),
        ("EL HABABI TRANSIT", "EL HABABI TRANSIT"),
        ("ESMATRANS", "ESMATRANS"),
        ("FLAM LOGISTIC", "FLAM LOGISTIC"),
        ("GAMMA TRANSIT", "GAMMA TRANSIT"),
        ("GDANA TRANSIT", "GDANA TRANSIT"),
        ("GEFCO MAROC", "GEFCO MAROC"),
        ("GOURRI TRANSIT", "GOURRI TRANSIT"),
        ("GRUPO IGLESIAS Y PINEDA", "GRUPO IGLESIAS Y PINEDA"),
        ("GUANTER TRANSIT SARL", "GUANTER TRANSIT SARL"),
        ("HIGH TRANSIT", "HIGH TRANSIT"),
        ("I.T.F.I SARL", "I.T.F.I SARL"),
        ("IPSEN GROUP TRANSIT", "IPSEN GROUP TRANSIT"),
        ("J.L TRANSIT", "J.L TRANSIT"),
        ("KENA SARL", "KENA SARL"),
        ("KHESMA TRANS", "KHESMA TRANS"),
        ("L.T.X 'LOCOMOTIVE TRANS EXPRE:", "L.T.X 'LOCOMOTIVE TRANS EXPRE:"),
        ("LES 2 Z A TRANSIT", "LES 2 Z A TRANSIT"),
        ("LES 3T+I", "LES 3T+I"),
        ("LINEA", "LINEA"),
        ("LOGMAN SARL", "LOGMAN SARL"),
        ("LOS CARGOS LOGISTICS", "LOS CARGOS LOGISTICS"),
        ("LYDIA TRANS", "LYDIA TRANS"),
        ("MANASSI TRANSIT", "MANASSI TRANSIT"),
        ("MARINE MAROC", "MARINE MAROC"),
        ("MAROC TRANSIT PRODUCT", "MAROC TRANSIT PRODUCT"),
        ("MATRANORD SARL", "MATRANORD SARL"),
        ("MEDITRANS", "MEDITRANS"),
        ("MEMO CONSIGNATION", "MEMO CONSIGNATION"),
        ("MILLENIUM TRANSIT", "MILLENIUM TRANSIT"),
        ("MODEL TRANS", "MODEL TRANS"),
        ("MSTT LINE", "MSTT LINE"),
        ("MULTI TRANS ALLIANCE", "MULTI TRANS ALLIANCE"),
        ("NADA TRANS", "NADA TRANS"),
        ("NANEZ SURVEYOR", "NANEZ SURVEYOR"),
        ("NEJTRANS", "NEJTRANS"),
        ("NORATRA", "NORATRA"),
        ("NORD EAST TRANSIT", "NORD EAST TRANSIT"),
        ("NOUZ BEG TRANS", "NOUZ BEG TRANS"),
        ("OCEAN WAVE NAVIGATION", "OCEAN WAVE NAVIGATION"),
        ("OMNILOGISTIC", "OMNILOGISTIC"),
        ("ONEZEMAI TRANSIT SARL", "ONEZEMAI TRANSIT SARL"),
        ("OUAHLA TRANSIT TRANSPORT", "OUAHLA TRANSIT TRANSPORT"),
        ("PALM TRANSIT", "PALM TRANSIT"),
        ("PROCUMAR", "PROCUMAR"),
        ("PROLOGISTIC", "PROLOGISTIC"),
        ("PUERTO TRANSIT SARL", "PUERTO TRANSIT SARL"),
        ("RAHIMA TRANS", "RAHIMA TRANS"),
        ("RECOING JACQUETY", "RECOING JACQUETY"),
        ("REDA TRANSIT", "REDA TRANSIT"),
        ("ROCKS INTERNATIONAL", "ROCKS INTERNATIONAL"),
        ("SECORA TRANS", "SECORA TRANS"),
        ("SERTRANS", "SERTRANS"),
        ("SIMEXTRA", "SIMEXTRA"),
        ("SOLINGE", "SOLINGE"),
        ("SONESM SARL", "SONESM SARL"),
        ("Soratra transit", "Soratra transit"),
        ("STE NEHAME DE TRANSIT&CONSIGNP", "STE NEHAME DE TRANSIT&CONSIGNP"),
        ("SUNCROPS", "SUNCROPS"),
        ("T.T.H.A", "T.T.H.A"),
        ("Tanger PUBLICITE TRANSIT", "Tanger PUBLICITE TRANSIT"),
        ("TANOUTI TRANSIT", "TANOUTI TRANSIT"),
        ("TERAL TRANSIT", "TERAL TRANSIT"),
    ],string="Transitaire")