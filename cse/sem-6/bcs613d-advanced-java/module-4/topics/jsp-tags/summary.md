# JSP Tags

## Overview

JSP provides various tag types for embedding Java code and controlling page behavior including scriptlet tags, declaration tags, expression tags, directive tags, and action tags. These tags enable separation of presentation and logic while maintaining dynamic content generation capabilities.

## Key Points

- **Scriptlet Tag**: <% Java statements %> for executable code
- **Declaration Tag**: <%! field/method declarations %> for class-level members
- **Expression Tag**: <%= expression %> for output evaluation
- **Directive Tag**: <%@ directive %> for page-level settings (page, include, taglib)
- **Action Tags**: <jsp:action> standard tags (include, forward, useBean)
- **Comment Tag**: <%-- JSP comment --%> not sent to client
- **JSTL Tags**: Custom tag libraries for common operations
- **Custom Tags**: User-defined tags for reusable functionality

## Important Concepts

- Scriptlets execute per request, declarations execute at page initialization
- Expressions automatically converted to String for output
- Page directive sets content type, imports, error pages
- Include directive for static inclusion at translation time
- jsp:include action for dynamic inclusion at request time

## Notes

- Remember syntax differences: <% %> scriptlet, <%= %> expression, <%! %> declaration
- For exams, know when to use each tag type
- Practice page directive with contentType and import attributes
