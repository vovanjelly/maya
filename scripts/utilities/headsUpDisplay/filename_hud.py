import pymel.core as pm
import maya.api.OpenMaya as om
import os

hud_filename_save_callback = None
hud_filename_open_callback = None

def hud_file_object(*args):
    try:
        filename = os.path.basename(pm.system.sceneName())
        return filename
    except:
        return ""
        

def toggle_file_hud():
    if pm.headsUpDisplay('HUDFilename', exists=True):
        pm.headsUpDisplay('HUDFilename', rem=True)
    else:
        create_file_hud()
    
 
def create_file_hud(event=None):
    try:
        pm.headsUpDisplay('HUDFilename', 
            section=8, 
            block=0,
            blockSize='medium',
            label='filename',
            labelFontSize='small',
            command=hud_file_object)
    except RuntimeError:
        pm.warning('HUD position is occupied!')
        return
        
    global hud_filename_save_callback
    try:
        om.MSceneMessage.removeCallback(hud_filename_save_callback)
        om.MSceneMessage.removeCallback(hud_filename_open_callback)
    except:
        pass

    hud_filename_save_callback = om.MSceneMessage.addCallback(om.MSceneMessage.kAfterSave, create_file_hud)
    hud_filename_open_callback = om.MSceneMessage.addCallback(om.MSceneMessage.kAfterOpen, create_file_hud)
        

toggle_file_hud()
