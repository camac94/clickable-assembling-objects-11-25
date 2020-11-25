#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on Wed Nov 25 11:28:36 2020
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
    originPath='/Users/catie/Desktop/assembling_images/final nov 22 official assembling objects test_lastrun.py',
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
    text='Welcome to the Assembling Objects Test.\n\nPress any key to move forward.',
    font='times new roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endwelcome = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
participant_instructions = visual.TextStim(win=win, name='participant_instructions',
    text='This is an untimed multiple-choice test.\n\nThe left-most box shows shapes broken up. The 4 boxes on the right show the shapes assembled into a new figure. Select the answer where the shapes are assembled correctly.\n\nTo select your answer, press 1, 2, 3, or 4 on the keyboard.\n\nPress any key to begin the test.',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
remove_instructions = keyboard.Keyboard()

# Initialize components for Routine "sample_question_instructions"
sample_question_instructionsClock = core.Clock()
sample_instructions = visual.TextStim(win=win, name='sample_instructions',
    text='The next slide will show a sample question. \n\nPractice responding by pressing your response (1, 2, 3, 4) on the keyboard.',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_sampleinstructions = keyboard.Keyboard()

# Initialize components for Routine "actual_sample_question"
actual_sample_questionClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='practiceq.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
endsamplequestion = keyboard.Keyboard()

# Initialize components for Routine "sample_question_feedback_and_start_test"
sample_question_feedback_and_start_testClock = core.Clock()
sample_feedback = visual.TextStim(win=win, name='sample_feedback',
    text='The correct answer was 3. This concludes the sample question.\n\nThe test will now begin. Press any key to start. Good luck!\n\n',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
starttestaftersample = keyboard.Keyboard()

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

# Initialize components for Routine "thank_you_slide"
thank_you_slideClock = core.Clock()
thankyouslide = visual.TextStim(win=win, name='thankyouslide',
    text='The test is now complete. Thank you!\n\nPress any key to exit the test.',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
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
        theseKeys = endwelcome.getKeys(keyList=None, waitRelease=False)
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
# keep track of which components have finished
sample_question_instructionsComponents = [sample_instructions, end_sampleinstructions]
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
# the Routine "sample_question_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "actual_sample_question"-------
continueRoutine = True
# update component parameters for each repeat
endsamplequestion.keys = []
endsamplequestion.rt = []
_endsamplequestion_allKeys = []
# keep track of which components have finished
actual_sample_questionComponents = [image, endsamplequestion]
for thisComponent in actual_sample_questionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
actual_sample_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "actual_sample_question"-------
while continueRoutine:
    # get current time
    t = actual_sample_questionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=actual_sample_questionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *endsamplequestion* updates
    waitOnFlip = False
    if endsamplequestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endsamplequestion.frameNStart = frameN  # exact frame index
        endsamplequestion.tStart = t  # local t and not account for scr refresh
        endsamplequestion.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endsamplequestion, 'tStartRefresh')  # time at next scr refresh
        endsamplequestion.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endsamplequestion.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endsamplequestion.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endsamplequestion.status == STARTED and not waitOnFlip:
        theseKeys = endsamplequestion.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
        _endsamplequestion_allKeys.extend(theseKeys)
        if len(_endsamplequestion_allKeys):
            endsamplequestion.keys = _endsamplequestion_allKeys[-1].name  # just the last key pressed
            endsamplequestion.rt = _endsamplequestion_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in actual_sample_questionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "actual_sample_question"-------
for thisComponent in actual_sample_questionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if endsamplequestion.keys in ['', [], None]:  # No response was made
    endsamplequestion.keys = None
thisExp.addData('endsamplequestion.keys',endsamplequestion.keys)
if endsamplequestion.keys != None:  # we had a response
    thisExp.addData('endsamplequestion.rt', endsamplequestion.rt)
thisExp.addData('endsamplequestion.started', endsamplequestion.tStartRefresh)
thisExp.addData('endsamplequestion.stopped', endsamplequestion.tStopRefresh)
thisExp.nextEntry()
# the Routine "actual_sample_question" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sample_question_feedback_and_start_test"-------
continueRoutine = True
# update component parameters for each repeat
starttestaftersample.keys = []
starttestaftersample.rt = []
_starttestaftersample_allKeys = []
# keep track of which components have finished
sample_question_feedback_and_start_testComponents = [sample_feedback, starttestaftersample]
for thisComponent in sample_question_feedback_and_start_testComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sample_question_feedback_and_start_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sample_question_feedback_and_start_test"-------
while continueRoutine:
    # get current time
    t = sample_question_feedback_and_start_testClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sample_question_feedback_and_start_testClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sample_feedback* updates
    if sample_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sample_feedback.frameNStart = frameN  # exact frame index
        sample_feedback.tStart = t  # local t and not account for scr refresh
        sample_feedback.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sample_feedback, 'tStartRefresh')  # time at next scr refresh
        sample_feedback.setAutoDraw(True)
    
    # *starttestaftersample* updates
    waitOnFlip = False
    if starttestaftersample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        starttestaftersample.frameNStart = frameN  # exact frame index
        starttestaftersample.tStart = t  # local t and not account for scr refresh
        starttestaftersample.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(starttestaftersample, 'tStartRefresh')  # time at next scr refresh
        starttestaftersample.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(starttestaftersample.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(starttestaftersample.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if starttestaftersample.status == STARTED and not waitOnFlip:
        theseKeys = starttestaftersample.getKeys(keyList=None, waitRelease=False)
        _starttestaftersample_allKeys.extend(theseKeys)
        if len(_starttestaftersample_allKeys):
            starttestaftersample.keys = _starttestaftersample_allKeys[-1].name  # just the last key pressed
            starttestaftersample.rt = _starttestaftersample_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sample_question_feedback_and_start_testComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sample_question_feedback_and_start_test"-------
for thisComponent in sample_question_feedback_and_start_testComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sample_feedback.started', sample_feedback.tStartRefresh)
thisExp.addData('sample_feedback.stopped', sample_feedback.tStopRefresh)
# check responses
if starttestaftersample.keys in ['', [], None]:  # No response was made
    starttestaftersample.keys = None
thisExp.addData('starttestaftersample.keys',starttestaftersample.keys)
if starttestaftersample.keys != None:  # we had a response
    thisExp.addData('starttestaftersample.rt', starttestaftersample.rt)
thisExp.addData('starttestaftersample.started', starttestaftersample.tStartRefresh)
thisExp.addData('starttestaftersample.stopped', starttestaftersample.tStopRefresh)
thisExp.nextEntry()
# the Routine "sample_question_feedback_and_start_test" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
questions = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('image_stimulus revised w images.xlsx'),
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
    # keep track of which components have finished
    trialComponents = [question_images, participant_response]
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
            theseKeys = participant_response.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _participant_response_allKeys.extend(theseKeys)
            if len(_participant_response_allKeys):
                participant_response.keys = _participant_response_allKeys[0].name  # just the first key pressed
                participant_response.rt = _participant_response_allKeys[0].rt
                # was this correct?
                if (participant_response.keys == str(corrAns)) or (participant_response.keys == corrAns):
                    participant_response.corr = 1
                else:
                    participant_response.corr = 0
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
    questions.addData('question_images.started', question_images.tStartRefresh)
    questions.addData('question_images.stopped', question_images.tStopRefresh)
    # check responses
    if participant_response.keys in ['', [], None]:  # No response was made
        participant_response.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           participant_response.corr = 1;  # correct non-response
        else:
           participant_response.corr = 0;  # failed to respond (incorrectly)
    # store data for questions (TrialHandler)
    questions.addData('participant_response.keys',participant_response.keys)
    questions.addData('participant_response.corr', participant_response.corr)
    if participant_response.keys != None:  # we had a response
        questions.addData('participant_response.rt', participant_response.rt)
    questions.addData('participant_response.started', participant_response.tStartRefresh)
    questions.addData('participant_response.stopped', participant_response.tStopRefresh)
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
        theseKeys = exit.getKeys(keyList=None, waitRelease=False)
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
