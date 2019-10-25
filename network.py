import os
import sys
from time import sleep
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from py2cytoscape import cyrest
from IPython.display import Image


cytoscape=cyrest.cyclient(host="localhost", port=8081, version="V1")
cytoscape.version()