---
name: blogger-html-post-writer
description: >
  Generates complete, production-ready Blogger HTML posts using a unified
  design template aligned with Google Search Essentials. Use when the user asks
  to write, draft, or create a blog post, article, or tutorial for Blogger.
  Outputs a self-contained HTML block (no <html>/<body> wrappers) with content,
  optional code blocks with copy buttons, a Table of Contents, callout boxes,
  step badges, inline terminals, data tables, syntax highlighting via Prism.js,
  and all CSS bundled at the bottom inside a <style> tag. Always use the
  antinna-blog-container design system, and adhere strictly to Google Search
  Essentials guidelines (helpfulness, E-E-A-T, semantic headers, descriptive links,
  image alt text, and anti-spam protocols).
---

# Blogger HTML Post Writer Skill

## Overview

This skill generates **complete, self-contained Blogger post HTML** — the kind you paste directly into Blogger's HTML editor. The output is a single block of HTML optimized to conform strictly with **Google Search Essentials (formerly Google Webmaster Guidelines)**.

The generated output is structured as follows:
1. **Hero banner image** (Blogger CDN `<div class="separator">` pattern with descriptive SEO alt text)
2. **Lead paragraph** (a brief, compelling, helpful intro demonstrating expertise)
3. **Optional badges** (npm, GitHub, etc., for open-source verification)
4. **Callout boxes** (success / warning / info variants)
5. **Table of Contents (TOC)** with smooth-scroll semantic anchors
6. **Sectioned content** with logical `<h2>` and `<h3>` heading hierarchies (no skipping levels)
7. **Mac-style code windows** with Prism.js syntax highlighting + Copy button (fully HTML-escaped)
8. **Inline terminal snippets**, ordered / unordered lists, data tables
9. **Closing scripts** (Prism.js loader + copy-button JS)
10. **All CSS** bundled inside a `<style>` block at the very end

---

## CRITICAL GOOGLE SEARCH ESSENTIALS RULES

To guarantee that all generated content is highly eligible for crawling, indexing, and ranking in Google Search, you MUST enforce the following guidelines:

### 1. High-Quality, Helpful, People-First Content (E-E-A-T)
- **Experience & Expertise:** Write in an authoritative, technical, and precise voice. Do not write generic or shallow articles. Back explanations with deep architectural insights, design patterns, and platform-specific edge cases.
- **Completeness:** Code examples must be fully functional and complete. Do not truncate essential files with `// ...` placeholder comments unless absolutely redundant. Give readers self-contained solutions.
- **Originality:** Avoid repeating content verbatim or generating thin pages. Provide original comparative analyses, visual diagrams (tables), and real-world troubleshooting steps.

### 2. Descriptive Hyperlinks (Anchor Text)
- **Descriptive Anchors:** Never use generic or low-value link phrases such as "click here", "link", "source", "website", or the raw URL itself.
- **Contextual Anchors:** Use descriptive anchor text that explains exactly what the destination page contains.
  - *Bad:* `Check out the code <a href="...">here</a>.`
  - *Good:* `Explore the custom styles implementation on the <a href="..." target="_blank">react-i18n vanilla branch</a>.`

### 3. Accessible & Contextual Images
- **Descriptive Alt Attributes:** Every image must contain a highly descriptive, contextual `alt` attribute that explains the image content to search crawlers and screen readers. Do not leave the `alt` tag empty or generic.
  - *Bad:* `alt="Banner"` or `alt="image"`
  - *Good:* `alt="Complete React zero-dependency localization dashboard displaying English, Hindi, and RTL Arabic bidi translations"`
- **Responsive Sizing:** Ensure image elements contain explicit width and height metadata attributes and are fully responsive via CSS.

### 4. Semantic Header Hierarchies
- **Sequential Headings:** Maintain a clean, logical heading hierarchy. Use `<h2>` for main sections, `<h3>` for subsections, and `<h4>` for granular definitions. Never skip heading levels (e.g. going from `<h2>` directly to `<h4>`).
- **Indexable Headings:** Every heading should have an explicit, unique, and descriptive `id` attribute matching the Table of Contents anchor links.

