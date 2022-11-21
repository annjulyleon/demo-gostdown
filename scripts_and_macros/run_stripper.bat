@echo off
python %~dp0\..\scripts_and_macros\stripper.py -s "..\docs_gost" -d "..\docs" -i *.bat *.ps1 *.lua report-beginning.md report-end.md *.docx *.pdf -a
@echo on