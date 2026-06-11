"""
SensorPy – Messdaten analysieren
=================================
Dieses Modul enthält alle Funktionen zur Analyse von Umweltmessdaten.

Aufgabe: Implementiert jede Funktion so, dass sie der Beschreibung
im Docstring entspricht. Die Signatur (Name, Parameter, Rückgabetyp)
darf NICHT verändert werden.

Datenformat (eine Zeile aus messdaten.csv als dict):
    {
        "sensor_id":       "S01",
        "timestamp":       "2024-03-01 08:00",
        "temperatur":      19.2,
        "luftfeuchtigkeit": 52.1,
        "co2":             480.0
    }
"""

import csv


# ──────────────────────────────────────────────────────────────
# PERSON A
# ──────────────────────────────────────────────────────────────

def load_data(filename: str) -> list[dict]:
    """Liest eine CSV-Datei mit Messdaten ein und gibt sie als Liste zurück.

    Jede Zeile der CSV wird in ein dict umgewandelt.
    Numerische Felder (temperatur, luftfeuchtigkeit, co2) werden
    automatisch in float konvertiert.

    Args:
        filename: Pfad zur CSV-Datei (z. B. "data/messdaten.csv")

    Returns:
        Liste von dicts, eines pro Zeile. Leere Liste bei Fehler.

    Beispiel:
        >>> daten = load_data("data/messdaten.csv")
        >>> print(daten[0]["sensor_id"])
        S01
        >>> print(daten[0]["temperatur"])
        19.2
    """
    # TODO: Implementierung hier einfügen
    pass


def calculate_average(values: list[float]) -> float:
    """Berechnet den Durchschnitt einer Liste von Zahlen.

    Args:
        values: Liste mit float-Werten (darf nicht leer sein)

    Returns:
        Arithmetisches Mittel aller Werte, gerundet auf 2 Dezimalstellen.

    Beispiel:
        >>> calculate_average([10.0, 20.0, 30.0])
        20.0
        >>> calculate_average([19.2, 21.4, 24.7])
        21.77
    """
    # TODO: Implementierung hier einfügen
    pass


def find_extremes(values: list[float]) -> tuple[float, float]:
    """Findet den kleinsten und grössten Wert einer Liste.

    Args:
        values: Liste mit float-Werten (darf nicht leer sein)

    Returns:
        Tupel (minimum, maximum)

    Beispiel:
        >>> find_extremes([19.2, 21.4, 24.7, 17.5])
        (17.5, 24.7)
    """
    # TODO: Implementierung hier einfügen
    pass


def count_above_threshold(values: list[float], threshold: float) -> int:
    """Zählt, wie viele Werte in der Liste den Schwellenwert überschreiten.

    Args:
        values:    Liste mit float-Werten
        threshold: Schwellenwert (Werte > threshold werden gezählt)

    Returns:
        Anzahl der Werte, die strikt grösser als threshold sind.

    Beispiel:
        >>> count_above_threshold([19.2, 27.1, 24.7, 33.2, 21.4], 25.0)
        2
    """
    # TODO: Implementierung hier einfügen
    pass


# ──────────────────────────────────────────────────────────────
# PERSON B
# ──────────────────────────────────────────────────────────────

def classify_value(value: float, limits: dict) -> str:
    """Klassifiziert einen Messwert anhand von Grenzwerten.

    Die limits-dict hat folgende Struktur:
        {
            "niedrig":  <obere Grenze für "niedrig">,
            "normal":   <obere Grenze für "normal">,
            "hoch":     <obere Grenze für "hoch">
            # alles darüber gilt als "kritisch"
        }

    Args:
        value:  Der zu klassifizierende Messwert
        limits: Dict mit den Grenzwerten (siehe oben)

    Returns:
        Einen der folgenden Strings: "niedrig", "normal", "hoch", "kritisch"

    Beispiel (Temperatur-Grenzen: niedrig<18, normal<26, hoch<32):
        >>> grenzen = {"niedrig": 18.0, "normal": 26.0, "hoch": 32.0}
        >>> classify_value(15.0, grenzen)
        'niedrig'
        >>> classify_value(22.0, grenzen)
        'normal'
        >>> classify_value(28.5, grenzen)
        'hoch'
        >>> classify_value(35.0, grenzen)
        'kritisch'
    """
    if value <= limits["niedrig"]:
        return "niedrig"
    elif value <= limits["normal"]:
        return "normal"
    elif value <= limits["hoch"]:
        return "hoch"
    else:
        return "kritisch"
    pass

