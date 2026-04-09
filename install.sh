#!/bin/bashls
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
clear
echo adcione as suas chaves nas variaveis no seu .env
touch .env
