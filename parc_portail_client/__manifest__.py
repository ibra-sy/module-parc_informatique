# -*- coding: utf-8 -*-
{
    "name": "Portail Client – Gestion de Parc",
    "version": "1.0.0",
    "category": "Website",
    "summary": "Portail client : équipements, contrats, factures (PDF) et tickets d’intervention.",
    "description": """
Ce module ajoute un portail dédié aux clients :
 • tableau de bord personnalisé
 • consultation des équipements, contrats, factures
 • téléchargement PDF des factures
 • création & suivi des tickets d’intervention
 • page Mon profil (mise à jour des coordonnées)
""",
    "author": "Dev SYLLA",
    "website": "https://votre-site-web.com",
    "license": "LGPL-3",
    "depends": [
        "base",
        "web",
        "portal",
        "website",
        "mail",
        "account",           # pour les PDF et l’état des factures
        "parc_client",
        "parc_equipement",
        "parc_contrat",
        "parc_facturation",
        "parc_intervention",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/portal_menu.xml",
        "views/portal_templates.xml",
        "report/facture_report.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
