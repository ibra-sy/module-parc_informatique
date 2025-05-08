{
    'name': 'Facturation Automatisée - Parc Informatique',
    'version': '1.0',
    'category': 'Services/Infogérance',
    'summary': 'Génère automatiquement les factures liées aux contrats',
    'author': 'Sylla Dev',
    'depends': ['base', 'mail', 'parc_contrat'],
    'data': [
        'security/ir.model.access.csv',
        'data/facture_sequence.xml',
        'data/cron_facturation.xml',
        'views/facture_views.xml',
    ],
    'installable': True,
    'application': False,
}
