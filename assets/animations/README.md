# Animazioni

Una cartella per fascia di giorni mancanti allo stipendio:

| Cartella | Giorni mancanti |
|----------|------------------|
| 30d      | 21+ |
| 20d      | 11-20 |
| 10d      | 8-10 |
| 67d      | 6-7 (six seven meme) |
| 5d       | 4-5 |
| 3d       | 3 |
| 2d       | 2 |
| 1d       | 1 |
| payday   | 0 (arrivato) |

Metti dentro ogni cartella le GIF che vuoi (consigliato < 1.5MB l'una — piano free Cloudflare Pages: max 25MB per file, ma restare leggeri aiuta banda/tempi di caricamento).

Poi aggiungi il nome file in `manifest.json` (root di questa cartella), dentro l'array della fascia giusta. Basta la stringa col nome file:

```json
"67d": ["six-seven-1.gif", "six-seven-2.gif"]
```

Il formato oggetto `{ "file": "...", "duration": 3200, "loop": 0 }` è supportato anch'esso (duration = ms totali del ciclo, loop = 0 significa loop infinito nativo del GIF) — generato automaticamente girando lo script `assets/animations/build-manifest.py`, non serve compilarlo a mano.

Ad ogni refresh della pagina lo script pesca una GIF a caso tra quelle elencate per la fascia corrente. Fascia senza file in manifest -> fallback a emoji default.
