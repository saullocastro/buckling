import { existsSync } from 'fs';
import { join, dirname, relative } from 'path';

function getPreferredExtension() {
  const args = process.argv;
  const hasTypst = args.includes('--typst');
  const hasPdf = args.includes('--pdf');
  const hasDocx = args.includes('--docx');
  const hasHtml = args.includes('--html');

  if (hasDocx) return '.jpg';
  if (hasTypst) return '.pdf';
  if (hasPdf) return '.pdf';
  if (hasHtml) return '.svg'; 
  // Default fallback
  throw new Error('No valid build target specified. Please use --typst, --pdf, --docx, or --html.');    
}

const resolveWildcardTransform = {
  name: 'resolve-wildcard-images',
  doc: 'Replace .* wildcards in image paths based on the build target.',
  stage: 'document',
  plugin: (opts, utils) => (tree, vfile) => {
    const images = utils.selectAll('image', tree);
    const cwd = process.cwd();
    const vfileDir = vfile.path ? dirname(vfile.path) : cwd;
    const dirs = [vfileDir, join(cwd, 'content')];
    const ext = getPreferredExtension();

    for (const node of images) {
      if (!node.url || !node.url.endsWith('.*')) continue;
      const base = node.url.slice(0, -2); // strip .*
      for (const dir of dirs) {
          const candidate = join(dir, base + ext);
          if (existsSync(candidate)) {
            node.url = relative(vfileDir, candidate);
            break;
          }
        }
    }
  }
};

const plugin = {
  name: 'Resolve Wildcard Images Plugin',
  transforms: [resolveWildcardTransform]
};

export default plugin;
