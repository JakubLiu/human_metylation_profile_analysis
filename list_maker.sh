#!/usr/bin/bash


for file in /mnt/c/Users/Lenovo/Desktop/STUDIA/BIOINFORMATYKA/METYLACJA/KLASYFIKACJA/kolumny/*
do

	sed 's/','/'.'/g' $file | sed -z 's/\n/,/g;s/, $/\n/' > $file"_mod.txt"

done

echo 'done.'
