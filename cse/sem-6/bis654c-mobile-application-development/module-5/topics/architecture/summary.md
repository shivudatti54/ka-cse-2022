# Android App Architecture

## Overview

Modern Android architecture separates concerns using patterns like MVVM (Model-View-ViewModel) and components like ViewModel, LiveData, and Repository. Clean architecture improves testability, maintainability, and scalability.

## Key Points

- **MVVM Pattern**: Model (data), View (UI), ViewModel (logic/state)
- **ViewModel**: Survives configuration changes, holds UI state and business logic
- **LiveData**: Observable data holder with lifecycle awareness
- **Repository Pattern**: Single source of truth abstracting data sources
- **Data Layer**: Room database, network APIs, SharedPreferences
- **Dependency Injection**: Hilt or Dagger for managing object creation

## Important Concepts

- Separation of concerns improves testability
- ViewModels survive rotation but not process death
- LiveData only updates active observers
- Repository mediates between ViewModels and data sources
- Single Activity architecture with Navigation Component

## Notes

- Never pass Context or View references to ViewModel
- Observe LiveData only in UI layer (Activity/Fragment)
- Use Repository for data abstraction
- Implement offline-first architecture with Room + network
