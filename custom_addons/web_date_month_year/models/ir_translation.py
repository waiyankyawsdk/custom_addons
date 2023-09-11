# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models

DEFAULT_YEAR_FORMAT = '%Y'
DEFAULT_MONTH_FORMAT = '%m/%Y'


class IrTranslation(models.Model):
    _inherit = "ir.translation"

    @api.model
    def get_translations_for_webclient(self, mods, lang):
        translations_per_module, lang_params = super(IrTranslation, self).get_translations_for_webclient(mods, lang)
        if not lang:
            lang = self._context["lang"]
        langs = self.env['res.lang']._lang_get(lang)
        if langs:
            lang_params = langs.read([
                "name", "direction", "date_format",
                "month_format", "year_format",  # extra fields to read
                "time_format", "grouping", "decimal_point",
                "thousands_sep", "week_start"])[0]
            lang_params['week_start'] = int(lang_params['week_start'])
            lang_params['code'] = lang
        return translations_per_module, lang_params
