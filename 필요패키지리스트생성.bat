@echo off
setlocal

set OUTPUT_FILE=requirements.txt

if exist "%OUTPUT_FILE%" (
    del "%OUTPUT_FILE%"
)
pause
for %%f in (*.py) do (
    findstr /r "import from" "%%f" | findstr /v "import .* as" | findstr /v "from .* import" | findstr /v "#" | findstr /v "^\s*$" | sort | uniq >> "%OUTPUT_FILE%"
    pause
)

endlocal
