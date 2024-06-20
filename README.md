# geostyler-qgis-plugin
QGIS Plugin for Exporting Layerstyles to Different Formats


**Experimental**

To test clone the repository and create a symlink pointing to your QGIS plugins directory

Windows Command Prompt:

```
mklink /D "%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\geostyler" "C:\GitHub\geostyler-plugin\geostyler"
```

PowerShell:

```ps
$AppDataPath = [Environment]::GetFolderPath("ApplicationData")
$SourcePath = "C:\GitHub\geostyler-plugin\geostyler"
$LinkPath = Join-Path -Path $AppDataPath -ChildPath "QGIS\QGIS3\profiles\default\python\plugins\geostyler"

# Create symbolic link
New-Item -ItemType SymbolicLink -Path $LinkPath -Target $SourcePath
```

Bash (untested):

```
ln -s /path/to/source /home/username/.local/share/QGIS/QGIS3/profiles/default/python/plugins/geostyler
```
