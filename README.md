<!-- prettier-ignore -->
# 🚀 ML Lab — Shresth Panigrahi

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

Welcome to my Machine Learning lab — a tidy, visual place to learn, experiment, and contribute practical ML work.

**What you'll find**
- 📚 Curated notebooks demonstrating ML workflows and analyses.
- 📈 Small projects and experiments using real datasets (e.g., `USA_Housing.csv`).
- 🧪 Reproducible code and clear notes to help you learn quickly.

**Highlights**
- Purpose: hands-on learning and building practical ML intuition.
- Focus: supervised & unsupervised learning, feature engineering, model evaluation, and applied demos.

**Repository structure (suggested)**

- data/ — raw and processed datasets (avoid committing large raw files)
- notebooks/ — exploratory and tutorial notebooks
- src/ — reusable scripts and modules
- models/ — saved model artifacts and checkpoints
- README.md — this file

---

**Quick start**

1. Create and activate the `ml` virtual environment (already available in this repo):

```bash
cd "/Users/shresthpanigrahi/Desktop/Machine Learning"
source ml/bin/activate
```

2. Install dependencies (if not already installed):

```bash
pip install -r requirements.txt
```

3. Open the notebook server and pick a notebook from `notebooks/` or open `USA_Housing.ipynb`:

```bash
jupyter notebook
```

**Tips**
- Use the `ml` virtual environment kernel in Jupyter for consistent packages.
- Keep experiments small and document decisions in Markdown cells.

---

**How to contribute**

- Add a new notebook under `notebooks/` or a script under `src/`.
- Open an issue describing your idea, or submit a pull request with a short description of changes.
- Use clear commit messages and keep datasets in `data/` or provide download links.

---

If you'd like, I can:
- add a polished `notebooks/` index
- register the `ml` kernel with Jupyter
- generate a starter notebook template

Happy learning — iterate often and document discoveries! ✨
