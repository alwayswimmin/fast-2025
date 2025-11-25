**High-level overview (2–3 sentences)**  
This talk describes a bench-to-bedside program developing a **non-viral CRISPR-based gene-editing therapy** for Angelman syndrome, using a novel delivery platform called **STEP** to get CRISPR editors into neurons. The speakers walk through the science behind STEP, the strong results in Angelman mouse and human neuron models, and the complex translational work—manufacturing, safety, dosing, and delivery route studies in monkeys—needed to reach a first-in-human clinical trial.

---

## Speaker introductions

**Core team mentioned in the talk**

- **Jiangbing “Jang Bing” Xu, PhD**  
  - Role: Engineer and technology developer on the Yale team.  
  - Expertise: Drug delivery, nanotechnology, and chemical engineering approaches for delivering biological payloads (like CRISPR) into specific cell types.  
  - Affiliation: Yale University. His lab developed the **STEP** (small-molecule–based) delivery platform used to carry CRISPR ribonucleoproteins (RNPs) into neurons.

- **Y. “Yang” Wei Jiang, MD/PhD (Angelman clinician-scientist at Yale)**  
  - Role: Neuroscientist and Angelman syndrome expert leading the **disease-focused preclinical work**.  
  - Background: Longstanding work on Angelman syndrome, including generating and using Angelman mouse models; deeply involved in multiple therapeutic approaches (ASOs, gene therapy, etc.).  
  - Affiliation: Yale University; his lab tested STEP–CRISPR in Angelman mouse models and patient-derived neurons.

- **Alison (FAST leadership; clinical translation lead)**  
  - Role: Represents FAST (Foundation for Angelman Syndrome Therapeutics) and the translational/clinical side of the program.  
  - Focus: Moving therapies **out of academic labs and into human clinical trials**, coordinating preclinical, regulatory, and clinical efforts, and securing funding.  
  - Works closely with:  
    - **Jennifer** – regulatory and CMC (manufacturing) expert, key driver of IND-enabling and regulatory strategy.  
    - **Rush University** (Liz at Rush) – clinical trial site partner.  
    - **AS2 Bio, Courageous, and other partners** – for development and manufacturing.

---

## Main sections / topics (in order)

1. Bench-to-bedside program structure and NIH support  
2. CRISPR basics and why delivery is the main challenge  
3. Limitations of viral vectors and conventional nanoparticles for brain delivery  
4. The STEP platform: a non-viral delivery system for CRISPR RNPs  
5. Proof-of-concept in human neurons and organoids  
6. Application to Angelman syndrome: strategy and rationale  
7. Mouse model results: efficacy, timing, and safety advantages  
8. Translational path: IND-enabling studies and key questions  
9. Non-human primate (monkey) studies: route of administration and brain distribution  
10. Manufacturing challenges for a three-component CRISPR–STEP drug  
11. Overall development roadmap, collaboration model, and impact on other disorders  

---

## 1. Bench-to-bedside program structure and NIH support

- The project was designed from the start as a **bench-to-bedside pipeline**, connecting discovery and preclinical work at Yale with clinical trials at Yale and Rush.  
- This integrated ecosystem—basic science, translational science, manufacturing, regulatory, and clinical operations—was a major reason the **NIH awarded >$40 million** to support the program.  
- The community (families, FAST, and partners) helped build this ecosystem, demonstrating that Angelman syndrome can serve as a **model platform** for rare neurogenetic disease drug development.  
- The program is structured in stages: **preclinical efficacy**, **toxicology and safety**, **manufacturing**, and then **first-in-human clinical trials**.  
- The talk begins with preclinical data (technology and animal models) and then moves to how that is being translated into a human-ready therapeutic.

---

## 2. CRISPR basics and why delivery is the main challenge

- **CRISPR** originated as a bacterial defense system against viruses: bacteria store viral DNA “memories” and use a protein (like Cas9) guided by RNA to **cut viral genomes**.  
- For human use, CRISPR is typically a **two-component system**:  
  - **Cas protein** (e.g., Cas9) – the “molecular scissors” that cut or modify DNA.  
  - **Guide RNA (gRNA)** – the “address code” that directs Cas to a specific DNA sequence.  
- CRISPR has been engineered beyond simple cutting to enable **gene correction** and **epigenome editing**, meaning it can fix mutations or change gene activity without fully cutting the DNA.  
- The central challenge is **delivery**: getting this relatively large, complex machinery into the **right cells (neurons)** in the **right tissue (brain)** at the **right time**, in a safe and controlled way.  
- The talk emphasizes that while CRISPR’s editing power is well known, **safe, precise delivery to the brain** is the bottleneck for clinical use in Angelman syndrome.

---

## 3. Limitations of viral vectors and conventional nanoparticles for brain delivery

