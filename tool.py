"""Classify gateway heartbeat age against local thresholds."""
from __future__ import annotations
def status(last_seen:float,now:float,degraded:float=60,stale:float=300)->dict:
 age=max(0,now-last_seen);state='healthy' if age<=degraded else 'degraded' if age<=stale else 'stale';return {'age':age,'status':state}
def summarize(records:list[dict],now:float,**thresholds)->dict:
 out={}
 for row in records:out[str(row['id'])]=status(float(row['last_seen']),now,**thresholds)
 return out
if __name__=='__main__':
 import json,sys;p=json.load(sys.stdin);print(json.dumps(summarize(p['records'],p['now'],degraded=p.get('degraded',60),stale=p.get('stale',300)),indent=2))
