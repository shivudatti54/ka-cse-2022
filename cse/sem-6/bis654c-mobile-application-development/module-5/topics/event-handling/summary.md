# Event Handling in Android - Summary

## Key Definitions

- **Event Listener**: An interface containing callback methods invoked when specific user interactions occur on a View
- **Event Handler**: The code logic that executes in response to an event
- **MotionEvent**: An object containing data about touch events including coordinates, pressure, and action type
- **GestureDetector**: A utility class that detects common gestures like scrolls, flings, and double-taps
- **Event Propagation**: The flow of events through the view hierarchy from parent to child and potentially back up

## Important Formulas

- Event handling callback signature: `public void onEventName(View v)`
- Touch event return value: `true` = event consumed, `false` = propagate event
- MotionEvent action extraction: `int action = event.getAction() & MotionEvent.ACTION_MASK`

## Key Points

1. Android uses the observer pattern for event handling where Views are subjects and listeners are observers

2. The OnClickListener interface has a single method `onClick(View v)` for handling click events

3. OnTouchListener provides comprehensive touch control through the `onTouch(View v, MotionEvent event)` method

4. Multiple approaches exist for implementing listeners: XML onClick attribute, anonymous classes, lambda expressions, and activity-implemented listeners

5. MotionEvent contains detailed touch information including getX(), getY(), getPressure(), and getAction()

6. GestureDetector simplifies complex gesture recognition with predefined callbacks like onFling(), onScroll(), and onDoubleTap()

7. The return value of event handlers controls whether events propagate to parent views

8. For functional interfaces (single abstract method), lambda expressions provide cleaner syntax

## Common Mistakes

1. **Forgetting to return true**: Not returning true in onTouch() prevents receiving subsequent MOVE and UP events

2. **Incorrect method signature**: Using android:onClick with wrong method signature causes RuntimeException

3. **Memory leaks**: Creating new listener objects inside loops or frequently called methods

4. **Ignoring event cancellation**: Not handling ACTION_CANCEL can leave UI in inconsistent state during gestures

5. **Confusing onClick with onTouch**: Using onClick for drag operations fails because onClick doesn't track movement