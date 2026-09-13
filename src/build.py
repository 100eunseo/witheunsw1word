# -*- coding: utf-8 -*-
"""template.html + data.json → ../lesson2_quiz_interactive.html"""
import os
here = os.path.dirname(os.path.abspath(__file__))
tpl  = open(os.path.join(here, 'template.html'), encoding='utf-8').read()
data = open(os.path.join(here, 'data.json'), encoding='utf-8').read()
assert '__DATA__' in tpl, 'template.html에 __DATA__ 자리가 없습니다'
dst = os.path.join(here, '..', 'lesson2_quiz_interactive.html')
open(dst, 'w', encoding='utf-8').write(tpl.replace('__DATA__', data))
print('빌드 완료:', os.path.getsize(dst), 'bytes')
