import os


class NameDatasetV1:

    def __init__(self, fn_ext=None, ln_ext=None):
        first_names_filename = os.path.join(os.path.dirname(__file__), 'v1/first_names.all.txt')
        with open(first_names_filename, 'r', errors='ignore', encoding='utf8') as r:
            self.first_names = set(r.read().strip().split('\n'))
        last_names_filename = os.path.join(os.path.dirname(__file__), 'v1/last_names.all.txt')
        with open(last_names_filename, 'r', errors='ignore', encoding='utf8') as r:
            self.last_names = set(r.read().strip().split('\n'))
        if fn_ext is not None and isinstance(fn_ext,list):
            for i in fn_ext: self.first_names.add(i.lower())
        if ln_ext is not None and isinstance(ln_ext,list):
            for i in ln_ext: self.last_names.add(i.lower())

    def search_first_name(self, first_name, use_upper_case=False):
        return self._query(self.first_names, first_name, use_upper_case)

    def search_last_name(self, last_name, use_upper_case=False):
        return self._query(self.last_names, last_name, use_upper_case)

    @staticmethod
    def _query(search_set, key, use_upper_case):
        if use_upper_case and key.title() != key:
            return False
        return key.strip().lower() in search_set
