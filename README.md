
---

# Sistem de Licitații

Acest proiect implementează un sistem de licitații client-server folosind socket-uri în Python. Sistemul permite mai multor clienți să se conecteze la un server, să adauge produse pentru licitație și să plaseze oferte pentru produse. Serverul gestionează lista de clienți și produse licitate și notifică clienții despre noi oferte și rezultate ale licitațiilor.

## Funcționalități

- **Înregistrarea clientului**: Clienții se conectează la server cu un nume unic.
- **Adăugare produs**: Clienții pot adăuga produse pentru licitație, specificând un preț de pornire.
- **Plasare ofertă**: Clienții pot plasa oferte pentru produsele aflate în curs de licitație.
- **Notificări**: Clienții primesc notificări când sunt adăugate produse noi, când sunt plasate oferte și când se încheie licitațiile.
- **Timp licitație**: Fiecare licitație are o durată predefinită gestionată de server.

## Cerințe

- Python 3.x

## Structura Fișierelor

- `client.py`: Codul aplicației client.
- `server.py`: Codul aplicației server.
- `auction.py`: Codul pentru gestionarea licitațiilor.
- `product.py`: Codul pentru gestionarea produselor.

## Utilizare

### Server

1. Pornește serverul rulând `server.py`:

   ```bash
   python server.py
   ```

   Serverul va porni și va asculta conexiuni pe `localhost:12345`.

### Client

1. Pornește un client rulând `client.py`:

   ```bash
   python client.py
   ```

2. Introdu numele tău unic când ți se cere. Dacă numele este deja folosit, va trebui să introduci un alt nume.
3. După conectare, vei vedea lista de comenzi disponibile:

   - `ADAUGA_PRODUS <nume_produs> <pret_initial>`: Adaugă un nou produs pentru licitație.
   - `PUNE_LICITATIE <nume_produs> <suma_licitata>`: Plasează o ofertă pentru un produs existent.
   - `EXIT`: Ieșire din aplicație.

### Exemple de Utilizare

1. **Adaugă un produs pentru licitație**:

   ```plaintext
   ADAUGA_PRODUS masina 100
   ```

   Adaugă un nou produs numit "sabie" cu un preț de pornire de 100.

2. **Plasează o ofertă**:

   ```plaintext
   PUNE_LICITATIE masina 150
   ```

   Plasează o ofertă de 150 pentru produsul numit "sabie".

3. **Ieși din aplicație**:

   ```plaintext
   EXIT
   ```

   Deconectează clientul de la server.

## Detalii Implementare

### `server.py`

- Gestionează conexiunile și interacțiunile cu clienții.
- Se ocupă de adăugarea produselor, plasarea ofertelor și notificarea clienților despre evenimentele licitațiilor.
- Gestionează durata licitațiilor pentru fiecare produs.

### `client.py`

- Se conectează la server și permite utilizatorului să interacționeze cu sistemul de licitații.
- Trimite comenzi către server și primește notificări.

### `auction.py`

- Gestionează lista de produse și clienți.
- Se ocupă de adăugarea produselor, plasarea ofertelor și notificarea clienților.
- Gestionează durata licitațiilor și finalizează licitațiile.

### `product.py`

- Reprezintă un produs aflat în licitație.
- Gestionează plasarea ofertelor și menține informații despre cea mai mare ofertă și ofertant.

---
