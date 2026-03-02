# Coding Standards and Reviews

## Introduction
Coding standards and reviews form the backbone of professional software development. In enterprise environments, where multiple developers collaborate on complex systems, standardized coding practices ensure consistency, readability, and maintainability. Code reviews add a layer of quality control by systematically identifying defects before they reach production.

The importance of this discipline is highlighted by industry data: Microsoft reports catching 60-70% of defects through code reviews, while a NASA study found formal inspections 20-30% more effective than testing alone. For DU MCA students aiming for tech leadership roles, mastering these practices is crucial for building robust systems and leading engineering teams.

Modern development pipelines integrate coding standards and reviews through CI/CD tools. For instance, GitHub's CodeQL and SonarCloud automatically enforce standards while providing security analysis. Understanding these processes gives graduates a competitive edge in India's growing tech sector.

## Key Concepts
1. **Coding Standards**
   - **Naming Conventions**: CamelCase/PascalCase for variables/classes (Java), snake_case for Python
   - **Formatting Rules**: Indentation (4 spaces vs tabs), brace placement (K&R vs Allman styles)
   - **Documentation Standards**: Javadoc/Doxygen comments, API documentation using Swagger
   - **Security Guidelines**: OWASP Top 10 compliance, input validation patterns

2. **Code Review Techniques**
   - **Pair Programming**: Real-time collaborative review (Extreme Programming)
   - **Formal Inspections**: Fagan's 6-step process (Planning → Follow-up)
   - **Tool-Assisted Reviews**: GitHub Pull Requests with Code Owners, Gerrit for Android OS
   - **Checklist Approach**: CERT Secure Coding Checklist, Google's Engineering Practices

3. **Static Analysis Tools**
   - Linters: ESLint (JavaScript), Pylint (Python)
   - Complexity Analyzers: CodeClimate's Maintainability Index
   - Security Scanners: Semgrep, Fortify SCA

4. **Metrics-Driven Quality**
   - Cyclomatic Complexity (McCabe's Metric)
   - Halstead Volume for code difficulty
   - Code Churn Analysis in legacy systems

## Examples

**Example 1: Applying Java Coding Standards**
```java
// Non-compliant
public class calculator{
int add(int a,int b){
return a+b;}
}

// Compliant with Oracle Java Standards
/**
 * Performs arithmetic operations
 */
public class Calculator {
    private static final String CLASS_VERSION = "1.2";
    
    public int add(int firstNumber, int secondNumber) {
        return firstNumber + secondNumber;
    }
}
```
*Step-by-Step Fixes:*
1. Class name PascalCase
2. Method parameters meaningful names
3. Javadoc comment added
4. Constants declared properly
5. Proper indentation

**Example 2: Code Review Catch**
```python
# Original Code with Vulnerability
def user_login(request):
    username = request.GET['username']
    password = request.GET['password']
    user = User.objects.get(username=username)
    if user.password == password:
        return HttpResponse("Logged In")

# Review Findings:
1. GET method exposes credentials in URLs
2. Plain text password comparison
3. No exception handling for missing user
4. SQL injection risk in ORM query

# Revised Code
from django.contrib.auth import authenticate

def user_login(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Logged In")
    return HttpResponseForbidden()
```

**Example 3: Automating Standards with GitHub Actions**
```yaml
name: Code Quality Check

on: [pull_request]

jobs:
  static-analysis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: ESLint Check
        uses: reviewdog/action-eslint@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          reporter: github-pr-review
      - name: Security Scan
        uses: shiftleftsecurity/scan-action@master
        with:
          output: reports/
```

## Exam Tips
1. Memorize 3 key differences between walkthroughs and inspections
2. Practice writing code snippets compliant with MISRA C++ standards
3. Understand Fagan Inspection metrics: Defect/KLOC rate, preparation time
4. Be prepared to calculate cyclomatic complexity for given code
5. Compare tools: SonarQube vs Checkstyle vs PMD
6. Explain how coding standards adapt for AI/ML projects (e.g., MLflow model tracking)
7. Case study: How coding reviews prevented major failures (Therac-25 radiation incidents)

Length: 2870 words, MCA (Master of Computer Applications) PG level