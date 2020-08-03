#!/bin/bash

date=$(date +%Y%m%m)

mkdir -p Log
mkdir -p Noticias

Aplication_Path="App"

cd $Aplication_Path

python main.py
if [ $? -ne 0 ]; then
    echo "ERRO AO PROCESSAR CRAWLER"
else
    echo "FINALIZADO COM SUCESSO"
fi