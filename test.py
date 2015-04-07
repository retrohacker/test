#!/usr/bin/env python
import json
import subprocess
import os
import sys

divider = '\n===============================================\n'

with open('./tests.json') as json_file:
  tests = json.load(json_file)

cwd = os.getcwd()
status = 0


for test in tests['tests']:
  # Build image
  workdir = os.path.join(cwd)
  for path in test['path']:
    workdir = os.path.join(workdir,path)
  print divider + workdir + divider
  os.chdir(workdir)
  tag = tests['repo'] + ':' + test['tag']
  proc = subprocess.Popen(' '.join(['docker','build','--no-cache','-t',tag,'.']),shell=True)
  proc.communicate()
  if proc.returncode != 0:
    status = 1

  # Build test
  workdir = os.path.join(cwd)
  for path in test['test']:
    workdir = os.path.join(workdir,path)
  print divider + workdir + divider
  os.chdir(workdir)
  tag = tag + '-test'
  proc = subprocess.Popen(' '.join(['docker','build','--no-cache','-t',tag,'.']),shell=True)
  proc.communicate()
  if proc.returncode != 0:
    status = 1

sys.exit(status)
