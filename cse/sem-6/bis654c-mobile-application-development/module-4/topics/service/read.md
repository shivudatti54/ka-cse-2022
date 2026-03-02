# Android Services

## Introduction to Android Services

A **Service** is an application component that can perform long-running operations in the background without providing a user interface. Services are one of the four fundamental Android components alongside Activities, Broadcast Receivers, and Content Providers. They continue running even when the user switches to another application.

## Types of Android Services

### 1. Started Service (Unbound Service)

A started service is launched by calling `startService()`. Once started, it can run indefinitely in the background, even if the component that started it is destroyed.

```java
// Starting a service
Intent intent = new Intent(this, MyService.class);
startService(intent);
```

**Key Characteristics:**

- Runs independently of the starting component
- Must stop itself using `stopSelf()` or be stopped by another component using `stopService()`
- Does not return a result to the caller
- Suitable for tasks like downloading files or uploading data

### 2. Bound Service

A bound service allows components to bind to it using `bindService()`. It provides a client-server interface that allows components to interact with the service, send requests, and receive results.

```java
// Binding to a service
Intent intent = new Intent(this, MyBoundService.class);
bindService(intent, serviceConnection, Context.BIND_AUTO_CREATE);
```

**Key Characteristics:**

- Runs only as long as at least one component is bound to it
- Multiple components can bind simultaneously
- Destroyed when all components unbind
- Provides an IBinder interface for communication

### 3. IntentService

IntentService is a subclass of Service that handles asynchronous requests on a worker thread. It processes intents one at a time in a queue and stops itself when work is complete.

```java
public class MyIntentService extends IntentService {
 public MyIntentService() {
 super("MyIntentService");
 }

 @Override
 protected void onHandleIntent(Intent intent) {
 // Handle the intent on a worker thread
 String action = intent.getAction();
 if ("DOWNLOAD".equals(action)) {
 performDownload();
 }
 }
}
```

**Key Characteristics:**

- Creates a worker thread automatically
- Processes requests sequentially (one at a time)
- Stops itself after all requests are handled
- Provides default implementation of `onBind()` that returns null
- Deprecated in API 30; replaced by `WorkManager` or `JobIntentService`

## Service Lifecycle

### Started Service Lifecycle

```
startService()
 |
 v
+------------------+
| onCreate() | Called when service is first created
+------------------+
 |
 v
+------------------+
| onStartCommand() | Called each time startService() is invoked
+------------------+
 |
 v
Service is running
 |
 v (stopSelf() or stopService())
+------------------+
| onDestroy() | Service is destroyed and resources released
+------------------+
```

### Bound Service Lifecycle

```
bindService()
 |
 v
+------------------+
| onCreate() | Called when service is first created
+------------------+
 |
 v
+------------------+
| onBind() | Returns IBinder for client communication
+------------------+
 |
 v
Clients are bound
 |
 v (all clients unbind)
+------------------+
| onUnbind() | Called when all clients disconnect
+------------------+
 |
 v
+------------------+
| onDestroy() | Service is destroyed
+------------------+
```

### Lifecycle Callback Methods

| Method             | Description                                                      |
| ------------------ | ---------------------------------------------------------------- |
| `onCreate()`       | Called once when the service is first created                    |
| `onStartCommand()` | Called each time a client starts the service                     |
| `onBind()`         | Called when a component binds to the service                     |
| `onUnbind()`       | Called when all clients have disconnected                        |
| `onRebind()`       | Called when new clients bind after onUnbind returned true        |
| `onDestroy()`      | Called when the service is no longer used and is being destroyed |

## Implementing a Started Service

```java
public class DownloadService extends Service {

 @Override
 public void onCreate() {
 super.onCreate();
 // Initialize resources
 }

 @Override
 public int onStartCommand(Intent intent, int flags, int startId) {
 // Perform work here
 String url = intent.getStringExtra("download_url");

 new Thread(() -> {
 downloadFile(url);
 stopSelf(startId); // Stop when work is done
 }).start();

 return START_STICKY; // Restart if killed
 }

 @Override
 public IBinder onBind(Intent intent) {
 return null; // Not a bound service
 }

 @Override
 public void onDestroy() {
 super.onDestroy();
 // Clean up resources
 }
}
```

