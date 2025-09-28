## **Titel der Arbeit**  
- Entwicklung einer Pipeline für realitätsnahe Audio-Augmentation (z.B. für Live-Musik Cue-Detection Modelle)
- Entwicklung einer Audio-Augmentation-Pipeline zur Simulation von Live-Performance-Variationen
- Pipeline Development for realistic audio augmentation

## **Problemstellung**

In der Livemusik bleibt die automatische Cue-Erkennung aufgrund der Komplexität und Unvorhersagbarkeit der echten Welt noch sehr schwierig.   
Gegebenheiten wie Umgebungsfaktoren, menschliche Variabilität und Unvorhersagbarkeit erschweren die automatische Cue-Erkennung deutlich.

Eine Überlegung wäre, ob sich ein zugeschnittenes KI-Modell für die Cue-Erkennung trainieren lässt.  
Die Cue-Zeitpunkte würden Labels/Targets entsprechen.  
Bei diesem Ansatz liegt die zentrale Herausforderung jedoch in der Datenknappheit. Für die meisten Bands wäre es unwirtschaftlich und schlicht zu aufwendig, ihre Songs hundertfach aufzunehmen, um eine solide Datengrundlage für das Training eines solchen Modells zu schaffen.

Der Zweck dieser Arbeit ist es zu untersuchen, wie man via Perturbationen die Komplexität echter Performances sinnvoll nachstellen kann, um damit künstliche Datensätze aus wenigen Datenpunkten als Trainingsgrundlage zu schaffen.

## **Zielsetzung**

Das Hauptziel dieser Arbeit ist die Entwicklung einer konfigurierbaren Pipeline als Basis eines Cue-Detection-Frameworks, welche aus sehr wenigen annotierten Live-Aufnahmen künstliche, robuste Trainingsdatensätze mit realitätsnaher Varianz für das Modelltraining generiert.

Dabei wird untersucht,  
1. Welchen Grad an Varianz man in echten Liveaufnahmen eines Musikstücks wiederfindet
2. Welche Arten von künstlichen Perturbationen robuste Trainingsdaten erzeugen und tatsächlich realitätsnah sind
3. wie die Hyperparameter und Kombinationen dieser Perturbationen sinnvoll gewählt werden können, sodass eine ähnliche Varianz erreicht wird wie die der echten Liveaufnahmen.
4. *optional* (~~Wie gut die Modelle, die auf augmentierten Daten trainiert wurden, auf echten Live-Aufnahmen funktionieren~~)

Der Fokus dieser Bachelorarbeit liegt also auf der sinnvollen prototypischen Umsetzung der Datenaugmentation unter Anwendung wissenschaftlich fundierter Methoden. 
Idealerweise soll die Implementierung bereits Output liefern, welches sofort für das Training eines Cue-Detection-Modells verwendet werden kann. 

*optional*
(~~Im Rahmen des Frameworks werden einfache, auf CNN oder LSTM basierende Modelle trainiert um die Qualität der augmentierten Daten zu prüfen und zu vergleichen. (TODO wie "einfach" sollen die Modelle sein?)
Die Cues wären im Kontext dieser Arbeit, um es simpel zu halten, lediglich annotierte Zeitpunkte und würden für das Modell als Labels/Targets dienen. ~~) 



