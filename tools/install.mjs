#!/usr/bin/env node
import { existsSync, lstatSync, mkdirSync, readlinkSync, symlinkSync, unlinkSync } from "node:fs";
import { homedir } from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const targetRoot = path.resolve(process.env.SKILLS_HOME || path.join(process.env.CODEX_HOME || path.join(homedir(), ".codex"), "skills"));
const target = path.join(targetRoot, "social-media-creator-workflow");
const forceLinks = process.argv.includes("--force-links");
mkdirSync(targetRoot, { recursive: true });
if (existsSync(target)) {
  const stat = lstatSync(target);
  const same = stat.isSymbolicLink() && path.resolve(path.dirname(target), readlinkSync(target)) === root;
  if (same) {
    console.log(`ok ${target}`);
    process.exit(0);
  }
  if (!forceLinks || !stat.isSymbolicLink()) throw new Error(`${target} exists and is not the managed link`);
  unlinkSync(target);
}
symlinkSync(root, target, "dir");
console.log(`installed ${target}`);
