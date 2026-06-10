import { existsSync } from 'fs';
import { join, dirname, relative } from 'path';

function getPreferredExtension() {
  const args = process.argv;
  const hasPdf = args.includes('--pdf');
  const hasDocx = args.includes('--docx');
  const hasHtml = args.includes('--html');
  const hasJats = args.includes('--jats') || args.includes('--xml');
  const hasTex = args.includes('--tex');
  const hasPandoc = process.env.PANDOC === '1';

  if (hasDocx) return '.jpg';
  if (hasJats) return '.jpg';
  if (hasTex && hasPandoc) return '.jpg';
  if (hasTex) return '.pdf';
  if (hasPdf) return '.pdf';
  if (hasHtml) return '.svg'; 
  // Default fallback
  throw new Error('No valid build target specified. Please use --pdf, --tex, --docx, --jats, or --html.');    
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