### 5. Spam Prevention & Visibility
- **No Hidden Content:** All text and code must be completely visible and readable. Never use microscopic fonts, colors that blend with the background, or hidden CSS styles.
- **No Keyword Stuffing:** Use technical terms and code keyword definitions naturally in context. Do not stuff titles, headers, or metadata block fields with redundant variations of keywords.

---

## TECHNICAL CODING & STRUCTURE RULES

- **NEVER** output `<html>`, `<head>`, or `<body>` tags. Blogger posts are HTML fragments.
- **ALWAYS** put the `<style>` block at the **very end** of the output, after all content and scripts.
- **ALWAYS** put `<script>` blocks just before the `<style>` block (after content).
- **ALWAYS** generate the full CSS — never say "add CSS here" or truncate it.
- **ALWAYS** include the complete Table of Contents with working `href="#section-id"` anchors.
- **ALWAYS** use `!important` on all CSS rules to defeat Blogger's theme styles.
- Use **Prism.js** from the CDN for code syntax highlighting (loaded dynamically via JS).
- The primary design system class is `.antinna-blog-container`.
- When code blocks are present, always include the Copy button and the corresponding JS.

---

## HTML Structure Template

Use the following structure for every post. Fill in the placeholders.

```html
<!-- BANNER IMAGE -->
<div class="separator" style="clear: both">
  <a
    href="FULL_IMAGE_URL"
    style="display: block; padding: 1em 0; text-align: center"
    ><img
      alt="DESCRIPTIVE_SEO_CONTEXT_EXPLAINING_IMAGE_CONTENT"
      border="0"
      data-original-height="HEIGHT"
      data-original-width="WIDTH"
      src="THUMBNAIL_IMAGE_URL"
  /></a>
</div>

<!-- OPTIONAL: NPM / GITHUB BADGES SECTION -->
<div style="display: flex; gap: 10px; margin-bottom: 25px; flex-wrap: wrap">
  <a href="NPM_URL" target="_blank">
    <img src="https://img.shields.io/npm/v/PACKAGE_NAME.svg?style=flat-square" alt="npm version" />
  </a>
  <!-- Add more badges as needed -->
</div>

<!-- MAIN CONTENT CONTAINER -->
<div class="antinna-blog-container">

  <!-- LEAD PARAGRAPH -->
  <p>LEAD_PARAGRAPH_TEXT</p>

  <!-- OPTIONAL CALLOUT (use type: success | warning | info) -->
  <div class="antinna-callout antinna-callout-success">
    <div class="antinna-callout-title">CALLOUT_TITLE</div>
    <p class="antinna-callout-body">CALLOUT_BODY_TEXT</p>
  </div>

  <hr class="antinna-divider" />

  <!-- TABLE OF CONTENTS -->
  <div class="antinna-toc">
    <h3>TABLE_OF_CONTENTS_TITLE</h3>
    <ul>
      <li><a href="#section-1">1. SECTION_ONE_TITLE</a></li>
      <li><a href="#section-2">2. SECTION_TWO_TITLE</a></li>
      <!-- ... -->
    </ul>
  </div>

  <hr class="antinna-divider" />

  <!-- SECTION HEADING WITH STEP BADGE -->
  <h2 id="section-1">
    <span class="antinna-step-badge">Step 1</span> SECTION_ONE_TITLE
  </h2>
  <p>SECTION_BODY_TEXT</p>

  <!-- CODE WINDOW (with Prism.js language class) -->
  <div class="antinna-code-wrapper">
    <div class="antinna-code-header">
      <div class="antinna-mac-dots">
        <span class="dot red"></span><span class="dot yellow"></span
        ><span class="dot green"></span>
      </div>
      <span class="antinna-code-title">FILENAME_OR_DESCRIPTION</span>
      <button class="antinna-copy-btn">Copy</button>
    </div>
    <pre><code class="language-LANG">CODE_HERE</code></pre>
  </div>

  <!-- INLINE TERMINAL SNIPPET (for short shell commands) -->
  <div class="antinna-inline-terminal">$ COMMAND_HERE</div>

  <!-- WARNING CALLOUT -->
  <div class="antinna-callout antinna-callout-warning">
    <div class="antinna-callout-title">⚠️ WARNING_TITLE</div>
    <p class="antinna-callout-body">WARNING_BODY</p>
  </div>

  <h2 id="section-2">
    <span class="antinna-step-badge">Step 2</span> SECTION_TWO_TITLE
  </h2>
  <p>...</p>

  <!-- DATA TABLE (when listing parameters, flags, comparisons) -->
  <div class="antinna-table-overflow">
    <table class="antinna-data-table">
      <thead>
        <tr>
          <th>COLUMN_1</th>
          <th>COLUMN_2</th>
          <th>COLUMN_3</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>VALUE</code></td>
          <td>DESCRIPTION</td>
          <td>NOTES</td>
        </tr>
      </tbody>
    </table>
  </div>

  <hr class="antinna-divider" />

  <!-- CLOSING SECTION (license, CTA, etc.) -->
  <h3>📄 CLOSING_SECTION_TITLE</h3>
  <p>CLOSING_TEXT</p>

</div>
<!-- END .antinna-blog-container -->

<!-- PRISM.JS SYNTAX HIGHLIGHTING (load ONLY the languages used in this post) -->
<link
  href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css"
  rel="stylesheet"
/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
<!-- Add language components as needed: -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-javascript.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-typescript.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-json.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-dart.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-kotlin.min.js"></script>

<!-- INTERACTIVE SCRIPTS: SMOOTH TOC SCROLL + COPY BUTTONS -->
<script>
  document.addEventListener("DOMContentLoaded", () => {
    // 1. Smooth Scrolling for Table of Contents
    const tocLinks = document.querySelectorAll(".antinna-toc a");
    tocLinks.forEach((link) => {
      link.addEventListener("click", function (e) {
        e.preventDefault();
        const targetId = this.getAttribute("href").substring(1);
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
          targetElement.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      });
    });

    // 2. Copy Button Functionality
    const copyButtons = document.querySelectorAll(".antinna-copy-btn");
    copyButtons.forEach((button) => {
      button.addEventListener("click", async () => {
        const container = button.closest(".antinna-code-wrapper");
        if (!container) return;
        const targetCodeBlock = container.querySelector("pre code");
        if (!targetCodeBlock) return;
        const codeContent = targetCodeBlock.innerText;
        try {
          await navigator.clipboard.writeText(codeContent);
          button.textContent = "Copied!";
          button.classList.add("copied");
          setTimeout(() => {
            button.textContent = "Copy";
            button.classList.remove("copied");
          }, 2000);
        } catch (err) {
          console.error("Failed to copy text contents:", err);
          button.textContent = "Error";
        }
      });
    });
  });
</script>

<!-- UNIFIED STYLESHEET (always placed at the very end) -->
<style>
  /* =============================================
     ANTINNA BLOGGER UNIFIED DESIGN SYSTEM v3
     All rules use !important to override Blogger themes
  ============================================= */

  html {
    scroll-behavior: smooth !important;
  }

  /* 1. Core Container */
  .antinna-blog-container {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
      Ubuntu, Cantarell, sans-serif !important;
    color: #2d3748 !important;
    line-height: 1.8 !important;
    max-width: 860px !important;
    margin: 0 auto !important;
    padding: 20px !important;
    -webkit-font-smoothing: antialiased !important;
  }

  /* 2. Typography */
  .antinna-blog-container h2 {
    color: #1a202c !important;
    font-size: 1.7rem !important;
    margin-top: 3rem !important;
    margin-bottom: 1.25rem !important;
    display: flex !important;
    align-items: center !important;
    border-bottom: 2px solid #edf2f7 !important;
    padding-bottom: 0.5rem !important;
    font-weight: 700 !important;
    scroll-margin-top: 90px !important;
  }
  .antinna-blog-container h3 {
    color: #2d3748 !important;
    font-size: 1.35rem !important;
    margin-top: 1.5rem !important;
    margin-bottom: 0.75rem !important;
    font-weight: 600 !important;
  }
  .antinna-blog-container p {
    margin-bottom: 1.5rem !important;
    font-size: 1.05rem !important;
  }
  .antinna-blog-container ul,
  .antinna-blog-container ol {
    margin-bottom: 1.5rem !important;
    padding-left: 1.5rem !important;
  }
  .antinna-blog-container li {
    margin-bottom: 0.75rem !important;
    font-size: 1.05rem !important;
  }
  .antinna-blog-container strong {
    color: #1a202c !important;
  }
  .antinna-blog-container a {
    color: #3182ce !important;
    text-decoration: none !important;
    font-weight: 500 !important;
    transition: color 0.2s ease !important;
  }
  .antinna-blog-container a:hover {
    color: #2b6cb0 !important;
    text-decoration: underline !important;
  }

  /* 3. Inline Code */
  .antinna-blog-container code:not(pre code) {
    background-color: #f7fafc !important;
    color: #dd6b20 !important;
    padding: 0.2rem 0.4rem !important;
    border-radius: 4px !important;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo,
      monospace !important;
    font-size: 0.9em !important;
    border: 1px solid #e2e8f0 !important;
  }

  /* 4. Dividers */
  .antinna-divider {
    border: 0 !important;
    border-top: 2px solid #edf2f7 !important;
    margin: 2.5rem 0 !important;
  }

  /* 5. Callout Boxes */
  .antinna-callout {
    padding: 1.5rem !important;
    border-radius: 8px !important;
    margin: 2rem 0 !important;
    border-left: 5px solid !important;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.03) !important;
  }
  .antinna-callout-success {
    background-color: #f0fff4 !important;
    border-color: #38a169 !important;
  }
  .antinna-callout-warning {
    background-color: #fffaf0 !important;
    border-color: #dd6b20 !important;
  }
  .antinna-callout-info {
    background-color: #ebf8ff !important;
    border-color: #3182ce !important;
  }
  .antinna-callout-title {
    font-weight: 700 !important;
    margin-bottom: 0.5rem !important;
    font-size: 1.1rem !important;
  }
  .antinna-callout-success .antinna-callout-title {
    color: #22543d !important;
  }
  .antinna-callout-warning .antinna-callout-title {
    color: #7b341e !important;
  }
  .antinna-callout-info .antinna-callout-title {
    color: #2b6cb0 !important;
  }
  .antinna-callout-body {
    font-size: 1rem !important;
    margin: 0 !important;
  }
  .antinna-callout-success .antinna-callout-body {
    color: #276749 !important;
  }
  .antinna-callout-warning .antinna-callout-body {
    color: #9c4221 !important;
  }
  .antinna-callout-info .antinna-callout-body {
    color: #2a69ac !important;
  }

  /* 6. Table of Contents */
  .antinna-toc {
    background: #f7fafc !important;
    padding: 1.5rem 2rem !important;
    border-radius: 8px !important;
    border: 1px solid #e2e8f0 !important;
  }
  .antinna-toc h3 {
    margin-top: 0 !important;
    font-size: 1.15rem !important;
  }
  .antinna-toc ul {
    list-style-type: none !important;
    padding-left: 0 !important;
    margin-bottom: 0 !important;
  }
  .antinna-toc li {
    margin-bottom: 0.5rem !important;
  }
  .antinna-toc a {
    color: #4a5568 !important;
    cursor: pointer !important;
    font-weight: 400 !important;
  }
  .antinna-toc a:hover {
    color: #3182ce !important;
  }

  /* 7. Step Badges */
  .antinna-step-badge {
    background: #3182ce !important;
    color: #fff !important;
    padding: 0.3rem 0.8rem !important;
    border-radius: 6px !important;
    font-size: 0.85rem !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    margin-right: 1rem !important;
    display: inline-block !important;
    box-shadow: 0 2px 4px rgba(49, 130, 206, 0.3) !important;
    white-space: nowrap !important;
  }
  .antinna-step-badge.danger {
    background: #e53e3e !important;
    box-shadow: 0 2px 4px rgba(229, 62, 62, 0.3) !important;
  }
  .antinna-step-badge.success {
    background: #38a169 !important;
    box-shadow: 0 2px 4px rgba(56, 161, 105, 0.3) !important;
  }

  /* 8. Mac-Style Code Windows */
  .antinna-code-wrapper {
    margin: 2rem 0 !important;
    background: #1d1f21 !important;
    border-radius: 10px !important;
    overflow: hidden !important;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.15),
      0 8px 10px -6px rgba(0, 0, 0, 0.08) !important;
  }
  .antinna-code-header {
    background: #282a2e !important;
    color: #a0aec0 !important;
    padding: 0.75rem 1.25rem !important;
    font-size: 0.85rem !important;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif !important;
    display: flex !important;
    align-items: center !important;
    border-bottom: 1px solid #111 !important;
  }
  .antinna-mac-dots {
    display: flex !important;
    gap: 6px !important;
    margin-right: 15px !important;
  }
  .antinna-mac-dots .dot {
    width: 12px !important;
    height: 12px !important;
    border-radius: 50% !important;
  }
  .antinna-mac-dots .red {
    background-color: #ff5f56 !important;
  }
  .antinna-mac-dots .yellow {
    background-color: #ffbd2e !important;
  }
  .antinna-mac-dots .green {
    background-color: #27c93f !important;
  }
  .antinna-code-title {
    flex-grow: 1 !important;
    font-weight: 500 !important;
    letter-spacing: 0.02em !important;
  }
  .antinna-copy-btn {
    background-color: #3f3f3f !important;
    border: 1px solid #555 !important;
    color: #cbd5e1 !important;
    padding: 4px 10px !important;
    border-radius: 5px !important;
    font-size: 0.72rem !important;
    cursor: pointer !important;
    margin-left: 14px !important;
    font-weight: 600 !important;
    font-family: inherit !important;
    transition: all 0.15s ease-in-out !important;
  }
  .antinna-copy-btn:hover {
    background-color: #4b5563 !important;
    color: #f8fafc !important;
    border-color: #6b7280 !important;
  }
  .antinna-copy-btn.copied {
    background-color: #059669 !important;
    border-color: #059669 !important;
    color: #ffffff !important;
  }

  /* 9. Prism.js Overrides (forces transparent bg to match our dark window) */
  .antinna-code-wrapper pre[class*="language-"] {
    margin: 0 !important;
    padding: 1.5rem !important;
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    box-shadow: none !important;
    text-shadow: none !important;
    overflow-x: auto !important;
  }
  .antinna-code-wrapper code[class*="language-"] {
    font-family: "SFMono-Regular", Consolas, Menlo, Monaco, monospace !important;
    font-size: 0.9rem !important;
    line-height: 1.6 !important;
    background: none !important;
    text-shadow: none !important;
  }
  /* Fallback for non-Prism code blocks */
  .antinna-code-wrapper pre {
    margin: 0 !important;
    padding: 1.5rem !important;
    overflow-x: auto !important;
  }
  .antinna-code-wrapper pre code {
    font-family: "SFMono-Regular", Consolas, Menlo, Monaco, monospace !important;
    font-size: 0.9rem !important;
    color: #e4e4e4 !important;
    line-height: 1.6 !important;
    background: none !important;
    padding: 0 !important;
    border: none !important;
  }

  /* 10. Inline Terminal Snippets */
  .antinna-inline-terminal {
    background-color: #0f172a !important;
    color: #38bdf8 !important;
    font-family: "Fira Code", "Cascadia Code", Consolas, monospace !important;
    padding: 8px 14px !important;
    border-radius: 6px !important;
    font-size: 0.88rem !important;
    display: block !important;
    width: max-content !important;
    max-width: 100% !important;
    margin: 10px 0 !important;
    border: 1px solid #1e293b !important;
    overflow-x: auto !important;
  }

  /* 11. Data Tables */
  .antinna-table-overflow {
    overflow-x: auto !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 10px !important;
    margin: 20px 0 !important;
  }
  .antinna-data-table {
    width: 100% !important;
    border-collapse: collapse !important;
    font-size: 0.88rem !important;
    text-align: left !important;
  }
  .antinna-data-table th {
    background: #f8fafc !important;
    font-weight: 600 !important;
    color: #1a202c !important;
    padding: 14px 16px !important;
    border-bottom: 2px solid #e2e8f0 !important;
  }
  .antinna-data-table td {
    padding: 14px 16px !important;
    border-bottom: 1px solid #e2e8f0 !important;
    vertical-align: top !important;
    color: #2d3748 !important;
  }
  .antinna-data-table tr:last-child td {
    border-bottom: none !important;
  }

  /* 12. Mobile Responsive Breakpoints */
  @media (max-width: 640px) {
    .antinna-blog-container {
      padding: 12px !important;
    }
    .antinna-blog-container h2 {
      font-size: 1.35rem !important;
    }
    .antinna-code-title {
      font-size: 0.75rem !important;
      white-space: nowrap !important;
      overflow: hidden !important;
      text-overflow: ellipsis !important;
      max-width: 120px !important;
    }
    .antinna-mac-dots {
      margin-right: 8px !important;
    }
    .antinna-toc {
      padding: 1rem !important;
    }
    .antinna-inline-terminal {
      width: 100% !important;
    }
  }
</style>
```

