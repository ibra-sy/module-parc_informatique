{
    'name': 'Parc Informatique',
    'version': '1.0.0',
    'summary': 'Gestion complète des clients, équipements, contrats, factures et interventions',
    'description': """
        Module principal pour la gestion du parc informatique.
        - Ce module installe automatiquement les modules suivants :
          - Gestion des Clients
          - Gestion des Équipements
          - Gestion des Contrats
          - Gestion des Factures
          - Gestion des Interventions
    """,
    'category': 'Services/Infogérance',
    'author': 'Sylla Dev',
    'website': 'https://tonsite.com',
    'license': 'LGPL-3',
    'depends': [
        'parc_client',
        'parc_contrat',
        'parc_equipement',
        'parc_facturation',
        'parc_intervention'
    ],
    'data': [
        'views/menu_views.xml',
    ],
    'icon': '/parc_informatique/static/description/icon.png',
    'installable': True,
    'application': True,
    'auto_install': False,
}
