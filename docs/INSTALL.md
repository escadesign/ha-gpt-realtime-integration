# Installation (HA OS, Raspberry Pi 4, UR22 MKII)

## Repositories
- **Add-on Repo**: z.B. `https://github.com/<user>/gpt-realtime-assist-addon`
- **Integration Repo**: z.B. `https://github.com/<user>/gpt-realtime-assist-integration`

## 1) Add-on installieren
1. Supervisor → Add-on Store → Repositories → Add → Add-on-Repo-URL eintragen.
2. Add-on "Realtime Assist (OpenAI gpt-realtime)" auswählen und installieren.
3. Optionen setzen:
   - `openai_api_key` (Pflicht)
   - `input_device`/`output_device`: `auto` oder `plughw:CARD=UR22mkII,DEV=0`
   - `language`: `de`, `voice`: `alloy`, `sample_rate`: `24000`
   - Basic-Auth / HA-URL nach Bedarf anpassen.
4. Add-on starten und `https://<HA-IP>:8443/api/health` prüfen.

## 2) Integration bereitstellen
1. Integration-Repo clonen oder als ZIP laden.
2. Verzeichnis `custom_components/gpt_realtime_assist` in dein Home-Assistant `config/custom_components/` kopieren.
3. (Optional) Integration-Repo als HACS Custom Repository registrieren.

## 3) Integration einrichten
1. Home Assistant → Einstellungen → Geräte & Dienste → Integration hinzufügen → "GPT Realtime Assist".
2. Host: Ingress-URL oder `https://<HA-IP>:8443`.
3. Benutzer/Passwort gemäß Add-on-Optionen.

## 4) Blueprint importieren
1. Integration-Repo → `blueprints/automation/*.yaml` herunterladen.
2. Home Assistant → Einstellungen → Automatisierungen → Blueprints → Import.
3. Blueprint `zha_hue_ptt.yaml` (ZHA) oder `hue_bridge_ptt.yaml` (Hue Bridge) wählen und Gerät/Event zuordnen.

## 5) Funktionstest
1. Service **gpt_realtime_assist.ptt_start** ausführen → sprechen → **gpt_realtime_assist.ptt_stop**.
2. Audio-Ausgabe erfolgt über UR22 MKII.
3. Beispiel „Schalte Wohnzimmerlicht ein.“ → Tool-Call an Home Assistant, Gerät reagiert.