- Two main delivery systems dominate the field today:  
  - **AAV (adeno-associated virus)** – a viral vector used widely in gene therapy.  
  - **Nanoparticles**, especially **lipid nanoparticles (LNPs)** – used for mRNA vaccines and some gene therapies.  
- **Problems with AAV for CRISPR**:  
  - AAV can cause **long-term expression** of the Cas protein (potentially for years), which increases the risk of **off-target edits** and immune reactions.  
  - Because CRISPR is an active genome-editing tool, prolonged presence in cells is undesirable; we want **short, transient exposure**.  
- **Problems with conventional nanoparticles for brain delivery**:  
  - Intravenous delivery requires crossing the **blood–brain barrier (BBB)**, which most particles cannot do efficiently.  
  - Even with local (intrathecal/intracerebral) delivery, typical nanoparticles are **too large** (often >60–100 nm) to move freely through the **tight extracellular spaces** in brain tissue (often <30 nm).  
- As a result, both AAV and standard nanoparticles are **suboptimal for delivering CRISPR to neurons** in Angelman syndrome.  
- This motivated the development of a **new, non-viral, small-sized delivery approach** specifically tailored for brain and neuron targeting.

---

## 4. The STEP platform: a non-viral delivery system for CRISPR RNPs

- **STEP** is a **small-molecule–based delivery approach**:  
  - STEP molecules are **tiny (~2 kDa)** chemicals with **two functional “arms”**.  
  - One arm binds to the **payload** (here, CRISPR RNP – Cas protein + guide RNA).  
  - The other arm is designed to interact with **specific cell types or organs** (e.g., neurons).  
- When conjugated, a small number of STEP molecules (on the order of **10–20 per CRISPR RNP**) are enough to **ferry the CRISPR complex into cells** and then release it.  
- The resulting **STEP–CRISPR RNP complex** is about **10 nm in size**, which is ideal for **penetrating brain tissue** and moving through the narrow extracellular spaces.  
- STEP is a **concept and a library**: many different STEP molecules have been synthesized, each with different targeting properties (some prefer neurons, some astrocytes, some other organs).  
- For Angelman syndrome, the team selected a **neuron-targeting STEP** that efficiently delivers CRISPR RNPs into neurons, enabling high editing efficiency with **transient presence** of the Cas protein.

---

## 5. Proof-of-concept in human neurons and organoids

- The team tested STEP–CRISPR RNPs in **patient-derived neurons** grown in 2D culture (on flasks).  
- A **single treatment** edited **over 90% of neurons** in these 2D cultures, indicating very high delivery and editing efficiency.  
- They also tested in **3D brain organoids** (spherical, 3D cultures that better mimic brain structure), and again a single treatment edited **most cells within the organoid**, with efficiencies up to ~90%.  
- These results show that STEP can **penetrate dense 3D neural tissue** and deliver CRISPR effectively, not just in simple cell monolayers.  
- This human-cell proof-of-concept provided strong justification to move into **in vivo animal models** and eventually toward clinical translation.

---

## 6. Application to Angelman syndrome: strategy and rationale

- Angelman syndrome is caused by **loss of function of the maternal UBE3A gene** in neurons; the paternal copy is present but **silenced by an antisense transcript** (UBE3A-ATS).  
- Existing approaches (like **antisense oligonucleotides, ASOs**) work by **transiently inactivating UBE3A-ATS**, which reactivates the paternal UBE3A, but they require **repeated dosing** over time.  
- The STEP–CRISPR strategy is to **permanently inactivate the UBE3A-ATS** using genome editing, so that the paternal UBE3A gene is **durably re-expressed** after a **single treatment**.  
- This concept has been supported by prior work using other tools (e.g., AAV-delivered Cas9, small molecules, and RNA-based approaches) showing that **silencing the antisense** can restore UBE3A.  
- The expectation is that this CRISPR-based approach should be applicable across **different Angelman genotypes** (e.g., deletions, mutations), because it targets the **shared mechanism**—the antisense silencer—rather than the specific mutation.

---

## 7. Mouse model results: efficacy, timing, and safety advantages

- Using a well-established **Angelman mouse model** (generated years ago and widely used in the field), the team delivered STEP–CRISPR RNPs by **intracerebral injection**.  
- Western blot data from mouse brains showed **clear reactivation of UBE3A protein** in treated animals, with very little or no UBE3A in untreated controls.  
- They tested treatment at **multiple ages**:  
  - **Newborn (day 1)**  
  - **Juvenile (day 21)**  
  - **Adult (day 42)**  
  and found **similar rescue of motor function** across ages, with some assays showing adults doing as well or even better than newborns.  