def filter_by_sensor(data: list[dict], sensor_id: str) -> list[dict]:
    """Filtert die Messdaten nach einer bestimmten Sensor-ID.

    Args:
        data:      Liste von Messdaten-dicts (Ausgabe von load_data)
        sensor_id: Sensor-ID, nach der gefiltert werden soll (z. B. "S01")

    Returns:
        Neue Liste, die nur Einträge mit der angegebenen sensor_id enthält.
        Leere Liste, wenn kein passender Eintrag gefunden wird.

    Beispiel:
        >>> daten = load_data("data/messdaten.csv")
        >>> s01 = filter_by_sensor(daten, "S01")
        >>> all(d["sensor_id"] == "S01" for d in s01)
        True
    """
    return [d for d in data if d["sensor_id"] == sensor_id]
    pass

def generate_report(data: list[dict]) -> str:
    """Erstellt einen Textbericht aus den Messdaten.

    Der Bericht enthält:
    - Gesamtanzahl der Messungen
    - Durchschnitt, Min und Max für Temperatur, Luftfeuchtigkeit und CO2
    - Anzahl der kritischen Temperaturmessungen (> 30 °C)
    - Liste aller vorhandenen Sensor-IDs

    Args:
        data: Liste von Messdaten-dicts (Ausgabe von load_data)

    Returns:
        Formatierter mehrzeiliger String.

    Beispiel-Output (gekürzt):
        ========== SensorPy Bericht ==========
        Messungen total:       36
        Sensoren:              S01, S02

        -- Temperatur (°C) --
        Durchschnitt:          22.48
        Min / Max:             15.9 / 33.2
        Kritische Werte (>30): 2

        -- Luftfeuchtigkeit (%) --
        ...
        ======================================
    """
    if not data:
        return "Keine Daten vorhanden"
    
    # Extrahiere alle Messwerte
    temps = [d["temperatur"] for d in data]
    humidities = [d["luftfeuchtigkeit"] for d in data]
    co2_values = [d["co2"] for d in data]
    sensor_ids = sorted(set(d["sensor_id"] for d in data))
    
    # Berechne Statistiken für Temperatur
    temp_avg = round(sum(temps) / len(temps), 2)
    temp_min = min(temps)
    temp_max = max(temps)
    temp_critical = sum(1 for t in temps if t > 30)
    
    # Berechne Statistiken für Luftfeuchtigkeit
    humidity_avg = round(sum(humidities) / len(humidities), 2)
    humidity_min = min(humidities)
    humidity_max = max(humidities)
    
    # Berechne Statistiken für CO2
    co2_avg = round(sum(co2_values) / len(co2_values), 2)
    co2_min = min(co2_values)
    co2_max = max(co2_values)
    
    # Formatiere den Bericht
    report = "========== SensorPy Bericht ==========\n"
    report += f"Messungen total:       {len(data)}\n"
    report += f"Sensoren:              {', '.join(sensor_ids)}\n"
    report += "\n-- Temperatur (°C) --\n"
    report += f"Durchschnitt:          {temp_avg}\n"
    report += f"Min / Max:             {temp_min} / {temp_max}\n"
    report += f"Kritische Werte (>30): {temp_critical}\n"
    report += "\n-- Luftfeuchtigkeit (%) --\n"
    report += f"Durchschnitt:          {humidity_avg}\n"
    report += f"Min / Max:             {humidity_min} / {humidity_max}\n"
    report += "\n-- CO2 (ppm) --\n"
    report += f"Durchschnitt:          {co2_avg}\n"
    report += f"Min / Max:             {co2_min} / {co2_max}\n"
    report += "======================================\n"
    
    return report
    pass
