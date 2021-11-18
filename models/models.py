# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reparacion(models.Model):
    _inherit = 'mrp.repair'


    @api.model
    def create(self,values):
        ultima=self.env['mrp.repair'].search([],order='name desc',limit=1).name
        numero=ultima[ultima.find('/')+1:]
        nombre=ultima[:ultima.find('/')+1]

        numero=int(numero)+1
        numero_completo=nombre+('00000' + str(numero))[-5:]
        secuencia=self.env['ir.sequence'].sudo().search([('code','=','mrp.repair')],limit=1)
        vals={
            'number_next_actual':numero+1
        }
        secuencia.sudo().write(vals)
        values['name']= numero_completo
        override_create = super(Reparacion,self).create(values)
        new_object = self.env['mrp.repair'].browse(override_create.id)
        if new_object.id:
            new_object.write({'name': numero_completo})
        return new_object
        return override_create.write(values)