---

## Component Reference: All Available UI Blocks

### Banner Image
```html
<div class="separator" style="clear: both">
  <a href="FULL_URL" style="display: block; padding: 1em 0; text-align: center">
    <img alt="DESCRIPTIVE_SEO_CONTEXT_EXPLAINING_IMAGE_CONTENT" border="0" data-original-height="H" data-original-width="W" src="THUMBNAIL_URL" />
  </a>
</div>
```

### Lead Paragraph
```html
<p>LEAD_TEXT (compelling 2-3 sentence intro that hooks the reader and demonstrates real expertise)</p>
```

### Callout Variants
```html
<!-- Success / Architecture Strategy -->
<div class="antinna-callout antinna-callout-success">
  <div class="antinna-callout-title">✅ TITLE</div>
  <p class="antinna-callout-body">BODY</p>
</div>

<!-- Warning -->
<div class="antinna-callout antinna-callout-warning">
  <div class="antinna-callout-title">⚠️ TITLE</div>
  <p class="antinna-callout-body">BODY</p>
</div>

<!-- Info (blue) -->
<div class="antinna-callout antinna-callout-info">
  <div class="antinna-callout-title">ℹ️ TITLE</div>
  <p class="antinna-callout-body">BODY</p>
</div>
```

### Table of Contents
```html
<div class="antinna-toc">
  <h3>📖 Quick Navigation</h3>
  <ul>
    <li><a href="#section-id-1">1. Section Title</a></li>
    <li><a href="#section-id-2">2. Section Title</a></li>
  </ul>
</div>
```

