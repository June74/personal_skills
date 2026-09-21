"""Validate this kit's JSON memory-record contract with Python's standard library."""
import argparse
from datetime import date,datetime
import json
from pathlib import Path
import re
import sys

FIELDS={'id','namespace','kind','status','statement','source_ref','source_date','recorded_at','valid_from','valid_to','confidence','supersedes','review_after','expires_at','sensitivity','links'}

def validate(record):
    errors=[]
    if not isinstance(record,dict): return ['record must be an object']
    if set(record)!=FIELDS: errors.append('record fields differ from the schema')
    for key in ['id','namespace','statement','source_ref']:
        if not isinstance(record.get(key),str) or not record[key].strip(): errors.append(f'{key} must be a nonempty string')
    namespace=record.get('namespace','')
    if not isinstance(namespace,str) or not re.fullmatch(r'user/global|project/[a-zA-Z0-9_-]+(?:/episodes)?',namespace): errors.append('namespace must be user/global or project/ID[/episodes]')
    for key,allowed in {
        'kind':{'preference','fact','decision','episode','hypothesis','lesson'},
        'status':{'candidate','accepted','superseded'},
        'confidence':{'observed','user-stated','inferred'},
        'sensitivity':{'synthetic','public','private'}}.items():
        if not isinstance(record.get(key),str) or record[key] not in allowed: errors.append(f'invalid {key}')
    dates={}
    for key in ['source_date','valid_from','valid_to','review_after','expires_at']:
        value=record.get(key)
        if value is None and key in ['valid_to','expires_at']: continue
        try:
            if not isinstance(value,str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}',value): raise ValueError()
            dates[key]=date.fromisoformat(value)
        except (ValueError,TypeError): errors.append(f'{key} must be an ISO date')
    try:
        value=record.get('recorded_at')
        if not isinstance(value,str): raise ValueError()
        stamp=datetime.fromisoformat(value.replace('Z','+00:00'))
        if stamp.tzinfo is None: raise ValueError()
    except (ValueError,TypeError): errors.append('recorded_at must include date, time and timezone')
    if 'valid_to' in dates and 'valid_from' in dates and dates['valid_to']<dates['valid_from']: errors.append('valid_to precedes valid_from')
    if 'review_after' in dates and 'valid_from' in dates and dates['review_after']<dates['valid_from']: errors.append('review_after precedes valid_from')
    if 'expires_at' in dates and 'valid_from' in dates and dates['expires_at']<dates['valid_from']: errors.append('expires_at precedes valid_from')
    supersedes=record.get('supersedes')
    if supersedes is not None and (not isinstance(supersedes,str) or not supersedes.strip()): errors.append('supersedes must be a nonempty id or null')
    if supersedes is not None and supersedes==record.get('id'): errors.append('a record cannot supersede itself')
    links=record.get('links')
    if not isinstance(links,list): errors.append('links must be an array')
    else:
        for link in links:
            if not isinstance(link,dict) or set(link)!={'relation','target_id'} or not all(isinstance(v,str) and v.strip() for v in link.values()): errors.append('each link needs nonempty relation and target_id')
    return errors

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record')
    args=parser.parse_args()
    try:
        errors=validate(json.loads(Path(args.record).read_text(encoding='utf-8')))
    except (ValueError,OSError) as exc:
        print(f'INVALID: {exc}',file=sys.stderr);return 1
    if errors:
        for error in errors: print('INVALID: '+error,file=sys.stderr)
        return 1
    print('Valid record structure. Truth, sensitivity and authorization are not verified.')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
