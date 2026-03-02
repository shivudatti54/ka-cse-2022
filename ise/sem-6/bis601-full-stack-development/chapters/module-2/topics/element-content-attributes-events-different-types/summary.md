# **Element Content & Attributes, Events, Different Types of Events, How to Bind an Event to an Element, Event Delegation, Event Listeners**

### Element Content & Attributes

- **Element Content**:
  - The text content of an element.
  - Can be accessed using the `innerHTML` or `textContent` property.
- **Element Attributes**:
  - The key-value pairs associated with an element.
  - Can be accessed using the `getAttribute()` and `setAttribute()` methods.
- **Attributes**:
  - A set of key-value pairs associated with an element.
  - Can be accessed using the `attributedValue` property.

### Events

- **Event**:
  - A notification sent to an element when a user interacts with it.
  - Can be triggered by various events such as mouse clicks, key presses, and form submissions.
- **Event Types**:
  - `click`: triggered when an element is clicked.
  - `mouseover`: triggered when an element is hovered over.
  - `keydown`: triggered when a key is pressed.
  - `submit`: triggered when a form is submitted.

### How to Bind an Event to an Element

- **Event Listener**:
  - A function that is executed when an event is triggered.
  - Can be attached to an element using the `addEventListener()` method.
- **Event Binders**:
  - `addEventListener()`: binds an event listener to an element.
  - `removeEventListener()`: removes an event listener from an element.

### Event Delegation

- **Event Delegation**:
  - A technique used to handle events on elements that don't have direct access to the event target.
  - Uses a common ancestor element to bind events to.
- **Example**:
  - Bind a click event to a parent element and use event delegation to handle clicks on its child elements.

### Event Listeners

- **Event Listener Functions**:
  - Functions that are executed when an event is triggered.
  - Can be anonymous or named.
- **Event Listener Properties**:
  - `target`: the element that triggered the event.
  - `preventDefault()`: prevents the default behavior of the event.
  - `stopPropagation()`: stops the event from propagating to other elements.
