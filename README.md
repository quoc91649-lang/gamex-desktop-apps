# GameX Desktop Apps

This repository hosts Python desktop applications built via GameX platform.

## Structure

Each app is stored in `apps/<app-name>/` with its source code.
GitHub Actions automatically builds each app into a Windows .exe file.

## Build Process

1. Admin uploads Python source (.zip/.rar) via GameX platform
2. Source code is pushed to this repo
3. GitHub Actions runs PyInstaller on Windows runner
4. .exe is uploaded to GitHub Releases
5. Download link is saved to Supabase database

