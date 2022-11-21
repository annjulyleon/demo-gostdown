@echo off
python %~dp0\..\scripts_and_macros\copy_img.py -s "..\docs_gost" -d "..\docs_gost\_img" -c
@echo on

powershell.exe -command .\build.ps1 ^
-md .\report-beginning.md,.\01_setup\01_what_is_happening.md,.\01_setup\02_install.md,.\01_setup\03_all_together.md,.\02_md_to_docx\01_folder_structure.md,.\02_md_to_docx\02_gd_examples.md,.\02_md_to_docx\03_build_doc_macro_final.md,.\03_md_to_web\01_build_web.md,.\03_md_to_web\02_remove_gd_tags.md,.\03_md_to_web\04_useful_plugins.md,.\03_md_to_web\05_pdf_thoughts.md,.\04_vscode_settings\01_setup_workspace.md,.\04_vscode_settings\02_tasks_snippets.md,.\report-end.md ^
-template template-report.docx ^
-pdf report.pdf ^
-docx report.docx ^
-embedfonts ^
-counters

@echo off
python %~dp0\..\scripts_and_macros\copy_img.py -r
@echo on