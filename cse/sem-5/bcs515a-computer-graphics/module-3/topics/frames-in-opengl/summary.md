# Frames in OpenGL - Summary

## Key Definitions and Concepts

- **Framebuffer Object (FBO)**: An off-screen rendering target that stores rendered pixels in attachments (textures or renderbuffers) instead of the visible screen.
- **Renderbuffer**: A buffer object optimized for rendering that cannot be sampled by shaders but provides efficient storage for depth and stencil data.
- **Double Buffering**: Technique using front and back buffers to ensure smooth frame display without visual artifacts.
- **Framebuffer Completeness**: Status check ensuring an FBO is properly configured before rendering operations.
- **Multiple Render Targets (MRT)**: Ability to render to multiple color attachments simultaneously.

## Important Formulas and Theorems

- FBO creation: glGenFramebuffers(1, &fbo); glBindFramebuffer(GL_FRAMEBUFFER, fbo);
- Completeness check: glCheckFramebufferStatus(GL_FRAMEBUFFER) == GL_FRAMEBUFFER_COMPLETE
- Texture attachment: glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, texture, 0);
- Renderbuffer attachment: glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, rbo);

## Key Points

- FBOs enable off-screen rendering essential for post-processing effects, shadow mapping, and deferred rendering.
- Renderbuffers are faster for depth/stencil storage but cannot be read as textures.
- Always check framebuffer completeness after FBO setup before rendering.
- Double buffering prevents screen tearing by displaying only complete frames.
- MRT requires glDrawBuffers to specify multiple color attachment points.
- Textures attached to FBOs can be sampled in subsequent rendering passes.
- The default framebuffer is provided by the window system; FBOs are user-created.

## Common Mistakes to Avoid

1. Forgetting to check framebuffer completeness before rendering, leading to undefined behavior.
2. Using renderbuffers when you need to read the rendered data as a texture.
3. Not setting glViewport to FBO dimensions when rendering to off-screen buffers.
4. Mismatching attachment dimensions - all attachments must have the same width and height.
5. Not unbinding FBOs before rendering to the screen, resulting in invisible output.

## Revision Tips

1. Practice creating complete FBOs with both color texture and depth renderbuffer attachments.
2. Remember the attachment point enums: GL_COLOR_ATTACHMENT0, GL_DEPTH_ATTACHMENT, GL_STENCIL_ATTACHMENT.
3. Review the framebuffer completeness requirements checklist before exams.
4. Understand when to use renderbuffers (depth/stencil) vs textures (need to sample later).
