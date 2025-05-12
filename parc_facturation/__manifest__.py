# custom_addons/parc_facturation/__manifest__.py
{
    "name": "Facturation Automatisée - Parc Informatique",
    "version": "1.0.1",
    "summary": "Génère automatiquement les factures liées aux contrats d’infogérance",
    "category": "Services/Infogérance",
    "author": "Sylla Dev",
    "license": "LGPL-3",
    "depends": [
        "base",
        "mail",
        "parc_contrat",  
        "auth_signup",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/facture_sequence.xml",
        #"data/cron_facturation.xml",
        "data/mail_template.xml",
        "views/facture_views.xml",
    ],
    "installable": True,
    "application": False,
}