### Section Heading with Step Badge
```html
<h2 id="section-id-1">
  <span class="antinna-step-badge">Step 1</span> Section Title
</h2>
```
Badge variants: default (blue), `class="danger"` (red), `class="success"` (green).
For non-step sections: `<span class="antinna-step-badge">Overview</span>`, `<span class="antinna-step-badge">Setup</span>`, `<span class="antinna-step-badge success">FAQ</span>`.

### Mac-Style Code Window
```html
<div class="antinna-code-wrapper">
  <div class="antinna-code-header">
    <div class="antinna-mac-dots">
      <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
    </div>
    <span class="antinna-code-title">📂 filename.ext OR Description</span>
    <button class="antinna-copy-btn">Copy</button>
  </div>
  <pre><code class="language-LANG">YOUR CODE HERE</code></pre>
</div>
```
Supported `language-LANG` values: `javascript`, `typescript`, `json`, `bash`, `dart`, `kotlin`, `text`, `css`, `html`, `python`, `java`.

### Inline Terminal (short commands)
```html
<div class="antinna-inline-terminal">$ npm install package-name</div>
```

### Data Table
```html
<div class="antinna-table-overflow">
  <table class="antinna-data-table">
    <thead>
      <tr><th>Flag</th><th>Syntax</th><th>Description</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><code>--flag</code></td>
        <td><code>command --flag=value</code></td>
        <td>What this flag does.</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Horizontal Divider
```html
<hr class="antinna-divider" />
```

### NPM / GitHub Badges (for open-source posts)
```html
<div style="display: flex; gap: 10px; margin-bottom: 25px; flex-wrap: wrap">
  <a href="NPM_URL" target="_blank">
    <img src="https://img.shields.io/npm/v/PACKAGE.svg?style=flat-square" alt="npm version" />
  </a>
  <a href="LICENSE_URL" target="_blank">
    <img src="https://img.shields.io/npm/l/PACKAGE.svg?style=flat-square" alt="license" />
  </a>
