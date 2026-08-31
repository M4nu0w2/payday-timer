"""Rigenera manifest.json scansionando le cartelle giorno per giorno.

Uso:
    python build-manifest.py

Richiede Pillow (pip install pillow). Per ogni GIF calcola durata totale
di un ciclo (ms) e il loop count nativo (0 = loop infinito, embedded nel
file stesso -> il browser lo rispetta da solo, nessun trucco JS necessario).
"""
import json
import os
from PIL import Image

FOLDERS = ['30d', '20d', '10d', '67d', '5d', '3d', '2d', '1d', 'payday']
EXTS = ('.gif', '.png', '.webp')
BASE = os.path.dirname(os.path.abspath(__file__))


def gif_meta(path):
    try:
        im = Image.open(path)
        n_frames = getattr(im, 'n_frames', 1)
        total = 0
        for i in range(n_frames):
            im.seek(i)
            d = im.info.get('duration', 100) or 0
            total += max(d, 20)
        loop = im.info.get('loop', None)
        return total, loop
    except Exception as e:
        print('WARN', path, e)
        return None, None


def main():
    out = {}
    for folder in FOLDERS:
        folder_path = os.path.join(BASE, folder)
        files = []
        if os.path.isdir(folder_path):
            files = sorted(f for f in os.listdir(folder_path) if f.lower().endswith(EXTS))
        entries = []
        for f in files:
            duration, loop = gif_meta(os.path.join(folder_path, f))
            entries.append({'file': f, 'duration': duration, 'loop': loop})
        out[folder] = entries

    with open(os.path.join(BASE, 'manifest.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)

    for folder, entries in out.items():
        print(folder, '->', len(entries), 'file')


if __name__ == '__main__':
    main()
