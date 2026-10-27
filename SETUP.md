# Setup & Deployment Guide — Koushikkatkam Profile Repository

This package contains the complete, production-ready GitHub profile portfolio for **Koushik Katkam** (`@Koushikkatkam`), styled in the **Obsidian Aurora — Digital Lab** theme.

Follow these step-by-step instructions to create the repository and publish your profile to GitHub.

---

## 1. Project Directory Structure

Ensure the following files and folders are present:

```text
Koushikkatkam/
├── .github/
│   └── workflows/
│       └── snake.yml                   # Automated contribution snake action
├── assets/
│   ├── banner.svg                      # Obsidian Aurora hero banner (animated SMIL)
│   ├── digital-lab-telemetry.svg       # Four core disciplines telemetry card
│   ├── tech-constellation.svg          # Animated interactive technology constellation graph
│   ├── section-rule.svg                # Animated glowing neon divider with traveling pulse
│   ├── activity-grid.svg               # Obsidian Aurora activity matrix with data probe tracer
│   └── footer-signature.svg            # Animated KK monogram & fluid cursive signature
├── README.md                           # Complete animated profile README
└── SETUP.md                            # This setup & configuration guide
```

---

## 2. Create the GitHub Profile Repository

To display a profile README on your GitHub user page:

1. Sign in to your GitHub account: **[https://github.com/Koushikkatkam](https://github.com/Koushikkatkam)**.
2. Click the **+** (New repository) icon in the top right, or navigate directly to **[https://github.com/new](https://github.com/new)**.
3. In **Repository name**, enter exactly:
   ```text
   Koushikkatkam
   ```
   *(GitHub will display a special notice: "You found a secret! Koushikkatkam/Koushikkatkam is a ✨special✨ repository that you can use to add a README.md to your GitHub profile.")*
4. Ensure the repository visibility is set to **Public** *(profile READMEs will not display if private)*.
5. Leave "Add a README file", "Add .gitignore", and "Choose a license" **unchecked** (we will upload our completed files).
6. Click **Create repository**.

---

## 3. Uploading the Project

You can publish using either the Git Command Line or GitHub's Web Interface.

### Option A: Using Git Command Line (Recommended)

In your terminal, navigate to the extracted project directory and run:

```bash
# 1. Initialize git if not already initialized
git init

# 2. Stage all project files (including hidden .github folder)
git add .

# 3. Create initial commit
git commit -m "feat: complete Obsidian Aurora profile README and digital lab portfolio"

# 4. Set default branch to main
git branch -M main

# 5. Add remote origin for Koushikkatkam
git remote add origin https://github.com/Koushikkatkam/Koushikkatkam.git

# 6. Push to GitHub
git push -u origin main
```

### Option B: Using GitHub Web Interface

1. On the empty repository page on GitHub, click **uploading an existing file**.
2. Drag and drop `README.md`, `SETUP.md`, the `assets/` folder, and the `.github/` folder.
   > **Note:** Some browsers do not drag hidden folders (starting with `.`) properly. If `.github/workflows/snake.yml` is skipped, click **Add file** > **Create new file**, name it `.github/workflows/snake.yml`, paste the contents of `snake.yml`, and commit.
3. Click **Commit changes**.

Your profile README is now live at **[https://github.com/Koushikkatkam](https://github.com/Koushikkatkam)**!

---

## 4. Enabling GitHub Actions for the Contribution Snake

The included workflow (`.github/workflows/snake.yml`) automatically plays the contribution snake animation across your GitHub activity grid and deploys the resulting SVGs to an isolated `output` branch.

### Step 1: Enable Workflow Write Permissions (Important!)
By default, GitHub restricts GitHub Actions from writing to repository branches. You must enable write permissions:

1. Go to your repository on GitHub: `https://github.com/Koushikkatkam/Koushikkatkam`.
2. Click **Settings** (top tab bar).
3. In the left sidebar, click **Actions** > **General**.
4. Scroll down to **Workflow permissions**.
5. Select **Read and write permissions**.
6. Check the box **Allow GitHub Actions to create and approve pull requests** (optional, recommended).
7. Click **Save**.

### Step 2: Trigger the First Workflow Run
1. Navigate to the **Actions** tab of your repository.
2. If prompted with *"Workflows aren't being run on this repository"*, click **I understand my workflows, go ahead and enable them**.
3. In the left sidebar, click **Generate contribution snake**.
4. Click the **Run workflow** dropdown on the right and click the green **Run workflow** button.
5. Wait ~30–45 seconds. The workflow will finish with a green checkmark.
6. A new orphan branch named `output` will automatically be created containing:
   - `github-contribution-grid-snake.svg`
   - `github-contribution-grid-snake-dark.svg`

### Step 3: (Optional) Switching to the Dynamic Live Snake in README
The profile README is pre-configured with `assets/activity-grid.svg` as a zero-downtime fallback so your profile looks complete immediately without broken images.

Once your snake workflow has run successfully, you can switch the contribution section in `README.md` to dynamic SVGs by replacing:

```html
<img src="assets/activity-grid.svg" alt="Obsidian Aurora Contribution Matrix" width="100%"/>
```

with the dynamic picture tag:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Koushikkatkam/Koushikkatkam/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Koushikkatkam/Koushikkatkam/output/github-contribution-grid-snake.svg">
  <img alt="Koushik Katkam Contribution Snake" src="https://raw.githubusercontent.com/Koushikkatkam/Koushikkatkam/output/github-contribution-grid-snake.svg" width="100%">
</picture>
```

---

## 5. Maintaining Your Portfolio

* **Adding New Projects:** To add a project, edit the table in `README.md` under Section `03`. Follow the existing card template (Title, Stack, Capability bullet points, and Live Application / Repository links).
* **Palette Compliance:** If designing additional graphics or badges, adhere to the **Obsidian Aurora** color tokens:
  - Deep Navy: `#080B14`
  - Dark Surface: `#101827`
  - Electric Cyan: `#43E7FF`
  - Aurora Violet: `#9475FF`
  - Warm Amber: `#FFB454`
  - Main Text: `#F2F6FF`
  - Muted Text: `#9BA9BF`
