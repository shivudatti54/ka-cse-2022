# Android Architecture

## Introduction

Android Architecture refers to the structural design and organization of an Android application, defining how components interact, data flows, and business logic is separated from presentation layers. In mobile application development, a well-designed architecture is crucial for creating maintainable, scalable, and testable applications. Android, being an open-source operating system, provides a flexible framework that allows developers to implement various architectural patterns depending on the complexity and requirements of their applications.

The Android platform follows a component-based architecture where applications are built from reusable components like Activities, Services, Broadcast Receivers, and Content Providers. However, without a proper architectural pattern, applications can quickly become difficult to maintain as they grow in size. This has led to the widespread adoption of architectural patterns such as MVC (Model-View-Controller), MVP (Model-View-Presenter), and MVVM (Model-View-ViewModel) in Android development. Understanding these architectures is essential for any developer aiming to build professional-grade Android applications that can withstand the test of time and continuous feature additions.

Modern Android development has increasingly embraced Clean Architecture, which emphasizes the separation of concerns across multiple layers: the presentation layer, domain layer, and data layer. This approach ensures that business logic remains independent of UI frameworks and database implementations, making the codebase more robust and adaptable to changes. For University of Delhi's Computer Science curriculum, mastering Android architecture patterns is fundamental as it prepares students to develop enterprise-level mobile applications with proper code organization and industry-standard practices.

## Key Concepts

### MVC (Model-View-Controller) Architecture

MVC is one of the oldest and most widely used architectural patterns in software development. In the context of Android, the Model represents the data layer (including database and network operations), the View corresponds to the XML layouts and UI components, and the Controller is typically the Activity or Fragment that handles user interactions. The Activity acts as both the controller and view, making it responsible for updating the UI and handling user events. While MVC provides a straightforward separation, Android's implementation often leads to Activities becoming bloated with too many responsibilities, making the code harder to test and maintain.

The Model component encapsulates the application's data and business logic. It includes data classes, repositories, and data sources such as SQLite databases or network APIs. The View is responsible for rendering the user interface and displaying data received from the Controller. In Android, Views are implemented through XML layouts or programmatically created UI elements. The Controller acts as an intermediary between the Model and the View, processing user input and updating the Model accordingly. When the Model changes, the Controller updates the View to reflect those changes.

### MVP (Model-View-Presenter) Architecture

MVP addresses some of the shortcomings of MVC by introducing a clear separation between the View and the business logic. In this pattern, the View is passive and only displays data, while the Presenter handles all user interactions and business logic. The Model in MVP remains similar to MVC, representing the data layer. The key difference is that the Presenter communicates with the View through an interface, which makes the View easily mockable for unit testing.

The View interface in MVP defines methods for updating the UI, such as showData() or showError(). The Activity or Fragment implements this interface, while the Presenter holds a reference to the View and calls these methods to update the UI. This separation ensures that the Presenter is completely independent of Android-specific classes, making it highly testable through unit tests. However, the Presenter still needs to handle the lifecycle of the View, which can lead to memory leak issues if not managed properly. Despite this limitation, MVP has been a popular choice for Android development, especially in applications where thorough unit testing is crucial.

### MVVM (Model-View-ViewModel) Architecture

MVVM has become the preferred architectural pattern for modern Android development, especially with the introduction of Jetpack components like ViewModel and LiveData. In MVVM, the ViewModel acts as a bridge between the View and the Model, holding and managing UI-related data in a lifecycle-conscious way. The ViewModel survives configuration changes like screen rotations, ensuring that data is not lost during such events. This significantly reduces the burden on the Activity or Fragment, which only needs to observe data changes from the ViewModel.

The ViewModel class is designed to store and manage UI-related data in a lifecycle-conscious manner. It allows data to survive configuration changes such as screen rotations, preventing data loss and unnecessary network calls. LiveData is an observable data holder that respects the lifecycle of other app components, updating only those observers that are in an active state. This combination of ViewModel and LiveData provides a robust foundation for building reactive Android applications. The Repository pattern is often used alongside MVVM to abstract data sources, providing a clean API for data access to the rest of the application.

### Clean Architecture

Clean Architecture represents the most comprehensive approach to structuring Android applications, emphasizing strict separation of concerns across three distinct layers. The innermost layer is the Domain layer, which contains business logic and use cases, independent of any external frameworks. The middle layer is the Data layer, which implements the interfaces defined in the domain layer and handles data sources like databases and network APIs. The outermost layer is the Presentation layer, which includes Activities, Fragments, ViewModels, and UI components.

The Dependency Rule is fundamental to Clean Architecture, stating that dependencies can only point inward. Inner layers have no knowledge of outer layers, meaning that business logic should not depend on UI frameworks or database implementations. This allows developers to change implementations in outer layers without affecting the core business logic. Use cases in the domain layer encapsulate specific business rules, making the application more maintainable and testable. Clean Architecture also facilitates parallel development, where different team members can work on different layers simultaneously without interfering with each other's work.

## Examples

### Example 1: Implementing MVVM with ViewModel and LiveData

Consider a simple login application where users enter their credentials to authenticate. In MVVM, the ViewModel would handle the authentication logic and expose the result through LiveData.

