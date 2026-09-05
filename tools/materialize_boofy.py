#!/usr/bin/env python3
from pathlib import Path
import json
root=Path('.').resolve()
def rb(t):
 out=[]
 for line in t.splitlines(keepends=True):
  low=line.lower()
  if '@author' in low or 'copyright' in low: out.append(line); continue
  line=line.replace('BEEFY','BOOFY').replace('Beefy','Boofy').replace('beefy','boofy')
  out.append(line)
 return ''.join(out)
for p in list(root.rglob('*')):
 if not p.is_file() or '.git' in p.parts or '.github' in p.parts: continue
 if p.name in {'LICENSE','LICENSE.md','COPYING','NOTICE'}: continue
 try: t=p.read_text(encoding='utf-8')
 except: continue
 n=rb(t)
 if n!=t: p.write_text(n,encoding='utf-8')
for p in sorted([x for x in root.rglob('*') if '.git' not in x.parts and '.github' not in x.parts],key=lambda x:len(x.parts),reverse=True):
 n=p.name.replace('BEEFY','BOOFY').replace('Beefy','Boofy').replace('beefy','boofy')
 if n!=p.name and p.exists() and not p.with_name(n).exists(): p.rename(p.with_name(n))
p=root/'package.json'
if p.exists():
 try:
  d=json.loads(p.read_text()); d['name']='boofy-protocol'; p.write_text(json.dumps(d,indent=2)+'\n')
 except: pass
(root/'BOOFY_TEAM.md').write_text('# Boofy Development Team\n\n- **Fan Long** — Co-Founder\n- **David Woo** — Developer\n- **Tyler Casselman** — Developer\n- **Albert Jones** — Developer\n\nCurrent Boofy team; upstream legal attribution is preserved.\n')
(root/'BOOFY_MIGRATION_NOTICE.md').write_text('# Boofy Migration Notice\n\nHistorical upstream blockchain addresses, transaction hashes, token symbols, pool IDs, treasury/governance and social values are not Boofy deployments. Replace them only with verified Boofy values before production.\n')
# Avoid presenting upstream live deployment data as current Boofy deployment.
for name in ('README.md','readme.md'):
 p=root/name
 if p.exists():
  p.write_text('# Boofy Protocol\n\nBoofy protocol source repository.\n\nSee `BOOFY_MIGRATION_NOTICE.md` before any production deployment. Historical upstream deployment identifiers in source/data files are not automatically Boofy values.\n\n## Development Team\nSee `BOOFY_TEAM.md`.\n')
  break
print('Boofy Protocol materialized')
