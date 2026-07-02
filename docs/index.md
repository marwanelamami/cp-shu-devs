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

<iframe id="roadmap-iframe" src="roadmap.html" style="width:100%; height:650px; border:none; overflow:hidden; transition: height 0.2s ease-out;" scrolling="no"></iframe>

<script>
  window.addEventListener('message', function(e) {
    if (e.data && e.data.type === 'resize-roadmap') {
      const iframe = document.getElementById('roadmap-iframe');
      if (iframe) {
        iframe.style.height = e.data.height + 'px';
      }
    }
  });
</script>

---

## Training Methodology

To get the most out of this playbook:

1. **Follow the Roadmap**: Topics are ordered sequentially, building on top of previous concepts.
2. **Review Code Examples**: Check out the optimized templates for each topic.
3. **Practice**: Solve the linked problems at the end of each topic on platforms like Codeforces and CSES.
