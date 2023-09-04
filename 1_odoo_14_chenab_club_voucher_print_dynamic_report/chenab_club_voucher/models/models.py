from odoo import models, fields, api
from num2words import num2words


class AccountPayment(models.Model):
    _inherit = 'account.payment'


    def num2words_sum(self,amount):
        in_words = num2words(amount)
        return in_words
