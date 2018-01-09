import os
version = ""
command_download = 'Launcher_Folder/Mac/Launcher.app/Contents/MacOS/Launcher -d'
command_install = 'Launcher_Folder/Mac/Launcher.app/Contents/MacOS/Launcher -i Resource\ Editor Stable'
cmd_download = 'Launcher_Folder\Win\Launcher.exe -d'
cmd_install = 'Launcher_Folder\Win\Launcher.exe -i ResourceEditor Stable'

branch_info_list = ["Stable", "Blitz To Stable", "Tanks", "development", "re_stable"]
tools_Stable_list = ["ASK", "AssetCacheServer", "CMakeTool", "QuickEd", "Resource\ Editor", "ResourceEditor", "SceneViewer (MacOS)", "SceneViewer_Android", "SceneViewer_Win10", "SceneViewer_iOS", "Tank Editor", "Tank Viewer"]
# tools_BlitzToStable_list = ["AssetCacheServer", "QuickEd", "Resource\ Editor", "Tank Editor", "Tank Viewer"]
# tools_Tanks_list = ["AssetCacheServer", "CMakeTool", "QuickEd", "Resource\ Editor", "Tank Editor GIT", "Tank Viewer GIT"]
# tools_development_list = ["ASK", "AssetCacheServer", "CMakeTool", "QuickEd", "Resource\ Editor", "SceneViewer (MacOS)", "SceneViewer_Android", "SceneViewer_Win10", "SceneViewer_iOS", "Tank Editor", "Tank Viewer", "Tank Editor GIT", "Tank Viewer GIT"]

download_folder = "Launcher_Folder/DAVATools"
launcher_folder = "Launcher_Folder"
launcher_preferenses_mac = os.path.expanduser('~/Library/Application Support/DAVAEngine/Launcher')
launcher_preferenses_file = 'localConfig.yaml'
launcher_preferenses_win = os.path.expanduser('~\Documents\DAVAProject\Launcher')