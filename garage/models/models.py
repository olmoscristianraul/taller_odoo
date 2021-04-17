# -*- coding: utf-8 -*-
from odoo import models, fields, api

class aparcamiento(models.Model):
    _name = 'garage.aparcamiento'
    _description = 'Permite definir las caracteristicas de un aparcamiento'

    name = fields.Char('Direccción', required=True)
    plazas = fields.Integer(string='Plazas', required=True)

    #Relaciones
    coche_id =fields.One2many('garage.coche','aparcamiento_id', string=('Coches'))


class coche(models.Model):
    _name = 'garage.coche'
    _description = 'Permite definir las caracteristicas de un coche'
    _order = 'name'

    name = fields.Char('Matricula', required=True, size=7)
    plazas = fields.Integer(string='Plazas', required=True)
    modelo =  fields.Char(string='Modelo', required=True)
    contruido = fields.Date(string='Fecha de construcción')
    consumo = fields.Float('Consumo',(4,1), default=0.0, help='Consumo promedio cada 100 kms')
    #annos = fields.Integer('Años', compute='_get_annos', store=True)#no se requiere strore = true en este ejemplo
    annos = fields.Integer('Años', compute='_get_annos')
    descripcion = fields.Text('Descripción')

    aparcamiento_id = fields.Many2one('garage.aparcamiento', string='Aparcamiento')
    aparcamiento_ids = fields.Many2many('garage.mantenimiento', string='Mantenimientos')

    @api.depends('construido')
    def _getannos(self):
        for coche in self:
            coche.annos = 0
            
class mantenimiento(models.Model):
    _name = 'garage.mantenimiento'
    _description = 'Permite definir el mantenimiento rutinario de un coche'
    fecha = fields.Date(string='Fecha', required = True, default = fields.date.today())
    tipo = fields.Selection(string='Tipo', selection[('l','Lavar',('r','Revisión',('m','Mecánica',('p','Pintura'], default = 'l')
    coste = fields.Float('Coste', (8,2), help='Coste total del mantenimiento')
    
    coche_ids = fields.Many2many('garage.coche', string='Coche')