# Wikidata Explorer


## Inhalt

- [Über das Projekt](#über-das-projekt)
- [Ziel der Aufgabe](#ziel-der-aufgabe)
- [Projektablauf](#projektablauf)
- [Anweisungen für den Start des Projekts](#anweisungen-für-den-start-des-projekts)
- [Ergebnisse ansehen](#ergebnisse-ansehen)

## Über das Projekt

**Wikidata Explorer** ist eine schlanke Webanwendung, die im Rahmen einer Mini-Aufgabe zur Arbeit mit der Wissensdatenbank **Wikidata** entwickelt wurde.

Die Anwendung ermöglicht es Nutzer:innen, nach beliebigen Begriffen zu suchen und strukturierte Informationen wie **Beschreibungen**, **Eigenschaften** und **Bilder** zu verschiedenen Entitäten (z. B. Städte, Personen, Organisationen usw.) in einer übersichtlichen Benutzeroberfläche anzuzeigen.

---

##  Ziel der Aufgabe

Das Ziel dieser Aufgabe ist es, eine einfache generische Visualisierung von Wikidata-Einträgen zu implementieren. 
Entwicklung ein Konzept für eine einfache Benutzeroberfläche zur Visualisierung von Wikidata-Einträgen
- Die Benutzeroberfläche soll eine Art Suchbegriff bereitstellen
- Das Suchergebnis soll visualisiert werden
- Die Benutzerschnittstelle sollte alle oder einige der zugehörigen Eigenschaften der Ergebnisse anzeigen

---

## Projektablauf

1. **Entwurf eines UI-Prototyps** in Figma zur Visualisierung der geplanten Anwendung  
<img src="https://github.com/user-attachments/assets/8ce66030-a3f5-464e-86c8-43bb43d32aa5" width="300"/>
<img src="https://github.com/user-attachments/assets/bd5b866d-b285-4c39-a7ad-83c9f26367de" width="300"/>
<img src="https://github.com/user-attachments/assets/588e1075-169f-4b77-8caa-b77834a18910" width="300"/>

2. **Einführung in SPARQL-Abfragen** und die Nutzung des Wikidata Query Service:  
   👉 [https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries)

3. **Implementierung der Anwendung** mit dem Webframework **Flask** in der Programmiersprache **Python**,  
   inklusive Einsatz des Template-Systems **Jinja2** zur Darstellung der Benutzeroberfläche.

---

## Anweisungen für den Start des Projekts

### 🔧 Voraussetzungen

- **Python 3.8** oder höher  
- **Internetverbindung** (für SPARQL-Anfragen an den Wikidata-Server)

---
#### 1. Repository klonen

```bash
git clone https://github.com/ERNAZERO/wikidata_explorer.git
cd wikidata_explorer
```
#### 2. Virtuelle Umgebung erstellen und aktivieren
```
python -m venv venv*
```
*auf MacOs oder Linux:*
```
source venv/bin/activate  
```
*auf Windows:*
```
venv\Scripts\activate
```
#### 3. Abhängigkeiten installieren
```
pip install -r requirements.txt
```
#### 4. Projekt starten
```
python app.py
```
#### 5. Anwendung im Browser öffnen
http://127.0.0.1:5000

---

## Ergebnisse ansehen
<img src="https://github.com/user-attachments/assets/b111d560-a7a8-41a6-9954-977671b318b7" width="300"/>
<img src="https://github.com/user-attachments/assets/18bbcd95-04d5-41f6-93ad-4db65aee490b" width="300"/>
<img src="https://github.com/user-attachments/assets/d64a59b5-2401-4fa1-a01b-cc9c50d77eab" width="300"/>
