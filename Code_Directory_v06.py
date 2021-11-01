import maya.cmds as cmds
import sys
sys.path.append('D:/New_Learn/Mel/Code_Directory_Making/File')

list = cmds.getFileList( folder= "D:/New_Learn/Mel/Code_Directory_Making/File/Main/CodeDir" )


               
def VNCode():
    if cmds.window( "VNCode_Directory", exists = True):
        cmds.deleteUI ("VNCode_Directory" ,window=True)

                
    #if cmds.windowPref( "VNCode_Directory", exists = True):
    #    cmds.windowPref ("VNCode_Directory" ,r=True)
    
    window2 = cmds.window("VNCode Directory", iconName='Short Name', widthHeight=(300, 700), s = False, bgc = (0.1,0.1,0.1) ) # entire Window
    cmds.columnLayout(adjustableColumn=True, columnAttach=('both', 15), rowSpacing=10, columnWidth=250 )# making button and etc in column
    cmds.separator()
    cmds.text( label='Search Code' ,align='center' )
    WrittenTextField = cmds.textField('SearchBox') 
    cmds.button( label='Search',align='center', command = 'Code_Directory_v06.SearchSelected()', bgc = (0.5,0.6,0.8))
    cmds.textScrollList("FullList", append=[], ra = True )
    for i in list:
        cmds.textScrollList("FullList", append=[i], e = True)
    
    cmds.button( label='Open',align='center', command = 'Code_Directory_v06.OpenScriptWindow()', bgc = (0.5,0.6,0.8) )
    cmds.separator( height=1, style='none' )
    cmds.text( label='Save Code' ,align='center' )
    cmds.textField('NewScriptName') 
    cmds.scrollField('WriteNewScript')
    collection1 = cmds.radioCollection("melOrPy")
    rb2 = cmds.radioButton('Mel' )
    rb1 = cmds.radioButton('Python' )
    cmds.radioCollection( collection1, edit=True, select=rb2 )
    cmds.button( label='Add To Dir',align='center', command = 'Code_Directory_v06.SaveFile(),Code_Directory_v06.AddToDir()', bgc = (0.5,0.6,0.8) )
    cmds.showWindow( window2 )
    
def AddToDir():
    NewList = cmds.getFileList( folder= "D:/New_Learn/Mel/Code_Directory_Making/File/Main/CodeDir" )
    for i in NewList:
        cmds.textScrollList("FullList",ra = True, e = True)
    for i in NewList:
        cmds.textScrollList("FullList", append=[i], e = True)
              


def SearchSelected():
    SearchName = cmds.textField('SearchBox', q=True, text=True)
    AllList = cmds.getFileList( folder= "D:/New_Learn/Mel/Code_Directory_Making/File/Main/CodeDir", filespec= '*'+SearchName+'*' )
    
    for i in AllList:
        cmds.textScrollList("FullList",ra = True, e = True)
    for i in AllList:
        cmds.textScrollList("FullList", append=[i], e = True)
        

        
def OpenScriptWindow():
    with open("D:/New_Learn/Mel/Code_Directory_Making/File/Main/CodeDir/"+(cmds.textScrollList("FullList",si = True , q = True))[0], 'r') as f:
        lines = f.read()
    if cmds.window( "Script", exists = True):
        cmds.deleteUI ("Script" ,window= True)
    
    ScriptWin = cmds.window("Script", iconName='Short Name', widthHeight=(700, 700), s = False, bgc = (0.1,0.3,0.) )
    cmds.columnLayout(adjustableColumn=True, rowSpacing=10, columnWidth=250 )
    cmds.scrollField('ScriptBoard',tx = lines, ed =False, w =700, h =  700 )
    cmds.showWindow( ScriptWin )
    
def SaveFile():
    ButtonName = cmds.radioButton('Mel',sl = True, q = True )
    if ButtonName == True:
        db = '.mel'
    else:
        db = '.py'
        
    with open("D:/New_Learn/Mel/Code_Directory_Making/File/Main/CodeDir/"+(cmds.textField('NewScriptName', q=True, text=True))+db, 'w') as f:
        f.write(cmds.scrollField('WriteNewScript', q=True, text=True))
    with open("D:/New_Learn/Mel/Code_Directory_Making/File/Main/CodeDirBackup/"+(cmds.textField('NewScriptName', q=True, text=True))+db, 'w') as n:
        n.write(cmds.scrollField('WriteNewScript', q=True, text=True))

