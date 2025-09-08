#!/usr/bin/env node
/**
 * Build script for Ge-ez website
 * Generates static HTML from markdown documentation
 */

const fs = require('fs');
const path = require('path');
const { marked } = require('marked');

// Configure marked for syntax highlighting
marked.setOptions({
  highlight: function(code, lang) {
    if (lang === 'amharic' || lang === 'geez') {
      return `<pre><code class="language-amharic">${code}</code></pre>`;
    }
    return `<pre><code class="language-${lang}">${code}</code></pre>`;
  },
  breaks: true,
  gfm: true
});

// Create public directory
if (!fs.existsSync('public')) {
  fs.mkdirSync('public');
}

// Copy static assets
const staticFiles = ['amharic-alphabet.png'];
staticFiles.forEach(file => {
  if (fs.existsSync(file)) {
    fs.copyFileSync(file, path.join('public', file));
  }
});

// Read and process markdown files
const docsDir = 'docs';
const publicDir = 'public';

function processMarkdown(filePath, outputPath) {
  if (fs.existsSync(filePath)) {
    const content = fs.readFileSync(filePath, 'utf8');
    const html = marked(content);
    
    // Wrap in HTML template
    const fullHtml = generateHtmlTemplate(html, getTitleFromContent(content));
    
    fs.writeFileSync(outputPath, fullHtml);
    console.log(`Generated: ${outputPath}`);
  }
}

function getTitleFromContent(content) {
  const titleMatch = content.match(/^#\s+(.+)$/m);
  return titleMatch ? titleMatch[1] : 'Ge-ez Documentation';
}

function generateHtmlTemplate(content, title) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} - Ge-ez (ግእዝ)</title>
    <meta name="description" content="Ge-ez (ግእዝ) - The world's first complete Amharic programming language">
    <meta name="keywords" content="amharic, programming, language, ethiopia, geez">
    
    <!-- Open Graph -->
    <meta property="og:title" content="${title} - Ge-ez (ግእዝ)">
    <meta property="og:description" content="The world's first complete Amharic programming language">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://geez-lang.vercel.app">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="${title} - Ge-ez (ግእዝ)">
    <meta name="twitter:description" content="The world's first complete Amharic programming language">
    
    <!-- Styles -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 30px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        
        .logo {
            font-size: 3rem;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 10px;
        }
        
        .tagline {
            font-size: 1.2rem;
            color: #666;
            margin-bottom: 20px;
        }
        
        .nav {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }
        
        .nav a {
            color: #667eea;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 25px;
            background: rgba(102, 126, 234, 0.1);
            transition: all 0.3s ease;
        }
        
        .nav a:hover {
            background: #667eea;
            color: white;
            transform: translateY(-2px);
        }
        
        .content {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }
        
        .content h1 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 2.5rem;
        }
        
        .content h2 {
            color: #764ba2;
            margin: 30px 0 15px 0;
            font-size: 1.8rem;
        }
        
        .content h3 {
            color: #667eea;
            margin: 25px 0 10px 0;
            font-size: 1.4rem;
        }
        
        .content p {
            margin-bottom: 15px;
            font-size: 1.1rem;
        }
        
        .content code {
            background: #f8f9fa;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Monaco', 'Menlo', monospace;
            color: #e83e8c;
        }
        
        .content pre {
            background: #2d3748;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 10px;
            overflow-x: auto;
            margin: 20px 0;
        }
        
        .content pre code {
            background: none;
            padding: 0;
            color: inherit;
        }
        
        .content ul, .content ol {
            margin: 15px 0 15px 30px;
        }
        
        .content li {
            margin-bottom: 8px;
        }
        
        .content blockquote {
            border-left: 4px solid #667eea;
            padding-left: 20px;
            margin: 20px 0;
            font-style: italic;
            color: #666;
        }
        
        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: rgba(255, 255, 255, 0.8);
        }
        
        .try-button {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 30px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: 600;
            margin: 20px 0;
            transition: all 0.3s ease;
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }
        
        .try-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            
            .header, .content {
                padding: 20px;
            }
            
            .logo {
                font-size: 2rem;
            }
            
            .nav {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">Ge-ez (ግእዝ)</div>
            <div class="tagline">The world's first complete Amharic programming language</div>
            <nav class="nav">
                <a href="/">Home</a>
                <a href="/getting-started.html">Getting Started</a>
                <a href="/language-reference.html">Language Reference</a>
                <a href="/examples.html">Examples</a>
                <a href="/installation.html">Installation</a>
                <a href="https://github.com/Mightyshambel/Ge-ez" target="_blank">GitHub</a>
            </nav>
        </div>
        
        <div class="content">
            ${content}
        </div>
        
        <div class="footer">
            <p>Made with ❤️ for the Amharic-speaking programming community</p>
            <p>© 2024 Ge-ez (ግእዝ) - All rights reserved</p>
        </div>
    </div>
    
    <!-- Syntax highlighting -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
</body>
</html>`;
}

// Process main documentation files
const docsToProcess = [
  { input: 'README.md', output: 'index.html' },
  { input: 'docs/getting-started.md', output: 'getting-started.html' },
  { input: 'docs/language-reference.md', output: 'language-reference.html' },
  { input: 'docs/examples-showcase.md', output: 'examples.html' },
  { input: 'docs/installation.md', output: 'installation.html' }
];

docsToProcess.forEach(({ input, output }) => {
  processMarkdown(input, path.join(publicDir, output));
});

console.log('✅ Website build completed successfully!');
console.log('📁 Static files generated in ./public/');
console.log('🚀 Ready for Vercel deployment!');
