import nbformat
from nbclient import NotebookClient
import sys, subprocess

nb_path = 'WineQuality_EDA_MehraliHub.ipynb'

try:
    nb = nbformat.read(nb_path, as_version=4)
    client = NotebookClient(nb, timeout=600)
    print('Executing notebook...')
    client.execute()
    nbformat.write(nb, nb_path)
    print('Notebook executed and saved:', nb_path)
except Exception as e:
    print('Execution failed:', e)
    raise
