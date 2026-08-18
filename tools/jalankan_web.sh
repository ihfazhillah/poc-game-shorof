#!/bin/bash
# Menjalankan versi web (build-web/) di http://localhost:8090
cd "$(dirname "$0")/../build-web" && echo "Buka http://localhost:8090 di browser (Ctrl+C untuk berhenti)" && python3 -m http.server 8090
