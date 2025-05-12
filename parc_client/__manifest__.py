{
    'name': 'Gestion Clients - Parc Informatique',
    'version': '1.0.0',
    'summary': 'Gestion des clients entreprise pour le suivi du parc informatique',
    'description': """
        Module de gestion des clients d’infogérance :
        - Suivi des clients
        - Multi-sites (agences, sièges)
        - Préparation à la gestion de parc
    """,
    'category': 'Services/IT',
    'author': 'SSIH',
    'website': 'https://tonsite.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail','auth_signup', ],
    'data': [
        'security/ir.model.access.csv',
        'views/client_views.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
