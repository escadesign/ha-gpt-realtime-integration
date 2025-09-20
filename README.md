# GPT Realtime Assist Integration

Home Assistant Custom Integration für das Add-on „Realtime Assist (OpenAI gpt-realtime)“ mit Push-to-Talk-Services und Hue-Blueprints.

## Features
- Config Flow (Host + Basic Auth) für Add-on-Anbindung
- Services `gpt_realtime_assist.ptt_start` und `.ptt_stop`
- Blueprints für Hue (ZHA/Hue Bridge) PTT-Steuerung

## Verzeichnisstruktur
```
integration_repo/
├── custom_components/gpt_realtime_assist/
│   ├── __init__.py, config_flow.py, manifest.json, ...
├── blueprints/automation/
│   ├── zha_hue_ptt.yaml
│   └── hue_bridge_ptt.yaml
└── docs/INSTALL.md
```

## Installation
1. Repo clonen oder ZIP entpacken.
2. `custom_components/gpt_realtime_assist` in dein Home Assistant `config/custom_components/` kopieren.
3. (Optional) Repo als HACS Custom Repository hinzufügen.
4. Integration über Einstellungen → Geräte & Dienste → Integration hinzufügen → „GPT Realtime Assist“.
5. Blueprints importieren und auf deine Hue-Remote anwenden.

## Voraussetzungen
- Add-on läuft und stellt HTTPS-API bereit (`https://<HA-IP>:8443`).
- Basic Auth Zugangsdaten bekannt (Default: admin / ha).

## Lizenz
Siehe upstream `LICENSE` des Forks.
