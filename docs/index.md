---
hide:
  - navigation
  - toc
---

# CP Playbook

Welcome to the CP Playbook, a structured curriculum and collection of training resources maintained by the SHU Developers Club. This handbook provides organized notes, optimized code implementations, complexity analysis, and curated practice tasks to help you prepare for competitive programming contests, including LCPC and ICPC.

---

## Interactive Syllabus Roadmap

Use the accordion menu below to explore the topics in sequence. Click on any active category or subcategory to expand it, and click on any topic to go directly to its guidebook notes.

<div id="roadmap-container"></div>

<script>
  (function() {
    var container = document.getElementById('roadmap-container');
    if (!container) return;

    fetch('roadmap.html')
      .then(function(r) { return r.text(); })
      .then(function(html) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');

        // Inject the <style> block from roadmap.html into document <head>
        var styleEls = doc.querySelectorAll('style');
        styleEls.forEach(function(s) {
          var style = document.createElement('style');
          style.textContent = s.textContent;
          document.head.appendChild(style);
        });

        // Inject the body HTML (the rm-container div) into the placeholder
        var body = doc.querySelector('body');
        if (body) {
          container.innerHTML = body.innerHTML;
        }

        // Re-execute any <script> tags that were inside roadmap.html body
        var scripts = container.querySelectorAll('script');
        scripts.forEach(function(oldScript) {
          var newScript = document.createElement('script');
          newScript.textContent = oldScript.textContent;
          oldScript.parentNode.replaceChild(newScript, oldScript);
        });
      })
      .catch(function(err) {
        console.error('Failed to load roadmap:', err);
      });
  })();
</script>

---

## Training Methodology

To get the most out of this playbook:

1. **Follow the Roadmap**: Topics are ordered sequentially, building on top of previous concepts.
2. **Review Code Examples**: Check out the optimized templates for each topic.
3. **Practice**: Solve the linked problems at the end of each topic on platforms like Codeforces and CSES.
