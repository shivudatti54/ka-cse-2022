# Android Architecture - Summary

## Key Definitions and Concepts

- Android Architecture: Structural design of an Android application defining component interactions and data flow
- MVC (Model-View-Controller): Traditional pattern where Activity handles both View and Controller responsibilities
- MVP (Model-View-Presenter): Pattern separating View and Presenter with communication through interfaces
- MVVM (Model-View-ViewModel): Modern pattern using ViewModel and LiveData for lifecycle-aware data handling
- Clean Architecture: Three-layer approach with Domain, Data, and Presentation layers following Dependency Rule
- Repository Pattern: Abstraction layer providing unified data access API from multiple sources

## Important Formulas and Theorems

- Dependency Rule: Dependencies in Clean Architecture only point inward toward the Domain layer
- Lifecycle Awareness: ViewModel survives configuration changes and LiveData only notifies active observers
- Separation of Concerns: Business logic, UI, and data operations must be in separate components

## Key Points

- MVC leads to bloated Activities as they handle both UI and business logic in Android
- MVP improves testability by using interfaces for View-Presenter communication
- MVVM is the recommended pattern for modern Android development with Jetpack components
- ViewModel holds UI-related data survives configuration changes like screen rotation
- LiveData is lifecycle-aware and automatically handles observer lifecycle
- Repository pattern abstracts multiple data sources (local database, network API)
- Clean Architecture ensures business logic is independent of frameworks
- Clean Architecture has three layers: Domain (inner), Data (middle), Presentation (outer)
- Use Cases in Domain layer encapsulate specific business rules
- Dependency Injection is commonly used to provide dependencies to classes

## Common Mistakes to Avoid

- Putting all code in Activity/Fragment classes without proper separation
- Ignoring lifecycle management leading to memory leaks with LiveData
- Confusing MVC implementation where Activity acts as both View and Controller
- Not using interfaces in MVP, making Presenter tightly coupled to specific Activity
- Breaking Dependency Rule by letting outer layers depend on inner layer details

## Revision Tips

- Create comparison charts between MVC, MVP, and MVVM focusing on responsibilities of each component
- Practice implementing MVVM with ViewModel and LiveData in small projects
- Remember that ViewModel should NOT hold references to Views to prevent memory leaks
- Focus on understanding why separation of concerns matters for testability and maintainability
- Review Android Jetpack documentation for latest best practices in architecture components