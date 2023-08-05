import time

from . import Record, types

__all__ = ['CacheNode']


class CacheValue:
    def __init__(self):
        self.data = {}

    def check_ttl(self, record):
        return record.ttl < 0 or record.timestamp + record.ttl >= time.time()

    def get(self, qtype):
        if qtype == types.ANY:
            for qt in self.data.keys():
                yield from self.get(qt)
            return
        results = self.data.get(qtype)
        if results is not None:
            keys = list(results.keys())
            for key in keys:
                record = results[key]
                if self.check_ttl(record):
                    yield record
                else:
                    results.pop(key, None)

    def add(self, record):
        if self.check_ttl(record):
            results = self.data.setdefault(record.qtype, {})
            results[record.data] = record


class CacheNode:
    def __init__(self):
        self.children = {}
        self.data = CacheValue()

    def get(self, fqdn, touch=False):
        current = self
        if isinstance(fqdn, str):
            keys = reversed(fqdn.split('.'))
        else:
            keys = fqdn
        for key in keys:
            child = current.children.get(key)
            if child is None:
                child = current.children.get('*')
            if child is None:
                if not touch: return
                child = CacheNode()
                current.children[key] = child
            current = child
        return current.data

    def query(self, fqdn, qtype):
        if isinstance(qtype, int):
            value = self.get(fqdn)
            if value is not None:
                yield from value.get(qtype)
        else:
            for t in qtype:
                yield from self.query(fqdn, t)

    def add(self,
            fqdn: str = None,
            qtype: int = None,
            data=None,
            ttl=-1,
            record: Record = None):
        if record is None:
            assert fqdn is not None
            assert qtype is not None
            assert data is not None
            record = Record(name=fqdn, data=data, qtype=qtype, ttl=ttl)
        value = self.get(record.name, True)
        value.add(record)
