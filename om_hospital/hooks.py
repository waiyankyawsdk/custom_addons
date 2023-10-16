import logging
from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

def test_post_init_test(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.config_parameter'].sudo().set_param('config_data_test' , "{'section' : {'option' : 'value'} }")
    print("Test post init test")
    _logger.info("---------------------------------------Done Post Init Test-----------------------------------------")

def post_load_hook():
    print("Server restart and post load triggered----------------------------------------------------------")

def post_upgrade_hook(cr, registry):
    print("Post Upgrade hook trigger---------------------------------------------------")