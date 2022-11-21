@echo off
python %~dp0\..\scripts_and_macros\acterm_list_maker.py -i "..\abbreviations.txt" -d "acronyms/project_snet.dic,acronyms/common.dic,acronyms/ml.dic" -o "..\abbreviations.md"
@echo on