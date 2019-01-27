import fire
import json

class VaultAnalyzer(object):
    """Analyzes vault files."""

    def analyze(self, file_name):
        with open(file_name) as vault_file:
            pass

if __name__ == '__main__':
    fire.Fire(VaultAnalyzer)