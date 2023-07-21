@ECHO OFF
IF EXIST %~dp0test_db (
    echo Deleting test_db
    DEL /Q /F %~dp0test_db
)

echo running build_up.py
python %~dp0build_up.py

@ECHO ON