import logging
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import base64
import os
import pathlib

_logger = logging.getLogger(__name__)


class DocumentMigrateWizard(models.TransientModel):
    """_summary_

        1. Move 70 GB data to the document_migration/wizard/docs
        2.Identify the models and fields for which doc is to be migrated  - inseta.sdf
        3.
    """

    _name = "document.migrate.wizard"
    _description = "Document Migrate Wizard"

    model_id = fields.Many2one('ir.model')

    file_field_id = fields.Many2one(
        'ir.model.fields', 
        domain="[('model_id','=', model_id)]",
        help='Binary Field the document is to be migrated to'
    )


    def find(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    def action_migrate(self):

        #os.path.dirname(os.path.abspath(__file__))
        
        """
        migrate org documents  = inseta.organisationdocuments
        """
        org_docs = self.env[self.model_id.model].sudo().search([(self.file_field_id.name,'=',False)])
        for rec in org_docs:
            if rec.legacy_filepath:
                file_name = rec.legacy_filepath.split('/')[3]

                _logger.info(f"file name {file_name}")

                path = pathlib.Path(__file__).parent.resolve()
                files_for_upload_dir = os.path.join(path, 'docs') #f"{path}/docs"
                _logger.info(f"file for upload {files_for_upload_dir}")

                found_file = self.find(file_name, files_for_upload_dir)
                if found_file:
                    file = open(found_file, "rb")
                    filestream = file.read()

                    file.close()

                    rec.write({self.file_field_id: base64.b64encode(filestream)})