First, create the ViewModel class:
```java
public class LoginViewModel extends ViewModel {
    private MutableLiveData<LoginResult> loginResult = new MutableLiveData<>();
    private MutableLiveData<Boolean> isLoading = new MutableLiveData<>(false);
    
    public void login(String username, String password) {
        isLoading.setValue(true);
        // Perform authentication (typically via Repository)
        // Simulating network call
        new Handler().postDelayed(() -> {
            isLoading.setValue(false);
            if (validateCredentials(username, password)) {
                loginResult.setValue(new LoginResult(true, "Login Successful"));
            } else {
                loginResult.setValue(new LoginResult(false, "Invalid credentials"));
            }
        }, 2000);
    }
    
    private boolean validateCredentials(String username, String password) {
        return !username.isEmpty() && !password.isEmpty() && password.length() >= 6;
    }
    
    public LiveData<LoginResult> getLoginResult() {
        return loginResult;
    }
    
    public LiveData<Boolean> getIsLoading() {
        return isLoading;
    }
}
```

In the Activity, observe these LiveData objects:
```java
public class LoginActivity extends AppCompatActivity {
    private LoginViewModel viewModel;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        
        viewModel = new ViewModelProvider(this).get(LoginViewModel.class);
        
        viewModel.getLoginResult().observe(this, result -> {
            Toast.makeText(this, result.getMessage(), Toast.LENGTH_SHORT).show();
        });
        
        viewModel.getIsLoading().observe(this, isLoading -> {
            // Show/hide progress indicator
        });
        
        findViewById(R.id.btnLogin).setOnClickListener(v -> {
            String username = ((EditText)findViewById(R.id.etUsername)).getText().toString();
            String password = ((EditText)findViewById(R.id.etPassword)).getText().toString();
            viewModel.login(username, password);
        });
    }
}
```

### Example 2: Repository Pattern Implementation

The Repository pattern provides a clean abstraction over data sources. Here's how to implement it:

```java
// Domain Layer - Interface defining data operations
public interface UserRepository {
    void getUser(int userId, Callback<User> callback);
    void saveUser(User user);
}

// Data Layer - Implementation
public class UserRepositoryImpl implements UserRepository {
    private final LocalDataSource localDataSource;
    private final RemoteDataSource remoteDataSource;
    
    public UserRepositoryImpl(LocalDataSource local, RemoteDataSource remote) {
        this.localDataSource = local;
        this.remoteDataSource = remote;
    }
    
    @Override
    public void getUser(int userId, Callback<User> callback) {
        // First check local cache
        User cachedUser = localDataSource.getUser(userId);
        if (cachedUser != null) {
            callback.onSuccess(cachedUser);
            return;
        }
        
        // If not in cache, fetch from remote
        remoteDataSource.getUser(userId, new Callback<User>() {
            @Override
            public void onSuccess(User user) {
                localDataSource.saveUser(user); // Cache for future
                callback.onSuccess(user);
            }
            
            @Override
            public void onError(Exception e) {
                callback.onError(e);
            }
        });
    }
    
    @Override
    public void saveUser(User user) {
        localDataSource.saveUser(user);
    }
}
```

### Example 3: MVP Contract Interface

Defining clear contracts makes MVP implementation cleaner:

```java
// Contract defining View and Presenter interfaces
public interface LoginContract {
    interface View {
        void showLoading();
        void hideLoading();
        void showError(String message);
        void navigateToHome();
    }
    
    interface Presenter {
        void attachView(View view);
        void detachView();
        void login(String username, String password);
    }
}

// Presenter Implementation
public class LoginPresenter implements LoginContract.Presenter {
    private LoginContract.View view;
    private UserRepository userRepository;
    
    public LoginPresenter(UserRepository repository) {
        this.userRepository = repository;
    }
    
    @Override
    public void attachView(LoginContract.View view) {
        this.view = view;
    }
    
    @Override
    public void detachView() {
        this.view = null;
    }
    
    @Override
    public void login(String username, String password) {
        if (view == null) return;
        
        if (username.isEmpty() || password.isEmpty()) {
            view.showError("Please enter username and password");
            return;
        }
        
        view.showLoading();
        
        userRepository.login(username, password, new Callback<LoginResponse>() {
            @Override
            public void onSuccess(LoginResponse response) {
                if (view != null) {
                    view.hideLoading();
                    view.navigateToHome();
                }
            }
            
            @Override
            public void onError(Exception e) {
                if (view != null) {
                    view.hideLoading();
                    view.showError(e.getMessage());
                }
            }
        });
    }
}
```

## Exam Tips

1. UNDERSTAND THE DIFFERENCES: For exam questions, clearly distinguish between MVC, MVP, and MVVM. Remember that in MVC the Activity handles both View and Controller responsibilities, while in MVP and MVVM these are separated into distinct classes.

2. KNOW THE ROLE OF VIEWMODEL: The ViewModel survives configuration changes, which is a crucial point. It holds UI-related data and communicates with the View through LiveData or other observable data holders.

3. CLEAN ARCHITECTURE LAYERS: Remember the three layers of Clean Architecture - Domain (innermost), Data (middle), and Presentation (outermost). The Dependency Rule states that dependencies only point inward.

4. REPOSITORY PATTERN: Understand that the Repository provides a clean API for data access, abstracting the complexity of multiple data sources (local and remote).

5. LIVE DATA CHARACTERISTICS: LiveData is lifecycle-aware and only updates observers in active states. It automatically handles lifecycle changes, reducing memory leaks.

6. PRESENTER VS VIEWMODEL: In MVP, the Presenter directly manipulates the View through an interface. In MVVM, the ViewModel exposes data that the View observes passively.

7. TESTABILITY: MVVM and MVP are more testable than MVC because business logic is separated from Android framework classes. Unit tests can be written without Android dependencies.

8. REAL-WORLD APPLICATIONS: Be prepared to explain with examples where each architecture would be preferred - small projects may use MVC, medium projects benefit from MVP, and large enterprise applications should use Clean Architecture with MVVM.