## **Vorgehensweise**
### Phase 1: Literaturrecherche/Einarbeitung
Anfangs findet eine Literaturrecherche statt, um herauszufinden, welche State-of-the-Art Ansätze zu Audio-Perturbationen oder Datengenerierung via Perturbationen im Allgemeinen existieren.
Parallel erfolgt idealerweise bereits die Einarbeitung in ausgewählte Audio-Analyse Libraries (z.B. https://librosa.org/doc/latest/index.html) für den Umgang mit Audiodateien und Perturbationen in Python.
### Phase 2: Datenbeschaffung & Varianzuntersuchung
Daraufhin wird empirisch untersucht, wie der Grad der Varianz eines Musikstücks/Songs über mehrere Liveaufnahmen hinweg grundsätzlich aussieht
(Hier eignen sich grundsätzlich Aufnahmen von Liveauftritten, in denen die Bands das "Taping" erlauben).
Es werden relevante Audio-Features (Lautstärke, Tempo, Spektrale Features, ...) aus den Liveaufnahmen extrahiert und analysiert, um ein Gesamtbild zu erhalten, welche Zielwerte in der eigenen Implementierung erreicht werden sollten.
### Phase 3: Pipeline-Implementierung
Es folgt die Überlegung, welche künstlichen Perturbationen in welchen Intensitäten und Kombinationen infrage kommen:  
- (variable) Tempoveränderung  
- (Semiton oder variables) Pitch-Shifting  
- Einmischen von Rausch- und Störgeräuschen (Publikumsgeräusche, Umgebungsgeräusche...)  
- Audio-Processing-FX um reale Bedingungen zu simulieren  
    - Low/Mid/High EQ  
    - Kompression  
    - Reverb / Delay, (ggf. subtil auch Chorus, Flanger, Phaser, …)  

Es muss also eine sinnvolle Pipeline zur Datenmanipulation und entsprechender Feature Extraction für die spätere Auswertung der Ergebnisse konzipiert werden.
Die Pipeline nimmt einen oder wenige annotierte Datenpunkte als Input und liefert einen einsetzbaren, künstlichen Datensatz mit passenden Annotationen als Output.
Bei zeitverändernden Perturbationen muss also auch die Annotation berücksichtigt und ebenfalls manipuliert werden.
Die Implementierung sollte seed-basiert sein um deterministische und reproduzierbare Transformationen zu gewährleisten.

Gegebenenfalls finden am Ende dieser Phase schon erste Tests mit fixen, willkürlich gewählten Parametern statt.

### Phase 4: Hyperparameteroptimierung
Die Aufgabe der Thesis ist es herauszufinden, welche Arten von Perturbationen und ihren jeweiligen Intensitäten hilfreich für die realistische Augmentation sind und welche nur wenig Nutzen bringen.
Je nach eingesetzten Perturbationen, steht man bei der Generierung vor einem sehr großen Hyperparameterraum.
Die naive Herangehensweise einer iterativen Datengenerierung mit willkürlichen Parametern und anschließender Validierung ist aufgrund der Komplexität und dem großen Perturbations-Parameterraum unpraktikabel.  
Es ist also essenziell, diese Problemstellung mit wissenschaftlich fundierten Methoden anzugehen, z.B. mit Grid Search oder Bayesianischer Optimierung. 

Die verschiedenen Optimierungsstrategien für die Hyperparameterwahl werden systematisch untersucht, verglichen und evaluiert um herauszufinden, welche am effektivsten und praktikabel sind.  

Ziel ist es in dieser Phase, die Distanz zwischen den Feature-Verteilungen echter und augmentierter Live-Aufnahmen, also die Varianz zwischen künstlichem und echten Datensatz, zu minimieren.

### Phase 5: Bewertung & Vergleich
Es müssen Bewertungsmetriken erwägt und implementiert werden, um die Wirksamkeit der künstlichen Datensätze zu bewerten.

Hier bietet sich die intrinsische Bewertung der Features der augmentierten Daten an, z.B. durch: 
- Vergleich der Verteilungen der echten und augmentierten Datensätzen
- Analyse entstehender Cluster
- Plausibilität und Musikidentität der augmentierten Daten bewerten
- Cross-Song Validation
- Robustheit über Genres hinweg
- Ablationsstudie
- ...

Je nach Bedarf können weitere Metriken hinzugenommen werden, um die erzeugten Datensätze aus mehreren Perspektiven zu bewerten. Die Wahl der konkreten Bewertungsmetriken wird also während des Arbeitsverlaufs stattfinden.

Die augmentierten Daten werden mit einer Baseline (Originaldaten, vorherige Pipeline Prototypen Implementierungen, Ablation, Random/Naive Augmentation, ..) verglichen.
Auch muss geprüft werden, ob die Annotationen der künstlichen Daten korrekt sind.




