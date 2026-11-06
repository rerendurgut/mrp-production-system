# 🏭 Material Requirements Planning (MRP) System

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat-square&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Boğaziçi University](https://img.shields.io/badge/Boğaziçi_University-IE442-003366?style=flat-square)](https://ie.boun.edu.tr/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

> **Enterprise Information Systems Project (IE 442)**  
> **Department of Industrial Engineering, Boğaziçi University**  
> **Author:** Recep Eren Durgut

---

## 📌 Project Overview

**Material Requirements Planning (MRP)** is a foundational computational system used in production and supply chain management to calculate gross requirements, net requirements, and planned order releases across complex multi-level Bills of Materials (BOM).

This repository implements an enterprise-grade MRP engine directly within a relational database architecture (**MySQL**), combined with an interactive Python **Streamlit** dashboard for real-time inventory monitoring and schedule tracking.

---

## 🏗️ Architecture & Database Design

The relational database schema is structured into normalized entities with cascading integrity:

1. **`items` & `bom`:** Defines parent-child component hierarchies, lead times, lot sizing rules, and assembly quantities.
2. **`orders`:** Tracks customer purchase orders, target delivery dates, and finished good quantities.
3. **`item_period`:** Time-phased scheduling table storing:
   * Gross Requirements ($GR_t$)
   * Scheduled Receipts ($SR_t$)
   * Projected Available Inventory ($EI_t$)
   * Net Requirements ($NR_t$)
   * Planned Order Receipts ($PORc_t$)
   * Planned Order Releases ($PORl_t$)
4. **Recursive Stored Procedures & Functions:**
   * `GetRequiredItemsCount`: Recursively navigates the BOM graph to evaluate cumulative sub-assembly requirements.
   * `UpdateMRP`: Computes time-phased netting and planned order explosions across all planning horizons.
5. **Event-Driven Database Triggers:**
   * `order_come`: Listens to incoming order records in the `orders` table and automatically triggers recalculation of downstream requirements.

---

## 📂 Repository Structure

```text
├── app.py                  # Streamlit frontend dashboard for inventory exploration
├── dosya_okuyucu.py        # Batch data ingestion and file loader
├── requirements.txt        # Python dependencies
├── sql/
│   ├── 1TABLES.sql         # Base relational table schema & constraints
│   ├── 2FUNCTION.sql       # Recursive BOM calculation functions
│   ├── 3PROCEDURE.sql      # Core time-phased netting stored procedure
│   ├── 4PROCEDURE2.sql     # Multi-level order explosion procedure
│   ├── 5TRIGGER.sql        # Real-time event-driven trigger definitions
│   └── 6TEST.sql           # Validation queries & sample scenarios
└── docs/
    └── IE_442_MRP_Report.pdf  # Comprehensive project report & BOM diagrams
```

---

## 🚀 Getting Started

### 1. Database Setup (MySQL)

Execute the SQL scripts in numerical sequence within your MySQL instance:

```bash
mysql -u root -p < sql/1TABLES.sql
mysql -u root -p mrp_database < sql/2FUNCTION.sql
mysql -u root -p mrp_database < sql/3PROCEDURE.sql
mysql -u root -p mrp_database < sql/4PROCEDURE2.sql
mysql -u root -p mrp_database < sql/5TRIGGER.sql
mysql -u root -p mrp_database < sql/6TEST.sql
```

### 2. Streamlit Dashboard

```bash
pip install -r requirements.txt

# Run the monitoring interface
streamlit run app.py
```

---

## 📑 Technical Report

The complete system architecture, mathematical derivations for inventory equations, and BOM trees are detailed in the [IE 442 MRP Report (PDF)](docs/IE_442_MRP_Report.pdf).

---

## 📜 License

MIT License. Developed by [Recep Eren Durgut](https://github.com/rerendurgut).
