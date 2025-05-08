<!-- -------------------------------------------------------------------- -->
<!--  Parc Informatique – ITSM Modules for Odoo 18                        -->
<!-- -------------------------------------------------------------------- -->

# Parc Informatique – ITSM modules for **Odoo 18**

A lightweight alternative to GLPI, entirely integrated in Odoo’s ERP stack.

| Module | Purpose |
|--------|---------|
| **parc_client**        | Company / site database and automatic portal account |
| **parc_equipement**    | Hardware & software inventory (warranty, status, pictures) |
| **parc_contrat**       | Managed-services contracts, billing frequency & status |
| **parc_facturation**   | Recurring invoices in XOF (or any currency) – PDF reports |
| **parc_intervention**  | Help-desk tickets, technician assignment, full history |
| **parc_portail_client**| Self-service portal (assets, contracts, invoices, tickets) |

---

## ✨ Key features

* **Multi-tenant** : each customer sees only its own assets and tickets.  
* **Recurring billing** : daily cron creates invoices on contract schedule.  
* **Email ready** : “forgot password” & ticket notifications (SMTP configurable).  
* **KPI dashboard** : counts for equipment, contracts, tickets, invoices.  
* **GLPI-style ticketing** : client chooses equipment, adds description, uploads files.  
* **Tech-friendly** : pure Odoo ORM, no external dependencies.

---

## 🗝️ Prerequisites

| Software | Min. version |
|----------|--------------|
| Odoo (Community / Enterprise) | **18.0** |
| PostgreSQL | 13 |
| Python | 3.10 |

> The modules might work on Odoo 17 but are *officially* supported on 18.

---

## 🚀 Quick start

```bash
git clone https://github.com/<your-org>/odoo-parc-modules.git \
          /opt/odoo/custom_addons

# Add the folder to odoo.conf
echo 'addons_path = /opt/odoo/odoo/addons,/opt/odoo/custom_addons' \
     >> /opt/odoo/etc/odoo.conf

# Initialise a fresh DB and install the suite
python odoo-bin -d parc_demo -i parc_client,parc_equipement,parc_contrat,\
parc_facturation,parc_intervention,parc_portail_client --db-filter=parc_demo$

A demo company, equipment and contracts are imported automatically (demo data can be disabled by removing demo/*.xml files).


---

⚙️ Configuration steps

1. SMTP server
Activate Settings ▸ Technical ▸ Outgoing Mail Servers
or import parc_client/data/mail_server.xml and edit credentials.


2. Sequences (already created, but adjustable)

Settings ▸ Technical ▸ Sequences :
EQP (equipments), CTR (contracts), FAC (invoices), INT (tickets)



3. User groups

Portal: automatically assigned to customer contacts

Technician: activate Settings ▸ Users ➜ “Parc Informatique / Technician”



4. Cron job

Settings ▸ Technical ▸ Scheduled Actions →
“Generate recurring invoices” (enabled daily at 03:00)





---

👤 Client portal

URL	Feature

/my	Dashboard
/my/equipments	Asset list (picture, serial, warranty, state)
/my/contracts	Contracts (PDF export)
/my/invoices	List + PDF download
/my/tickets	Ticket history
/my/tickets/new	Create new ticket
/my/profile	Edit contact details


First login

1. Back-office creates a Parc Client record and enters an Email.


2. The module generates a res.partner + Portal user (inactive).


3. Click “Action ▸ Send Invitation” to e-mail a password-setup link.




---

🧑‍💻 Development

# black & flake8
pip install -r dev-requirements.txt
black custom_addons
flake8 custom_addons
# run tests
python odoo-bin -d test_parc -i parc_* --test-enable --stop-after-init

Contributions are welcome — please open an issue or pull-request.


---

🛣️ Roadmap

Asset depreciation & amortisation

Multi-site stock / spare parts management

Technician mobile app (OWL)

SLA metrics & charts



---

📜 License

MIT


---

✉️ Support

Create an issue on GitHub or mail opensource@yourcompany.example.

> “Take care of your customers’ IT while Odoo takes care of the rest.”





<!-- -------------------------------------------------------------------- -->
<!--  Parc Informatique – ITSM Modules for Odoo 18                        -->
<!-- -------------------------------------------------------------------- -->

# Parc Informatique – ITSM modules for **Odoo 18**

A lightweight alternative to GLPI, entirely integrated in Odoo’s ERP stack.

| Module | Purpose |
|--------|---------|
| **parc_client**        | Company / site database and automatic portal account |
| **parc_equipement**    | Hardware & software inventory (warranty, status, pictures) |
| **parc_contrat**       | Managed-services contracts, billing frequency & status |
| **parc_facturation**   | Recurring invoices in XOF (or any currency) – PDF reports |
| **parc_intervention**  | Help-desk tickets, technician assignment, full history |
| **parc_portail_client**| Self-service portal (assets, contracts, invoices, tickets) |

---

## ✨ Key features

* **Multi-tenant** : each customer sees only its own assets and tickets.  
* **Recurring billing** : daily cron creates invoices on contract schedule.  
* **Email ready** : “forgot password” & ticket notifications (SMTP configurable).  
* **KPI dashboard** : counts for equipment, contracts, tickets, invoices.  
* **GLPI-style ticketing** : client chooses equipment, adds description, uploads files.  
* **Tech-friendly** : pure Odoo ORM, no external dependencies.

---

## 🗝️ Prerequisites

| Software | Min. version |
|----------|--------------|
| Odoo (Community / Enterprise) | **18.0** |
| PostgreSQL | 13 |
| Python | 3.10 |

> The modules might work on Odoo 17 but are *officially* supported on 18.

---

## 🚀 Quick start

```bash
git clone https://github.com/<your-org>/odoo-parc-modules.git \
          /opt/odoo/custom_addons

