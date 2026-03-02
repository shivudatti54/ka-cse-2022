# MVC Architecture Summary

## Core Components

- **Model**: Business logic and data management (JavaBeans, DAOs, Services)
- **View**: User interface rendering (JSP, HTML, JSON responses)
- **Controller**: Request handling and coordination (Servlets, Filter chains)

## Request Flow

1. HTTP Request → Controller Servlet
2. Controller invokes Model (business logic)
3. Model returns data to Controller
4. Controller forwards to View (JSP)
5. View renders HTML Response

## Key Principles

- **Separation of Concerns**: Each layer has distinct responsibilities
- **Independent Development**: Teams can work on separate layers
- **Testability**: Components can be unit tested in isolation
- **Reusability**: Models serve multiple views

## Implementation Technologies

- **Controller**: HttpServlet, @WebServlet annotations
- **Model**: Plain Old Java Objects (POJOs), DAO pattern
- **View**: JSP, JSTL, Expression Language (EL)

## Framework Evolution

Classical MVC (Servlets + JSP) → Spring MVC → RESTful Services

## Important Notes

- Controller should contain minimal logic (thin controller pattern)
- Model should be framework-agnostic for reusability
- View should only handle presentation, not business logic
- Forward vs Redirect: Forward maintains request scope; Redirect creates new request

## Assessment Focus

- Draw and explain the MVC flow diagram
- Identify components in a given code snippet
- Explain benefits of separation of concerns
- Compare forward() vs sendRedirect() methods