## **Titel der Arbeit**  

- Realitätsnahe Audio-Augmentation für Live-Musik
- Realistic Augmentation of Audio Data for Live Music


## **Geplanter Arbeitsverlauf**

| Teilaufgaben                                                                         | Zeitumfang |
| ------------------------------------------------------------------------------------ | ---------- |
| Literaturrecherche & Einarbeitung in Python-Bibliotheken                             | 60h        |
| Datenbeschaffung & Varianzuntersuchung echter Liveaufnahmen                          | 70h        |
| Implementierung von Datenmanipulations-/Extraktions- Pipeline(s)                     | 90h        |
| Exploration und Anwendung wissenschaftlicher Methoden für Auswahl der Hyperparameter | 50h        |
| Auswertung und Verschriftlichung der Ergebnisse                                      | 100h       |

## **Problemstellung**

In der Livemusik bleibt die automatische Cue-Erkennung aufgrund der Komplexität und Unvorhersagbarkeit der echten Welt bisher noch sehr schwierig.   
Die zentrale Herausforderung von KI-basierter Cue-Erkennung liegt in der Datenknappheit, da ausreichend viele Live-Aufnahmen selten oder teuer sind.

Der Zweck dieser Arbeit ist es zu untersuchen, wie man via Perturbationen die Komplexität echter Performance-Aufnahmen sinnvoll nachstellen kann, um damit künstliche Datensätze aus wenigen Datenpunkten als Trainingsgrundlage für spezialisierte KI-Modelle zu schaffen.

## **Zielsetzung**

Das Hauptziel dieser Arbeit ist die Entwicklung und Explorierung von Methoden zur Generierung synthetischer Audiodaten. 
Diese basieren auf einer datengetriebenen Analyse echter Live-Aufnahmen und weisen daher messbar realistische Live-Performance-Charakteristika auf.
Aus einer einzelnen annotierten Aufnahme werden also künstliche, robuste Trainingsdatensätze mit realitätsnaher Varianz generiert, welche voraussichtlich für zukünftige Arbeiten im Training spezialisierter Modelle verwendet werden können, als Basis eines Cue-Detection-Frameworks.

Die Thesis soll im Wesentlichen drei Fragen beantworten:
Wie unterscheiden sich verschiedene Live-Performances desselben Musikstücks in zeitlichen und spektralen Eigenschaften (Varianz)?
Wie unterscheiden sich verschiedene Augmentationsansätze via Perturbationen darin, realistische Live-Performance-Charakteristika zu generieren? 
Welche Ansätze können die statistischen Eigenschaften echter Live-Aufnahmen am besten reproduzieren?



## **Vorgehensweise**

Anfangs findet eine Literaturrecherche und die Einarbeitung in relevanter Python-Libraries für Audio-Analyse und Perturbation statt.
Daraufhin wird die Varianz echter Live-Aufnahmen empirisch untersucht, indem relevante Audio-Features extrahiert, analysiert und verglichen werden. Die Ergebnisse werden als Zielwerte für die anschließende Implementierung unserer Perturbationsmethodiken dienen. 
Für die Erstellung der künstlichen Datensätze wird eine modulare Pipeline entworfen, die es ermöglicht, gewählte Perturbationen anzuwenden und Features zu extrahieren.
Dabei gilt es herauszufinden, welche Arten von Perturbationen und deren Intensitäten vorteilhaft für eine realistische Augmentation sind.
Aufgrund des großen Hyperparameterraums werden für die Parameter-Optimierung wissenschaftlich fundierte Methoden hinsichtlich ihrer Eignung untersucht und evaluiert.
Die Bewertung der Ergebnisse erfolgt primär durch Vergleich der Feature-Verteilungen zwischen augmentierten und echten Live-Aufnahmen.
Ergänzend können weitere Metriken hinzugenommen werden, um die erzeugten Datensätze aus mehreren Perspektiven zu bewerten.


## **Ergebnisvereinbarung**
Die schriftliche Ausarbeitung der Arbeit erfolgt auf Englisch und umfasst nicht weniger als 30 und nicht mehr als 50 Seiten. Im Rahmen der Arbeit erstellter Quellcode wird dem Institut für weitere Forschungszwecke zur Verfügung gestellt. 
Der Quellcode wird sachlich und sauber dokumentiert. 
Die Ergebnisse der Arbeit werden im Rahmen einer Abschlusspräsentation mit anschließender Diskussion vor fachkundigem Publikum vorgestellt.