# Add the folder to odoo.conf
echo 'addons_path = /opt/odoo/odoo/addons,/opt/odoo/custom_addons' \
     >> /opt/odoo/etc/odoo.conf

# Initialise a fresh DB and install the suite
python odoo-bin -d parc_demo -i parc_client,parc_equipement,parc_contrat,\
parc_facturation,parc_intervention,parc_portail_client --db-filter=parc_demo$

A demo company, equipment and contracts are imported automatically (demo data can be disabled by removing demo/*.xml files).


---

⚙️ Configuration steps

1. SMTP server
Activate Settings ▸ Technical ▸ Outgoing Mail Servers
or import parc_client/data/mail_server.xml and edit credentials.


2. Sequences (already created, but adjustable)

Settings ▸ Technical ▸ Sequences :
EQP (equipments), CTR (contracts), FAC (invoices), INT (tickets)



3. User groups

Portal: automatically assigned to customer contacts

Technician: activate Settings ▸ Users ➜ “Parc Informatique / Technician”



4. Cron job

Settings ▸ Technical ▸ Scheduled Actions →
“Generate recurring invoices” (enabled daily at 03:00)





---

👤 Client portal

URL	Feature

/my	Dashboard
/my/equipments	Asset list (picture, serial, warranty, state)
/my/contracts	Contracts (PDF export)
/my/invoices	List + PDF download
/my/tickets	Ticket history
/my/tickets/new	Create new ticket
/my/profile	Edit contact details


First login

1. Back-office creates a Parc Client record and enters an Email.


2. The module generates a res.partner + Portal user (inactive).


3. Click “Action ▸ Send Invitation” to e-mail a password-setup link.




---

🧑‍💻 Development

# black & flake8
pip install -r dev-requirements.txt
black custom_addons
flake8 custom_addons
# run tests
python odoo-bin -d test_parc -i parc_* --test-enable --stop-after-init

Contributions are welcome — please open an issue or pull-request.


---

🛣️ Roadmap

Asset depreciation & amortisation

Multi-site stock / spare parts management

Technician mobile app (OWL)

SLA metrics & charts



---

📜 License

MIT


---

✉️ Support

Create an issue on GitHub or mail opensource@yourcompany.example.

> “Take care of your customers’ IT while Odoo takes care of the rest.”
<!-- -------------------------------------------------------------------- -->
<!--  Parc Informatique – ITSM Modules for Odoo 18                        -->
<!-- -------------------------------------------------------------------- -->

# Parc Informatique – ITSM modules for **Odoo 18**

A lightweight alternative to GLPI, entirely integrated in Odoo’s ERP stack.

| Module | Purpose |
|--------|---------|
| **parc_client**        | Company / site database and automatic portal account |
| **parc_equipement**    | Hardware & software inventory (warranty, status, pictures) |
| **parc_contrat**       | Managed-services contracts, billing frequency & status |
| **parc_facturation**   | Recurring invoices in XOF (or any currency) – PDF reports |
| **parc_intervention**  | Help-desk tickets, technician assignment, full history |
| **parc_portail_client**| Self-service portal (assets, contracts, invoices, tickets) |

---

## ✨ Key features

* **Multi-tenant** : each customer sees only its own assets and tickets.  
* **Recurring billing** : daily cron creates invoices on contract schedule.  
* **Email ready** : “forgot password” & ticket notifications (SMTP configurable).  
* **KPI dashboard** : counts for equipment, contracts, tickets, invoices.  
* **GLPI-style ticketing** : client chooses equipment, adds description, uploads files.  
* **Tech-friendly** : pure Odoo ORM, no external dependencies.

---

## 🗝️ Prerequisites

| Software | Min. version |
|----------|--------------|
| Odoo (Community / Enterprise) | **18.0** |
| PostgreSQL | 13 |
| Python | 3.10 |

> The modules might work on Odoo 17 but are *officially* supported on 18.

---

## 🚀 Quick start

```bash
git clone https://github.com/<your-org>/odoo-parc-modules.git \
          /opt/odoo/custom_addons

# Add the folder to odoo.conf
echo 'addons_path = /opt/odoo/odoo/addons,/opt/odoo/custom_addons' \
     >> /opt/odoo/etc/odoo.conf

# Initialise a fresh DB and install the suite
python odoo-bin -d parc_demo -i parc_client,parc_equipement,parc_contrat,\
parc_facturation,parc_intervention,parc_portail_client --db-filter=parc_demo$

A demo company, equipment and contracts are imported automatically (demo data can be disabled by removing demo/*.xml files).


---

⚙️ Configuration steps

1. SMTP server
Activate Settings ▸ Technical ▸ Outgoing Mail Servers
or import parc_client/data/mail_server.xml and edit credentials.


2. Sequences (already created, but adjustable)

Settings ▸ Technical ▸ Sequences :
EQP (equipments), CTR (contracts), FAC (invoices), INT (tickets)



3. User groups

Portal: automatically assigned to customer contacts

Technician: activate Settings ▸ Users ➜ “Parc Informatique / Technician”



4. Cron job

Settings ▸ Technical ▸ Scheduled Actions →
“Generate recurring invoices” (enabled daily at 03:00)





---

👤 Client portal

URL	Feature

/my	Dashboard
/my/equipments	Asset list (picture, serial, warranty, state)
/my/contracts	Contracts (PDF export)
/my/invoices	List + PDF download
/my/tickets	Ticket history
/my/tickets/new	Create new ticket
/my/profile	Edit contact details


First login

1. Back-office creates a Parc Client record and enters an Email.


2. The module generates a res.partner + Portal user (inactive).


3. Click “Action ▸ Send Invitation” to e-mail a password-setup link.




---

🧑‍💻 Development

# black & flake8
pip install -r dev-requirements.txt
black custom_addons
flake8 custom_addons
# run tests
python odoo-bin -d test_parc -i parc_* --test-enable --stop-after-init

Contributions are welcome — please open an issue or pull-request.


---

🛣️ Roadmap

Asset depreciation & amortisation

Multi-site stock / spare parts management

Technician mobile app (OWL)

SLA metrics & charts



---

📜 License

MIT


---

✉️ Support

Create an issue on GitHub or mail opensource@yourcompany.example.

> “Take care of your customers’ IT while Odoo takes care of the rest.”










