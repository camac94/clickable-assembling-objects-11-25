/************************************* 
 * Clickable Assembling Objects Test *
 *************************************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'clickable assembling objects';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
flowScheduler.add(sample_question_instructionsRoutineBegin());
flowScheduler.add(sample_question_instructionsRoutineEachFrame());
flowScheduler.add(sample_question_instructionsRoutineEnd());
flowScheduler.add(practice_q_feedbackRoutineBegin());
flowScheduler.add(practice_q_feedbackRoutineEachFrame());
flowScheduler.add(practice_q_feedbackRoutineEnd());
const questionsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(questionsLoopBegin, questionsLoopScheduler);
flowScheduler.add(questionsLoopScheduler);
flowScheduler.add(questionsLoopEnd);
flowScheduler.add(thank_you_slideRoutineBegin());
flowScheduler.add(thank_you_slideRoutineEachFrame());
flowScheduler.add(thank_you_slideRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'q2.png', 'path': 'q2.png'},
    {'name': 'q8.png', 'path': 'q8.png'},
    {'name': 'q1.png', 'path': 'q1.png'},
    {'name': 'image_stimulus revised w images.xlsx', 'path': 'image_stimulus revised w images.xlsx'},
    {'name': 'q9.png', 'path': 'q9.png'},
    {'name': 'q5.png', 'path': 'q5.png'},
    {'name': 'q12.png', 'path': 'q12.png'},
    {'name': 'q3.png', 'path': 'q3.png'},
    {'name': 'q10.png', 'path': 'q10.png'},
    {'name': 'q11.png', 'path': 'q11.png'},
    {'name': 'q6.png', 'path': 'q6.png'},
    {'name': 'q13.png', 'path': 'q13.png'},
    {'name': 'practiceq.png', 'path': 'practiceq.png'},
    {'name': 'q14.png', 'path': 'q14.png'},
    {'name': 'q15.png', 'path': 'q15.png'},
    {'name': 'q7.png', 'path': 'q7.png'},
    {'name': 'q4.png', 'path': 'q4.png'},
    {'name': 'q16.png', 'path': 'q16.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.5';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var welcomeClock;
var text;
var endwelcome;
var instructionsClock;
var participant_instructions;
var remove_instructions;
var sample_question_instructionsClock;
var sample_instructions;
var end_sampleinstructions;
var practiceq;
var sampleBox1;
var sampleBox2;
var sampleBox3;
var sampleBox4;
var mouse3;
var text_2;
var practice_q_feedbackClock;
var feedbacksample;
var key_resp;
var trialClock;
var question_images;
var participant_response;
var nextq;
var box1;
var box2;
var box3;
var box4;
var mouse;
var instructionsreal;
var thank_you_slideClock;
var thankyouslide;
var exit;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Welcome to the Assembling Objects Test.\n\nPress the space bar to move forward.',
    font: 'times new roman',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  endwelcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  participant_instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'participant_instructions',
    text: 'This is an untimed multiple-choice test.\n\nThe left-most box shows shapes broken up. The 4 boxes on the right show the shapes assembled into a new figure. Select the answer where the shapes are assembled correctly.\n\nTo select your answer, click on the box under your answer. Once selected, it will turn black. Keep in mind that you cannot change your mind once you select a box.\n\nPress the space bar to move forward.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  remove_instructions = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "sample_question_instructions"
  sample_question_instructionsClock = new util.Clock();
  sample_instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'sample_instructions',
    text: 'Here is a sample question.\n\nPractice responding by clicking the box under your answer. It will turn black once selected.\n',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  end_sampleinstructions = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  practiceq = new visual.ImageStim({
    win : psychoJS.window,
    name : 'practiceq', units : undefined, 
    image : 'practiceq.png', mask : undefined,
    ori : 0, pos : [0, (- 0.1)], size : [1, 0.35],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  sampleBox1 = new visual.Rect ({
    win: psychoJS.window, name: 'sampleBox1', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.13), (- 0.302)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  sampleBox2 = new visual.Rect ({
    win: psychoJS.window, name: 'sampleBox2', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.05, (- 0.302)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  sampleBox3 = new visual.Rect ({
    win: psychoJS.window, name: 'sampleBox3', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.23, (- 0.302)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  sampleBox4 = new visual.Rect ({
    win: psychoJS.window, name: 'sampleBox4', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.41, (- 0.302)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  mouse3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse3.mouseClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Press the space bar to move forward.',
    font: 'Times new roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -9.0 
  });
  
  // Initialize components for Routine "practice_q_feedback"
  practice_q_feedbackClock = new util.Clock();
  feedbacksample = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbacksample',
    text: 'The correct answer was the 3rd box.\n\nThis is the end of the sample question. Press the space bar to begin the test. Good luck!',
    font: 'times new roman',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  question_images = new visual.ImageStim({
    win : psychoJS.window,
    name : 'question_images', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1.25, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  participant_response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  nextq = new visual.TextStim({
    win: psychoJS.window,
    name: 'nextq',
    text: 'Press the space bar to move forward.',
    font: 'times new roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  box1 = new visual.Rect ({
    win: psychoJS.window, name: 'box1', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.23), (- 0.28)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  box2 = new visual.Rect ({
    win: psychoJS.window, name: 'box2', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.03, (- 0.28)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  box3 = new visual.Rect ({
    win: psychoJS.window, name: 'box3', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.26, (- 0.28)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  box4 = new visual.Rect ({
    win: psychoJS.window, name: 'box4', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.47, (- 0.28)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  instructionsreal = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionsreal',
    text: 'Click on the box under your answer to select. It will turn black once selected.',
    font: 'times new roman',
    units: undefined, 
    pos: [0, 0.33], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -8.0 
  });
  
  // Initialize components for Routine "thank_you_slide"
  thank_you_slideClock = new util.Clock();
  thankyouslide = new visual.TextStim({
    win: psychoJS.window,
    name: 'thankyouslide',
    text: 'The test is now complete. Thank you!\n\nPress the space bar to exit the test.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  exit = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _endwelcome_allKeys;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'welcome'-------
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    endwelcome.keys = undefined;
    endwelcome.rt = undefined;
    _endwelcome_allKeys = [];
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(text);
    welcomeComponents.push(endwelcome);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


var continueRoutine;
function welcomeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'welcome'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *endwelcome* updates
    if (t >= 0.0 && endwelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endwelcome.tStart = t;  // (not accounting for frame time here)
      endwelcome.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endwelcome.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endwelcome.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endwelcome.clearEvents(); });
    }

    if (endwelcome.status === PsychoJS.Status.STARTED) {
      let theseKeys = endwelcome.getKeys({keyList: ['space'], waitRelease: false});
      _endwelcome_allKeys = _endwelcome_allKeys.concat(theseKeys);
      if (_endwelcome_allKeys.length > 0) {
        endwelcome.keys = _endwelcome_allKeys[_endwelcome_allKeys.length - 1].name;  // just the last key pressed
        endwelcome.rt = _endwelcome_allKeys[_endwelcome_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'welcome'-------
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('endwelcome.keys', endwelcome.keys);
    if (typeof endwelcome.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('endwelcome.rt', endwelcome.rt);
        routineTimer.reset();
        }
    
    endwelcome.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _remove_instructions_allKeys;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions'-------
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    remove_instructions.keys = undefined;
    remove_instructions.rt = undefined;
    _remove_instructions_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(participant_instructions);
    instructionsComponents.push(remove_instructions);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *participant_instructions* updates
    if (t >= 0.0 && participant_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      participant_instructions.tStart = t;  // (not accounting for frame time here)
      participant_instructions.frameNStart = frameN;  // exact frame index
      
      participant_instructions.setAutoDraw(true);
    }

    
    // *remove_instructions* updates
    if (t >= 0.0 && remove_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      remove_instructions.tStart = t;  // (not accounting for frame time here)
      remove_instructions.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { remove_instructions.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { remove_instructions.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { remove_instructions.clearEvents(); });
    }

    if (remove_instructions.status === PsychoJS.Status.STARTED) {
      let theseKeys = remove_instructions.getKeys({keyList: [], waitRelease: false});
      _remove_instructions_allKeys = _remove_instructions_allKeys.concat(theseKeys);
      if (_remove_instructions_allKeys.length > 0) {
        remove_instructions.keys = _remove_instructions_allKeys[_remove_instructions_allKeys.length - 1].name;  // just the last key pressed
        remove_instructions.rt = _remove_instructions_allKeys[_remove_instructions_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instructions'-------
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('remove_instructions.keys', remove_instructions.keys);
    if (typeof remove_instructions.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('remove_instructions.rt', remove_instructions.rt);
        routineTimer.reset();
        }
    
    remove_instructions.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _end_sampleinstructions_allKeys;
var gotValidClick;
var checkboxes;
var clicked;
var sample_question_instructionsComponents;
function sample_question_instructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'sample_question_instructions'-------
    t = 0;
    sample_question_instructionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    end_sampleinstructions.keys = undefined;
    end_sampleinstructions.rt = undefined;
    _end_sampleinstructions_allKeys = [];
    sampleBox1.setFillColor(new util.Color([1, 1, 1]));
    sampleBox2.setFillColor(new util.Color([1, 1, 1]));
    sampleBox3.setFillColor(new util.Color([1, 1, 1]));
    sampleBox4.setFillColor(new util.Color([1, 1, 1]));
    // setup some python lists for storing info about the mouse3
    mouse3.clicked_name = [];
    gotValidClick = false; // until a click is received
    checkboxes = [sampleBox1, sampleBox2, sampleBox3, sampleBox4];
    clicked = [];
    
    // keep track of which components have finished
    sample_question_instructionsComponents = [];
    sample_question_instructionsComponents.push(sample_instructions);
    sample_question_instructionsComponents.push(end_sampleinstructions);
    sample_question_instructionsComponents.push(practiceq);
    sample_question_instructionsComponents.push(sampleBox1);
    sample_question_instructionsComponents.push(sampleBox2);
    sample_question_instructionsComponents.push(sampleBox3);
    sample_question_instructionsComponents.push(sampleBox4);
    sample_question_instructionsComponents.push(mouse3);
    sample_question_instructionsComponents.push(text_2);
    
    for (const thisComponent of sample_question_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


var _pj;
function sample_question_instructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'sample_question_instructions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = sample_question_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sample_instructions* updates
    if (t >= 0.0 && sample_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sample_instructions.tStart = t;  // (not accounting for frame time here)
      sample_instructions.frameNStart = frameN;  // exact frame index
      
      sample_instructions.setAutoDraw(true);
    }

    
    // *end_sampleinstructions* updates
    if (t >= 0.0 && end_sampleinstructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_sampleinstructions.tStart = t;  // (not accounting for frame time here)
      end_sampleinstructions.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_sampleinstructions.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_sampleinstructions.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_sampleinstructions.clearEvents(); });
    }

    if (end_sampleinstructions.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_sampleinstructions.getKeys({keyList: [], waitRelease: false});
      _end_sampleinstructions_allKeys = _end_sampleinstructions_allKeys.concat(theseKeys);
      if (_end_sampleinstructions_allKeys.length > 0) {
        end_sampleinstructions.keys = _end_sampleinstructions_allKeys[_end_sampleinstructions_allKeys.length - 1].name;  // just the last key pressed
        end_sampleinstructions.rt = _end_sampleinstructions_allKeys[_end_sampleinstructions_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *practiceq* updates
    if (t >= 0.0 && practiceq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceq.tStart = t;  // (not accounting for frame time here)
      practiceq.frameNStart = frameN;  // exact frame index
      
      practiceq.setAutoDraw(true);
    }

    
    // *sampleBox1* updates
    if (t >= 0.0 && sampleBox1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sampleBox1.tStart = t;  // (not accounting for frame time here)
      sampleBox1.frameNStart = frameN;  // exact frame index
      
      sampleBox1.setAutoDraw(true);
    }

    
    // *sampleBox2* updates
    if (t >= 0.0 && sampleBox2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sampleBox2.tStart = t;  // (not accounting for frame time here)
      sampleBox2.frameNStart = frameN;  // exact frame index
      
      sampleBox2.setAutoDraw(true);
    }

    
    // *sampleBox3* updates
    if (t >= 0.0 && sampleBox3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sampleBox3.tStart = t;  // (not accounting for frame time here)
      sampleBox3.frameNStart = frameN;  // exact frame index
      
      sampleBox3.setAutoDraw(true);
    }

    
    // *sampleBox4* updates
    if (t >= 0.0 && sampleBox4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sampleBox4.tStart = t;  // (not accounting for frame time here)
      sampleBox4.frameNStart = frameN;  // exact frame index
      
      sampleBox4.setAutoDraw(true);
    }

    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    for (var box, _pj_c = 0, _pj_a = checkboxes, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        box = _pj_a[_pj_c];
        if ((mouse3.isPressedIn(box) && (! _pj.in_es6(box.name, clicked)))) {
            box.color = "black";
            clicked.append(box.name);
        }
    }
    
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of sample_question_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var _mouseXYs;
var _mouseButtons;
function sample_question_instructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'sample_question_instructions'-------
    for (const thisComponent of sample_question_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end_sampleinstructions.keys', end_sampleinstructions.keys);
    if (typeof end_sampleinstructions.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_sampleinstructions.rt', end_sampleinstructions.rt);
        routineTimer.reset();
        }
    
    end_sampleinstructions.stop();
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = mouse3.getPos();
    _mouseButtons = mouse3.getPressed();
    psychoJS.experiment.addData('mouse3.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse3.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse3.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse3.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse3.rightButton', _mouseButtons[2]);
    if (mouse3.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse3.clicked_name', mouse3.clicked_name[0]);}
    // the Routine "sample_question_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var practice_q_feedbackComponents;
function practice_q_feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'practice_q_feedback'-------
    t = 0;
    practice_q_feedbackClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    practice_q_feedbackComponents = [];
    practice_q_feedbackComponents.push(feedbacksample);
    practice_q_feedbackComponents.push(key_resp);
    
    for (const thisComponent of practice_q_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_q_feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'practice_q_feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practice_q_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedbacksample* updates
    if (t >= 0.0 && feedbacksample.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbacksample.tStart = t;  // (not accounting for frame time here)
      feedbacksample.frameNStart = frameN;  // exact frame index
      
      feedbacksample.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_q_feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_q_feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'practice_q_feedback'-------
    for (const thisComponent of practice_q_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "practice_q_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var questions;
var currentLoop;
function questionsLoopBegin(questionsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  questions = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'image_stimulus revised w images.xlsx',
    seed: undefined, name: 'questions'
  });
  psychoJS.experiment.addLoop(questions); // add the loop to the experiment
  currentLoop = questions;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisQuestion of questions) {
    const snapshot = questions.getSnapshot();
    questionsLoopScheduler.add(importConditions(snapshot));
    questionsLoopScheduler.add(trialRoutineBegin(snapshot));
    questionsLoopScheduler.add(trialRoutineEachFrame(snapshot));
    questionsLoopScheduler.add(trialRoutineEnd(snapshot));
    questionsLoopScheduler.add(endLoopIteration(questionsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function questionsLoopEnd() {
  psychoJS.experiment.removeLoop(questions);

  return Scheduler.Event.NEXT;
}


var _participant_response_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    question_images.setImage(ImageFile);
    participant_response.keys = undefined;
    participant_response.rt = undefined;
    _participant_response_allKeys = [];
    box1.setFillColor(new util.Color('white'));
    box2.setFillColor(new util.Color('white'));
    box3.setFillColor(new util.Color('white'));
    box4.setFillColor(new util.Color('white'));
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    checkboxes = [box1, box2, box3, box4];
    clicked = [];
    
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(question_images);
    trialComponents.push(participant_response);
    trialComponents.push(nextq);
    trialComponents.push(box1);
    trialComponents.push(box2);
    trialComponents.push(box3);
    trialComponents.push(box4);
    trialComponents.push(mouse);
    trialComponents.push(instructionsreal);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


var prevButtonState;
function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question_images* updates
    if (t >= 0.0 && question_images.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_images.tStart = t;  // (not accounting for frame time here)
      question_images.frameNStart = frameN;  // exact frame index
      
      question_images.setAutoDraw(true);
    }

    
    // *participant_response* updates
    if (t >= 0.0 && participant_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      participant_response.tStart = t;  // (not accounting for frame time here)
      participant_response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { participant_response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { participant_response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { participant_response.clearEvents(); });
    }

    if (participant_response.status === PsychoJS.Status.STARTED) {
      let theseKeys = participant_response.getKeys({keyList: ['space'], waitRelease: false});
      _participant_response_allKeys = _participant_response_allKeys.concat(theseKeys);
      if (_participant_response_allKeys.length > 0) {
        participant_response.keys = _participant_response_allKeys[0].name;  // just the first key pressed
        participant_response.rt = _participant_response_allKeys[0].rt;
        // was this correct?
        if (participant_response.keys == corrAns) {
            participant_response.corr = 1;
        } else {
            participant_response.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *nextq* updates
    if (t >= 0.0 && nextq.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nextq.tStart = t;  // (not accounting for frame time here)
      nextq.frameNStart = frameN;  // exact frame index
      
      nextq.setAutoDraw(true);
    }

    
    // *box1* updates
    if (t >= 0.0 && box1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      box1.tStart = t;  // (not accounting for frame time here)
      box1.frameNStart = frameN;  // exact frame index
      
      box1.setAutoDraw(true);
    }

    
    // *box2* updates
    if (t >= 0.0 && box2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      box2.tStart = t;  // (not accounting for frame time here)
      box2.frameNStart = frameN;  // exact frame index
      
      box2.setAutoDraw(true);
    }

    
    // *box3* updates
    if (t >= 0.0 && box3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      box3.tStart = t;  // (not accounting for frame time here)
      box3.frameNStart = frameN;  // exact frame index
      
      box3.setAutoDraw(true);
    }

    
    // *box4* updates
    if (t >= 0.0 && box4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      box4.tStart = t;  // (not accounting for frame time here)
      box4.frameNStart = frameN;  // exact frame index
      
      box4.setAutoDraw(true);
    }

    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [box1, box2, box3, box4]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
        }
      }
    }
    
    // *instructionsreal* updates
    if (t >= 0.0 && instructionsreal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructionsreal.tStart = t;  // (not accounting for frame time here)
      instructionsreal.frameNStart = frameN;  // exact frame index
      
      instructionsreal.setAutoDraw(true);
    }

    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    for (var box, _pj_c = 0, _pj_a = checkboxes, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        box = _pj_a[_pj_c];
        if ((mouse.isPressedIn(box) && (! _pj.in_es6(box.name, clicked)))) {
            box.color = "black";
            clicked.append(box.name);
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var correct;
function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (participant_response.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         participant_response.corr = 1;  // correct non-response
      } else {
         participant_response.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('participant_response.keys', participant_response.keys);
    psychoJS.experiment.addData('participant_response.corr', participant_response.corr);
    if (typeof participant_response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('participant_response.rt', participant_response.rt);
        routineTimer.reset();
        }
    
    participant_response.stop();
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name);
    
    correct = 0;
    for (var answer, _pj_c = 0, _pj_a = clicked, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        answer = _pj_a[_pj_c];
        if ((answer === corrAns)) {
            correct += 1;
        }
    }
    questions.addData("correct", correct);
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _exit_allKeys;
var thank_you_slideComponents;
function thank_you_slideRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'thank_you_slide'-------
    t = 0;
    thank_you_slideClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    exit.keys = undefined;
    exit.rt = undefined;
    _exit_allKeys = [];
    // keep track of which components have finished
    thank_you_slideComponents = [];
    thank_you_slideComponents.push(thankyouslide);
    thank_you_slideComponents.push(exit);
    
    for (const thisComponent of thank_you_slideComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function thank_you_slideRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'thank_you_slide'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = thank_you_slideClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thankyouslide* updates
    if (t >= 0.0 && thankyouslide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thankyouslide.tStart = t;  // (not accounting for frame time here)
      thankyouslide.frameNStart = frameN;  // exact frame index
      
      thankyouslide.setAutoDraw(true);
    }

    
    // *exit* updates
    if (t >= 0.0 && exit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      exit.tStart = t;  // (not accounting for frame time here)
      exit.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { exit.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { exit.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { exit.clearEvents(); });
    }

    if (exit.status === PsychoJS.Status.STARTED) {
      let theseKeys = exit.getKeys({keyList: ['space'], waitRelease: false});
      _exit_allKeys = _exit_allKeys.concat(theseKeys);
      if (_exit_allKeys.length > 0) {
        exit.keys = _exit_allKeys[_exit_allKeys.length - 1].name;  // just the last key pressed
        exit.rt = _exit_allKeys[_exit_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of thank_you_slideComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function thank_you_slideRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'thank_you_slide'-------
    for (const thisComponent of thank_you_slideComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('exit.keys', exit.keys);
    if (typeof exit.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('exit.rt', exit.rt);
        routineTimer.reset();
        }
    
    exit.stop();
    // the Routine "thank_you_slide" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
