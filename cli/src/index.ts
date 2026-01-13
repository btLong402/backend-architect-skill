#!/usr/bin/env node

import { Command } from 'commander';
import { initCommand } from './commands/init.js';
import type { AIType } from './types/index.js';
import { AI_TYPES } from './types/index.js';

const program = new Command();

program
    .name('backend-architect')
    .description('CLI to install Backend Architect skill for AI coding assistants')
    .version('1.0.0');

program
    .command('init')
    .description('Install Backend Architect skill to current project')
    .option('-a, --ai <type>', `AI assistant type (${AI_TYPES.join(', ')})`)
    .option('-f, --force', 'Overwrite existing files')
    .action(async (options) => {
        if (options.ai && !AI_TYPES.includes(options.ai)) {
            console.error(`Invalid AI type: ${options.ai}`);
            console.error(`Valid types: ${AI_TYPES.join(', ')}`);
            process.exit(1);
        }
        await initCommand({
            ai: options.ai as AIType | undefined,
            force: options.force,
        });
    });

// Default command (when run without subcommand)
program
    .action(async () => {
        await initCommand({});
    });

program.parse();
