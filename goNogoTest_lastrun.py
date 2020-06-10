#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on June 10, 2020, at 15:59
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'goNogoTest'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andrew\\Documents\\Work\\Projects\\go-nogo-test\\goNogoTest_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text='Space for blue, nothing for orange. Space to start.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr1Resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialBlue = visual.Polygon(
    win=win, name='trialBlue',
    edges=180, size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,1.000], fillColorSpace='rgb',
    opacity=1.0, depth=0.0, interpolate=True)
trialOrange = visual.Polygon(
    win=win, name='trialOrange',
    edges=180, size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1.000,0.004,-1.000], lineColorSpace='rgb',
    fillColor=[1.000,0.004,-1.000], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
trialFix = visual.TextStim(win=win, name='trialFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
trialResp = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='Thanks',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
instr1Resp.keys = []
instr1Resp.rt = []
_instr1Resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [instr1, instr1Resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1.frameNStart = frameN  # exact frame index
        instr1.tStart = t  # local t and not account for scr refresh
        instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        instr1.setAutoDraw(True)
    
    # *instr1Resp* updates
    waitOnFlip = False
    if instr1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1Resp.frameNStart = frameN  # exact frame index
        instr1Resp.tStart = t  # local t and not account for scr refresh
        instr1Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1Resp, 'tStartRefresh')  # time at next scr refresh
        instr1Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr1Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr1Resp.status == STARTED and not waitOnFlip:
        theseKeys = instr1Resp.getKeys(keyList=['space'], waitRelease=False)
        _instr1Resp_allKeys.extend(theseKeys)
        if len(_instr1Resp_allKeys):
            instr1Resp.keys = _instr1Resp_allKeys[-1].name  # just the last key pressed
            instr1Resp.rt = _instr1Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr1.started', instr1.tStartRefresh)
thisExp.addData('instr1.stopped', instr1.tStopRefresh)
# check responses
if instr1Resp.keys in ['', [], None]:  # No response was made
    instr1Resp.keys = None
thisExp.addData('instr1Resp.keys',instr1Resp.keys)
if instr1Resp.keys != None:  # we had a response
    thisExp.addData('instr1Resp.rt', instr1Resp.rt)
thisExp.addData('instr1Resp.started', instr1Resp.tStartRefresh)
thisExp.addData('instr1Resp.stopped', instr1Resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('goNogoCond1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    trialBlue.setOpacity(blueOpacity)
    trialOrange.setOpacity(orangeOpacity)
    trialResp.keys = []
    trialResp.rt = []
    _trialResp_allKeys = []
    # keep track of which components have finished
    trialComponents = [trialBlue, trialOrange, trialFix, trialResp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialBlue* updates
        if trialBlue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialBlue.frameNStart = frameN  # exact frame index
            trialBlue.tStart = t  # local t and not account for scr refresh
            trialBlue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialBlue, 'tStartRefresh')  # time at next scr refresh
            trialBlue.setAutoDraw(True)
        if trialBlue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialBlue.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialBlue.tStop = t  # not accounting for scr refresh
                trialBlue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialBlue, 'tStopRefresh')  # time at next scr refresh
                trialBlue.setAutoDraw(False)
        
        # *trialOrange* updates
        if trialOrange.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trialOrange.frameNStart = frameN  # exact frame index
            trialOrange.tStart = t  # local t and not account for scr refresh
            trialOrange.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialOrange, 'tStartRefresh')  # time at next scr refresh
            trialOrange.setAutoDraw(True)
        if trialOrange.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialOrange.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialOrange.tStop = t  # not accounting for scr refresh
                trialOrange.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialOrange, 'tStopRefresh')  # time at next scr refresh
                trialOrange.setAutoDraw(False)
        
        # *trialFix* updates
        if trialFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialFix.frameNStart = frameN  # exact frame index
            trialFix.tStart = t  # local t and not account for scr refresh
            trialFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialFix, 'tStartRefresh')  # time at next scr refresh
            trialFix.setAutoDraw(True)
        if trialFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialFix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trialFix.tStop = t  # not accounting for scr refresh
                trialFix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialFix, 'tStopRefresh')  # time at next scr refresh
                trialFix.setAutoDraw(False)
        
        # *trialResp* updates
        waitOnFlip = False
        if trialResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialResp.frameNStart = frameN  # exact frame index
            trialResp.tStart = t  # local t and not account for scr refresh
            trialResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialResp, 'tStartRefresh')  # time at next scr refresh
            trialResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trialResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trialResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialResp.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                trialResp.tStop = t  # not accounting for scr refresh
                trialResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialResp, 'tStopRefresh')  # time at next scr refresh
                trialResp.status = FINISHED
        if trialResp.status == STARTED and not waitOnFlip:
            theseKeys = trialResp.getKeys(keyList=['space'], waitRelease=False)
            _trialResp_allKeys.extend(theseKeys)
            if len(_trialResp_allKeys):
                trialResp.keys = _trialResp_allKeys[-1].name  # just the last key pressed
                trialResp.rt = _trialResp_allKeys[-1].rt
                # was this correct?
                if (trialResp.keys == str(corrAns)) or (trialResp.keys == corrAns):
                    trialResp.corr = 1
                else:
                    trialResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('trialBlue.started', trialBlue.tStartRefresh)
    trials.addData('trialBlue.stopped', trialBlue.tStopRefresh)
    trials.addData('trialOrange.started', trialOrange.tStartRefresh)
    trials.addData('trialOrange.stopped', trialOrange.tStopRefresh)
    trials.addData('trialFix.started', trialFix.tStartRefresh)
    trials.addData('trialFix.stopped', trialFix.tStopRefresh)
    # check responses
    if trialResp.keys in ['', [], None]:  # No response was made
        trialResp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trialResp.corr = 1;  # correct non-response
        else:
           trialResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('trialResp.keys',trialResp.keys)
    trials.addData('trialResp.corr', trialResp.corr)
    if trialResp.keys != None:  # we had a response
        trials.addData('trialResp.rt', trialResp.rt)
    trials.addData('trialResp.started', trialResp.tStartRefresh)
    trials.addData('trialResp.stopped', trialResp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [thanks]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    if thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            thanks.tStop = t  # not accounting for scr refresh
            thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks, 'tStopRefresh')  # time at next scr refresh
            thanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
