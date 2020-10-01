# Experiment FSM
This package contains Python code to make finite state machines (FSMs), primarily for (neuro)science experiments.


## Specifying the FSM states

A state can be thought of as a discrete part of the task which is triggered by some condition being met and ends when some other condition is met (e.g., waiting for fixation, or a target hold). The state transition definition describes the structure of the task. For each possible state it lists all the possible subsequent states and the events that trigger those transitions.

For example, the parent class :class:`Experiment` has the following structure, where ovals represent states and arrows represent transitions:

[](readme-images/states.png)

A state transition definition is written in the code as an object with the name ``status`` that delineates all possible event-next state transitions that could occur from within each state. For the task illustrated above, the state transition definition in the code looks like

```
from experiment_fsm.fsm import FSMTable, StateTransitions
status = FSMTable(
        wait = StateTransitions(start_trial="trial", premature="penalty", stoppable=False),
        trial = StateTransitions(correct="reward", incorrect="penalty", timeout="penalty"),
        reward = StateTransitions(post_reward="wait"),
        penalty = StateTransitions(post_penalty="wait"),
    )
```

There are four states in this task (*wait*, *trial*, *reward*, and *penalty*). Each state name is entered in the ``status`` dictionary as a key with another dictionary for the value. That dictionary in turn contains keys which are the names of events that trigger state transitions (they can also be thought of as tests that must be passed in order to move to the next state), and values which are the names of the states that follow these events. So while this task is in the *wait* state, it can do one of four things at any moment: if the *start_trial* test is passed, it transitions to the *trial* state; if the *premature* test is passed, it transitions to the *penalty* state; if the experiment receives a stop signal from the server, the task ends; if none of these things occur, it remains in the *wait* state.

    ..  note::

        The key/value pair ``stop = None`` can be inserted into any state where you would like the server to be able to stop the task immediately. If a state's dictionary does not contain this entry and a stop command is received, the task will continue until it reaches a state that does contain it. Make sure at least one state has an exit transition, otherwise you will not be able to stop execution of your task! If you use the ``StateTransitions``, states are assumed to be stoppable by default (the more common condition). Sometimes states should not be stoppable, e.g., if during that state you run an actuator and you need to keep the task running until the action is complete.


## Transition functions