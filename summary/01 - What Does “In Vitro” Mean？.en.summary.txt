**High-level overview (2–3 sentences)**  
The talk explains what “in vitro” means and why in‑vitro models (“neurons in a dish”) are crucial for developing and testing gene‑targeted therapies before anything ever reaches animals or humans. Dr. Michael Boland uses his own son’s rare epilepsy (caused by an STXBP1 mutation) as a case study to show how human stem cells, brain organoids, and CRISPR-based tools can model disease and test whether a therapy might correct cellular defects.

---

## Speaker introduction

- **Name:** Dr. Michael Boland (referred to as Dr. Michael Bolan/Boland in the transcript)  
- **Current roles and affiliations:**
  - Strategic Director for Translational and Clinical Research  
  - Center for Epilepsy and Neurodevelopmental Disorders  
  - This center spans both:
    - University of Pennsylvania Perelman School of Medicine (“Penn Medicine”)  
    - Children’s Hospital of Philadelphia (CHOP)
- **Background and expertise:**
  - Former faculty member at Columbia University Medical Center  
  - Trained in:
    - Developmental neurobiology  
    - Pediatric epilepsy  
    - Genetics and transcriptomics  
  - Research experience with:
    - Human induced pluripotent stem cell (iPSC) models  
    - Genetic mouse models  
    - Monogenic (single‑gene) developmental and epileptic encephalopathies and autism spectrum disorders
- **Personal connection:**
  - Father of a son, Lucas, who has a developmental and epileptic encephalopathy caused by a frameshift mutation in the **STXBP1** gene  
  - Uses his son’s condition as a real-world example of how in‑vitro models can be used to understand disease and test gene‑targeted therapies.

---

## Main sections / topics (in order)

- Context for the session and why “in vitro” vs “in vivo” matters  
- Dr. Boland’s background and his son’s STXBP1 diagnosis  
- Basic genetic and cell biology concepts and terminology  
- Traditional cell lines and their limitations  
- Induced pluripotent stem cells (iPSCs): what they are and how they’re made  
- iPSC-based disease modeling strategies (trio, isogenic, knock‑in models)  
- Differentiating iPSCs into neurons and brain organoids  
- Choosing and evaluating organoid models (cell types, variability, activity)  
- Case study: modeling STXBP1 disorder in vitro (2D neurons and organoids)  
- Case study: CRISPR activation (CRISPRa) gene‑targeted therapy in organoids  
- Broader application to Angelman/UBE3A and why this work takes time and money  

Below, each section is summarized with key takeaways and, where relevant, definitions and examples.

---

### 1. Context for the session and why “in vitro” vs “in vivo” matters

- The organizers want families to be “grounded in knowledge” so they can understand complex talks and make informed decisions about future therapies for their children.  
- Two core concepts for the day are:
  - **In vitro** – experiments done “in glass,” i.e., in a dish or test tube, usually with cells.  
  - **In vivo** – experiments done “in the living,” i.e., inside an animal or human body.  
- In vitro models allow scientists to study DNA, RNA, and proteins (like UBE3A) in controlled conditions and to test drugs or gene therapies before moving to animals.  
- Understanding these terms is essential because all later discussions about gene therapy, drug development, and safety build on them.  
- The talk is positioned as the first step in a logical chain: in vitro → in vivo (animal) → eventually human trials.

---

### 2. Dr. Boland’s background and his son’s STXBP1 diagnosis

- Dr. Boland is a neuroscientist specializing in developmental neurobiology, pediatric epilepsy, and genetics, with extensive experience using human stem cells and mouse models to study single‑gene brain disorders.  
- While he was studying developmental and epileptic encephalopathies, his son Lucas was born and began having seizures on his first day of life.  
- Despite normal MRI, spinal tap, and infection workup, Lucas had an abnormal EEG; later genetic testing revealed a **frameshift mutation** in **STXBP1**, a gene critical for neuronal communication.  
- **STXBP1** is expressed in all neurons and is essential for **synaptic vesicle exocytosis**—the process by which neurotransmitters are released from one neuron into the synaptic cleft to signal the next neuron.  
- Dr. Boland uses Lucas’s STXBP1 mutation as a “model system” to show how in‑vitro tools can predict disease features and responses to gene‑targeted therapies.

---

### 3. Basic genetic and cell biology concepts and terminology

