# Case Study: Location-Based Task Reminder Application

## Introduction

This case study explores the development of a complete Android application that integrates multiple core concepts including SQLite database management, event handling, navigation, and location-based services. The application, "LocationReminder," allows users to create tasks with geographic location triggers—when the user enters or exits a specified location, the application notifies them about the associated task.

This case study demonstrates how Android components work together in a real-world application, providing practical insights into architecture patterns, component communication, and best practices for mobile development. Understanding this integrated approach is essential for developing production-ready mobile applications.

## Application Architecture

### Layered Architecture

The LocationReminder application follows a three-tier architecture:

**Presentation Layer**: This layer contains Activities, Fragments, and XML layouts. It handles user interface rendering and captures user input. The MainActivity displays the list of tasks, while AddTaskActivity allows task creation with location selection.

**Business Logic Layer**: This layer contains the Repository, ViewModel, and use-case classes. It manages data operations, applies business rules, and transforms data between the presentation and data layers. The TaskRepository acts as a single source of truth for task data.

**Data Layer**: This layer comprises the SQLite database, DAO (Data Access Object) classes, and entity models. Room persistence library simplifies database operations while maintaining SQLite's capabilities. The Task entity represents the data model, while TaskDao provides CRUD operations.

### Component Communication

The application uses LiveData for observable data holders, allowing the UI to automatically update when underlying data changes. ViewModel survives configuration changes, maintaining UI-related data during screen rotations. The Repository pattern abstracts data sources, enabling easy testing and modification.

## Database Implementation

### Entity Definition

```java
@Entity(tableName = "tasks")
public class Task {
 @PrimaryKey(autoGenerate = true)
 private int id;
 private String title;
 private String description;
 private double latitude;
 private double longitude;
 private double radius; // in meters
 private boolean isEnterTrigger; // true for entry, false for exit
 private boolean isCompleted;
 private long createdAt;
}
```

### DAO Operations

```java
@Dao
public interface TaskDao {
 @Insert
 long insert(Task task);
 @Update
 void update(Task task);
 @Delete
 void delete(Task task);
 @Query("SELECT * FROM tasks ORDER BY createdAt DESC")
 LiveData<List<Task>> getAllTasks();
 @Query("SELECT * FROM tasks WHERE id = :taskId")
 Task getTaskById(int taskId);
 @Query("DELETE FROM tasks WHERE id = :taskId")
 void deleteById(int taskId);
}
```

### Database Class

```java
@Database(entities = {Task.class}, version = 1, exportSchema = false)
public abstract class AppDatabase extends RoomDatabase {
 public abstract TaskDao taskDao();
}
```

## Event Handling and Location Services

### Location Listener Implementation

The application implements LocationListener to receive location updates:

```java
public class LocationFragment extends Fragment implements LocationListener {
 private LocationManager locationManager;

 @Override
 public void onLocationChanged(Location location) {
 // Check all tasks against current location
 checkTaskTriggers(location);
 }

 private void checkTaskTriggers(Location currentLocation) {
 List<Task> tasks = taskViewModel.getAllTasks().getValue();
 for (Task task : tasks) {
 Location taskLocation = new Location("");
 taskLocation.setLatitude(task.getLatitude());
 taskLocation.setLongitude(task.getLongitude());

 float distance = currentLocation.distanceTo(taskLocation);

 if (distance <= task.getRadius()) {
 if (task.isEnterTrigger()) {
 triggerNotification(task, "You arrived at: " + task.getTitle());
 }
 } else if (task.isEnterTrigger() && distance > task.getRadius() * 1.5) {
 // User has left the area after entering
 }
 }
 }
}
```

### Geofencing Approach

For better battery efficiency, the application also implements Google Play Services Geofencing API:

```java
private GeofencingClient geofencingClient;
private PendingIntent geofencePendingIntent;

private void addGeofence(Task task) {
 Geofence geofence = new Geofence.Builder()
 .setRequestId(String.valueOf(task.getId()))
 .setCircularRegion(
 task.getLatitude(),
 task.getLongitude(),
 (float) task.getRadius()
 )
 .setExpirationDuration(Geofence.NEVER_EXPIRE)
 .setTransitionTypes(
 task.isEnterTrigger() ?
 Geofence.GEOFENCE_TRANSITION_ENTER :
 Geofence.GEOFENCE_TRANSITION_EXIT
 )
 .build();

 GeofencingRequest request = new GeofencingRequest.Builder()
 .setInitialTrigger(GeofencingRequest.INITIAL_TRIGGER_ENTER)
 .addGeofence(geofence)
 .build();
}
```

## Navigation Implementation

### Navigation Graph

```xml
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
 xmlns:app="http://schemas.android.com/apk/res-auto"
 android:id="@+id/nav_graph"
 app:startDestination="@id/taskListFragment">

 <fragment
 android:id="@+id/taskListFragment"
 android:name="com.example.locationreminder.TaskListFragment"
 android:label="My Tasks">
 <action
 android:id="@+id/action_taskList_to_addTask"
 app:destination="@id/addTaskFragment" />
 </fragment>

 <fragment
 android:id="@+id/addTaskFragment"
 android:name="com.example.locationreminder.AddTaskFragment"
 android:label="Add New Task">
 <argument
 android:name="taskId"
 app:argType="integer"
 android:defaultValue="-1" />
 </fragment>

 <fragment
 android:id="@+id/mapFragment"
 android:name="com.example.locationreminder.MapFragment"
 android:label="Select Location" />
</navigation>
```

### Safe Args for Data Passing

```java
// In TaskListFragment
TaskListDirections.ActionTaskListToAddTask action =
 TaskListDirections.actionTaskListToAddTask();
Navigation.findNavController(view).navigate(action);

// In AddTaskFragment
int taskId = AddTaskArgs.fromBundle(getArguments()).getTaskId();
```

## SMS Integration

The application includes SMS notification capability for task reminders:

```java
private void sendSmsNotification(String phoneNumber, String message) {
 SmsManager smsManager = SmsManager.getDefault();
 try {
 ArrayList<String> parts = smsManager.divideMessage(message);
 if (parts.size() == 1) {
 smsManager.sendTextMessage(phoneNumber, null, message, null, null);
 } else {
 smsManager.sendMultipartTextMessage(phoneNumber, null, parts, null, null);
 }
 } catch (SecurityException e) {
 Log.e("SMS", "SMS permission not granted", e);
 }
}
```

## Exam Tips

1. **Understand Component Interactions**: Know how Activities, Fragments, ViewModels, and Repositories communicate and data flows between them.

2. **Room Database Fundamentals**: Remember that Room uses annotations (@Entity, @DAO, @Database) and generates implementation code at compile time.

3. **Location APIs**: Distinguish between LocationManager (GPS provider) and Google Play Services Location API (FusedLocationProviderClient).

4. **Geofencing vs Continuous Tracking**: Geofencing is more battery-efficient for location-triggered events compared to continuous location updates.

5. **Navigation Component**: Remember Safe Args for type-safe data passing between destinations and the navigation graph XML structure.

6. **Permissions**: Android 6.0+ requires runtime permission checks for dangerous permissions including ACCESS_FINE_LOCATION and SEND_SMS.

7. **Background Execution**: Understand how WorkManager or Foreground Services handle tasks that need to run even when the app is not in foreground.

8. **MVVM Pattern**: The ViewModel survives configuration changes and LiveData provides observable data holders for UI updates.
