@echo off
python %~dp0\..\scripts_and_macros\acterm_list_maker.py -i "..\glossary.txt" -d "glossary/project_snet.dic,glossary/common.dic,glossary/ml.dic" -o "..\glossary.md"
@echo on