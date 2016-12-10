# -----------------------------------------------------------------------------
# combineCurves.py
# -----------------------------------------------------------------------------

# Author: Morten Dalgaard Andersen
# Author URI: http://www.amorten.com
#
# License: Attribution-ShareAlike 4.0 International
# License URI: http://creativecommons.org/licenses/by-sa/4.0/
#
# Version: 1.0
# Modified: 2015-11-04
#
# -----------------------------------------------------------------------------
#
# Instructions on how to use:
#
#  1.	Copy the script to the Maya script folder.
#
#  2.	Enter the following two python commands to load the script:
#
#       import combineCurves as cc
#       cc.combineCurves()


import maya.cmds as cmds


def combineCurves():
    # Get curve shapes
    curves = cmds.ls(sl=True, transforms=True, dag=True, allPaths=True)
    curveShapes = cmds.listRelatives(curves, shapes=True, path=True)

    # Remove last selected from curveShapes
    # and get last selected transform for parenting
    curveShapes.pop()
    master = curves.pop()

    # Freeze transformation on child curve transforms and shapes
    cmds.makeIdentity(curves, apply=True, translate=True, rotate=True, scale=True)
    cmds.refresh()  # needed for parenting to work

    # Parent curveShapes to master
    cmds.parent(curveShapes, master, shape=True, relative=True)

    # Remove empty transforms
    cmds.delete(curves)

    # Select the curve
    cmds.select(master, replace=True)