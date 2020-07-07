from odoo import fields, models, api, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time


class account_paymnet_report(models.AbstractModel):
    _name = 'report.account_payment_report.payment_report_template'

    def _get_selected_date(self, form):
        selected_date = form['selected_date']
        return selected_date

    def _get_payments(self, selected_date):  #
        account_payment = self.env["account.payment"]
        data = []
        object_payments = account_payment.search([("payment_date", '=', selected_date)],
                                                 order='payment_date')
        total_amount = 0.0
        for toalats in object_payments:
            total_amount = total_amount + toalats.amount
        for payments in object_payments:
            res = {
                "name": payments.name,
                "payment_date": payments.payment_date,
                "communication": payments.communication,
                "payment_method": payments.payment_method,
                "payment_type": payments.payment_type,
                "partner_name": payments.partner_id.name,
                "journal_id": payments.journal_id.name,
                "amount": payments.amount,
                'amount_total': total_amount,
            }
            data.append(res)
            print('payment method', payments.payment_method)
            print('payment type', payments.payment_type)
            print('Data', data)

        if data:
            return data
        else:
            return {}

    @api.model
    def get_report_values(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        check_report = self.env['ir.actions.report']._get_report_from_name(
            'account_payment_report.account_paymnet_report_ref_id')
        return {
            'doc_ids': docids,
            'doc_model': check_report.model,
            'docs': docs,
            "time": time,
            "selected_date": self._get_selected_date(data['form']),
            "get_payments": self._get_payments,
        }
