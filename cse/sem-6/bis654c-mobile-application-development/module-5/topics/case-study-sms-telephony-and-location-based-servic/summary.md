# Case Study: SMS Telephony and Location Based Services - Summary

## Key Definitions and Concepts

- **SMS Telephony**: Text messaging service (160 chars/message) using `SmsManager` API in Android
- **LBS (Location Based Services)**: Apps using GPS/WiFi/cell tower data for location-aware functionality
- **GPS_PROVIDER**: Android service providing location data via satellites (high accuracy)
- **NETWORK_PROVIDER**: Location data from cellular/WiFi networks (lower accuracy)
- **Geocoding**: Converting coordinates to addresses using `Geocoder` class
- **Fused Location Provider**: Google Play services API for optimized battery usage in location tracking

## Important Formulas and Theorems

```java
// Haversine formula for distance between two coordinates
double dLat = Math.toRadians(lat2 - lat1);
double dLon = Math.toRadians(lon2 - lon1);
double a = Math.sin(dLat/2) * Math.sin(dLat/2) +
           Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2)) *
           Math.sin(dLon/2) * Math.sin(dLon/2);
double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
double distance = 6371 * c; // Earth radius in km
```

```kotlin
// SMS message splitting calculation
val numPages = ceil(message.length / 160.0).toInt()
```

**ACID Properties** (for SQLite transactions):

- Atomicity, Consistency, Isolation, Durability

## Key Points

1. SMS requires `SEND_SMS`/`RECEIVE_SMS` permissions in AndroidManifest.xml
2. Location access needs `ACCESS_FINE_LOCATION` or `ACCESS_COARSE_LOCATION`
3. Use `LocationListener` interface for real-time updates with `requestLocationUpdates()`
4. Always check GPS status using `LocationManager.isProviderEnabled()`
5. Battery-efficient location tracking uses `FusedLocationProviderClient`
6. SMS messages longer than 160 chars are split into multiple PDUs
7. Emergency alert systems combine SMS broadcasts with location coordinates
8. SQLite transactions (`BEGIN TRANSACTION`, `COMMIT`) ensure data integrity when storing location history
9. Reverse geocoding (coordinates → address) requires internet permission
10. Telephony features use `TelephonyManager` system service

## Common Mistakes to Avoid

1. Forgetting runtime permissions (Android 6.0+ needs `requestPermissions()`)
2. Not unregistering location listeners in `onPause()`, causing battery drain
3. Storing raw GPS data without SQLite transactions, risking data corruption
4. Assuming SMS is immediately sent - always implement `PendingIntent` callbacks

## Revision Tips

1. Practice writing permission requests:

```xml
<uses-permission android:name="android.permission.SEND_SMS"/>
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
```

2. Memorize key classes: `SmsManager`, `LocationManager`, `Geocoder`, `FusedLocationProviderClient`
3. Diagram the SMS sending process: Composition → Permission Check → SmsManager → Delivery Report
4. Study use cases: Uber-like apps (SMS ETA + live location tracking), emergency broadcast systems
