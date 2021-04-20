# -*- coding: utf-8 -*-
from odoo import models, fields, api
# from datetime import datetime
from dateutil.relativedelta import *
from datetime import date


class aparcamiento(models.Model):
    _name = 'garaje.aparcamiento'
    _description = 'Permite definir las caracteristicas de un aparcamiento'

    name = fields.Char('Direccción', required=True)
    plazas = fields.Integer(string='Plazas', required=True)
    
    #Relaciones
    coche_ids =fields.One2many('garaje.coche','aparcamiento_id', string='Coches')

    @api.depends('construido')
    def _get_annos(self):
        for coche in self:
            hoy = date.today()
            coche.annos = relativedelta(hoy,coche.construido).years



class coche(models.Model):
    _name = 'garaje.coche'
    _description = 'Permite definir las caracteristicas de un coche'
    _order = 'name'

    name = fields.Char('Matricula', required=True, size=7)
    modelo =  fields.Char(string='Modelo', required=True)
    construido = fields.Date(string='Fecha de construcción')
    consumo = fields.Float('Consumo',(4,1), default=0.0, help='Consumo promedio cada 100 kms')
    averiado = fields.Boolean(string='Averiado', default=False)
    annos = fields.Integer('Años', compute='_get_annos')
    descripcion = fields.Text('Descripción')

    aparcamiento_id = fields.Many2one('garaje.aparcamiento', string='Aparcamiento', required=True)
    mantenimiento_ids = fields.Many2many('garaje.mantenimiento', string='Mantenimientos')

    @api.depends('construido')
    def _get_annos(self):
        for coche in self:
            hoy=date.today()
            coche.annos = relativedelta(hoy,coche.construido).years

    #Restricciones, mismo formato que en la bd
    _sql_constraints=[('name_uniq', 'unique(name)', 'La matricula ya existe')]

class mantenimiento(models.Model):
    _name = 'garaje.mantenimiento'
    _description = 'Permite definir el mantenimiento rutinario de un coche'
    _order = 'fecha'

    fecha = fields.Date('Fecha', required=True, default = fields.date.today())
    tipo = fields.Selection(string='Tipo', selection=[('l','Lavar'),('r','Revisión'),('m','Mecánica'),('p','Pintura')], default = 'l')
    coste = fields.Float('Coste', (8,2), help='Coste total del mantenimiento')
    
    coche_ids = fields.Many2many('garaje.coche', string='Coches')

    def name_get(self):
        resultados = []
        for mantenimiento in self:
            descripcion = f'{len(mantenimiento.coche_ids)} coches - {mantenimiento.coste} $' 
            resultados.append((mantenimiento.id, descripcion))
        return resultados