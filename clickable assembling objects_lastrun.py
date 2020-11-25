#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on Wed Nov 25 13:33:42 2020
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
psychopyVersion = '2020.2.5'
expName = 'official assembling objects test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
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
    originPath='/Users/catie/Desktop/clickable assembling objects/clickable assembling objects_lastrun.py',
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

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Welcome to the Assembling Objects Test.\n\nPress the space bar to move forward.',
    font='times new roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endwelcome = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
participant_instructions = visual.TextStim(win=win, name='participant_instructions',
    text='This is an untimed multiple-choice test.\n\nThe left-most box shows shapes broken up. The 4 boxes on the right show the shapes assembled into a new figure. Select the answer where the shapes are assembled correctly.\n\nTo select your answer, click on the box under your answer. Once selected, it will turn black. Keep in mind that you cannot change your mind once you select a box.\n\nPress the space bar to move forward.',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
remove_instructions = keyboard.Keyboard()

# Initialize components for Routine "sample_question_instructions"
sample_question_instructionsClock = core.Clock()
sample_instructions = visual.TextStim(win=win, name='sample_instructions',
    text='Here is a sample question.\n\nPractice responding by clicking the box under your answer. It will turn black once selected.\n',
    font='Times New Roman',
    pos=(0,0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_sampleinstructions = keyboard.Keyboard()
practiceq = visual.ImageStim(
    win=win,
    name='practiceq', 
    image='practiceq.png', mask=None,
    ori=0, pos=(0, -0.1), size=(1, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
sampleBox1 = visual.Rect(
    win=win, name='sampleBox1',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.13, -0.302),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
sampleBox2 = visual.Rect(
    win=win, name='sampleBox2',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.05, -0.302),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
sampleBox3 = visual.Rect(
    win=win, name='sampleBox3',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.23, -0.302),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
sampleBox4 = visual.Rect(
    win=win, name='sampleBox4',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.41, -0.302),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
mouse3 = event.Mouse(win=win)
x, y = [None, None]
mouse3.mouseClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press the space bar to move forward.',
    font='Times new roman',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "practice_q_feedback"
practice_q_feedbackClock = core.Clock()
feedbacksample = visual.TextStim(win=win, name='feedbacksample',
    text='The correct answer was the 3rd box.\n\nThis is the end of the sample question. Press the space bar to begin the test. Good luck!',
    font='times new roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
question_images = visual.ImageStim(
    win=win,
    name='question_images', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.25, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
participant_response = keyboard.Keyboard()
nextq = visual.TextStim(win=win, name='nextq',
    text='Press the space bar to move forward.',
    font='times new roman',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
box1 = visual.Rect(
    win=win, name='box1',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.23, -0.28),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
box2 = visual.Rect(
    win=win, name='box2',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.03, -0.28),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
box3 = visual.Rect(
    win=win, name='box3',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.26, -0.28),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
box4 = visual.Rect(
    win=win, name='box4',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.47, -0.28),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
instructionsreal = visual.TextStim(win=win, name='instructionsreal',
    text='Click on the box under your answer to select. It will turn black once selected.',
    font='times new roman',
    pos=(0, 0.33), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "thank_you_slide"
thank_you_slideClock = core.Clock()
thankyouslide = visual.TextStim(win=win, name='thankyouslide',
    text='The test is now complete. Thank you!\n\nPress the space bar to exit the test.',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
exit = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
endwelcome.keys = []
endwelcome.rt = []
_endwelcome_allKeys = []
# keep track of which components have finished
welcomeComponents = [text, endwelcome]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *endwelcome* updates
    waitOnFlip = False
    if endwelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endwelcome.frameNStart = frameN  # exact frame index
        endwelcome.tStart = t  # local t and not account for scr refresh
        endwelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endwelcome, 'tStartRefresh')  # time at next scr refresh
        endwelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endwelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endwelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endwelcome.status == STARTED and not waitOnFlip:
        theseKeys = endwelcome.getKeys(keyList=['space'], waitRelease=False)
        _endwelcome_allKeys.extend(theseKeys)
        if len(_endwelcome_allKeys):
            endwelcome.keys = _endwelcome_allKeys[-1].name  # just the last key pressed
            endwelcome.rt = _endwelcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if endwelcome.keys in ['', [], None]:  # No response was made
    endwelcome.keys = None
thisExp.addData('endwelcome.keys',endwelcome.keys)
if endwelcome.keys != None:  # we had a response
    thisExp.addData('endwelcome.rt', endwelcome.rt)
thisExp.addData('endwelcome.started', endwelcome.tStartRefresh)
thisExp.addData('endwelcome.stopped', endwelcome.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
remove_instructions.keys = []
remove_instructions.rt = []
_remove_instructions_allKeys = []
# keep track of which components have finished
instructionsComponents = [participant_instructions, remove_instructions]
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
    
    # *participant_instructions* updates
    if participant_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        participant_instructions.frameNStart = frameN  # exact frame index
        participant_instructions.tStart = t  # local t and not account for scr refresh
        participant_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(participant_instructions, 'tStartRefresh')  # time at next scr refresh
        participant_instructions.setAutoDraw(True)
    
    # *remove_instructions* updates
    waitOnFlip = False
    if remove_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        remove_instructions.frameNStart = frameN  # exact frame index
        remove_instructions.tStart = t  # local t and not account for scr refresh
        remove_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(remove_instructions, 'tStartRefresh')  # time at next scr refresh
        remove_instructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(remove_instructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(remove_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if remove_instructions.status == STARTED and not waitOnFlip:
        theseKeys = remove_instructions.getKeys(keyList=None, waitRelease=False)
        _remove_instructions_allKeys.extend(theseKeys)
        if len(_remove_instructions_allKeys):
            remove_instructions.keys = _remove_instructions_allKeys[-1].name  # just the last key pressed
            remove_instructions.rt = _remove_instructions_allKeys[-1].rt
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
thisExp.addData('participant_instructions.started', participant_instructions.tStartRefresh)
thisExp.addData('participant_instructions.stopped', participant_instructions.tStopRefresh)
# check responses
if remove_instructions.keys in ['', [], None]:  # No response was made
    remove_instructions.keys = None
thisExp.addData('remove_instructions.keys',remove_instructions.keys)
if remove_instructions.keys != None:  # we had a response
    thisExp.addData('remove_instructions.rt', remove_instructions.rt)
thisExp.addData('remove_instructions.started', remove_instructions.tStartRefresh)
thisExp.addData('remove_instructions.stopped', remove_instructions.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sample_question_instructions"-------
continueRoutine = True
# update component parameters for each repeat
end_sampleinstructions.keys = []
end_sampleinstructions.rt = []
_end_sampleinstructions_allKeys = []
sampleBox1.setFillColor([1,1,1])
sampleBox2.setFillColor([1,1,1])
sampleBox3.setFillColor([1,1,1])
sampleBox4.setFillColor([1,1,1])
# setup some python lists for storing info about the mouse3
mouse3.clicked_name = []
gotValidClick = False  # until a click is received
checkboxes = [sampleBox1, sampleBox2, sampleBox3, sampleBox4]
clicked = []
# keep track of which components have finished
sample_question_instructionsComponents = [sample_instructions, end_sampleinstructions, practiceq, sampleBox1, sampleBox2, sampleBox3, sampleBox4, mouse3, text_2]
for thisComponent in sample_question_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sample_question_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sample_question_instructions"-------
while continueRoutine:
    # get current time
    t = sample_question_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sample_question_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sample_instructions* updates
    if sample_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sample_instructions.frameNStart = frameN  # exact frame index
        sample_instructions.tStart = t  # local t and not account for scr refresh
        sample_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sample_instructions, 'tStartRefresh')  # time at next scr refresh
        sample_instructions.setAutoDraw(True)
    
    # *end_sampleinstructions* updates
    waitOnFlip = False
    if end_sampleinstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_sampleinstructions.frameNStart = frameN  # exact frame index
        end_sampleinstructions.tStart = t  # local t and not account for scr refresh
        end_sampleinstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_sampleinstructions, 'tStartRefresh')  # time at next scr refresh
        end_sampleinstructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_sampleinstructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_sampleinstructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_sampleinstructions.status == STARTED and not waitOnFlip:
        theseKeys = end_sampleinstructions.getKeys(keyList=None, waitRelease=False)
        _end_sampleinstructions_allKeys.extend(theseKeys)
        if len(_end_sampleinstructions_allKeys):
            end_sampleinstructions.keys = _end_sampleinstructions_allKeys[-1].name  # just the last key pressed
            end_sampleinstructions.rt = _end_sampleinstructions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *practiceq* updates
    if practiceq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceq.frameNStart = frameN  # exact frame index
        practiceq.tStart = t  # local t and not account for scr refresh
        practiceq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceq, 'tStartRefresh')  # time at next scr refresh
        practiceq.setAutoDraw(True)
    
    # *sampleBox1* updates
    if sampleBox1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sampleBox1.frameNStart = frameN  # exact frame index
        sampleBox1.tStart = t  # local t and not account for scr refresh
        sampleBox1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sampleBox1, 'tStartRefresh')  # time at next scr refresh
        sampleBox1.setAutoDraw(True)
    
    # *sampleBox2* updates
    if sampleBox2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sampleBox2.frameNStart = frameN  # exact frame index
        sampleBox2.tStart = t  # local t and not account for scr refresh
        sampleBox2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sampleBox2, 'tStartRefresh')  # time at next scr refresh
        sampleBox2.setAutoDraw(True)
    
    # *sampleBox3* updates
    if sampleBox3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sampleBox3.frameNStart = frameN  # exact frame index
        sampleBox3.tStart = t  # local t and not account for scr refresh
        sampleBox3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sampleBox3, 'tStartRefresh')  # time at next scr refresh
        sampleBox3.setAutoDraw(True)
    
    # *sampleBox4* updates
    if sampleBox4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sampleBox4.frameNStart = frameN  # exact frame index
        sampleBox4.tStart = t  # local t and not account for scr refresh
        sampleBox4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sampleBox4, 'tStartRefresh')  # time at next scr refresh
        sampleBox4.setAutoDraw(True)
    for box in checkboxes:
        if mouse3.isPressedIn(box) and box.name not in clicked:
            box.color = "black"
            clicked.append(box.name)
    
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sample_question_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sample_question_instructions"-------
for thisComponent in sample_question_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sample_instructions.started', sample_instructions.tStartRefresh)
thisExp.addData('sample_instructions.stopped', sample_instructions.tStopRefresh)
# check responses
if end_sampleinstructions.keys in ['', [], None]:  # No response was made
    end_sampleinstructions.keys = None
thisExp.addData('end_sampleinstructions.keys',end_sampleinstructions.keys)
if end_sampleinstructions.keys != None:  # we had a response
    thisExp.addData('end_sampleinstructions.rt', end_sampleinstructions.rt)
thisExp.addData('end_sampleinstructions.started', end_sampleinstructions.tStartRefresh)
thisExp.addData('end_sampleinstructions.stopped', end_sampleinstructions.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('practiceq.started', practiceq.tStartRefresh)
thisExp.addData('practiceq.stopped', practiceq.tStopRefresh)
thisExp.addData('sampleBox1.started', sampleBox1.tStartRefresh)
thisExp.addData('sampleBox1.stopped', sampleBox1.tStopRefresh)
thisExp.addData('sampleBox2.started', sampleBox2.tStartRefresh)
thisExp.addData('sampleBox2.stopped', sampleBox2.tStopRefresh)
thisExp.addData('sampleBox3.started', sampleBox3.tStartRefresh)
thisExp.addData('sampleBox3.stopped', sampleBox3.tStopRefresh)
thisExp.addData('sampleBox4.started', sampleBox4.tStartRefresh)
thisExp.addData('sampleBox4.stopped', sampleBox4.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse3.getPos()
buttons = mouse3.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    for obj in [sampleBox1, sampleBox2, sampleBox3, sampleBox4]:
        if obj.contains(mouse3):
            gotValidClick = True
            mouse3.clicked_name.append(obj.name)
thisExp.addData('mouse3.x', x)
thisExp.addData('mouse3.y', y)
thisExp.addData('mouse3.leftButton', buttons[0])
thisExp.addData('mouse3.midButton', buttons[1])
thisExp.addData('mouse3.rightButton', buttons[2])
if len(mouse3.clicked_name):
    thisExp.addData('mouse3.clicked_name', mouse3.clicked_name[0])
thisExp.addData('mouse3.started', mouse3.tStart)
thisExp.addData('mouse3.stopped', mouse3.tStop)
thisExp.nextEntry()
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "sample_question_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_q_feedback"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
practice_q_feedbackComponents = [feedbacksample, key_resp]
for thisComponent in practice_q_feedbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_q_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_q_feedback"-------
while continueRoutine:
    # get current time
    t = practice_q_feedbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_q_feedbackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *feedbacksample* updates
    if feedbacksample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        feedbacksample.frameNStart = frameN  # exact frame index
        feedbacksample.tStart = t  # local t and not account for scr refresh
        feedbacksample.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedbacksample, 'tStartRefresh')  # time at next scr refresh
        feedbacksample.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_q_feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_q_feedback"-------
for thisComponent in practice_q_feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('feedbacksample.started', feedbacksample.tStartRefresh)
thisExp.addData('feedbacksample.stopped', feedbacksample.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "practice_q_feedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
questions = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('clickable image_stimulus revised w images.xlsx'),
    seed=None, name='questions')
thisExp.addLoop(questions)  # add the loop to the experiment
thisQuestion = questions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQuestion.rgb)
if thisQuestion != None:
    for paramName in thisQuestion:
        exec('{} = thisQuestion[paramName]'.format(paramName))

for thisQuestion in questions:
    currentLoop = questions
    # abbreviate parameter names if possible (e.g. rgb = thisQuestion.rgb)
    if thisQuestion != None:
        for paramName in thisQuestion:
            exec('{} = thisQuestion[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    question_images.setImage(ImageFile)
    participant_response.keys = []
    participant_response.rt = []
    _participant_response_allKeys = []
    box1.setFillColor('white')
    box2.setFillColor('white')
    box3.setFillColor('white')
    box4.setFillColor('white')
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    #Initializing Variables for Checkboxes
    checkboxes=[box1, box2, box3, box4]
    clicked=[]
    # keep track of which components have finished
    trialComponents = [question_images, participant_response, nextq, box1, box2, box3, box4, mouse, instructionsreal]
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
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *question_images* updates
        if question_images.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_images.frameNStart = frameN  # exact frame index
            question_images.tStart = t  # local t and not account for scr refresh
            question_images.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_images, 'tStartRefresh')  # time at next scr refresh
            question_images.setAutoDraw(True)
        
        # *participant_response* updates
        waitOnFlip = False
        if participant_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            participant_response.frameNStart = frameN  # exact frame index
            participant_response.tStart = t  # local t and not account for scr refresh
            participant_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(participant_response, 'tStartRefresh')  # time at next scr refresh
            participant_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(participant_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(participant_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if participant_response.status == STARTED and not waitOnFlip:
            theseKeys = participant_response.getKeys(keyList=['space'], waitRelease=False)
            _participant_response_allKeys.extend(theseKeys)
            if len(_participant_response_allKeys):
                participant_response.keys = _participant_response_allKeys[-1].name  # just the last key pressed
                participant_response.rt = _participant_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *nextq* updates
        if nextq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nextq.frameNStart = frameN  # exact frame index
            nextq.tStart = t  # local t and not account for scr refresh
            nextq.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nextq, 'tStartRefresh')  # time at next scr refresh
            nextq.setAutoDraw(True)
        
        # *box1* updates
        if box1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box1.frameNStart = frameN  # exact frame index
            box1.tStart = t  # local t and not account for scr refresh
            box1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box1, 'tStartRefresh')  # time at next scr refresh
            box1.setAutoDraw(True)
        
        # *box2* updates
        if box2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box2.frameNStart = frameN  # exact frame index
            box2.tStart = t  # local t and not account for scr refresh
            box2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box2, 'tStartRefresh')  # time at next scr refresh
            box2.setAutoDraw(True)
        
        # *box3* updates
        if box3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box3.frameNStart = frameN  # exact frame index
            box3.tStart = t  # local t and not account for scr refresh
            box3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box3, 'tStartRefresh')  # time at next scr refresh
            box3.setAutoDraw(True)
        
        # *box4* updates
        if box4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box4.frameNStart = frameN  # exact frame index
            box4.tStart = t  # local t and not account for scr refresh
            box4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box4, 'tStartRefresh')  # time at next scr refresh
            box4.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [box1, box2, box3, box4]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
        
        # *instructionsreal* updates
        if instructionsreal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsreal.frameNStart = frameN  # exact frame index
            instructionsreal.tStart = t  # local t and not account for scr refresh
            instructionsreal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsreal, 'tStartRefresh')  # time at next scr refresh
            instructionsreal.setAutoDraw(True)
        #Creating Checkboxes
        for box in checkboxes:
            if mouse.isPressedIn(box) and box.name not in clicked:
                box.color = "black"
                clicked.append(box.name)
        
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
    questions.addData('question_images.started', question_images.tStartRefresh)
    questions.addData('question_images.stopped', question_images.tStopRefresh)
    questions.addData('nextq.started', nextq.tStartRefresh)
    questions.addData('nextq.stopped', nextq.tStopRefresh)
    questions.addData('box1.started', box1.tStartRefresh)
    questions.addData('box1.stopped', box1.tStopRefresh)
    questions.addData('box2.started', box2.tStartRefresh)
    questions.addData('box2.stopped', box2.tStopRefresh)
    questions.addData('box3.started', box3.tStartRefresh)
    questions.addData('box3.stopped', box3.tStopRefresh)
    questions.addData('box4.started', box4.tStartRefresh)
    questions.addData('box4.stopped', box4.tStopRefresh)
    # store data for questions (TrialHandler)
    questions.addData('mouse.x', mouse.x)
    questions.addData('mouse.y', mouse.y)
    questions.addData('mouse.leftButton', mouse.leftButton)
    questions.addData('mouse.midButton', mouse.midButton)
    questions.addData('mouse.rightButton', mouse.rightButton)
    questions.addData('mouse.time', mouse.time)
    questions.addData('mouse.clicked_name', mouse.clicked_name)
    questions.addData('mouse.started', mouse.tStart)
    questions.addData('mouse.stopped', mouse.tStop)
    questions.addData('instructionsreal.started', instructionsreal.tStartRefresh)
    questions.addData('instructionsreal.stopped', instructionsreal.tStopRefresh)
    #Correct Point System
    correct=0
    for checkboxes in mouse.clicked_name:
        if checkboxes in corrAns:
            correct +=1
    questions.addData('correct', correct)
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'questions'


# ------Prepare to start Routine "thank_you_slide"-------
continueRoutine = True
# update component parameters for each repeat
exit.keys = []
exit.rt = []
_exit_allKeys = []
# keep track of which components have finished
thank_you_slideComponents = [thankyouslide, exit]
for thisComponent in thank_you_slideComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thank_you_slideClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thank_you_slide"-------
while continueRoutine:
    # get current time
    t = thank_you_slideClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thank_you_slideClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thankyouslide* updates
    if thankyouslide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thankyouslide.frameNStart = frameN  # exact frame index
        thankyouslide.tStart = t  # local t and not account for scr refresh
        thankyouslide.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thankyouslide, 'tStartRefresh')  # time at next scr refresh
        thankyouslide.setAutoDraw(True)
    
    # *exit* updates
    waitOnFlip = False
    if exit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exit.frameNStart = frameN  # exact frame index
        exit.tStart = t  # local t and not account for scr refresh
        exit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exit, 'tStartRefresh')  # time at next scr refresh
        exit.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(exit.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(exit.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if exit.status == STARTED and not waitOnFlip:
        theseKeys = exit.getKeys(keyList=['space'], waitRelease=False)
        _exit_allKeys.extend(theseKeys)
        if len(_exit_allKeys):
            exit.keys = _exit_allKeys[-1].name  # just the last key pressed
            exit.rt = _exit_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thank_you_slideComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thank_you_slide"-------
for thisComponent in thank_you_slideComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thankyouslide.started', thankyouslide.tStartRefresh)
thisExp.addData('thankyouslide.stopped', thankyouslide.tStopRefresh)
# check responses
if exit.keys in ['', [], None]:  # No response was made
    exit.keys = None
thisExp.addData('exit.keys',exit.keys)
if exit.keys != None:  # we had a response
    thisExp.addData('exit.rt', exit.rt)
thisExp.addData('exit.started', exit.tStartRefresh)
thisExp.addData('exit.stopped', exit.tStopRefresh)
thisExp.nextEntry()
# the Routine "thank_you_slide" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
