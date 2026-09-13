if exist "session.sqlite" del /f /q "session.sqlite"

cosmic-ray init config.toml session.sqlite
cosmic-ray exec config.toml session.sqlite
cr-report session.sqlite > cosmic-ray-report.txt
cr-html session.sqlite > cosmic-ray.html

start "" cosmic-ray.html
pause