- Humans have **46 chromosomes** in most cells: 23 from the mother and 23 from the father, making a **diploid** genome (two copies of each chromosome).  
- **Transfection** is introducing DNA into cells using **non‑viral** methods (e.g., lipid nanoparticles); this is often used for temporary expression or screening.  
- **Transduction** is introducing genetic material into cells using **viruses** (e.g., AAV), which can efficiently deliver DNA or RNA into many cell types.  
- These processes are central to how scientists manipulate cells in vitro—e.g., to introduce CRISPR components, reprogramming factors, or therapeutic genes.  
- Knowing these terms helps interpret how therapies are delivered in cell models and, later, in animals or humans.

---

### 4. Traditional cell lines and their limitations

- Commonly used lab cell lines include:
  - **HEK293** (human embryonic kidney cells)  
  - **HeLa** (cervical cancer cells)  
  - Retinal pigmented epithelium lines  
  - Neuroblastoma cell lines  
- These lines are often **aneuploid** (abnormal chromosome numbers) and essentially behave like “cancer in a dish,” making them poor models of normal human cells or specific brain diseases.  
- However, they are:
  - Easy to grow  
  - Easy to transfect  
  - Suitable for **high‑throughput screening** of thousands of compounds or genetic constructs (e.g., testing many CRISPR guide RNAs quickly).  
- They are typically used as an **early screening step** to see if a drug or genetic tool has any effect before moving to more realistic disease models.  
- Because they are so artificial, they are not usually used for detailed disease modeling or predicting patient‑level responses.

---

### 5. Induced pluripotent stem cells (iPSCs): what they are and how they’re made

- In 2007, Shinya Yamanaka showed that adult cells (like skin fibroblasts) can be reprogrammed back into a stem‑cell‑like state using a set of **reprogramming factors** delivered by viruses.  
- These reprogrammed cells are called **induced pluripotent stem cells (iPSCs)** and behave similarly to **embryonic stem cells**: they can give rise to virtually any cell type in the body.  
- iPSCs can be made from:
  - Skin punch biopsies (fibroblasts)  
  - Blood (mononuclear cells)  
- Because they avoid destroying embryos, iPSCs became the standard way to obtain human pluripotent cells for research; they have been shown to be functionally equivalent to embryonic stem cells (e.g., they were used to clone fertile mice).  
- Using specific small molecules and proteins that mimic developmental signals, iPSCs can be directed to become heart cells, muscle, pancreas, or brain cells (neurons, astrocytes, etc.).

---

### 6. iPSC-based disease modeling strategies (trio, isogenic, knock‑in models)

- **Trio / familial model:**  
  - iPSCs are derived from the **mother, father, and affected child**.  
  - This mirrors the “trio” used in whole‑exome sequencing to identify **de novo** mutations (present in the child but not in either parent).  
  - Neurons derived from the child’s iPSCs carry the disease‑causing mutation and associated physiological defects, while parental cells serve as genetic comparators.
- **Isogenic correction model:**  
  - iPSCs are made from an affected child, then **CRISPR/Cas9** is used to **correct** the mutation in those cells.  
  - The original and corrected lines are **isogenic** (same genetic background except for the mutation), so differences can be attributed to that specific mutation.  
- **Isogenic knock‑in model:**  
  - Start with an unaffected iPSC line and use CRISPR to **introduce specific mutations** into the gene of interest.  
  - This allows comparison of different mutations in the same gene on the same background, helping to understand how variant type affects disease severity.  
- These strategies help disentangle the effect of the primary mutation from **genetic modifiers**, which contribute to variability in symptoms among patients.

---

### 7. Differentiating iPSCs into neurons and brain organoids

- iPSCs can be differentiated into neurons through a **stepwise developmental process**:
  - iPSCs → neural rosettes (mimicking early neural tube) → neural stem cells → progenitors → immature neurons → mature neuronal networks.  
- This process uses timed exposure to small molecules and proteins that mimic **morphogen gradients** and developmental cues in specific brain regions.  
- An alternative is **forced expression of a transcription factor** like **NGN2** in iPSCs, which rapidly converts them into neurons, skipping many intermediate developmental stages; this is faster and cheaper.  
- A third, increasingly common approach is to generate **3D organoids or spheroids**, sometimes called “mini brains” (though they are not conscious and do not replicate a full brain).  
- Organoids are 3D aggregates of cells that self‑organize and recapitulate aspects of brain development, including layered structures and interacting neuronal networks.

---

### 8. Choosing and evaluating organoid models (cell types, variability, activity)

