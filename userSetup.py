import pymel.core as pm
import maya.cmds as cmds
import sys
sys.path.append('D:/New_Learn/Mel/Code_Directory_Making/File')
import Code_Directory_v06

def VNCodeDir():
    

    main_Window = pm.language.melGlobals.get('gMainWindow')
    
    main_obj = 'myCustomToolsMenu'
    menu_label = 'VNCodeDir'
    
    if pm.menu(main_obj, label = menu_label , exists = True, parent = main_Window):
        pm.deleteUI(pm.menu(main_obj, e = True, dai = True))
    
    custom_tool_menu = pm.menu(main_obj, label = menu_label , parent = main_Window, tearOff=True)
    
    pm.menuItem(label='VNCode_Directory', parent= custom_tool_menu, tearOff= True,command= 'Code_Directory_v06.VNCode()')
    cmds.shelfButton( rpt = True, annotation='VNCodeDir().', image1='VN.png', command='Code_Directory_v06.VNCode()', p = "Vishal", stp = "python" )
    

    

VNCodeDir()