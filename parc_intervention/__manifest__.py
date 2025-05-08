{
    'name': 'Gestion des interventions techniques',
    'version': '1.0',
    'category': 'Services/Infogérance',
    'summary': 'Tickets, interventions et suivi technique des clients',
    'author': 'Sylla Dev',
    'depends': ['base', 'mail', 'parc_equipement', 'parc_client'],
    'data': [
        'security/ir.model.access.csv',
        'views/intervention_views.xml',
    ],
    'installable': True,
    'application': False,
}
