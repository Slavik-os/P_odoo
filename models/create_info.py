from odoo import api,fields,models,tools,_
from odoo.exceptions import ValidationError

class InfoCreateManagment(models.Model):
    _name = "info.managment.create"
    _description = " Model for managment Selection Controll "

    def get_dum(self):
     query = "SELECT dum_list FROM dum_number_table"
     self.env.cr.execute(query)
     records = self.env.cr.fetchall()
     l = [] 
     for recs in records :
      for rec in recs :
       l.append((rec,rec))
     return l 
     #expiditeur_ids = fields.Selection(lambda self:self.get_dum(),string="TEST")
     expiditeur_ids = fields.Selection([("TEST","TEST")],string="KHDMI")
     test_field = fields.Selection([("TEST1","TEST2")],string="QWEWQE")
     print("HEREREEEEEEEEEEE !!!!!!!!!!!!!") 
