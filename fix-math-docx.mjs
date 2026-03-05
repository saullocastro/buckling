const fixMathForDocxTransform = {
  name: 'fix-math-for-docx',
  doc: 'Strip \\nonumber from math nodes for DOCX builds (Word uses equation* by default).',
  stage: 'document',
  plugin: (opts, utils) => (tree, vfile) => {
    if (!process.argv.includes('--docx')) return;

    const mathNodes = utils.selectAll('math', tree);
    for (const node of mathNodes) {
      if (!node.value) continue;
      node.value = node.value.replace(/\\nonumber\s*/g, '').trim();
    }

    const inlineMathNodes = utils.selectAll('inlineMath', tree);
    for (const node of inlineMathNodes) {
      if (!node.value) continue;
      node.value = node.value.replace(/\\nonumber\s*/g, '').trim();
    }
  }
};

const plugin = {
  name: 'Fix Math for DOCX Plugin',
  transforms: [fixMathForDocxTransform]
};

export default plugin;
