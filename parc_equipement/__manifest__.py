{
    'name': 'Gestion Équipements - Parc Informatique',
    'version': '1.0.0',
    'summary': 'Suivi des équipements IT (matériels, logiciels) affectés aux clients',
    'description': """
        Module pour gérer :
        - Équipements (ordinateurs, routeurs, imprimantes, etc.)
        - Licences logicielles
        - Affectation aux clients
        - Dates de garantie, état, etc.
    """,
    'category': 'Services/IT',
    'author': 'SSIH',
    'website': 'https://tonsite.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'parc_client'],
    'data': [
        'security/ir.model.access.csv',
        'data/equipement_sequence.xml',
        'views/equipement_views.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
