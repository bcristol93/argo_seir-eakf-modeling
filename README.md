# ARGOX + SEIR–EAKF Influenza Modeling Pipeline  
*End-to-end ARGO-based influenza nowcasting integrated with a humidity-forced SEIR model and Ensemble Adjustment Kalman Filter (EAKF).*

---

## 🔍 Overview

This repository contains a **fully reproducible modeling pipeline** combining:

1. **ARGOX**  
   - A Google Trends–augmented sparse regression framework  
   - Weekly influenza-like illness (ILI) prediction at the state or metropolitan level  
   - Rolling or short-window ElasticNet models with automated term selection  

2. **SEIR–EAKF**  
   - A daily SEIR compartmental model forced by **absolute humidity (AH)**  
   - State-specific humidity drivers extracted from **NECP R2 reanalysis data**  
   - Bayesian updating using an **Ensemble Adjustment Kalman Filter**  
   - Weekly assimilation of observed ILI, producing Rt and latent state estimates  

Together, these components create a **coherent real-time influenza surveillance model** suitable for research, manuscript analyses, and operational deployment.

---

## 📁 Repository Structure

### Ignored folders (generated automatically when running the notebook)

These are large and system-specific, so they are not stored in the GitHub repo.  
**They will be created automatically when the notebook is run.**

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/bcristol93/argo_seir-eakf-modeling.git
cd argo_seir-eakf-modeling

pip install -r requirements.txt

jupyter lab
