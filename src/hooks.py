from PyInstaller.utils.hooks import collect_submodules

# Add the 'src' directory as a hidden import
hiddenimports = collect_submodules('src')