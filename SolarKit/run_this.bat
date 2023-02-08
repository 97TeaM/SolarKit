@echo off

title SolarKit

if exist node_modules\ (
  echo You've already installed modules!
    pip install -r requirements.txt
    npm install -g npm@latest
    npm install -g ddos-stress
    npm update -g
  )

python __main__.py

pause
exit