- Organoids can be patterned to represent different brain regions, such as:
  - **Cortical organoids (CO)** – modeling the dorsal forebrain (cerebral cortex).  
  - **Medial ganglionic eminence organoids (MGO)** – modeling a region that produces **GABAergic interneurons** (inhibitory neurons).  
- In the developing cortex, about **25% of neurons are inhibitory** (GABAergic), and the balance between **excitatory** (glutamatergic) and **inhibitory** neurons is crucial; disruptions can lead to **hyperexcitability and epilepsy**.  
- Different published organoid protocols produce very different proportions of inhibitory neurons; some match the ~25% seen in vivo, others produce almost none.  
- For a gene like **STXBP1**, which affects communication between excitatory and inhibitory neurons, it is essential to choose an organoid protocol that generates both cell types in realistic proportions.  
- Even with the same protocol, organoids vary: some have good structure and activity, some look abnormal and die early, and some look fine but are electrically inert—so researchers must balance morphology and measurable activity.

---

### 9. Case study: modeling STXBP1 disorder in vitro (2D neurons and organoids)

- Dr. Boland generated iPSCs from:
  - Lucas (with an STXBP1 frameshift mutation)  
  - Himself and his wife (controls; his wife’s iPSCs were poor at making organoids, his were good).  
- First, they differentiated these iPSCs into **2D neurons** to test whether Lucas’s neurons showed **haploinsufficiency** (having only ~50% of normal protein due to a truncating mutation).  
- After about 65 days in culture, they measured STXBP1 protein levels and found that Lucas’s neurons had about **50% less STXBP1** than Dr. Boland’s neurons, as expected.  
- They then developed an **organoid model** from these iPSCs and examined neuronal activity using imaging that shows **synchronous oscillations** (bright flashes) and smaller “blips” representing microcircuit activity.  
- Lucas’s organoids showed **wider bursts**, more spikes within bursts, and altered timing (longer bursts and longer intervals between bursts) compared to controls—features that can serve as measurable readouts of disease‑related network dysfunction.

---

### 10. Case study: CRISPR activation (CRISPRa) gene‑targeted therapy in organoids

- Dr. Boland focused on **CRISPR activation (CRISPRa)**, a variant of CRISPR/Cas9 where:
  - The **Cas9 protein is catalytically dead** (cannot cut DNA).  
  - It is guided to specific DNA sequences (e.g., the **STXBP1 promoter**) by short guide RNAs.  
  - It is fused to a **transcriptional activation domain** that recruits the cell’s machinery to **increase gene transcription**.  
- The goal is to **upregulate STXBP1 expression** from the remaining healthy allele in Lucas’s cells to correct haploinsufficiency.  
- They first screened many guide RNAs in easy‑to‑use cell lines (HEK293T, neuroblastoma) and found that most guides effectively increased STXBP1 expression.  
- Next, they packaged the CRISPRa system into an **AAV virus** and **transduced 3‑month‑old organoids**; after 2–3 weeks, they confirmed that STXBP1 mRNA and protein levels in Lucas’s organoids were restored to normal.  
- Functionally, CRISPRa treatment:
  - Reduced the incidence of low‑amplitude “blip” events (suspected microcircuit/epilepsy‑related defects).  
  - Made the bursts in Lucas’s organoids shorter and more frequent, moving their activity pattern closer to that of control organoids—evidence that a gene‑targeted therapy can partially correct network‑level defects in vitro.

---

### 11. Broader application to Angelman/UBE3A and why this work takes time and money

- The same in‑vitro logic and tools are being applied to **Angelman syndrome** and **UBE3A**:
  - CRISPR/Cas9 gene editing to **destroy the UBE3A antisense transcript**, which normally silences the paternal UBE3A allele.  
  - Epigenetic tools to **methylate** and shut down the antisense transcript region, thereby reactivating paternal UBE3A.  
  - CRISPR activation (CRISPRa) approaches to **upregulate UBE3A** expression, especially for deletion genotypes.  
- These strategies must first be optimized and validated in **cell and organoid models** (like those described) before moving into **animal models** and eventually human trials.  
- Each step—designing tools, generating iPSCs, differentiating them, building organoids, validating activity, and testing therapies—can take **years** and requires significant funding.  
- The closing remarks emphasize that the complexity and elegance of this science explain **why progress is slow and expensive**, but also why it is necessary to do this groundwork before exposing animals or humans to new therapies.  
- The next talk in the series will move from in vitro to **in vivo animal models**, showing how candidate therapies tested in dishes are then evaluated in living systems.