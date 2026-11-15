"""Rebuild ../index.html (one self-contained file) from template.html + assets.
Run:  python src/build.py
"""
import json, base64, os
here = os.path.dirname(os.path.abspath(__file__))
p = lambda *a: os.path.join(here, *a)
t = open(p('template.html'), encoding='utf-8').read()
t = t.replace('/*FONTS*/', open(p('fonts.css'), encoding='utf-8').read())
t = t.replace('__SOUNDS__', open(p('sounds.json'), encoding='utf-8').read())
def uri(path, mime):
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(path, 'rb').read()).decode())
t = t.replace('__base__', uri(p('assets', 'base.jpg'), 'image/jpeg'))
for k, (x, y, w, h) in json.load(open(p('assets', 'layers.json'))).items():
    t = t.replace('__%s__' % k, uri(p('assets', k + '.png'), 'image/png'))
    t = t.replace('__pos_%s__' % k, 'left:%dpx;top:%dpx;width:%dpx;height:%dpx' % (x, y, w, h))
open(os.path.join(here, '..', 'index.html'), 'w', encoding='utf-8').write(t)
print('index.html', len(t) // 1024, 'KB')
