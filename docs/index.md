# CP Playbook

A competitive programming training resource created for LCPC preparation and broader CP growth, maintained by the SHU Developers Club community.

---

## Welcome

Welcome to the official CP Playbook. Here you will find structured topic notes, code implementations, complexity analysis, and curated practice problems designed to help you prepare for competitive programming contests.

## Topic Roadmap

<iframe id="roadmap-iframe" src="topics/basics/images/cp-roadmap.svg" width="100%" height="700" style="border: none; overflow: hidden; background: transparent;"></iframe>
<script>
  window.addEventListener('message', function(e) {
    if (e.data && e.data.type === 'resize') {
      const iframe = document.getElementById('roadmap-iframe');
      if (iframe) {
        iframe.style.height = e.data.height + 'px';
      }
    }
  });
</script>

## Getting Started

To get the most out of this handbook:
1. **Follow the Roadmap**: Topics are ordered sequentially, building on top of previous concepts.
2. **Review Code Examples**: Check out the optimized Python templates for each topic.
3. **Practice**: Solve the linked problems at the end of each topic on platforms like Codeforces and CSES.
