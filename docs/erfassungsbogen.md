## **Titel der Arbeit**  

- Realitätsnahe Audio-Augmentation für Live-Musik
- Realistic Augmentation of Audio Data for Live Music


## **Geplanter Arbeitsverlauf**

| Teilaufgaben                                                                         | Zeitumfang |
| ------------------------------------------------------------------------------------ | ---------- |
| Literaturrecherche & Einarbeitung in Python-Bibliotheken                             | 50h        |
| Datenbeschaffung & Varianzuntersuchung echter Liveaufnahmen                          | 70h        |
| Implementierung von Datenmanipulations-/Extraktions- Pipeline(s)                     | 70h        |
| Exploration und Anwendung wissenschaftlicher Methoden für Auswahl der Hyperparameter | 50h        |
| Bewertungsmetriken evaluieren und orchestrieren                                      | 50h        |
| Auswertung und Verschriftlichung der Ergebnisse                                      | 80h        |

## **Problemstellung**

In der Livemusik bleibt die automatische Cue-Erkennung aufgrund der Komplexität und Unvorhersagbarkeit der echten Welt bisher noch sehr schwierig.   
Die zentrale Herausforderung von KI-basierter Cue-Erkennung liegt in der Datenknappheit, da ausreichend viele Live-Aufnahmen selten oder teuer sind.

Der Zweck dieser Arbeit ist es zu untersuchen, wie man via Perturbationen die Komplexität echter Performance-Aufnahmen sinnvoll nachstellen kann, um damit künstliche Datensätze aus wenigen Datenpunkten als Trainingsgrundlage für spezialisierte KI-Modelle zu schaffen.

## **Zielsetzung**

Die Thesis soll im Wesentlichen drei Fragen beantworten:
Wie unterscheiden sich verschiedene Live-Performances desselben Musikstücks in zeitlichen und spektralen Eigenschaften (Varianz)?
Wie unterscheiden sich verschiedene Augmentationsansätze darin, realistische Live-Performance-Charakteristika nachzustellen, welchen Einfluss haben sie auf die Qualität der erzeugten Daten? 
Wie lässt sich eine geeignete Bewertungsmetrik für die Authentizität von Live-Performances auf Basis bestehender Metriken entwickeln?

Das Hauptziel der Arbeit ist die Entwicklung und Exploration von Methoden zur Generierung synthetischer Audiodaten. 
Diese basieren auf einer datengetriebenen Analyse echter Live-Aufnahmen und weisen daher messbar realistische Live-Performance-Charakteristika auf.
Aus einer einzelnen annotierten Aufnahme werden also künstliche, robuste Trainingsdatensätze mit realitätsnaher Varianz generiert.
Da etablierte Metriken für Live-Performance-Authentizität fehlen, wird eine domänenspezifische Bewertungsmethode auf Basis bestehender Ansätze entwickelt.


## **Vorgehensweise**

Anfangs findet eine Literaturrecherche und die Einarbeitung in relevante Python-Libraries für Audio-Analyse und Perturbation statt.
Daraufhin wird die Varianz echter Live-Aufnahmen empirisch untersucht, indem relevante Audio-Features extrahiert, analysiert und verglichen werden. Die Ergebnisse werden als Zielwerte für die anschließende Implementierung unserer Perturbationsmethodiken dienen. 
Für die Erstellung der künstlichen Datensätze wird eine modulare Pipeline entworfen, die es ermöglicht, gewählte Perturbationen anzuwenden und Features zu extrahieren.
Es gilt herauszufinden, welche Arten von Perturbationen und deren Intensitäten vorteilhaft für eine realistische Augmentation sind.
Aufgrund des großen Hyperparameterraums werden für die Parameter-Optimierung wissenschaftlich fundierte Methoden hinsichtlich ihrer Eignung untersucht und evaluiert.
Die Bewertung der Ergebnisse erfolgt primär durch Vergleich der Feature-Verteilungen zwischen augmentierten und echten Live-Aufnahmen.
Bestehende Evaluationsmetriken werden analysiert und speziell für die Live-Performance-Domäne adaptiert.


## **Ergebnisvereinbarung**
Die schriftliche Ausarbeitung der Arbeit erfolgt auf Englisch und umfasst nicht weniger als 30 und nicht mehr als 50 Seiten. Im Rahmen der Arbeit erstellter Quellcode wird dem Institut für weitere Forschungszwecke zur Verfügung gestellt. 
Der Quellcode wird sachlich und sauber dokumentiert. 
Die Ergebnisse der Arbeit werden im Rahmen einer Abschlusspräsentation mit anschließender Diskussion vor fachkundigem Publikum vorgestellt.

## Literatur
- [Effect of Sound Data Augmentation Methods](https://transactions.ismir.net/articles/10.5334/tismir.26)
- [MUDA Software Framework Paper](https://brianmcfee.net/papers/ismir2015_augmentation.pdf)
- [The Nature and Perception of Fluctuations in Human Musical Rhythms](https://pmc.ncbi.nlm.nih.gov/articles/PMC3202537/)
- [Music Performance Analysis: A Survey](https://arxiv.org/abs/1907.00178)
- [Tree-Structured Parsen Estimator (Bayesian Optimization)](https://arxiv.org/pdf/2304.11127)
- [Fréchet Audio Distance](https://www.isca-archive.org/interspeech_2019/kilgour19_interspeech.html)
- [Automated Data Augmentation for Audio Classification](https://dl.acm.org/doi/10.1109/TASLP.2024.3402049)