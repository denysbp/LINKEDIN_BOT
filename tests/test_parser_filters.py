#!/usr/bin/env python3
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
  sys.path.insert(0, ROOT)
os.environ.setdefault('TELEGRAM_TOKEN', 'dummy')
os.environ.setdefault('CHAT_ID', '1')

from services.parser import Parser
from services.filters import SmartFilter


def run():
    html = '''
    <div class="base-card">
      <a href="/jobs/view/123"></a>
      <h3 class="base-search-card__title">Junior Backend Python Developer</h3>
      <h4 class="base-search-card__subtitle">Acme</h4>
      <span class="job-search-card__location">Portugal</span>
      <time datetime="2026-04-09"></time>
    </div>
    '''

    parser = Parser()
    jobs = parser.parse(html)
    assert len(jobs) == 1, f'Esperava 1 vaga, obteve {len(jobs)}'

    job = jobs[0]
    assert 'junior' in job.title.lower()

    flt = SmartFilter()
    filtered = flt.filter(jobs)
    assert len(filtered) == 1, f'Filtro retornou {len(filtered)} vagas'
    assert filtered[0].link.startswith('https://')

    score = flt.score(job)
    assert score >= 5, f'Score esperado >=5, obtido {score}'


if __name__ == '__main__':
    run()
    print('TESTS OK')
