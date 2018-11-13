# © 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models


class Followers(models.Model):
    _name = 'mail.followers'
    _inherit = ['mail.followers']

    @api.model
    def create(self, vals):
        if 'partner_id' in vals and 'res_id' in vals and 'res_model' in vals:
            uniq_follower = self.env['mail.followers'].search(
                [
                    ('res_id', '=', int(vals['res_id'])),
                    ('partner_id', '=', int(vals['partner_id'])),
                    ('res_model', '=', vals['res_model'])
                ]
            )
            if uniq_follower:
                return uniq_follower[0]

        res = super(Followers, self).create(vals)
        res._invalidate_documents()
        return res
