{
    'name': 'Gestion des Contrats - Parc Informatique',
    'version': '1.0.0',
    'summary': 'Suivi des contrats d’infogérance avec clients et équipements',
    'description': """
        Module professionnel de gestion des contrats pour prestataire IT :
        - Liaison client / équipements
        - Dates et période
        - Fréquence de facturation
        - Montant fixe ou dynamique
        - Préparation à la facturation automatique
    """,
    'category': 'Services/Infogérance',
    'author': 'Sylla Dev',
    'website': 'https://tonsite.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'parc_client', 'parc_equipement'],
    'data': [
        'security/ir.model.access.csv',
        'views/contrat_views.xml',
        'data/contrat_sequence.xml',

    ],
    'application': False,
    'installable': True,
}
