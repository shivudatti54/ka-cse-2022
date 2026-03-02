# LocationReminder Case Study - Summary

## Key Definitions

- **Entity**: In Room database, an annotated class that represents a table in the SQLite database
- **DAO (Data Access Object)**: Interface containing methods for database CRUD operations, annotated with @DAO
- **Repository**: Design pattern that provides a clean API for data access, abstracting data sources
- **Geofencing**: Creating a virtual geographic boundary that triggers an action when a device enters or exits the area
- **LiveData**: Observable data holder class that respects the lifecycle of other app components

## Important Formulas

- **Distance Calculation**: `distanceTo(Location)` - calculates distance between two coordinates in meters
- **Geofence Radius**: Circular region defined by center (latitude, longitude) and radius in meters
- **Notification Trigger**: Occurs when device enters/exits defined geofence boundary

## Key Points

- The application demonstrates integration of SQLite, Location Services, Navigation, and SMS capabilities
- Room database simplifies SQLite operations through compile-time code generation
- MVVM architecture separates UI concerns from business logic effectively
- Geofencing API is more battery-efficient than continuous location monitoring
- Navigation Component provides type-safe argument passing through Safe Args
- Runtime permissions are required for location access and SMS on Android 6.0+
- ViewModel survives configuration changes, preserving UI state
- Repository pattern abstracts data sources, enabling easier testing

## Common Mistakes

1. **Forgetting Runtime Permissions**: Many students implement location functionality but forget that ACCESS_FINE_LOCATION requires runtime permission requests on Android 6.0+

2. **Memory Leaks**: Not properly handling Context references in LocationListener callbacks can cause memory leaks; always remove listeners in onDestroy()

3. **Battery Drain**: Using continuous GPS updates instead of Geofencing API for location-triggered events significantly drains battery

4. **Null Pointer Exceptions**: Failing to check if LiveData.getValue() returns null before accessing list elements

5. **Navigation Back Stack**: Not properly handling the back stack in Navigation Component can lead to unexpected app behavior when users press the back button