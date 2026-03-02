# Using Tomcat for Servlet Development - Summary

## Key Definitions and Concepts

- **Tomcat**: Open-source servlet container implementing Java Servlet, JSP, and WebSocket specifications.
- **WAR File**: Web Application Archive containing all web components (servlets, JSPs, config files).
- **web.xml**: Deployment descriptor mapping URLs to servlets and configuring application parameters.
- **Context Path**: URL namespace for web app (e.g., `http://localhost:8080/MyWebApp`).
- **Manager App**: Tomcat's web interface for deploying/undeploying applications without server restart.

## Important Formulas and Theorems

**1. Tomcat Directory Structure**

```bash
tomcat/
├── webapps/ (Deploy WAR files here)
├── conf/ (server.xml, context.xml)
├── logs/ (catalina.out for server logs)
└── work/ (compiled JSPs and temporary files)
```

**2. WAR File Creation Command**

```bash
jar -cvf MyWebApp.war *
```

**3. Default Servlet Mapping in web.xml**

```xml
<servlet-mapping>
    <servlet-name>MyServlet</servlet-name>
    <url-pattern>/myservlet</url-pattern>
</servlet-mapping>
```

## Key Points

1. Tomcat runs on **port 8080** by default (`http://localhost:8080`)
2. **Deployment Methods**:
   - Copy WAR file to `webapps/` directory
   - Use Manager App's HTML interface
   - Deploy via IDE integration (Eclipse/IntelliJ)
3. **Servlet Development Workflow**:
   - Write servlet → Compile to .class → Place in `WEB-INF/classes/`
   - Create web.xml → Build WAR → Deploy to Tomcat
4. **Essential Tomcat Configuration Files**:
   - `server.xml`: Main server configuration
   - `context.xml`: Shared configuration for all web apps
5. **Debugging Tools**:
   - Check `logs/catalina.out` for errors
   - Use `System.out.println()` for basic logging
6. **Security**:
   - Set `manager-gui` role in `tomcat-users.xml` for Manager App access
7. **JSP Compilation**: Tomcat auto-compiles JSPs to servlets in `work/` directory

## Common Mistakes to Avoid

1. **Port Conflicts**: Forgetting to stop Tomcat before restarting ("Address already in use" error)
2. **Incorrect WAR Structure**:
   - Placing servlet classes outside `WEB-INF/classes/`
   - Missing `web.xml` in `WEB-INF/`
3. **Permission Issues**:
   - Not setting execute permission on `*.sh` files (Linux/Mac)
   - Incorrect file ownership in Tomcat directories
4. **Caching Problems**:
   - Not clearing browser cache after servlet updates
   - Not deleting `work/` directory when JSP changes don't reflect

## Revision Tips

1. **Practice Deployment**:
   - Manually create a WAR file using command line
   - Deploy via both `webapps/` copy and Manager App
2. **Tomcat Documentation**:
   - Study `server.xml` and `web.xml` schema from Apache's official docs
3. **Exam Focus Areas**:
   - Memorize directory structure of Tomcat and web apps
   - Understand lifecycle: server start → deployment → request handling → undeployment
4. **Troubleshooting Drill**:
   - Simulate common errors (e.g., missing servlet mapping) and learn to read stack traces in catalina.out

**Exam Alert**: Frequently tested areas include WAR structure, deployment methods, and interpreting web.xml configurations. Always mention port numbers and directory paths precisely.