### onStartCommand() Return Values

| Return Value             | Behavior                                              |
| ------------------------ | ----------------------------------------------------- |
| `START_STICKY`           | Restarts service with null intent if killed by system |
| `START_NOT_STICKY`       | Does not restart unless there are pending intents     |
| `START_REDELIVER_INTENT` | Restarts and redelivers the last intent               |

## Implementing a Bound Service

### Using Local Binder Pattern

```java
public class MusicService extends Service {
 private final IBinder binder = new LocalBinder();
 private MediaPlayer mediaPlayer;

 public class LocalBinder extends Binder {
 MusicService getService() {
 return MusicService.this;
 }
 }

 @Override
 public IBinder onBind(Intent intent) {
 return binder;
 }

 public void playMusic(String path) {
 mediaPlayer = MediaPlayer.create(this, Uri.parse(path));
 mediaPlayer.start();
 }

 public void stopMusic() {
 if (mediaPlayer != null) {
 mediaPlayer.stop();
 mediaPlayer.release();
 }
 }
}
```

### Client Activity Binding

```java
public class MusicActivity extends AppCompatActivity {
 private MusicService musicService;
 private boolean isBound = false;

 private ServiceConnection connection = new ServiceConnection() {
 @Override
 public void onServiceConnected(ComponentName name, IBinder service) {
 MusicService.LocalBinder binder = (MusicService.LocalBinder) service;
 musicService = binder.getService();
 isBound = true;
 }

 @Override
 public void onServiceDisconnected(ComponentName name) {
 isBound = false;
 }
 };

 @Override
 protected void onStart() {
 super.onStart();
 Intent intent = new Intent(this, MusicService.class);
 bindService(intent, connection, Context.BIND_AUTO_CREATE);
 }

 @Override
 protected void onStop() {
 super.onStop();
 if (isBound) {
 unbindService(connection);
 isBound = false;
 }
 }
}
```

## Foreground Services

Foreground services perform operations that are noticeable to the user and must display a notification. They have higher priority than background services and are less likely to be killed by the system.

```java
public class LocationService extends Service {
 @Override
 public int onStartCommand(Intent intent, int flags, int startId) {
 Notification notification = new NotificationCompat.Builder(this, "channel_id")
 .setContentTitle("Tracking Location")
 .setContentText("Your location is being tracked")
 .setSmallIcon(R.drawable.ic_location)
 .build();

 startForeground(1, notification);

 // Perform location tracking
 return START_STICKY;
 }

 @Override
 public IBinder onBind(Intent intent) {
 return null;
 }
}
```

## Declaring Services in AndroidManifest.xml

Every service must be declared in the manifest:

```xml
<manifest>
 <application>
 <service
 android:name=".DownloadService"
 android:exported="false" />
 <service
 android:name=".MusicService"
 android:exported="false" />
 <service
 android:name=".LocationService"
 android:foregroundServiceType="location"
 android:exported="false" />
 </application>
</manifest>
```

## Comparison of Service Types

| Feature       | Started Service          | Bound Service       | IntentService         |
| ------------- | ------------------------ | ------------------- | --------------------- |
| Launch Method | startService()           | bindService()       | startService()        |
| Stops         | stopSelf()/stopService() | When all unbind     | Auto-stops after work |
| Thread        | Runs on main thread      | Runs on main thread | Worker thread         |
| Communication | No direct return         | IBinder interface   | Via broadcast/handler |
| Lifetime      | Independent              | Bound to clients    | Until queue is empty  |

## Exam Tips

1. **Know the lifecycle:** Be able to draw and explain both started and bound service lifecycles
2. **Understand return values:** Know the differences between START_STICKY, START_NOT_STICKY, and START_REDELIVER_INTENT
3. **Differentiate service types:** Be clear about when to use started vs bound vs IntentService
4. **Foreground services:** Remember that foreground services require a visible notification
5. **Manifest declaration:** Services must be declared in AndroidManifest.xml
