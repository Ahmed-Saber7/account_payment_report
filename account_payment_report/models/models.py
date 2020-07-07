# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.tools.translate import _
from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
import time
from odoo.exceptions import Warning as UserError


class payment_report(models.TransientModel):
    _name = 'payment.report'

    selected_date = fields.Date(string="Select Date ", required=True, )

    @api.multi
    def payment_report(self):
        [data] = self.read()
        data['form'] = self.read(['selected_date', 'get_payments'])[0]
        datas = {
            # 'type': type,
            'model': 'account.payment',
            'form': data
        }
        return self.env.ref('account_payment_report.account_paymnet_report_ref_id').with_context(
            landscape=False).report_action(self, data=datas)