- Behavioral tests (including **motor assays** and **seizure susceptibility paradigms**) showed that treated Angelman mice performed **much closer to wild-type** and had **significantly reduced seizure susceptibility**, regardless of whether they were treated at day 1 or day 21.  
- Importantly, imaging of Cas9 protein after injection showed it was **rapidly cleared**: detectable at 1–12 hours but almost gone by 24 hours, which greatly reduces the risk of **off-target genome editing** and is a major **safety advantage** over long-term viral expression.

---

## 8. Translational path: IND-enabling studies and key questions

- To move from mouse to human, the team must complete **IND-enabling studies**—the package of safety, toxicity, and pharmacology data required by regulators (e.g., FDA) before a **first-in-human trial**.  
- These studies ask critical questions:  
  - **Does the STEP–CRISPR RNP go where we want?** (brain regions like cortex, hippocampus, brainstem)  
  - **Does it effectively knock down UBE3A-ATS and restore paternal UBE3A protein?**  
  - **Does it cause toxicity or off-target effects elsewhere in the genome or body?**  
- They must characterize **pharmacodynamics** (what the drug does to the body/brain: antisense knockdown, UBE3A expression) and **pharmacokinetics/distribution** (where it goes, how long it stays).  
- Because this is a **new modality** (non-viral CRISPR RNP with STEP), there is **no existing regulatory template** like there is for AAV or ASOs, making the work slower, more complex, and more expensive.  
- The team runs many activities **in parallel** and brings in external experts to accelerate progress, but each step (especially safety and distribution studies) still takes **years**, which explains why the program has not yet reached human trials despite promising early data.

---

## 9. Non-human primate (monkey) studies: route of administration and brain distribution

- Mice are informative but not sufficient; **monkeys** are closer to humans in brain size and anatomy, so they are used to study **delivery route, distribution, and safety**.  
- The team compared three **routes of administration (ROA)** in monkeys:  
  - **IT/ICM (intrathecal / intrathecal at lumbar spine)** – like ASO delivery from below.  
  - **ICM at the back of the skull** – similar to some AAV gene therapy approaches.  
  - **ICV (intracerebroventricular)** – via a small neurosurgical catheter into the brain ventricle.  
- PET-CT imaging with a radiolabeled compound showed that **ICV delivery** produced **much better and more uniform brain distribution** at 0.5 hours, 24 hours, and 72 hours compared with lumbar or cisternal routes.  
- Because this therapy is intended as a **single-dose treatment**, the team concluded that the **ICV route**, although requiring a small neurosurgical procedure, is **feasible and likely optimal** for achieving broad brain coverage.  
- These monkey studies also showed that the tested doses were **tolerated**, with animals surviving and the compound spreading throughout the brain by 72 hours, giving confidence to proceed to more detailed safety and dose-finding work.

---

## 10. Manufacturing challenges for a three-component CRISPR–STEP drug

- The final therapeutic is **not a single molecule** but a **complex of three components**:  
  1. **Guide RNA**  
  2. **Cas protein**  
  3. **STEP molecule**  
- Each component requires its own **manufacturing process**, and then they must be **combined (complexed) in a controlled, reproducible way** to form the final drug product.  
- Manufacturing must meet **GMP (Good Manufacturing Practice)** standards, meaning extremely high purity, consistency, and safety suitable for human use—much more stringent than research-grade material.  
- Unlike ASOs or AAVs, there is **no established industrial playbook** for making and assembling this exact type of CRISPR–STEP product, so the team (with experts like Jennifer, Conrad, and Derek) has had to **invent and optimize processes from scratch**.  
- This manufacturing work is **technically complex, time-consuming, and expensive**, but it is essential to ensure that the product used in humans is **safe, stable, and of consistent quality**.

---

## 11. Overall development roadmap, collaboration model, and impact on other disorders

- The full drug development path includes: **discovery → preclinical efficacy → IND-enabling safety/toxicology → manufacturing scale-up → regulatory submissions → first-in-human clinical trial**.  
- Each step can reveal **unexpected findings** (e.g., mouse-effective doses being too high or too low in monkeys), requiring iteration and careful adjustment to maintain **rigor and safety**.  
- The program’s success relies on **intense collaboration** across disciplines and institutions: basic scientists at Yale, translational and regulatory experts (Jennifer and colleagues), clinical teams at Yale and Rush, industry partners (AS2 Bio, Courageous), and funding from NIH and the Angelman community.  
- Angelman syndrome is being used as a **platform and exemplar** for other rare neurodevelopmental disorders: the tools, processes, and regulatory pathways developed here can be adapted to other conditions that might benefit from **precision gene editing**.  
- FAST’s explicit goal is not only to make Angelman a “low-hanging fruit” success story but also to **ensure that what is learned and built here helps other diseases**, advancing the entire field of rare neurogenetic therapeutics.

---