</div>
```

---

## Script Block (always include when code windows are present)

```html
<script>
  document.addEventListener("DOMContentLoaded", () => {
    // Smooth TOC scrolling
    document.querySelectorAll(".antinna-toc a").forEach((link) => {
      link.addEventListener("click", function (e) {
        e.preventDefault();
        const el = document.getElementById(this.getAttribute("href").substring(1));
        if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });

    // Copy button functionality
    document.querySelectorAll(".antinna-copy-btn").forEach((button) => {
      button.addEventListener("click", async () => {
        const code = button.closest(".antinna-code-wrapper")?.querySelector("pre code");
        if (!code) return;
        try {
          await navigator.clipboard.writeText(code.innerText);
          button.textContent = "Copied!";
          button.classList.add("copied");
          setTimeout(() => { button.textContent = "Copy"; button.classList.remove("copied"); }, 2000);
        } catch { button.textContent = "Error"; }
      });
    });
  });
</script>
```

---

## Prism.js Language Components CDN Reference

Always load only the languages actually used in the post.

| Language | Script URL Suffix |
|---|---|
| JavaScript | `components/prism-javascript.min.js` |
| TypeScript | `components/prism-typescript.min.js` |
| JSON | `components/prism-json.min.js` |
| Bash/Shell | `components/prism-bash.min.js` |
| Dart | `components/prism-dart.min.js` |
| Kotlin | `components/prism-kotlin.min.js` |
| CSS | `components/prism-css.min.js` |
| Python | `components/prism-python.min.js` |
| Java | `components/prism-java.min.js` |
| TOML | `components/prism-toml.min.js` |

Base URL: `https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/`
Theme CSS: `https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css`
Core JS: `https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js`

---

## Workflow: How to Write a Post

1. **Ask** the user for: post topic/title, sections to cover, code examples needed (optional — infer from context if obvious).
2. **Generate** the full HTML block using the structure above. Never truncate.
3. **Always** include:
   - TOC with anchors matching all `<h2 id="...">` headings
   - Prism.js `<link>` + correct `<script>` language components
   - Interactive JS block (TOC scroll + copy buttons)
   - The complete `<style>` block at the very end
4. **Code language classes**: always add `class="language-LANG"` to `<code>` for Prism to highlight them.
5. **HTML entities**: Inside `<pre><code>`, escape `<` as `&lt;`, `>` as `&gt;`, `&` as `&amp;` where the code contains literal HTML/XML. Inside template literal JS strings, use `&lt;` when the code block itself shows HTML examples (like in post 2's Blogger theme snippet).
6. **Output format**: Deliver the raw HTML directly in a code block. The user pastes it directly into Blogger's HTML editor.

---

## HTML Entity Escaping Inside Code Blocks

When the code snippet **itself contains HTML tags** (e.g., showing `<script>` tags as example code), you MUST HTML-encode them:

| Raw Character | Escaped |
|---|---|
| `<` | `&lt;` |
| `>` | `&gt;` |
| `&` | `&amp;` |

Example:
```html
<pre><code class="language-html">&lt;script&gt;
  console.log("hello");
&lt;/script&gt;</code></pre>
```

---

## Post Length & Depth Guidelines

- **Minimum sections**: 3 (intro, body sections, closing)
- **Typical post**: 5–10 `<h2>` sections
- **Code blocks**: Include complete, working code — never truncate with `// ...`
- **Paragraphs**: Write in an authoritative, technical voice. Use technical terminology accurately.
- **Lists**: Use `<ol>` for ordered steps, `<ul>` for feature lists and bullet points.
- Posts should be **self-contained** — a reader should be able to follow the guide without needing to look anything up for the core steps.
